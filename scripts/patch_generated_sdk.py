#!/usr/bin/env python3
"""Apply post-generation fixes to the generated Python SDK.

Two defects come from openapi-generator's Python template and no config option
controls either, so they are patched after generation and before the commit.
See MIG-2365.

    1. setup.py defines PYTHON_REQUIRES and never passes it to setup(), so the
       wheel ships no Requires-Python and pip installs on any Python version.

    2. The package neither depends on certifi nor defaults ssl_ca_cert, so it
       falls back to OpenSSL's default trust store. On a python.org macOS build
       that store is empty and the first HTTPS call dies with
       CERTIFICATE_VERIFY_FAILED. urllib3 2.x does not pick up certifi on its
       own, so the dependency alone is not enough -- ssl_ca_cert has to default
       to certifi.where() as well.

Every patch is anchored to exact generated text. A missing anchor is a hard
error, never a silent skip: if a generator upgrade rewrites the template, the
build fails here rather than publishing a package quietly missing these fixes.

Patches are idempotent, so running twice over the same tree is a no-op.
"""

from __future__ import annotations

import argparse
import sys
from dataclasses import dataclass
from pathlib import Path

CERTIFI_REQUIREMENT = "certifi >= 2024.2.2"


class PatchError(RuntimeError):
    """Raised when an anchor no longer matches the generated output."""


@dataclass(frozen=True)
class Patch:
    """A single anchored substitution.

    `applied_marker` is what the patched text looks like afterwards. It is
    checked first so a second run reports "already applied" instead of failing
    on an anchor its own first run consumed.
    """

    path: str
    anchor: str
    replacement: str
    applied_marker: str
    description: str


PATCHES = (
    Patch(
        path="setup.py",
        anchor="    install_requires=REQUIRES,\n",
        replacement="    python_requires=PYTHON_REQUIRES,\n    install_requires=REQUIRES,\n",
        applied_marker="    python_requires=PYTHON_REQUIRES,\n",
        description="pass PYTHON_REQUIRES to setup() so the wheel declares Requires-Python",
    ),
    Patch(
        path="setup.py",
        anchor='    "typing-extensions >= 4.7.1",\n]',
        replacement=f'    "typing-extensions >= 4.7.1",\n    "{CERTIFI_REQUIREMENT}",\n]',
        applied_marker=f'"{CERTIFI_REQUIREMENT}"',
        description="add certifi to setup.py REQUIRES",
    ),
    Patch(
        path="requirements.txt",
        anchor="typing-extensions >= 4.7.1\n",
        replacement=f"typing-extensions >= 4.7.1\n{CERTIFI_REQUIREMENT}\n",
        applied_marker=CERTIFI_REQUIREMENT,
        description="add certifi to requirements.txt",
    ),
    Patch(
        path="{package}/configuration.py",
        anchor="import urllib3\n",
        replacement="import certifi\nimport urllib3\n",
        applied_marker="import certifi\n",
        description="import certifi in configuration.py",
    ),
    Patch(
        path="{package}/configuration.py",
        anchor="        self.ssl_ca_cert = ssl_ca_cert\n",
        replacement=(
            "        self.ssl_ca_cert = (\n"
            "            ssl_ca_cert if ssl_ca_cert is not None else certifi.where()\n"
            "        )\n"
        ),
        applied_marker="else certifi.where()",
        description="default ssl_ca_cert to certifi.where()",
    ),
)


def apply_patch(sdk_root: Path, package: str, patch: Patch) -> bool:
    """Apply one patch. Returns True if it changed the file, False if already applied.

    Raises PatchError if the target is missing or the anchor does not match
    exactly once.
    """
    target = sdk_root / patch.path.format(package=package)

    if not target.exists():
        raise PatchError(f"{target} does not exist; cannot apply: {patch.description}")

    text = target.read_text(encoding="utf-8")

    if patch.applied_marker in text:
        return False

    count = text.count(patch.anchor)
    if count != 1:
        raise PatchError(
            f"{target}: expected exactly 1 occurrence of the anchor for "
            f"{patch.description!r}, found {count}. The generator template "
            f"likely changed; update PATCHES in scripts/patch_generated_sdk.py.\n"
            f"  anchor: {patch.anchor!r}"
        )

    target.write_text(text.replace(patch.anchor, patch.replacement), encoding="utf-8")
    return True


def patch_sdk(sdk_root: Path, package: str) -> list[str]:
    """Apply every patch under `sdk_root`. Returns a log line per patch."""
    if not sdk_root.is_dir():
        raise PatchError(f"{sdk_root} is not a directory")

    results = []
    for patch in PATCHES:
        changed = apply_patch(sdk_root, package, patch)
        results.append(f"{'patched' if changed else 'already applied'}: {patch.description}")
    return results


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--sdk-root",
        type=Path,
        default=Path("sdks/python/v1"),
        help="Directory openapi-generator wrote the SDK into.",
    )
    parser.add_argument(
        "--package",
        default="ddx_interactions_api",
        help="Python package name inside --sdk-root (the generator's packageName).",
    )
    args = parser.parse_args(argv)

    try:
        for line in patch_sdk(args.sdk_root, args.package):
            print(line)
    except PatchError as exc:
        print(f"::error::{exc}", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
