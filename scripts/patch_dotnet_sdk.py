#!/usr/bin/env python3
"""Apply the identity fields the csharp generator won't emit to the csproj.

The generator hardcodes `Authors` and `Company` to "OpenAPI", `AssemblyTitle`
to "OpenAPI Library", `Description`, as these are not reachable through the 
generator config. An unpatched package would publish to Nuget with placeholder
text as its description.

It also packs the README. The csharp generator emits no `PackageReadmeFile`,
so an unpatched package renders on nuget.org with only its one-line description
and no readme at all. That needs both the property and a `<None>` item marking
the file for packing.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

AUTHORS = "DDx API Team"
COMPANY = "Democratic Data Exchange"
ASSEMBLY_TITLE = "DDx Interactions API Client"
DESCRIPTION = "C# client for the DDx Interactions API, generated from the OpenAPI spec."
COPYRIGHT = "Copyright (c) Democratic Data Exchange"
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
    args = parser.parse_args(argv)

    try:
        text = args.csproj.read_text(encoding="utf-8")
    except OSError as exc:
        print(f"error: cannot read {args.csproj}: {exc}", file=sys.stderr)
        return 2

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
