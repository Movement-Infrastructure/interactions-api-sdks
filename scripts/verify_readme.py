#!/usr/bin/env python3
"""Check a generated SDK README before it becomes a registry page.

The README is published content: `patch_python_sdk.py` points setup.py's
`long_description` at it, which is what PyPI renders as the whole project page.
That puts it in scope for docs/publish-leak-audit-checklist.md section 3, and
it is generated on every sync, so it needs a check rather than a review habit.

Two classes of rule:

Banned
    Text that must never reach a registry page -- an install command pointing
    at this private repository, a removed setuptools invocation, an internal
    Java class name, a non-production hostname. Each has been observed in the
    generator's default output; see templates/python/README.mustache.

Required
    Sections and the install command a consumer needs. Catches a template
    override that silently stopped being applied, which otherwise shows up
    only as a wrong README on the registry.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

# (compiled pattern, why it must not appear)
BANNED = [
    (
        re.compile(r"pip install git\+|gem ['\"]?\w+['\"]?, *git:|npm install git\+"),
        "installs from a git URL; this repository is private and that is not how "
        "a published package is installed",
    ),
    (
        re.compile(r"setup\.py\s+install"),
        "documents `setup.py install`, which setuptools removed",
    ),
    (
        re.compile(r"org\.openapitools\.codegen"),
        "leaks the generator's internal Java class name",
    ),
    (
        re.compile(r"\bapi-dev\.movementinfrastructure\.org\b"),
        "names a non-production host (leak-audit finding F4)",
    ),
    (
        re.compile(r"YOUR_(PASSWORD|USERNAME|API_KEY|ACCESS_TOKEN)"),
        "contains a credential placeholder that reads as a real instruction",
    ),
    (
        re.compile(r"^- Build date:", re.MULTILINE),
        "carries a build date, which churns the generated README on every run",
    ),
]


class ReadmeError(ValueError):
    """Raised when the README can't be read."""


def check(text: str, required: list[str]) -> list[str]:
    """Return a list of problems. Empty means the README is publishable."""
    problems = []

    for pattern, why in BANNED:
        match = pattern.search(text)
        if match:
            line = text.count("\n", 0, match.start()) + 1
            problems.append(f"line {line}: {match.group(0)!r} — {why}")

    for needle in required:
        if needle not in text:
            problems.append(f"missing required content: {needle!r}")

    return problems


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Check a generated SDK README before it becomes a registry page."
    )
    parser.add_argument("readme", type=Path, help="Path to the generated README.md.")
    parser.add_argument(
        "--require",
        action="append",
        default=[],
        metavar="TEXT",
        help="Substring that must appear. Repeatable.",
    )
    args = parser.parse_args(argv)

    try:
        text = args.readme.read_text(encoding="utf-8")
    except OSError as exc:
        print(f"error: cannot read {args.readme}: {exc}", file=sys.stderr)
        return 2

    problems = check(text, args.require)

    for problem in problems:
        print(f"::error file={args.readme}::{problem}")

    if problems:
        print(f"::error::{args.readme} is not publishable; {len(problems)} problem(s).")
        return 1

    print(f"{args.readme}: OK ({len(text.splitlines())} lines)")
    return 0


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
