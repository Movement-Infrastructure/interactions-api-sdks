#!/usr/bin/env python3
"""Compute and apply the next SDK package version from PR labels.

Reads the current version from an openapi-generator config, decides a bump from
the PR's labels, and rewrites the version key so the generator emits the new
version into the package manifest.

    interactions-api-major   bumps major (A); wins over the others
    interactions-api-patch   bumps patch (C)
    interactions-api-minor   no effect; minor (B) is the default

The version is read from a different path than the one written, so CI can read
the base branch while writing the PR branch. That keeps re-runs idempotent: a
PR whose labels change three times still lands one bump ahead of its base.

Each generator names its version key differently -- `packageVersion` for Python,
`gemVersion` for Ruby, `npmVersion` for TypeScript -- so the key is a parameter.
It defaults to `packageVersion` because that is the most common spelling, but
passing the wrong one is an error rather than a silent no-op.
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

DEFAULT_VERSION_KEY = "packageVersion"

_SEMVER_RE = re.compile(r"^(\d+)\.(\d+)\.(\d+)$")

# Guards against a key that would change the regex's meaning rather than the
# text it matches.
_KEY_RE = re.compile(r"^[A-Za-z_][A-Za-z0-9_]*$")


def _version_re(key: str) -> re.Pattern[str]:
    """Build the line matcher for `key`.
    """
    if not _KEY_RE.match(key):
        raise VersionError(
            f"invalid version key {key!r}; expected an identifier like "
            f"'packageVersion' or 'gemVersion'"
        )
    return re.compile(
        rf"^(?P<prefix>[ \t]*{re.escape(key)}:[ \t]*)(?P<value>[^\s#]+)"
        rf"(?P<suffix>[ \t]*(?:#.*)?)$",
        re.MULTILINE,
    )


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

    Pre-release and build metadata are rejected rather than truncated. The
    pipeline has no story for them, and guessing would put a wrong version in
    a published artifact.
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

    Largest label wins. A PR carrying both major and patch is contradictory,
    and treating a declared breaking change as breaking is the safe reading.
    """
    if MAJOR_LABEL in labels:
        return "major"
    if PATCH_LABEL in labels:
        return "patch"
    return DEFAULT_BUMP


def bump_version(version: Version, bump: str) -> Version:
    if bump == "major":
        return Version(version.major + 1, 0, 0)
    if bump == "minor":
        return Version(version.major, version.minor + 1, 0)
    if bump == "patch":
        return Version(version.major, version.minor, version.patch + 1)
    raise VersionError(f"unknown bump {bump!r}; expected one of {VALID_BUMPS}")


def read_package_version(config_text: str, key: str = DEFAULT_VERSION_KEY) -> Version:
    """Extract the version keyed by `key` from an openapi-generator config."""
    matches = _version_re(key).findall(config_text)
    if not matches:
        raise VersionError(f"no `{key}:` line found in config")
    if len(matches) > 1:
        raise VersionError(
            f"found {len(matches)} `{key}:` lines in config; expected exactly one"
        )
    return parse_version(matches[0][1])


def write_package_version(
    config_text: str, version: Version, key: str = DEFAULT_VERSION_KEY
) -> str:
    """Return the config with `key` set, leaving everything else byte-identical."""
    pattern = _version_re(key)
    if not pattern.search(config_text):
        raise VersionError(f"no `{key}:` line found in config")

    def _replace(match: re.Match[str]) -> str:
        return f"{match.group('prefix')}{version}{match.group('suffix')}"

    updated, count = pattern.subn(_replace, config_text)
    if count != 1:
        raise VersionError(
            f"expected exactly one `{key}:` line to rewrite, rewrote {count}"
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

    An empty or absent value means an unlabeled PR, which is normal and takes
    the default minor bump.
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
            "Override the label logic, for a bump run by hand outside a PR. "
            "In CI the labels decide."
        ),
    )
    parser.add_argument(
        "--version-key",
        default=DEFAULT_VERSION_KEY,
        help=(
            "Config key holding the version. Differs per generator: "
            "packageVersion (Python, C#), gemVersion (Ruby), npmVersion "
            f"(TypeScript). Default: {DEFAULT_VERSION_KEY}."
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
        current = read_package_version(current_text, args.version_key)
        bump = args.force_bump or select_bump(labels)
        nxt = bump_version(current, bump)
    except VersionError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2

    source = "--force-bump" if args.force_bump else "labels"
    print(f"current={current}")
    print(f"bump={bump} (from {source})")
    print(f"next={nxt}")

    # A major bump is the one outcome that breaks consumers, so make it visible
    # in the run log.
    if bump == "major":
        print(
            f"::notice::Applying a MAJOR bump {current} -> {nxt}. "
            "Confirm the breaking change is documented for consumers."
        )

    if args.write_config:
        try:
            target_text = args.write_config.read_text(encoding="utf-8")
            args.write_config.write_text(
                write_package_version(target_text, nxt, args.version_key),
                encoding="utf-8",
            )
        except OSError as exc:
            print(f"error: cannot rewrite --write-config: {exc}", file=sys.stderr)
            return 2
        except VersionError as exc:
            print(f"error: {exc}", file=sys.stderr)
            return 2
        print(f"wrote {args.version_key}: {nxt} to {args.write_config}")

    _emit_github_output(
        {"current": str(current), "next": str(nxt), "bump": bump}
    )
    return 0


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
