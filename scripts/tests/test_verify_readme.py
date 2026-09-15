"""Unit tests for scripts/verify_readme.py."""

import pytest

from verify_readme import (
    PRODUCTION_HOST,
    REQUIRED_BY_LANGUAGE,
    check,
    main,
)

REQUIRED = REQUIRED_BY_LANGUAGE["python"]

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

class TestCheck:
    def test_a_good_readme_has_no_problems(self):
        assert check(GOOD, REQUIRED) == []

    def test_rejects_a_git_install_instruction(self):
        # The default template's actual output, and the defect that motivated
        # the override.
        bad = GOOD.replace(
            "pip install ddx-interactions-api",
            "pip install git+https://github.com/Movement-Infrastructure/interactions-api-sdks.git",
        )
        assert any("git URL" in p for p in check(bad, []))

    def test_rejects_setup_py_install(self):
        bad = GOOD + "\n```sh\npython setup.py install --user\n```\n"
        assert any("setuptools removed" in p for p in check(bad, REQUIRED))

    def test_rejects_the_generator_class_name(self):
        bad = GOOD + "\n- Build package: org.openapitools.codegen.languages.PythonClientCodegen\n"
        assert any("Java class" in p for p in check(bad, REQUIRED))

    def test_allows_the_production_host(self):
        good = GOOD + f"\nAll URIs are relative to *https://{PRODUCTION_HOST}*\n"
        assert check(good, REQUIRED) == []

    def test_rejects_any_other_host_on_the_api_domain(self):
        # Matched by shape, so an environment nobody thought to list is still
        # caught. The spec's `servers` block is copied verbatim into the client.
        for host in (
            "api-dev.movementinfrastructure.org",
            "staging.movementinfrastructure.org",
            "api.internal.movementinfrastructure.org",
        ):
            bad = GOOD + f"\nSee https://{host} for testing.\n"
            assert any(PRODUCTION_HOST in p for p in check(bad, REQUIRED)), host

    def test_matches_hosts_regardless_of_case(self):
        bad = GOOD + "\nSee https://API-Dev.MovementInfrastructure.org here.\n"
        assert any(PRODUCTION_HOST in p for p in check(bad, REQUIRED))

    def test_the_production_host_is_allowed_regardless_of_case(self):
        good = GOOD + "\nAll URIs are relative to *https://API.MovementInfrastructure.ORG*\n"
        assert check(good, REQUIRED) == []

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

    def test_applies_the_built_in_requirements_without_any_flag(self, tmp_path):
        # Three workflows call this with no arguments. A gate the publish path
        # spells differently from the PR path is a gate that does not hold.
        target = tmp_path / "README.md"
        target.write_text(GOOD.replace("## Changelog", "## Changes"), encoding="utf-8")
        assert main([str(target)]) == 1

    def test_an_explicit_require_replaces_the_built_in_list(self, tmp_path):
        target = tmp_path / "README.md"
        target.write_text(GOOD.replace("## Changelog", "## Changes"), encoding="utf-8")
        assert main([str(target), "--require", "## Installation"]) == 0

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


# What templates/ruby/README.mustache produces. The ruby generator has no
# common_README partial, so this template renders the whole page itself.
GOOD_RUBY = """\
# ddx_interactions_api

DdxInteractionsApi - the Ruby gem for the Interactions API

Ruby client for the DDx Interactions API, generated from its OpenAPI
specification.

- API version: v1
- Gem version: 0.1.0

## Requirements

Ruby >= 3.0

## Installation

```shell
gem install ddx_interactions_api
```

## Changelog

API changes are recorded in the changelog.

## Getting Started

```ruby
config.username = ''
config.password = ENV.fetch('DDX_API_KEY')
```

All URIs are relative to *https://api.movementinfrastructure.org*
"""

# The two install routes the built-in ruby template offers instead of the
# registry. Both are what the override exists to remove.
DEFAULT_RUBY_INSTALL = """\
## Installation

### Build a gem

```shell
gem build ddx_interactions_api.gemspec
```

```shell
gem install ./ddx_interactions_api-0.1.0.gem
```

### Install from Git

    gem 'ddx_interactions_api', :git => 'https://github.com/Movement-Infrastructure/interactions-api-sdks.git'
"""


class TestRuby:
    RUBY = REQUIRED_BY_LANGUAGE["ruby"]

    def test_a_good_ruby_readme_has_no_problems(self):
        assert check(GOOD_RUBY, self.RUBY) == []

    def test_rejects_the_built_in_git_install(self):
        problems = check(DEFAULT_RUBY_INSTALL, self.RUBY)
        assert any("git URL" in p for p in problems)

    def test_the_built_in_local_gem_install_does_not_satisfy_the_requirement(self):
        """`gem install ./ddx_interactions_api-0.1.0.gem` must not count."""
        problems = check(DEFAULT_RUBY_INSTALL, self.RUBY)
        assert any("gem install ddx_interactions_api" in p for p in problems)

    def test_the_python_list_does_not_silently_pass_a_ruby_readme(self):
        """The failure mode this guards: a gate that checks the wrong language."""
        problems = check(GOOD_RUBY, REQUIRED_BY_LANGUAGE["python"])
        assert any("pip install" in p for p in problems)

    def test_main_applies_the_ruby_list(self, tmp_path):
        target = tmp_path / "README.md"
        target.write_text(GOOD_RUBY, encoding="utf-8")
        assert main([str(target), "--language", "ruby"]) == 0

    def test_main_defaults_to_python_and_so_fails_a_ruby_readme(self, tmp_path):
        target = tmp_path / "README.md"
        target.write_text(GOOD_RUBY, encoding="utf-8")
        assert main([str(target)]) == 1

    def test_main_rejects_an_unknown_language(self, tmp_path):
        target = tmp_path / "README.md"
        target.write_text(GOOD_RUBY, encoding="utf-8")
        with pytest.raises(SystemExit):
            main([str(target), "--language", "cobol"])
