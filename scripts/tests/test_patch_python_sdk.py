"""Unit tests for scripts/patch_python_sdk.py."""

import re

import pytest

from patch_python_sdk import (
    CERTIFI,
    CHANGELOG_URL,
    NO_LICENSE,
    PatchError,
    apply_exact,
    apply_regex,
    check_license,
    main,
    patch_sdk,
)

# Trimmed from the real generated setup.py. Every defect the patches address is
# present: no python_requires, no certifi, no project_urls, and a
# long_description holding the spec's info.description rather than the README.
SETUP_PY = '''\
# coding: utf-8

from setuptools import setup, find_packages  # noqa: H301

NAME = "ddx-interactions-api"
VERSION = "0.1.0"
PYTHON_REQUIRES = ">= 3.8"
REQUIRES = [
    "urllib3 >= 1.25.3, < 3.0.0",
    "python-dateutil >= 2.8.2",
    "pydantic >= 2",
    "typing-extensions >= 4.7.1",
]

setup(
    name=NAME,
    version=VERSION,
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    long_description_content_type='text/markdown',
    long_description="""\\
    Interactions API documentation
    """,  # noqa: E501
    package_data={"ddx_interactions_api": ["py.typed"]},
)
'''

CONFIGURATION_PY = '''\
class Configuration:
    def __init__(self, ssl_ca_cert=None):
        self.ssl_ca_cert = ssl_ca_cert
        self.verify_ssl = True
'''

PYPROJECT_TOML = '''\
[tool.poetry]
name = "ddx-interactions-api"
version = "0.1.0"
license = "MIT"
'''


def write_sdk(
    tmp_path,
    setup_py=SETUP_PY,
    configuration_py=CONFIGURATION_PY,
    pyproject_toml=PYPROJECT_TOML,
):
    (tmp_path / "setup.py").write_text(setup_py, encoding="utf-8")
    (tmp_path / "pyproject.toml").write_text(pyproject_toml, encoding="utf-8")
    pkg = tmp_path / "ddx_interactions_api"
    pkg.mkdir(exist_ok=True)
    (pkg / "configuration.py").write_text(configuration_py, encoding="utf-8")
    return tmp_path


class TestApplyExact:
    def test_replaces_the_anchor(self):
        assert apply_exact("a b c", "b", "X", "X", "f") == "a X c"

    def test_is_a_noop_when_the_marker_is_present(self):
        assert apply_exact("already X", "b", "X", "X", "f") == "already X"

    def test_rejects_a_missing_anchor(self):
        with pytest.raises(PatchError, match="matched 0 times"):
            apply_exact("a c", "b", "X", "marker", "f")

    def test_rejects_a_duplicated_anchor(self):
        with pytest.raises(PatchError, match="matched 2 times"):
            apply_exact("a b b", "b", "X", "marker", "f")


class TestApplyRegex:
    PATTERN = re.compile(r"x+")

    def test_replaces_the_match(self):
        assert apply_regex("a xxx b", self.PATTERN, "Y", "Y", "f") == "a Y b"

    def test_is_a_noop_when_the_marker_is_present(self):
        assert apply_regex("has Y", self.PATTERN, "Y", "Y", "f") == "has Y"

    def test_rejects_no_match(self):
        with pytest.raises(PatchError, match="matched 0 times"):
            apply_regex("abc", self.PATTERN, "Y", "marker", "f")

    def test_rejects_multiple_matches(self):
        with pytest.raises(PatchError, match="matched 2 times"):
            apply_regex("xx a xx", self.PATTERN, "Y", "marker", "f")


class TestCheckLicense:
    def test_accepts_a_real_license(self, tmp_path):
        assert check_license(write_sdk(tmp_path)) is None

    def test_rejects_the_generator_default(self, tmp_path):
        # What the generator writes when the spec carries no info.license.
        without = PYPROJECT_TOML.replace("MIT", NO_LICENSE)
        with pytest.raises(PatchError, match="no usable license"):
            check_license(write_sdk(tmp_path, pyproject_toml=without))

    def test_rejects_a_missing_license_field(self, tmp_path):
        without = PYPROJECT_TOML.replace('license = "MIT"\n', "")
        with pytest.raises(PatchError, match="no usable license"):
            check_license(write_sdk(tmp_path, pyproject_toml=without))

    def test_names_the_upstream_fix(self, tmp_path):
        # The recovery is an upstream edit, so the error has to say where.
        without = PYPROJECT_TOML.replace("MIT", NO_LICENSE)
        with pytest.raises(PatchError, match="MercuryApiServiceCollectionExtensions"):
            check_license(write_sdk(tmp_path, pyproject_toml=without))

    def test_a_missing_pyproject_is_an_error(self, tmp_path):
        with pytest.raises(PatchError, match="cannot read"):
            check_license(tmp_path)


