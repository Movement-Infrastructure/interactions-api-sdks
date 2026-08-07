#!/usr/bin/env python3
"""Compute and apply the next SDK package version from PR labels.

MIG-1925. Reads the current version from an openapi-generator config, decides a
bump from the PR's labels, and rewrites `packageVersion` so the generator emits
the new version into the package manifest as part of the same diff.

Label semantics match the repo's label descriptions and PR template:

    interactions-api-patch   bumps patch (C). The only label the tooling reads.
    interactions-api-minor   informational. Minor (B) is the default anyway.
    interactions-api-major   informational. Major (A) bumps are manual (MIG-1926);
                             this label only flags PRs that needed one.

So the label logic reduces to: patch label present -> patch, otherwise minor.
A major bump is reachable only via an explicit `--force-bump major`, which is
what the manual process in MIG-1926 calls.

The current version is read from a *separate* path than the one written, so the
workflow can read the base branch's committed version while writing the PR
branch's working copy. That makes re-runs idempotent: a PR whose labels change
three times still lands on one bump from the base, not three compounding ones.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from dataclasses import dataclass
from pathlib import Path

PATCH_LABEL = "interactions-api-patch"
MINOR_LABEL = "interactions-api-minor"
MAJOR_LABEL = "interactions-api-major"

DEFAULT_BUMP = "minor"
VALID_BUMPS = ("major", "minor", "patch")

# Matches the `packageVersion:` line in openapi-generator-config.yaml.
#
# Deliberately a line rewrite rather than a YAML load/dump round-trip: the
# config is hand-maintained and its comments carry the rationale for each
# field. PyYAML discards comments on dump, so a round-trip would silently
# strip them on the first bump.
_PACKAGE_VERSION_RE = re.compile(
    r"^(?P<prefix>[ \t]*packageVersion:[ \t]*)(?P<value>[^\s#]+)(?P<suffix>[ \t]*(?:#.*)?)$",
    re.MULTILINE,
)

_SEMVER_RE = re.compile(r"^(\d+)\.(\d+)\.(\d+)$")


class VersionError(ValueError):
    """Raised when a version string or config file can't be handled."""


@dataclass(frozen=True)
class Version:
    major: int
    minor: int
    patch: int

    def __str__(self) -> str:
        return f"{self.major}.{self.minor}.{self.patch}"


def parse_version(text: str) -> Version:
    """Parse a strict `A.B.C` version. Quotes are tolerated; suffixes are not.

    Pre-release and build metadata (`1.2.3-rc1`, `1.2.3+build`) are rejected
    rather than silently truncated — the pipeline has no story for them yet,
    and guessing would produce a wrong version in a published artifact.
    """
    stripped = text.strip().strip("\"'")
    match = _SEMVER_RE.match(stripped)
    if not match:
        raise VersionError(
            f"expected a version of the form A.B.C, got {text.strip()!r}"
        )
    return Version(*(int(part) for part in match.groups()))


def select_bump(labels: list[str]) -> str:
    """Decide the bump from PR label names.

    Only the patch label changes behavior. Minor is the default, so its label
    is decorative; major is manual, so its label is a flag for humans and is
    deliberately not honored here.
    """
    return "patch" if PATCH_LABEL in labels else DEFAULT_BUMP


def bump_version(version: Version, bump: str) -> Version:
    if bump == "major":
        return Version(version.major + 1, 0, 0)
    if bump == "minor":
        return Version(version.major, version.minor + 1, 0)
    if bump == "patch":
        return Version(version.major, version.minor, version.patch + 1)
    raise VersionError(f"unknown bump {bump!r}; expected one of {VALID_BUMPS}")


def read_package_version(config_text: str) -> Version:
    """Extract `packageVersion` from an openapi-generator config."""
    matches = _PACKAGE_VERSION_RE.findall(config_text)
    if not matches:
        raise VersionError("no `packageVersion:` line found in config")
    if len(matches) > 1:
        raise VersionError(
            f"found {len(matches)} `packageVersion:` lines in config; expected exactly one"
        )
    return parse_version(matches[0][1])


