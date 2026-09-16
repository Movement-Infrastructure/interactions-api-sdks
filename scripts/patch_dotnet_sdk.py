#!/usr/bin/env python3
"""Apply the identity fields the csharp generator won't emit to the csproj.

The generator hardcodes `Authors` and `Company` to "OpenAPI", `AssemblyTitle`
to "OpenAPI Library", `Description` to "A library generated from a OpenAPI doc"
and `Copyright` to "No Copyright". None of it is reachable through generator
config: `licenseId`, `packageGuid`, `packageName`, `packageTags` and
`packageVersion` are the only package fields the csharp generator exposes, so
an unpatched package would publish to NuGet attributed to a third party with
placeholder text as its description.

A targeted element rewrite rather than an XML round-trip: ElementTree discards
the csproj's comments and reflows the whole document, and the generated file
carries a comment explaining the GenerateAssemblyInfo workaround. Same reason
bump_version.py rewrites a line instead of round-tripping YAML.

It also packs the README. The csharp generator emits no `PackageReadmeFile`,
so an unpatched package renders on nuget.org with only its one-line description
and no readme at all. That needs both the property and a `<None>` item marking
the file for packing.

Idempotent: it sets element text rather than splicing, inserts the readme
property only when absent, and skips the `<None>` item when it is already
there, so re-running changes nothing. It does NOT touch `Version` -- that flows
from `packageVersion` in the generator config via bump_version.py, and
overwriting it would undo the bump.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

AUTHORS = "DDx API Team"
COMPANY = "Movement Infrastructure"
ASSEMBLY_TITLE = "DDx Interactions API Client"
DESCRIPTION = "C# client for the DDx Interactions API, generated from the OpenAPI spec."
COPYRIGHT = "Copyright (c) Movement Infrastructure"
PACKAGE_README = "README.md"

# Relative to the csproj at src/<PackageId>/, so two levels up to sdks/csharp/v1.
# Forward slashes: MSBuild accepts them on every platform, backslashes only on
# Windows.
README_INCLUDE = "../../README.md"
README_ITEM_GROUP = (
    "  <ItemGroup>\n"
    f'    <None Include="{README_INCLUDE}" Pack="true" PackagePath="/" />\n'
    "  </ItemGroup>\n"
)

# Element name -> value we require in the published package.
PATCHED_PROPERTIES = {
    "Authors": AUTHORS,
    "Company": COMPANY,
    "AssemblyTitle": ASSEMBLY_TITLE,
    "Description": DESCRIPTION,
    "Copyright": COPYRIGHT,
}

# Generator defaults that must never reach NuGet, keyed by element name.
GENERATED_DEFAULTS = {
    "Authors": {"OpenAPI"},
    "Company": {"OpenAPI"},
    "AssemblyTitle": {"OpenAPI Library"},
    "Description": {"A library generated from a OpenAPI doc"},
    "Copyright": {"No Copyright"},
}


class PatchError(ValueError):
    """Raised when the csproj is missing or not shaped as expected."""


def _property_re(name: str) -> re.Pattern[str]:
    """Build the matcher for a single MSBuild property element."""
    return re.compile(
        rf"(?P<open><{re.escape(name)}>)(?P<value>.*?)(?P<close></{re.escape(name)}>)",
        re.DOTALL,
    )


def read_property(csproj: str, name: str) -> str | None:
    """Return the text of `name`, or None if the element is absent."""
    match = _property_re(name).search(csproj)
    return None if match is None else match.group("value")


def set_property(csproj: str, name: str, value: str) -> str:
    """Return `csproj` with `name` set to `value`, leaving the rest byte-identical."""
    pattern = _property_re(name)
    matches = pattern.findall(csproj)

    if not matches:
        raise PatchError(
            f"no <{name}> element found; the generator template changed"
        )
    if len(matches) > 1:
        raise PatchError(
            f"found {len(matches)} <{name}> elements, expected exactly one"
        )

    return pattern.sub(
        lambda m: f"{m.group('open')}{value}{m.group('close')}", csproj, count=1
    )


def ensure_property(csproj: str, name: str, value: str) -> str:
    """Set `name`, inserting the element when the generator did not emit it."""
    if read_property(csproj, name) is not None:
        return set_property(csproj, name, value)

    match = re.search(r"\n(?P<indent>[ \t]*)</PropertyGroup>", csproj)
    if match is None:
        raise PatchError(
            "no </PropertyGroup> to insert into; the generator template changed"
        )

    return (
        csproj[: match.start()]
        + f"\n{match.group('indent')}  <{name}>{value}</{name}>"
        + csproj[match.start() :]
    )


def ensure_readme_item(csproj: str) -> str:
    """Return `csproj` with the README marked for packing."""
    if README_INCLUDE in csproj:
        return csproj

    if "</Project>" not in csproj:
        raise PatchError("no </Project>; the generator template changed")

    return csproj.replace("</Project>", README_ITEM_GROUP + "</Project>", 1)


def patch_csproj(csproj: str) -> str:
    """Return `csproj` with every generator-default identity field replaced."""
    if "<Project" not in csproj:
        raise PatchError("file does not look like an MSBuild project")

    for name, value in PATCHED_PROPERTIES.items():
        csproj = set_property(csproj, name, value)

    csproj = ensure_property(csproj, "PackageReadmeFile", PACKAGE_README)
    csproj = ensure_readme_item(csproj)

    return csproj


def check_no_generated_defaults(csproj: str) -> list[str]:
    """Return a list of problems that should block a publish. Empty means clean."""
    problems = []

    for name, defaults in GENERATED_DEFAULTS.items():
        value = read_property(csproj, name)
        if value is None:
            problems.append(f"<{name}> is missing")
        elif value in defaults:
            problems.append(f"<{name}> is the generator default ({value!r})")
        elif not value.strip():
            problems.append(f"<{name}> is empty")

    version = read_property(csproj, "Version")
    if version is None:
        problems.append("<Version> is missing")
    elif version.startswith("0.0.0"):
        problems.append("<Version> is the 0.0.0 placeholder; the version bump did not run")

    if read_property(csproj, "PackageLicenseExpression") is None:
        problems.append("<PackageLicenseExpression> is missing; licenseId is unset")

    if read_property(csproj, "PackageReadmeFile") is None:
        problems.append(
            "<PackageReadmeFile> is missing; the package would render on nuget.org "
            "with no readme"
        )
    elif README_INCLUDE not in csproj:
        problems.append(
            f"<PackageReadmeFile> is set but {README_INCLUDE} is not packed; "
            "dotnet pack fails on a readme it cannot find"
        )

    return problems


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Patch the generated C# SDK csproj in place."
    )
    parser.add_argument(
        "csproj",
        type=Path,
        help="Path to the generated csproj, e.g. "
        "sdks/csharp/v1/src/Ddx.InteractionsApi/Ddx.InteractionsApi.csproj.",
    )
    parser.add_argument(
        "--check-only",
        action="store_true",
        help="Report publish blockers without writing. For use as a publish gate.",
    )
    args = parser.parse_args(argv)

    try:
        text = args.csproj.read_text(encoding="utf-8")
    except OSError as exc:
        print(f"error: cannot read {args.csproj}: {exc}", file=sys.stderr)
        return 2

    if args.check_only:
        problems = check_no_generated_defaults(text)
        for problem in problems:
            print(f"::error::{problem}")
        if problems:
            print("::error::Refusing to publish with generated-default metadata.")
            return 1
        print(f"Metadata checks passed: {args.csproj}")
        return 0

    try:
        patched = patch_csproj(text)
    except PatchError as exc:
        print(f"::error::{args.csproj}: {exc}", file=sys.stderr)
        return 2

    args.csproj.write_text(patched, encoding="utf-8")
    print(f"patched {args.csproj}: Authors={AUTHORS!r}, Company={COMPANY!r}")
    return 0


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