class TestPatchSdk:
    def test_an_unlicensed_sdk_is_not_patched(self, tmp_path):
        without = PYPROJECT_TOML.replace("MIT", NO_LICENSE)
        root = write_sdk(tmp_path, pyproject_toml=without)
        with pytest.raises(PatchError, match="no usable license"):
            patch_sdk(root)
        assert "_LONG_DESCRIPTION" not in (root / "setup.py").read_text()

    def test_adds_python_requires(self, tmp_path):
        patch_sdk(write_sdk(tmp_path))
        assert "python_requires=PYTHON_REQUIRES," in (tmp_path / "setup.py").read_text()

    def test_adds_certifi_to_requires(self, tmp_path):
        patch_sdk(write_sdk(tmp_path))
        assert CERTIFI in (tmp_path / "setup.py").read_text()

    def test_defaults_ssl_ca_cert_to_certifi(self, tmp_path):
        patch_sdk(write_sdk(tmp_path))
        text = (tmp_path / "ddx_interactions_api" / "configuration.py").read_text()
        assert "certifi.where()" in text

    def test_adds_the_changelog_project_url(self, tmp_path):
        patch_sdk(write_sdk(tmp_path))
        text = (tmp_path / "setup.py").read_text()
        assert "project_urls" in text
        assert CHANGELOG_URL in text

    def test_points_long_description_at_the_readme(self, tmp_path):
        # The whole point: PyPI renders long_description as the project page,
        # and the generator hardcodes a 30-character stub there.
        patch_sdk(write_sdk(tmp_path))
        text = (tmp_path / "setup.py").read_text()
        assert "long_description=_LONG_DESCRIPTION" in text
        assert "Interactions API documentation" not in text

    def test_defines_long_description_before_setup_is_called(self, tmp_path):
        patch_sdk(write_sdk(tmp_path))
        text = (tmp_path / "setup.py").read_text()
        assert text.index("_LONG_DESCRIPTION = ") < text.index("setup(")

    def test_drops_the_noqa_that_guarded_the_replaced_literal(self, tmp_path):
        patch_sdk(write_sdk(tmp_path))
        assert "# noqa: E501" not in (tmp_path / "setup.py").read_text()

    def test_patches_a_setup_py_with_no_noqa(self, tmp_path):
        without = SETUP_PY.replace('""",  # noqa: E501', '""",')
        patch_sdk(write_sdk(tmp_path, setup_py=without))
        text = (tmp_path / "setup.py").read_text()
        assert "long_description=_LONG_DESCRIPTION," in text
        assert ",," not in text

    def test_keeps_the_content_type(self, tmp_path):
        patch_sdk(write_sdk(tmp_path))
        assert "long_description_content_type" in (tmp_path / "setup.py").read_text()

    def test_patched_setup_py_is_valid_python(self, tmp_path):
        patch_sdk(write_sdk(tmp_path))
        compile((tmp_path / "setup.py").read_text(), "setup.py", "exec")

    def test_reports_the_files_it_changed(self, tmp_path):
        changed = patch_sdk(write_sdk(tmp_path))
        assert set(changed) == {"setup.py", "ddx_interactions_api/configuration.py"}

    def test_is_idempotent(self, tmp_path):
        root = write_sdk(tmp_path)
        patch_sdk(root)
        once = (root / "setup.py").read_text()

        assert patch_sdk(root) == []
        assert (root / "setup.py").read_text() == once

    def test_a_changed_api_description_still_patches(self, tmp_path):
        # The regex exists so a routine upstream docs edit doesn't hard-fail
        # the pipeline the way an exact anchor on this prose would.
        edited = SETUP_PY.replace(
            "Interactions API documentation", "Some entirely different wording"
        )
        patch_sdk(write_sdk(tmp_path, setup_py=edited))
        assert "long_description=_LONG_DESCRIPTION" in (tmp_path / "setup.py").read_text()

    def test_a_template_change_fails_loudly(self, tmp_path):
        broken = SETUP_PY.replace("    install_requires=REQUIRES,\n", "")
        with pytest.raises(PatchError, match="matched 0 times"):
            patch_sdk(write_sdk(tmp_path, setup_py=broken))

    def test_a_missing_file_is_an_error(self, tmp_path):
        with pytest.raises(PatchError, match="cannot read"):
            patch_sdk(tmp_path)


class TestMain:
    def test_patches_the_sdk(self, tmp_path):
        assert main([str(write_sdk(tmp_path))]) == 0
        assert "_LONG_DESCRIPTION" in (tmp_path / "setup.py").read_text()

    def test_rerun_reports_nothing_to_do(self, tmp_path):
        root = write_sdk(tmp_path)
        main([str(root)])
        assert main([str(root)]) == 0

    def test_a_broken_template_exits_nonzero(self, tmp_path):
        broken = SETUP_PY.replace("    install_requires=REQUIRES,\n", "")
        assert main([str(write_sdk(tmp_path, setup_py=broken))]) == 2

    def test_a_missing_directory_exits_nonzero(self, tmp_path):
        assert main([str(tmp_path / "nope")]) == 2

    def test_a_missing_license_exits_nonzero(self, tmp_path):
        without = PYPROJECT_TOML.replace("MIT", NO_LICENSE)
        assert main([str(write_sdk(tmp_path, pyproject_toml=without))]) == 2
