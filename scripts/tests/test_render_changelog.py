"""Unit tests for scripts/render_changelog.py."""

import json

import pytest

from render_changelog import (
    EXIT_UNDECLARED_BREAKING,
    HEADER,
    NO_CHANGES_TEXT,
    Change,
    ChangelogError,
    main,
    parse_changes,
    prepend_entry,
    render_entry,
    render_no_changes_entry,
)

# oasdiff output for a spec edit that touched no part of the contract -- a
# description reworded, an example added.
NO_CHANGES_JSON = "[]"

# Only the informational half of OASDIFF_JSON, for the cases that need a diff
# with nothing breaking in it.
NON_BREAKING_JSON = json.dumps(
    [
        {
            "id": "endpoint-added",
            "text": "endpoint added",
            "level": 1,
            "operation": "GET",
            "path": "/v{version}/auth/me",
            "section": "paths",
            "fingerprint": "a1b2c3d4e5f6",
        }
    ]
)

# Verbatim `oasdiff changelog -f json` output, taken from a real run against
# openapi/v1/swagger.json. The three vendorSource entries are the same schema
# change reported once per declared request media type -- collapsing them is
# the property under test.
OASDIFF_JSON = json.dumps(
    [
        {
            "id": "request-property-became-required",
            "text": "the request property `interactions/items/vendorSource` became required (media type: text/json)",
            "level": 3,
            "operation": "POST",
            "path": "/v{version}/interactions",
            "section": "paths",
            "fingerprint": "b9b4f02339df",
        },
        {
            "id": "request-property-became-required",
            "text": "the request property `interactions/items/vendorSource` became required (media type: application/json)",
            "level": 3,
            "operation": "POST",
            "path": "/v{version}/interactions",
            "section": "paths",
            "fingerprint": "b9b4f02339e0",
        },
        {
            "id": "request-property-became-required",
            "text": "the request property `interactions/items/vendorSource` became required (media type: application/*+json)",
            "level": 3,
            "operation": "POST",
            "path": "/v{version}/interactions",
            "section": "paths",
            "fingerprint": "b9b4f02339e1",
        },
        {
            "id": "endpoint-added",
            "text": "endpoint added",
            "level": 1,
            "operation": "GET",
            "path": "/v{version}/auth/me",
            "section": "paths",
            "fingerprint": "a1b2c3d4e5f6",
        },
    ]
)


class TestParseChanges:
    def test_collapses_media_type_duplicates(self):
        changes = parse_changes(OASDIFF_JSON)
        assert len(changes) == 2

    def test_strips_the_media_type_suffix(self):
        required = next(c for c in parse_changes(OASDIFF_JSON) if c.level == 3)
        assert "media type" not in required.text
        assert required.text.endswith("became required")

    def test_preserves_oasdiff_order(self):
        changes = parse_changes(OASDIFF_JSON)
        assert changes[0].operation == "POST"
        assert changes[1].operation == "GET"

    def test_empty_array_is_no_changes(self):
        assert parse_changes("[]") == []

    def test_empty_input_is_no_changes(self):
        assert parse_changes("") == []

    def test_null_is_no_changes(self):
        assert parse_changes("null") == []

    def test_rejects_invalid_json(self):
        with pytest.raises(ChangelogError, match="not valid JSON"):
            parse_changes("{not json")

    def test_rejects_a_non_array(self):
        with pytest.raises(ChangelogError, match="JSON array"):
            parse_changes('{"id": "x"}')

    def test_rejects_an_entry_without_text(self):
        with pytest.raises(ChangelogError, match="no `text`"):
            parse_changes('[{"id": "x", "level": 1}]')


