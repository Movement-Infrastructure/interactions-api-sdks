"""Unit tests for scripts/verify_readme.py."""

from verify_readme import check, main

# What templates/python/README.mustache produces. Kept short; the rules under
# test are about what must and must not appear, not about length.
GOOD = """\
# ddx-interactions-api
Interactions API documentation

Python client for the DDx Interactions API, generated from its OpenAPI
specification.

- API version: v1
- Package version: 0.1.0

## Requirements

Python 3.8+

## Installation

```sh
pip install ddx-interactions-api
```

## Changelog

API changes are recorded in [CHANGELOG.md](CHANGELOG.md).

## Documentation for API Endpoints
"""

REQUIRED = ["pip install ddx-interactions-api", "## Installation", "## Changelog"]


class TestCheck:
    def test_a_good_readme_has_no_problems(self):
        assert check(GOOD, REQUIRED) == []

    def test_rejects_a_git_install_instruction(self):
        # The default template's actual output, and the defect that motivated
        # the override: it points consumers at this private repository.
        bad = GOOD.replace(
            "pip install ddx-interactions-api",
            "pip install git+https://github.com/Movement-Infrastructure/interactions-api-sdks.git",
        )
        problems = check(bad, [])
        assert any("private" in p for p in problems)

    def test_rejects_setup_py_install(self):
        bad = GOOD + "\n```sh\npython setup.py install --user\n```\n"
        assert any("setuptools removed" in p for p in check(bad, REQUIRED))

    def test_rejects_the_generator_class_name(self):
        bad = GOOD + "\n- Build package: org.openapitools.codegen.languages.PythonClientCodegen\n"
        assert any("Java class name" in p for p in check(bad, REQUIRED))

    def test_rejects_a_non_production_host(self):
        bad = GOOD + "\nSee https://api-dev.movementinfrastructure.org for testing.\n"
        assert any("non-production host" in p for p in check(bad, REQUIRED))

    def test_rejects_a_credential_placeholder(self):
        bad = GOOD + "\nconfiguration.password = 'YOUR_PASSWORD'\n"
        assert any("credential placeholder" in p for p in check(bad, REQUIRED))

    def test_rejects_a_build_date(self):
        bad = GOOD.replace("- API version: v1", "- API version: v1\n- Build date: 2026-09-01")
        assert any("churns" in p for p in check(bad, REQUIRED))

    def test_reports_the_line_number(self):
        bad = GOOD + "\npython setup.py install\n"
        assert any(p.startswith("line ") for p in check(bad, REQUIRED))

    def test_reports_missing_required_content(self):
        problems = check(GOOD, ["## Nonexistent Section"])
        assert any("missing required content" in p for p in problems)

    def test_catches_a_template_override_that_stopped_applying(self):
        # The failure this guards: the -t flag is dropped, the built-in
        # template comes back, and nobody notices until it is on the registry.
        default_output = GOOD.replace(
            "pip install ddx-interactions-api",
            "pip install git+https://github.com/Movement-Infrastructure/interactions-api-sdks.git",
        )
        assert len(check(default_output, REQUIRED)) >= 2

    def test_reports_every_problem_not_just_the_first(self):
        bad = GOOD.replace("pip install ddx-interactions-api", "pip install git+https://x.git")
        bad += "\npython setup.py install\n"
        assert len(check(bad, REQUIRED)) >= 3


class TestMain:
    def test_passes_on_a_good_readme(self, tmp_path):
        target = tmp_path / "README.md"
        target.write_text(GOOD, encoding="utf-8")
        args = [str(target)]
        for item in REQUIRED:
            args += ["--require", item]
        assert main(args) == 0

    def test_fails_on_a_bad_readme(self, tmp_path):
        target = tmp_path / "README.md"
        target.write_text(GOOD + "\npython setup.py install\n", encoding="utf-8")
        assert main([str(target)]) == 1

    def test_fails_when_required_content_is_absent(self, tmp_path):
        target = tmp_path / "README.md"
        target.write_text(GOOD, encoding="utf-8")
        assert main([str(target), "--require", "## Nope"]) == 1

    def test_missing_file_exits_two(self, tmp_path):
        assert main([str(tmp_path / "nope.md")]) == 2
