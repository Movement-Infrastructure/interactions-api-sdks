#!/usr/bin/env python3
"""Render an SDK CHANGELOG entry from `oasdiff changelog -f json` output.

Consumes JSON rather than oasdiff's own markdown for three reasons: its
markdown emits a `# API Changelog v1 vs. v1` heading that says nothing (the
sync workflow's cutover guard already enforces matching `info.version`), it
reports the same schema change once per request media type -- three times over,
for a spec declaring `application/json`, `text/json` and `application/*+json`
-- and it has no place to put the package version the entry needs to be filed
under.

The entry is read from one changelog and written to another, the same split
bump_version.py uses: CI reads the base branch's copy and writes the PR
branch's. That is what keeps re-runs idempotent. The generate workflows fire on
`labeled`/`unlabeled`, so a reviewer applying `interactions-api-major` after
the PR opens recomputes the version -- and this regenerates the entry against
an unchanged base rather than appending a second one.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path

HEADER = """\
# Changelog

Generated from `openapi/v1/swagger.json` by `.github/workflows/generate-*-sdk.yml`.
Do not edit by hand; edits are overwritten on the next spec sync.
"""

# oasdiff severity levels. 3 is what it counts as a breaking change and what
# `oasdiff breaking --fail-on ERR` exits non-zero on.
LEVEL_ERR = 3
LEVEL_WARN = 2

LEVEL_MARKERS = {
    LEVEL_ERR: "**breaking** ",
    LEVEL_WARN: "_warning_ ",
}

# oasdiff appends the media type to the message, which turns one schema change
# into one line per declared request media type. The change is the same change.
_MEDIA_TYPE_SUFFIX = re.compile(r"\s*\(media type: [^)]+\)")

# Anchors the prepend. Entries go directly below the header, newest first.
_ENTRY_MARKER = "\n## "


class ChangelogError(ValueError):
    """Raised when oasdiff output or a changelog file can't be handled."""


@dataclass(frozen=True)
class Change:
    """One deduplicated change, keyed by where it applies."""

    level: int
    operation: str
    path: str
    text: str

    @property
    def heading(self) -> str:
        """The section this change is filed under."""
        if self.operation and self.path:
            return f"{self.operation} {self.path}"
        return "General"


def _strip_media_type(text: str) -> str:
    return _MEDIA_TYPE_SUFFIX.sub("", text)


def parse_changes(raw: str) -> list[Change]:
    """Parse `oasdiff changelog -f json` output into deduplicated changes.

    oasdiff emits `[]` for no changes, which is a valid empty result rather
    than an error.
    """
    try:
        entries = json.loads(raw or "[]")
    except json.JSONDecodeError as exc:
        raise ChangelogError(f"oasdiff output is not valid JSON: {exc}") from exc

    if entries is None:
        return []
    if not isinstance(entries, list):
        raise ChangelogError("expected oasdiff output to be a JSON array")

    seen: set[Change] = set()
    changes: list[Change] = []

    for entry in entries:
        if not isinstance(entry, dict):
            raise ChangelogError("expected each oasdiff entry to be an object")
        if "text" not in entry:
            raise ChangelogError("oasdiff entry has no `text`; output format changed")

        change = Change(
            level=int(entry.get("level", LEVEL_WARN)),
            operation=str(entry.get("operation", "")),
            path=str(entry.get("path", "")),
            text=_strip_media_type(str(entry["text"])),
        )

        # Order-preserving dedupe: the media-type duplicates collapse here.
        if change not in seen:
            seen.add(change)
            changes.append(change)

    return changes


def render_entry(changes: list[Change], version: str, date: str) -> str:
    """Render one changelog entry. Returns "" when there is nothing to report."""
    if not changes:
        return ""

    # Breaking changes first within each section; oasdiff's own order otherwise.
    by_heading: dict[str, list[Change]] = {}
    for change in changes:
        by_heading.setdefault(change.heading, []).append(change)

    lines = [f"## {version} — {date}", ""]

    for heading in sorted(by_heading, key=lambda h: (h == "General", h)):
        lines.append(f"### {heading}")
        for change in sorted(by_heading[heading], key=lambda c: -c.level):
            marker = LEVEL_MARKERS.get(change.level, "")
            lines.append(f"- {marker}{change.text}")
        lines.append("")

    return "\n".join(lines)


def prepend_entry(existing: str, entry: str) -> str:
    """Insert `entry` below the header and above any older entries."""
    if not entry:
        return existing

    if not existing.strip():
        return f"{HEADER}\n{entry}"

    index = existing.find(_ENTRY_MARKER)
    if index == -1:
        # No entries yet: header only.
        return f"{existing.rstrip()}\n\n{entry}"

    head = existing[:index].rstrip()
    tail = existing[index:].lstrip("\n")
    return f"{head}\n\n{entry}\n{tail}"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Render an SDK CHANGELOG entry from oasdiff JSON output."
    )
    parser.add_argument(
        "--oasdiff-json",
        type=Path,
        required=True,
        help="File holding `oasdiff changelog -f json` output. `-` reads stdin.",
    )
    parser.add_argument("--version", required=True, help="Package version to file the entry under.")
    parser.add_argument("--date", required=True, help="Entry date, ISO 8601 (YYYY-MM-DD).")
    parser.add_argument(
        "--current-changelog",
        type=Path,
        help=(
            "Changelog to read existing entries from. In CI this is the base "
            "branch's copy, which is what makes re-runs idempotent. Absent or "
            "missing means the changelog is being created."
        ),
    )
    parser.add_argument(
        "--write-changelog",
        type=Path,
        help="Changelog to write. Omit for a dry run that prints the entry only.",
    )
    args = parser.parse_args(argv)

    if str(args.oasdiff_json) == "-":
        raw = sys.stdin.read()
    else:
        try:
            raw = args.oasdiff_json.read_text(encoding="utf-8")
        except OSError as exc:
            print(f"error: cannot read --oasdiff-json: {exc}", file=sys.stderr)
            return 2

    try:
        changes = parse_changes(raw)
    except ChangelogError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2

    entry = render_entry(changes, args.version, args.date)

    if not entry:
        # A spec edit that changes no part of the API contract -- a description
        # reworded, an example added. Nothing worth a changelog line.
        print("No API changes reported by oasdiff; leaving the changelog alone.")
        return 0

    breaking = sum(1 for c in changes if c.level >= LEVEL_ERR)
    print(f"{len(changes)} change(s), {breaking} breaking, filed under {args.version}.")

    if not args.write_changelog:
        print()
        print(entry)
        return 0

    existing = ""
    if args.current_changelog and args.current_changelog.exists():
        try:
            existing = args.current_changelog.read_text(encoding="utf-8")
        except OSError as exc:
            print(f"error: cannot read --current-changelog: {exc}", file=sys.stderr)
            return 2

    try:
        args.write_changelog.parent.mkdir(parents=True, exist_ok=True)
        args.write_changelog.write_text(
            prepend_entry(existing, entry), encoding="utf-8"
        )
    except OSError as exc:
        print(f"error: cannot write --write-changelog: {exc}", file=sys.stderr)
        return 2

    print(f"wrote {args.write_changelog}")
    return 0


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