class TestRenderEntry:
    def test_no_changes_renders_nothing(self):
        assert render_entry([], "1.0.0", "2026-09-01") == ""

    def test_heads_the_entry_with_version_and_date(self):
        entry = render_entry(parse_changes(OASDIFF_JSON), "0.2.0", "2026-09-01")
        assert entry.startswith("## 0.2.0 — 2026-09-01")

    def test_groups_by_operation_and_path(self):
        entry = render_entry(parse_changes(OASDIFF_JSON), "0.2.0", "2026-09-01")
        assert "### POST /v{version}/interactions" in entry
        assert "### GET /v{version}/auth/me" in entry

    def test_marks_breaking_changes(self):
        entry = render_entry(parse_changes(OASDIFF_JSON), "0.2.0", "2026-09-01")
        assert "- **breaking** the request property" in entry

    def test_leaves_informational_changes_unmarked(self):
        entry = render_entry(parse_changes(OASDIFF_JSON), "0.2.0", "2026-09-01")
        assert "- endpoint added" in entry

    def test_sorts_breaking_changes_first_within_a_section(self):
        changes = [
            Change(level=1, operation="POST", path="/x", text="info thing"),
            Change(level=3, operation="POST", path="/x", text="breaking thing"),
        ]
        entry = render_entry(changes, "1.0.0", "2026-09-01")
        assert entry.index("breaking thing") < entry.index("info thing")

    def test_files_pathless_changes_under_general(self):
        changes = [Change(level=1, operation="", path="", text="api description changed")]
        assert "### General" in render_entry(changes, "1.0.0", "2026-09-01")

    def test_general_sorts_last(self):
        changes = [
            Change(level=1, operation="", path="", text="general thing"),
            Change(level=1, operation="GET", path="/x", text="endpoint thing"),
        ]
        entry = render_entry(changes, "1.0.0", "2026-09-01")
        assert entry.index("endpoint thing") < entry.index("general thing")


class TestRenderNoChangesEntry:
    def test_heads_the_entry_with_version_and_date(self):
        entry = render_no_changes_entry("0.2.0", "2026-09-01")
        assert entry.startswith("## 0.2.0 — 2026-09-01")

    def test_says_the_contract_did_not_change(self):
        assert NO_CHANGES_TEXT in render_no_changes_entry("0.2.0", "2026-09-01")

    def test_prepends_like_any_other_entry(self):
        older = "## 0.1.0 — 2026-08-01\n\n### GET /y\n- endpoint added\n"
        result = prepend_entry(
            f"{HEADER}\n{older}", render_no_changes_entry("0.2.0", "2026-09-01")
        )
        assert result.index("0.2.0") < result.index("0.1.0")


class TestPrependEntry:
    ENTRY = "## 0.2.0 — 2026-09-01\n\n### GET /x\n- endpoint added\n"
    OLDER = "## 0.1.0 — 2026-08-01\n\n### GET /y\n- endpoint added\n"

    def test_creates_the_file_with_a_header(self):
        result = prepend_entry("", self.ENTRY)
        assert result.startswith("# Changelog")
        assert self.ENTRY in result

    def test_adds_the_first_entry_below_a_header_only_file(self):
        result = prepend_entry(HEADER, self.ENTRY)
        assert result.startswith("# Changelog")
        assert self.ENTRY.strip() in result

    def test_puts_the_newest_entry_first(self):
        existing = f"{HEADER}\n{self.OLDER}"
        result = prepend_entry(existing, self.ENTRY)
        assert result.index("0.2.0") < result.index("0.1.0")

    def test_keeps_the_header_above_all_entries(self):
        existing = f"{HEADER}\n{self.OLDER}"
        result = prepend_entry(existing, self.ENTRY)
        assert result.index("# Changelog") < result.index("0.2.0")

    def test_preserves_older_entries(self):
        existing = f"{HEADER}\n{self.OLDER}"
        assert "0.1.0" in prepend_entry(existing, self.ENTRY)

    def test_an_empty_entry_changes_nothing(self):
        existing = f"{HEADER}\n{self.OLDER}"
        assert prepend_entry(existing, "") == existing


