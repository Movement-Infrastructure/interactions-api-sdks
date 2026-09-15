#!/usr/bin/env python3
"""Check a generated SDK README before it becomes a registry page.

`patch_python_sdk.py` points setup.py's `long_description` at the README, so it
renders as the whole PyPI project page. It is regenerated on every spec sync,
which makes it published content that needs a check rather than a review habit.

Banned
    Text that must not reach a registry page. Every pattern here has been seen
    in the generator's default output.

Required
    Content a consumer needs. Catches a template override that silently stopped
    applying -- otherwise visible only as a wrong page on the registry.

The required list lives here rather than in each caller's argv: several
workflows run this, and if the gate from the publish path is spelled differently 
from the PR path it will not hold `--language` selects between the lists; only
the language name travels in argv, so the two paths for a language cannot
disagree about the content.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

PRODUCTION_HOST = "api.movementinfrastructure.org"

# (compiled pattern, why it must not appear)
BANNED = [
    (
        # The ruby generator writes `gem 'x', :git => '...'`; Bundler also
        # accepts `git:` and `github:`. All three bypass the registry.
        re.compile(
            r"pip install git\+"
            r"|gem ['\"]?[\w-]+['\"]?,\s*:?(?:git|github)\s*(?:=>|:)"
            r"|npm install git\+"
        ),
        "installs from a git URL, bypassing the registry the package is published to",
    ),
    (
        re.compile(r"setup\.py\s+install"),
        "documents `setup.py install`, which setuptools removed",
    ),
    (
        re.compile(r"org\.openapitools\.codegen"),
        "names the generator's internal Java class",
    ),
    # Any host on the API domain but the production one. Matching the shape
    # rather than a list of environment names keeps a newly added environment
    # from slipping through, and keeps their names out of this file.
    (
        re.compile(
            rf"\b(?!{re.escape(PRODUCTION_HOST)})[a-z0-9-]+\.movementinfrastructure\.org\b",
            re.IGNORECASE,
        ),
        f"names a host other than {PRODUCTION_HOST}; the spec's `servers` block "
        "is copied verbatim into the client",
    ),
    (
        re.compile(r"YOUR_(PASSWORD|USERNAME|API_KEY|ACCESS_TOKEN)"),
        "contains a credential placeholder that reads as a real instruction",
    ),
    (
        re.compile(r"^- Build date:", re.MULTILINE),
        "carries a build date, which churns the README on every run",
    ),
    # The generator links model and endpoint docs relative to the SDK
    # directory. This README renders on a registry page, where a relative link
    # resolves to nothing, and docs/ ships in neither package.
    (
        re.compile(r"\]\(docs/[A-Za-z0-9_]+\.md"),
        "links docs/ relatively; on a registry page that resolves to nothing",
    ),
]

# What templates/<language>/README.mustache exists to produce. The install
# command is load-bearing: each built-in template installs from a git URL or a
# locally built artifact, so its absence means the override stopped applying.
REQUIRED_BY_LANGUAGE = {
    "python": [
        "pip install ddx-interactions-api",
        "## Installation",
        "## Changelog",
    ],
    "ruby": [
        "gem install ddx_interactions_api",
        "## Installation",
        "## Changelog",
    ],
}

DEFAULT_LANGUAGE = "python"


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
        "--language",
        choices=sorted(REQUIRED_BY_LANGUAGE),
        default=DEFAULT_LANGUAGE,
        help=(
            "Which language's required-content list to apply. "
            f"Default: {DEFAULT_LANGUAGE}."
        ),
    )
    parser.add_argument(
        "--require",
        action="append",
        metavar="TEXT",
        help=(
            "Substring that must appear. Repeatable. Replaces the selected "
            "language's built-in list rather than adding to it."
        ),
    )
    args = parser.parse_args(argv)
    required = (
        REQUIRED_BY_LANGUAGE[args.language] if args.require is None else args.require
    )

    try:
        text = args.readme.read_text(encoding="utf-8")
    except OSError as exc:
        print(f"error: cannot read {args.readme}: {exc}", file=sys.stderr)
        return 2

    problems = check(text, required)

    for problem in problems:
        print(f"::error file={args.readme}::{problem}")

    if problems:
        print(f"::error::{args.readme} is not publishable; {len(problems)} problem(s).")
        return 1

    print(f"{args.readme}: OK ({len(text.splitlines())} lines)")
    return 0


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
