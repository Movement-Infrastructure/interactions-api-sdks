"""Unit tests for scripts/bump_version.py (MIG-1925)."""

import json

import pytest

from bump_version import (
    MAJOR_LABEL,
    MINOR_LABEL,
    PATCH_LABEL,
    Version,
    VersionError,
    _parse_labels,
    bump_version,
    main,
    parse_version,
    read_package_version,
    select_bump,
    write_package_version,
)

# Trimmed from the real sdks/python/v1/openapi-generator-config.yaml. The
# comments matter: preserving them across a rewrite is the property under test.
CONFIG = """\
# openapi-generator config for the Python v1 SDK.

packageName: mi_interactions_api
projectName: mi-interactions-api

# Placeholder; the version-bump workflow rewrites this on each sync PR.
packageVersion: 1.4.2

library: urllib3

globalProperties:
  apiTests: "false"
"""


class TestParseVersion:
    def test_parses_components(self):
        assert parse_version("1.2.3") == Version(1, 2, 3)

    def test_tolerates_surrounding_whitespace_and_quotes(self):
        assert parse_version('  "1.2.3" ') == Version(1, 2, 3)
        assert parse_version("'0.0.0'") == Version(0, 0, 0)

    def test_handles_multi_digit_components(self):
        assert parse_version("10.20.30") == Version(10, 20, 30)

    @pytest.mark.parametrize(
        "text",
        [
            "1.2",  # too few components
            "1.2.3.4",  # too many
            "1.2.3-rc1",  # pre-release: no pipeline story yet
            "1.2.3+build5",  # build metadata
            "v1.2.3",  # leading v
            "",
            "abc",
        ],
    )
    def test_rejects_non_strict_versions(self, text):
        with pytest.raises(VersionError):
            parse_version(text)


class TestSelectBump:
    def test_patch_label_selects_patch(self):
        assert select_bump([PATCH_LABEL]) == "patch"

    def test_no_labels_defaults_to_minor(self):
        assert select_bump([]) == "minor"

    def test_minor_label_is_decorative(self):
        assert select_bump([MINOR_LABEL]) == "minor"

    def test_major_label_selects_major(self):
        assert select_bump([MAJOR_LABEL]) == "major"

    def test_patch_wins_over_minor(self):
        assert select_bump([MINOR_LABEL, PATCH_LABEL]) == "patch"

    def test_major_wins_over_everything(self):
        # Contradictory labelling; of the two readings, honoring the declared
        # breaking change is the safe one.
        assert select_bump([MAJOR_LABEL, PATCH_LABEL]) == "major"
        assert select_bump([MAJOR_LABEL, MINOR_LABEL, PATCH_LABEL]) == "major"

    def test_unrelated_labels_are_ignored(self):
        assert select_bump(["bug", "documentation"]) == "minor"


class TestBumpVersion:
    def test_major_zeroes_minor_and_patch(self):
        assert bump_version(Version(1, 4, 2), "major") == Version(2, 0, 0)

    def test_minor_zeroes_patch(self):
        assert bump_version(Version(1, 4, 2), "minor") == Version(1, 5, 0)

    def test_patch_increments_only_patch(self):
        assert bump_version(Version(1, 4, 2), "patch") == Version(1, 4, 3)

    def test_bumps_from_zero(self):
        assert bump_version(Version(0, 0, 0), "minor") == Version(0, 1, 0)
        assert bump_version(Version(0, 0, 0), "patch") == Version(0, 0, 1)
        assert bump_version(Version(0, 0, 0), "major") == Version(1, 0, 0)

    def test_rejects_unknown_bump(self):
        with pytest.raises(VersionError):
            bump_version(Version(1, 0, 0), "sideways")


class TestReadPackageVersion:
    def test_reads_version_from_config(self):
        assert read_package_version(CONFIG) == Version(1, 4, 2)

    def test_reads_quoted_version(self):
        assert read_package_version('packageVersion: "2.0.1"\n') == Version(2, 0, 1)

    def test_reads_indented_version(self):
        assert read_package_version("  packageVersion: 3.1.4\n") == Version(3, 1, 4)

    def test_ignores_trailing_comment(self):
        assert read_package_version("packageVersion: 1.0.0  # placeholder\n") == Version(
            1, 0, 0
        )

    def test_raises_when_absent(self):
        with pytest.raises(VersionError, match="no `packageVersion:` line"):
            read_package_version("packageName: foo\n")

    def test_raises_when_duplicated(self):
        text = "packageVersion: 1.0.0\npackageVersion: 2.0.0\n"
        with pytest.raises(VersionError, match="expected exactly one"):
            read_package_version(text)

    def test_does_not_match_a_similarly_named_key(self):
        with pytest.raises(VersionError):
            read_package_version("otherPackageVersionThing: 1.0.0\n")


class TestWritePackageVersion:
    def test_updates_the_version(self):
        updated = write_package_version(CONFIG, Version(1, 5, 0))
        assert "packageVersion: 1.5.0" in updated
        assert "packageVersion: 1.4.2" not in updated

    def test_preserves_every_other_line(self):
        updated = write_package_version(CONFIG, Version(9, 9, 9))
        before = [ln for ln in CONFIG.splitlines() if "packageVersion" not in ln]
        after = [ln for ln in updated.splitlines() if "packageVersion" not in ln]
        assert before == after

    def test_preserves_comments(self):
        updated = write_package_version(CONFIG, Version(2, 0, 0))
        assert "# openapi-generator config for the Python v1 SDK." in updated
        assert "# Placeholder; the version-bump workflow rewrites this" in updated

    def test_preserves_indentation(self):
        updated = write_package_version("  packageVersion: 1.0.0\n", Version(1, 1, 0))
        assert updated == "  packageVersion: 1.1.0\n"

    def test_preserves_trailing_comment(self):
        updated = write_package_version(
            "packageVersion: 1.0.0  # placeholder\n", Version(1, 1, 0)
        )
        assert updated == "packageVersion: 1.1.0  # placeholder\n"

    def test_round_trips(self):
        updated = write_package_version(CONFIG, Version(7, 8, 9))
        assert read_package_version(updated) == Version(7, 8, 9)

    def test_raises_when_absent(self):
        with pytest.raises(VersionError, match="no `packageVersion:` line"):
            write_package_version("packageName: foo\n", Version(1, 0, 0))