class TestMain:
    def _args(self, tmp_path, **overrides):
        source = tmp_path / "oasdiff.json"
        source.write_text(OASDIFF_JSON, encoding="utf-8")
        args = {
            "--oasdiff-json": str(source),
            "--version": "0.2.0",
            "--date": "2026-09-01",
        }
        args.update(overrides)
        return [item for pair in args.items() for item in pair]

    def test_dry_run_writes_nothing(self, tmp_path):
        target = tmp_path / "CHANGELOG.md"
        assert main(self._args(tmp_path)) == 0
        assert not target.exists()

    def test_writes_the_changelog(self, tmp_path):
        target = tmp_path / "CHANGELOG.md"
        assert main(self._args(tmp_path, **{"--write-changelog": str(target)})) == 0

        written = target.read_text(encoding="utf-8")
        assert written.startswith("# Changelog")
        assert "## 0.2.0 — 2026-09-01" in written
        assert "**breaking**" in written

    def test_reads_existing_entries_from_the_current_changelog(self, tmp_path):
        current = tmp_path / "base" / "CHANGELOG.md"
        current.parent.mkdir()
        current.write_text(f"{HEADER}\n## 0.1.0 — 2026-08-01\n\n### GET /y\n- endpoint added\n", encoding="utf-8")
        target = tmp_path / "CHANGELOG.md"

        main(
            self._args(
                tmp_path,
                **{"--current-changelog": str(current), "--write-changelog": str(target)},
            )
        )

        written = target.read_text(encoding="utf-8")
        assert written.index("0.2.0") < written.index("0.1.0")

    def test_rerunning_against_the_same_base_is_idempotent(self, tmp_path):
        # The generate workflows re-run on labeled/unlabeled. Reading from an
        # unchanged base is what stops a second entry being appended.
        current = tmp_path / "base" / "CHANGELOG.md"
        current.parent.mkdir()
        current.write_text(HEADER, encoding="utf-8")
        target = tmp_path / "CHANGELOG.md"

        args = self._args(
            tmp_path,
            **{"--current-changelog": str(current), "--write-changelog": str(target)},
        )
        main(args)
        once = target.read_text(encoding="utf-8")
        main(args)
        assert target.read_text(encoding="utf-8") == once

    def test_a_version_change_replaces_rather_than_appends(self, tmp_path):
        # A reviewer applying interactions-api-major re-runs the bump, so the
        # same spec diff must be re-filed under the new version, not both.
        current = tmp_path / "base" / "CHANGELOG.md"
        current.parent.mkdir()
        current.write_text(HEADER, encoding="utf-8")
        target = tmp_path / "CHANGELOG.md"

        main(self._args(tmp_path, **{"--current-changelog": str(current), "--write-changelog": str(target), "--version": "0.2.0"}))
        main(self._args(tmp_path, **{"--current-changelog": str(current), "--write-changelog": str(target), "--version": "1.0.0"}))

        written = target.read_text(encoding="utf-8")
        assert "1.0.0" in written
        assert "0.2.0" not in written

    def test_no_changes_still_files_an_entry(self, tmp_path):
        # A version that reaches the registry with no line here reads as a gap
        # in the record rather than as a release that changed no contract.
        source = tmp_path / "oasdiff.json"
        source.write_text(NO_CHANGES_JSON, encoding="utf-8")
        target = tmp_path / "CHANGELOG.md"

        code = main([
            "--oasdiff-json", str(source),
            "--version", "0.2.0",
            "--date", "2026-09-01",
            "--write-changelog", str(target),
        ])

        assert code == 0
        written = target.read_text(encoding="utf-8")
        assert written.startswith("# Changelog")
        assert "## 0.2.0 — 2026-09-01" in written
        assert NO_CHANGES_TEXT in written

    def test_no_changes_replaces_a_stale_entry_from_an_earlier_run(self, tmp_path):
        # The failure this closes: run 1 committed an entry to the PR branch,
        # then the spec change it described was reverted. Skipping the write
        # would leave that entry in place to be merged.
        current = tmp_path / "base" / "CHANGELOG.md"
        current.parent.mkdir()
        current.write_text(HEADER, encoding="utf-8")

        target = tmp_path / "CHANGELOG.md"
        target.write_text(
            f"{HEADER}\n## 0.2.0 — 2026-09-01\n\n### POST /x\n"
            "- **breaking** the request property `x` became required\n",
            encoding="utf-8",
        )

        source = tmp_path / "oasdiff.json"
        source.write_text(NO_CHANGES_JSON, encoding="utf-8")

        assert main([
            "--oasdiff-json", str(source),
            "--version", "0.2.0",
            "--date", "2026-09-02",
            "--current-changelog", str(current),
            "--write-changelog", str(target),
        ]) == 0

        written = target.read_text(encoding="utf-8")
        assert "became required" not in written
        assert NO_CHANGES_TEXT in written

    def test_missing_oasdiff_file_is_an_error(self, tmp_path):
        assert main([
            "--oasdiff-json", str(tmp_path / "nope.json"),
            "--version", "0.2.0",
            "--date", "2026-09-01",
        ]) == 2

    def test_invalid_oasdiff_json_is_an_error(self, tmp_path):
        source = tmp_path / "oasdiff.json"
        source.write_text("{not json", encoding="utf-8")
        assert main([
            "--oasdiff-json", str(source),
            "--version", "0.2.0",
            "--date", "2026-09-01",
        ]) == 2


