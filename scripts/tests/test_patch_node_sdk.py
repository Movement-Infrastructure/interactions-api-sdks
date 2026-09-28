"""Unit tests for scripts/patch_node_sdk.py."""

import json

import pytest

from patch_node_sdk import (
    AUTHOR,
    LICENSE,
    NODE_ENGINES,
    PUBLISHED_FILES,
    TEST_DEV_DEPENDENCIES,
    TSCONFIG_INCLUDE,
    PatchError,
    check_no_generated_defaults,
    main,
    patch_package,
    patch_tsconfig,
)

# Verbatim shape of what openapi-generator 7.10.0's typescript-fetch template
# emits. The defects under test are all present here: third-party author, no
# license, no engines, no files allowlist.
GENERATED_PACKAGE = {
    "name": "ddx-interactions-api",
    "version": "0.1.0",
    "description": "OpenAPI client for ddx-interactions-api",
    "author": "OpenAPI-Generator",
    "repository": {
        "type": "git",
        "url": "https://github.com/Movement-Infrastructure/interactions-api-sdks.git",
    },
    "main": "./dist/index.js",
    "typings": "./dist/index.d.ts",
    "module": "./dist/esm/index.js",
    "sideEffects": False,
    "scripts": {"build": "tsc && tsc -p tsconfig.esm.json", "prepare": "npm run build"},
    "devDependencies": {"typescript": "^4.0 || ^5.0"},
}

# Likewise verbatim. Note the absent `include`, which is the defect.
GENERATED_TSCONFIG = {
    "compilerOptions": {
        "declaration": True,
        "target": "es6",
        "module": "commonjs",
        "moduleResolution": "node",
        "outDir": "dist",
        "typeRoots": ["node_modules/@types"],
    },
    "exclude": ["dist", "node_modules"],
}


def write_sdk(tmp_path, package=None, tsconfig=None):
    """Lay out a minimal generated SDK directory and return its path."""
    (tmp_path / "package.json").write_text(
        json.dumps(GENERATED_PACKAGE if package is None else package), encoding="utf-8"
    )
    (tmp_path / "tsconfig.json").write_text(
        json.dumps(GENERATED_TSCONFIG if tsconfig is None else tsconfig),
        encoding="utf-8",
    )
    return tmp_path


class TestPatchPackage:
    def test_replaces_the_generator_author(self):
        assert patch_package(dict(GENERATED_PACKAGE))["author"] == AUTHOR

    def test_sets_a_license(self):
        assert patch_package(dict(GENERATED_PACKAGE))["license"] == LICENSE

    def test_sets_the_node_engine_floor(self):
        # typescript-fetch relies on global fetch, so the floor is load-bearing
        # rather than cosmetic.
        assert patch_package(dict(GENERATED_PACKAGE))["engines"] == {"node": NODE_ENGINES}

    def test_restricts_published_files_to_built_output(self):
        assert patch_package(dict(GENERATED_PACKAGE))["files"] == PUBLISHED_FILES

    def test_keeps_the_generated_build_script(self):
        # The patch adds to `scripts`; clobbering `build` would break `prepare`.
        patched = patch_package(dict(GENERATED_PACKAGE))
        assert patched["scripts"]["build"] == "tsc && tsc -p tsconfig.esm.json"
        assert patched["scripts"]["test"] == "vitest run"

    def test_keeps_the_generated_typescript_dev_dependency(self):
        patched = patch_package(dict(GENERATED_PACKAGE))
        assert patched["devDependencies"]["typescript"] == "^4.0 || ^5.0"
        for name, spec in TEST_DEV_DEPENDENCIES.items():
            assert patched["devDependencies"][name] == spec

    def test_leaves_version_alone(self):
        # The bump flows from npmVersion through the generator; rewriting it
        # here would silently undo it.
        assert patch_package(dict(GENERATED_PACKAGE))["version"] == "0.1.0"

    def test_is_idempotent(self):
        once = patch_package(dict(GENERATED_PACKAGE))
        twice = patch_package(dict(once))
        assert once == twice

    def test_rejects_a_missing_name(self):
        broken = {k: v for k, v in GENERATED_PACKAGE.items() if k != "name"}
        with pytest.raises(PatchError, match="no `name`"):
            patch_package(broken)

    def test_rejects_a_missing_version(self):
        broken = {k: v for k, v in GENERATED_PACKAGE.items() if k != "version"}
        with pytest.raises(PatchError, match="no `version`"):
            patch_package(broken)

    def test_rejects_a_name_mismatch(self):
        with pytest.raises(PatchError, match="disagree"):
            patch_package(dict(GENERATED_PACKAGE), expected_name="something-else")

    def test_accepts_a_matching_name(self):
        patched = patch_package(
            dict(GENERATED_PACKAGE), expected_name="ddx-interactions-api"
        )
        assert patched["name"] == "ddx-interactions-api"

    def test_rejects_a_non_object(self):
        with pytest.raises(PatchError, match="did not parse to an object"):
            patch_package(["not", "an", "object"])


