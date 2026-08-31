#!/usr/bin/env python3
"""Apply the fixes the typescript-fetch generator can't be configured to make.

Two generated files need work before the SDK builds or publishes correctly, and
neither is reachable through generator config -- `npmName`, `npmVersion` and
`npmRepository` are the only package.json fields typescript-fetch exposes, and
the tsconfig template takes no options at all.

package.json
    Hardcodes `author` to "OpenAPI-Generator", omits `license`, `homepage` and
    `engines`, and ships no `files` allowlist, so an unpatched package would
    publish with third-party authorship, no license, and the whole source tree
    including this repo's generator config.

tsconfig.json
    Has no `include`, so `tsc` compiles everything under the project root that
    isn't explicitly excluded. That drags the hand-written test suite into
    dist/ -- where the `files` allowlist would then publish it -- and makes the
    build type-check the test dependencies' .d.ts files, which fail under the
    generator's `moduleResolution: node`.

Kept here rather than inline in the workflows because both the generate and the
test workflow need it, and the two copies of the equivalent Python patch have
to be manually kept in sync.

Idempotent: it sets values rather than splicing text, so re-running changes
nothing. It does NOT touch `version` -- that flows from `npmVersion` in the
generator config via bump_version.py, and overwriting it here would silently
undo the bump.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

# Node 18 is the floor because typescript-fetch targets the platform's global
# fetch, which is not available earlier.
NODE_ENGINES = ">=18"

# Only built output ships. `files` is an allowlist and takes precedence over
# .npmignore, which is why the generated .npmignore is suppressed instead of
# maintained. npm always adds package.json and README on top of this.
PUBLISHED_FILES = ["dist"]

AUTHOR = "DDx API Team"
LICENSE = "MIT"
DESCRIPTION = "Node client for the DDx Interactions API, generated from the OpenAPI spec."
HOMEPAGE = "https://github.com/Movement-Infrastructure/interactions-api-sdks"

# Test-only dependencies for the smoke suite in test/. They live here because
# package.json is regenerated on every sync and hand-edits would be clobbered.
TEST_DEV_DEPENDENCIES = {
    "vitest": "^2.1.0",
    "msw": "^2.6.0",
}

TEST_SCRIPTS = {
    "test": "vitest run",
}

# Confines the build to the generated client. Without it the test suite lands
# in dist/ and its dependencies get type-checked by the build.
TSCONFIG_INCLUDE = ["src"]

# Generator defaults that must never reach a registry.
GENERATED_DEFAULT_AUTHORS = {"OpenAPI-Generator", "OpenAPI Generator Community"}


class PatchError(ValueError):
    """Raised when a generated file is missing or not shaped as expected."""


def patch_package(package: dict, expected_name: str | None = None) -> dict:
    """Return `package` with the publish-blocking fields filled in.

    Mutates and returns the same dict. Raises PatchError if the generator
    produced something unrecognisable, so a template change fails the build
    rather than silently publishing a package missing these fields.
    """
    if not isinstance(package, dict):
        raise PatchError("package.json did not parse to an object")

    for required in ("name", "version"):
        if not package.get(required):
            raise PatchError(
                f"package.json has no `{required}`; the generator did not run "
                f"with npmName set, or its template changed"
            )

    if expected_name is not None and package["name"] != expected_name:
        raise PatchError(
            f"package.json name is {package['name']!r}, expected {expected_name!r}; "
            f"npmName in the generator config and the publish target disagree"
        )

    package["description"] = DESCRIPTION
    package["author"] = AUTHOR
    package["license"] = LICENSE
    package["homepage"] = HOMEPAGE
    package["engines"] = {"node": NODE_ENGINES}
    package["files"] = list(PUBLISHED_FILES)

    package.setdefault("devDependencies", {}).update(TEST_DEV_DEPENDENCIES)
    package.setdefault("scripts", {}).update(TEST_SCRIPTS)

    return package


def patch_tsconfig(tsconfig: dict) -> dict:
    """Return `tsconfig` restricted to compiling the generated client."""
    if not isinstance(tsconfig, dict):
        raise PatchError("tsconfig.json did not parse to an object")

    if "compilerOptions" not in tsconfig:
        raise PatchError(
            "tsconfig.json has no `compilerOptions`; the generator template changed"
        )

    tsconfig["include"] = list(TSCONFIG_INCLUDE)
    return tsconfig


def check_no_generated_defaults(package: dict) -> list[str]:
    """Return a list of problems that should block a publish. Empty means clean."""
    problems = []

    if package.get("author") in GENERATED_DEFAULT_AUTHORS:
        problems.append(f"author is the generator default ({package['author']!r})")
    if not package.get("license"):
        problems.append("license is unset")
    if str(package.get("version", "")).startswith("0.0.0"):
        problems.append("version is the 0.0.0 placeholder; the version bump did not run")
    if not package.get("files"):
        problems.append("files allowlist is unset; the whole source tree would publish")

    return problems


def _read_json(path: Path) -> dict:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except OSError as exc:
        raise PatchError(f"cannot read {path}: {exc}") from exc
    except json.JSONDecodeError as exc:
        raise PatchError(f"{path} is not valid JSON: {exc}") from exc


def _write_json(path: Path, data: dict) -> None:
    # Trailing newline so the file matches what npm and editors write.
    path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Patch the generated Node SDK in place."
    )
    parser.add_argument(
        "sdk_dir",
        type=Path,
        help="The generated SDK directory, e.g. sdks/node/v1.",
    )
    parser.add_argument(
        "--expect-name",
        help="Fail unless package.json's name matches this, e.g. ddx-interactions-api.",
    )
    parser.add_argument(
        "--check-only",
        action="store_true",
        help="Report publish blockers without writing. For use as a publish gate.",
    )
    args = parser.parse_args(argv)

    package_path = args.sdk_dir / "package.json"
    tsconfig_path = args.sdk_dir / "tsconfig.json"

    try:
        package = _read_json(package_path)

        if args.check_only:
            problems = check_no_generated_defaults(package)
            for problem in problems:
                print(f"::error::{problem}")
            if problems:
                print("::error::Refusing to publish with generated-default metadata.")
                return 1
            print(f"Metadata checks passed: {package['name']} {package['version']}")
            return 0

        patched_package = patch_package(package, expected_name=args.expect_name)
        patched_tsconfig = patch_tsconfig(_read_json(tsconfig_path))
    except PatchError as exc:
        print(f"::error::{exc}", file=sys.stderr)
        return 2

    _write_json(package_path, patched_package)
    _write_json(tsconfig_path, patched_tsconfig)

    print(
        f"patched {package_path}: {patched_package['name']} {patched_package['version']}"
    )
    print(f"patched {tsconfig_path}: include={patched_tsconfig['include']}")
    return 0


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