class TestBreakingChangeGuard:
    """`--bump` cross-checks the label-derived version against the real diff."""

    def _run(self, tmp_path, oasdiff_json, bump=None, write=True):
        source = tmp_path / "oasdiff.json"
        source.write_text(oasdiff_json, encoding="utf-8")
        target = tmp_path / "CHANGELOG.md"

        argv = [
            "--oasdiff-json", str(source),
            "--version", "0.2.0",
            "--date", "2026-09-01",
        ]
        if bump:
            argv += ["--bump", bump]
        if write:
            argv += ["--write-changelog", str(target)]

        return main(argv), target

    def test_breaking_under_a_minor_bump_fails(self, tmp_path):
        code, _ = self._run(tmp_path, OASDIFF_JSON, bump="minor")
        assert code == EXIT_UNDECLARED_BREAKING

    def test_breaking_under_a_patch_bump_fails(self, tmp_path):
        code, _ = self._run(tmp_path, OASDIFF_JSON, bump="patch")
        assert code == EXIT_UNDECLARED_BREAKING

    def test_a_failed_guard_writes_nothing(self, tmp_path):
        # The generate workflow commits whatever is on disk after this step, so
        # a rejected run must not leave a changelog behind.
        _, target = self._run(tmp_path, OASDIFF_JSON, bump="minor")
        assert not target.exists()

    def test_a_failed_guard_prints_the_entry(self, tmp_path, capsys):
        self._run(tmp_path, OASDIFF_JSON, bump="minor")
        assert "**breaking**" in capsys.readouterr().out

    def test_the_error_names_the_label_to_apply(self, tmp_path, capsys):
        self._run(tmp_path, OASDIFF_JSON, bump="minor")
        assert "interactions-api-major" in capsys.readouterr().err

    def test_breaking_under_a_major_bump_passes(self, tmp_path):
        code, target = self._run(tmp_path, OASDIFF_JSON, bump="major")
        assert code == 0
        assert "**breaking**" in target.read_text(encoding="utf-8")

    def test_a_non_breaking_diff_passes_under_a_minor_bump(self, tmp_path):
        code, target = self._run(tmp_path, NON_BREAKING_JSON, bump="minor")
        assert code == 0
        assert "endpoint added" in target.read_text(encoding="utf-8")

    def test_no_changes_passes_under_any_bump(self, tmp_path):
        code, _ = self._run(tmp_path, NO_CHANGES_JSON, bump="patch")
        assert code == 0

    def test_the_guard_is_off_without_the_flag(self, tmp_path):
        # Omitting --bump is a dry run or a hand invocation, where there is no
        # label set to contradict.
        code, target = self._run(tmp_path, OASDIFF_JSON)
        assert code == 0
        assert target.exists()

    def test_an_unknown_bump_is_rejected_by_argparse(self, tmp_path):
        with pytest.raises(SystemExit):
            self._run(tmp_path, OASDIFF_JSON, bump="nonsense")