class TestPatchTsconfig:
    def test_confines_the_build_to_src(self):
        assert patch_tsconfig(dict(GENERATED_TSCONFIG))["include"] == TSCONFIG_INCLUDE

    def test_keeps_the_generated_compiler_options(self):
        patched = patch_tsconfig(dict(GENERATED_TSCONFIG))
        assert patched["compilerOptions"]["outDir"] == "dist"
        assert patched["compilerOptions"]["declaration"] is True

    def test_keeps_the_generated_exclude(self):
        assert patch_tsconfig(dict(GENERATED_TSCONFIG))["exclude"] == [
            "dist",
            "node_modules",
        ]

    def test_is_idempotent(self):
        once = patch_tsconfig(dict(GENERATED_TSCONFIG))
        assert patch_tsconfig(dict(once)) == once

    def test_rejects_a_tsconfig_without_compiler_options(self):
        with pytest.raises(PatchError, match="compilerOptions"):
            patch_tsconfig({"exclude": ["dist"]})

    def test_rejects_a_non_object(self):
        with pytest.raises(PatchError, match="did not parse to an object"):
            patch_tsconfig([])


class TestCheckNoGeneratedDefaults:
    def test_unpatched_package_is_rejected(self):
        problems = check_no_generated_defaults(dict(GENERATED_PACKAGE))
        assert any("author" in p for p in problems)
        assert any("license" in p for p in problems)
        assert any("files" in p for p in problems)

    def test_patched_package_is_clean(self):
        assert check_no_generated_defaults(patch_package(dict(GENERATED_PACKAGE))) == []

    def test_placeholder_version_is_rejected(self):
        patched = patch_package(dict(GENERATED_PACKAGE))
        patched["version"] = "0.0.0"
        assert any("0.0.0" in p for p in check_no_generated_defaults(patched))

    def test_generator_community_author_is_rejected(self):
        patched = patch_package(dict(GENERATED_PACKAGE))
        patched["author"] = "OpenAPI Generator Community"
        assert any("author" in p for p in check_no_generated_defaults(patched))


class TestMain:
    def test_patches_both_files(self, tmp_path):
        sdk = write_sdk(tmp_path)

        assert main([str(sdk), "--expect-name", "ddx-interactions-api"]) == 0

        package = json.loads((sdk / "package.json").read_text(encoding="utf-8"))
        tsconfig = json.loads((sdk / "tsconfig.json").read_text(encoding="utf-8"))
        assert package["author"] == AUTHOR
        assert package["license"] == LICENSE
        assert tsconfig["include"] == TSCONFIG_INCLUDE

    def test_written_files_end_with_a_newline(self, tmp_path):
        sdk = write_sdk(tmp_path)
        main([str(sdk)])
        assert (sdk / "package.json").read_text(encoding="utf-8").endswith("}\n")
        assert (sdk / "tsconfig.json").read_text(encoding="utf-8").endswith("}\n")

    def test_is_idempotent_on_disk(self, tmp_path):
        sdk = write_sdk(tmp_path)
        main([str(sdk)])
        once = (sdk / "package.json").read_text(encoding="utf-8")
        main([str(sdk)])
        assert (sdk / "package.json").read_text(encoding="utf-8") == once

    def test_check_only_fails_on_an_unpatched_sdk(self, tmp_path):
        assert main([str(write_sdk(tmp_path)), "--check-only"]) == 1

    def test_check_only_passes_on_a_patched_sdk(self, tmp_path):
        sdk = write_sdk(tmp_path, package=patch_package(dict(GENERATED_PACKAGE)))
        assert main([str(sdk), "--check-only"]) == 0

    def test_check_only_does_not_write(self, tmp_path):
        sdk = write_sdk(tmp_path)
        original = (sdk / "package.json").read_text(encoding="utf-8")
        main([str(sdk), "--check-only"])
        assert (sdk / "package.json").read_text(encoding="utf-8") == original

    def test_missing_package_json_is_an_error(self, tmp_path):
        assert main([str(tmp_path)]) == 2

    def test_missing_tsconfig_is_an_error(self, tmp_path):
        (tmp_path / "package.json").write_text(
            json.dumps(GENERATED_PACKAGE), encoding="utf-8"
        )
        assert main([str(tmp_path)]) == 2

    def test_invalid_json_is_an_error(self, tmp_path):
        (tmp_path / "package.json").write_text("{not json", encoding="utf-8")
        assert main([str(tmp_path)]) == 2

    def test_name_mismatch_is_an_error(self, tmp_path):
        assert main([str(write_sdk(tmp_path)), "--expect-name", "other"]) == 2