class TestParseLabels:
    def test_parses_json_array(self):
        assert _parse_labels('["a", "b"]') == ["a", "b"]

    @pytest.mark.parametrize("raw", [None, "", "   ", "[]"])
    def test_treats_missing_or_empty_as_no_labels(self, raw):
        assert _parse_labels(raw) == []

    def test_rejects_malformed_json(self):
        with pytest.raises(VersionError, match="not valid JSON"):
            _parse_labels("[unquoted]")

    @pytest.mark.parametrize("raw", ['{"a": 1}', '"a"', "[1, 2]", "[null]"])
    def test_rejects_non_string_arrays(self, raw):
        with pytest.raises(VersionError, match="array of strings"):
            _parse_labels(raw)


class TestMain:
    @pytest.fixture
    def config_file(self, tmp_path):
        path = tmp_path / "openapi-generator-config.yaml"
        path.write_text(CONFIG, encoding="utf-8")
        return path

    def test_dry_run_leaves_the_file_untouched(self, config_file):
        assert main(["--current-config", str(config_file)]) == 0
        assert config_file.read_text(encoding="utf-8") == CONFIG

    def test_writes_the_bumped_version(self, config_file):
        exit_code = main(
            [
                "--current-config",
                str(config_file),
                "--write-config",
                str(config_file),
                "--labels-json",
                json.dumps([PATCH_LABEL]),
            ]
        )
        assert exit_code == 0
        assert read_package_version(config_file.read_text(encoding="utf-8")) == Version(
            1, 4, 3
        )

    def test_defaults_to_minor_without_labels(self, config_file):
        main(["--current-config", str(config_file), "--write-config", str(config_file)])
        assert read_package_version(config_file.read_text(encoding="utf-8")) == Version(
            1, 5, 0
        )

    def test_force_bump_overrides_labels(self, config_file):
        main(
            [
                "--current-config",
                str(config_file),
                "--write-config",
                str(config_file),
                "--labels-json",
                json.dumps([PATCH_LABEL]),
                "--force-bump",
                "major",
            ]
        )
        assert read_package_version(config_file.read_text(encoding="utf-8")) == Version(
            2, 0, 0
        )

    def test_reruns_are_idempotent_when_reading_from_a_separate_base(self, tmp_path):
        # The CI shape: --current-config is the base branch's copy and never
        # changes; --write-config is the PR branch's working copy. Running
        # repeatedly must converge on one bump, not compound.
        base = tmp_path / "base.yaml"
        base.write_text(CONFIG, encoding="utf-8")
        working = tmp_path / "working.yaml"
        working.write_text(CONFIG, encoding="utf-8")

        for _ in range(3):
            main(
                [
                    "--current-config",
                    str(base),
                    "--write-config",
                    str(working),
                    "--labels-json",
                    json.dumps([PATCH_LABEL]),
                ]
            )

        assert read_package_version(working.read_text(encoding="utf-8")) == Version(
            1, 4, 3
        )

    def test_major_label_bumps_major_end_to_end(self, config_file):
        main(
            [
                "--current-config",
                str(config_file),
                "--write-config",
                str(config_file),
                "--labels-json",
                json.dumps([MAJOR_LABEL]),
            ]
        )
        assert read_package_version(config_file.read_text(encoding="utf-8")) == Version(
            2, 0, 0
        )

    def test_notices_a_major_bump(self, config_file, capsys):
        main(
            [
                "--current-config",
                str(config_file),
                "--labels-json",
                json.dumps([MAJOR_LABEL]),
            ]
        )
        out = capsys.readouterr().out
        assert "::notice::" in out
        assert "MAJOR" in out

    def test_no_notice_for_a_routine_bump(self, config_file, capsys):
        main(["--current-config", str(config_file)])
        assert "::notice::" not in capsys.readouterr().out

    def test_emits_github_output(self, config_file, tmp_path, monkeypatch):
        output = tmp_path / "gh-output"
        monkeypatch.setenv("GITHUB_OUTPUT", str(output))

        main(
            [
                "--current-config",
                str(config_file),
                "--labels-json",
                json.dumps([PATCH_LABEL]),
            ]
        )

        written = output.read_text(encoding="utf-8")
        assert "current=1.4.2" in written
        assert "next=1.4.3" in written
        assert "bump=patch" in written

    def test_reports_error_for_missing_config(self, tmp_path, capsys):
        exit_code = main(["--current-config", str(tmp_path / "nope.yaml")])
        assert exit_code == 2
        assert "cannot read --current-config" in capsys.readouterr().err

    def test_reports_error_for_unparseable_version(self, tmp_path, capsys):
        path = tmp_path / "bad.yaml"
        path.write_text("packageVersion: not-a-version\n", encoding="utf-8")
        exit_code = main(["--current-config", str(path)])
        assert exit_code == 2
        assert "error:" in capsys.readouterr().err