def write_package_version(config_text: str, version: Version) -> str:
    """Return the config with `packageVersion` set, leaving everything else byte-identical."""
    if not _PACKAGE_VERSION_RE.search(config_text):
        raise VersionError("no `packageVersion:` line found in config")

    def _replace(match: re.Match[str]) -> str:
        return f"{match.group('prefix')}{version}{match.group('suffix')}"

    updated, count = _PACKAGE_VERSION_RE.subn(_replace, config_text)
    if count != 1:
        raise VersionError(
            f"expected exactly one `packageVersion:` line to rewrite, rewrote {count}"
        )
    return updated


def _emit_github_output(pairs: dict[str, str]) -> None:
    """Append key=value lines to $GITHUB_OUTPUT when running under Actions."""
    output_path = os.environ.get("GITHUB_OUTPUT")
    if not output_path:
        return
    with open(output_path, "a", encoding="utf-8") as handle:
        for key, value in pairs.items():
            handle.write(f"{key}={value}\n")


def _parse_labels(raw: str | None) -> list[str]:
    """Parse the JSON array GitHub Actions produces for PR label names.

    `${{ toJSON(github.event.pull_request.labels.*.name) }}` renders a JSON
    array. An empty or absent value means an unlabeled PR, which is a normal
    state (it takes the default minor bump), not an error.
    """
    if not raw or not raw.strip():
        return []
    try:
        parsed = json.loads(raw)
    except json.JSONDecodeError as exc:
        raise VersionError(f"--labels-json is not valid JSON: {exc}") from exc
    if not isinstance(parsed, list) or not all(isinstance(x, str) for x in parsed):
        raise VersionError("--labels-json must be a JSON array of strings")
    return parsed


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Compute and apply the next SDK package version from PR labels."
    )
    parser.add_argument(
        "--current-config",
        type=Path,
        required=True,
        help=(
            "Config to read the current version from. In CI this is the base "
            "branch's copy, which is what makes re-runs idempotent."
        ),
    )
    parser.add_argument(
        "--write-config",
        type=Path,
        help=(
            "Config to rewrite with the new version. Omit for a dry run that "
            "only reports what would change."
        ),
    )
    parser.add_argument(
        "--labels-json",
        help='JSON array of PR label names, e.g. \'["interactions-api-patch"]\'.',
    )
    parser.add_argument(
        "--force-bump",
        choices=VALID_BUMPS,
        help=(
            "Override the label logic. `major` is the manual escape hatch "
            "documented in MIG-1926; labels never produce a major bump."
        ),
    )
    args = parser.parse_args(argv)

    try:
        current_text = args.current_config.read_text(encoding="utf-8")
    except OSError as exc:
        print(f"error: cannot read --current-config: {exc}", file=sys.stderr)
        return 2

    try:
        labels = _parse_labels(args.labels_json)
        current = read_package_version(current_text)
        bump = args.force_bump or select_bump(labels)
        nxt = bump_version(current, bump)
    except VersionError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2

    source = "--force-bump" if args.force_bump else "labels"
    print(f"current={current}")
    print(f"bump={bump} (from {source})")
    print(f"next={nxt}")

    # The major label is informational, and a PR carrying it without a manual
    # bump is a likely mistake. Surface it as an Actions warning rather than
    # failing: the author may have labelled it purely to flag the API break.
    if MAJOR_LABEL in labels and args.force_bump != "major":
        print(
            f"::warning::PR carries {MAJOR_LABEL} but major bumps are manual; "
            f"applying a {bump} bump instead. See MIG-1926."
        )

    if args.write_config:
        try:
            target_text = args.write_config.read_text(encoding="utf-8")
            args.write_config.write_text(
                write_package_version(target_text, nxt), encoding="utf-8"
            )
        except OSError as exc:
            print(f"error: cannot rewrite --write-config: {exc}", file=sys.stderr)
            return 2
        except VersionError as exc:
            print(f"error: {exc}", file=sys.stderr)
            return 2
        print(f"wrote packageVersion: {nxt} to {args.write_config}")

    _emit_github_output(
        {"current": str(current), "next": str(nxt), "bump": bump}
    )
    return 0


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
