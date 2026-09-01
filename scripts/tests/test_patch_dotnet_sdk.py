"""Unit tests for scripts/patch_dotnet_sdk.py."""

import pytest

from patch_dotnet_sdk import (
    ASSEMBLY_TITLE,
    AUTHORS,
    COMPANY,
    COPYRIGHT,
    DESCRIPTION,
    PatchError,
    check_no_generated_defaults,
    main,
    patch_csproj,
    read_property,
    set_property,
)

# Trimmed from the real generated csproj. The comment matters: preserving it
# across a rewrite is the property under test, and it is why this patches text
# rather than round-tripping XML.
CSPROJ = """\
<Project Sdk="Microsoft.NET.Sdk">

  <PropertyGroup>
    <GenerateAssemblyInfo>false</GenerateAssemblyInfo><!-- setting GenerateAssemblyInfo to false causes this bug https://github.com/dotnet/project-system/issues/3934 -->
    <TargetFramework>net8.0</TargetFramework>
    <AssemblyName>Ddx.InteractionsApi</AssemblyName>
    <PackageId>Ddx.InteractionsApi</PackageId>
    <Authors>OpenAPI</Authors>
    <Company>OpenAPI</Company>
    <AssemblyTitle>OpenAPI Library</AssemblyTitle>
    <Description>A library generated from a OpenAPI doc</Description>
    <Copyright>No Copyright</Copyright>
    <Version>0.1.0</Version>
    <PackageLicenseExpression>MIT</PackageLicenseExpression>
    <Nullable>annotations</Nullable>
  </PropertyGroup>

  <ItemGroup>
    <PackageReference Include="Newtonsoft.Json" Version="13.0.3" />
  </ItemGroup>
</Project>
"""


class TestReadProperty:
    def test_reads_an_element(self):
        assert read_property(CSPROJ, "Version") == "0.1.0"

    def test_absent_element_is_none(self):
        assert read_property(CSPROJ, "PackageProjectUrl") is None


class TestSetProperty:
    def test_replaces_the_value(self):
        assert "<Authors>Someone</Authors>" in set_property(CSPROJ, "Authors", "Someone")

    def test_leaves_other_elements_untouched(self):
        patched = set_property(CSPROJ, "Authors", "Someone")
        assert "<Company>OpenAPI</Company>" in patched
        assert "<TargetFramework>net8.0</TargetFramework>" in patched

    def test_rejects_a_missing_element(self):
        with pytest.raises(PatchError, match="no <Nope> element"):
            set_property(CSPROJ, "Nope", "x")

    def test_rejects_a_duplicated_element(self):
        doubled = CSPROJ.replace(
            "<Version>0.1.0</Version>", "<Version>0.1.0</Version><Version>0.2.0</Version>"
        )
        with pytest.raises(PatchError, match="expected exactly one"):
            set_property(doubled, "Version", "9.9.9")


class TestPatchCsproj:
    def test_sets_every_identity_field(self):
        patched = patch_csproj(CSPROJ)
        assert f"<Authors>{AUTHORS}</Authors>" in patched
        assert f"<Company>{COMPANY}</Company>" in patched
        assert f"<AssemblyTitle>{ASSEMBLY_TITLE}</AssemblyTitle>" in patched
        assert f"<Description>{DESCRIPTION}</Description>" in patched
        assert f"<Copyright>{COPYRIGHT}</Copyright>" in patched

    def test_preserves_the_generator_comment(self):
        # An XML round-trip would drop this; the comment explains a real
        # workaround, so losing it silently would be a regression.
        assert "project-system/issues/3934" in patch_csproj(CSPROJ)

    def test_preserves_package_references(self):
        assert 'Include="Newtonsoft.Json"' in patch_csproj(CSPROJ)

    def test_leaves_version_alone(self):
        # The bump flows from packageVersion through the generator.
        assert "<Version>0.1.0</Version>" in patch_csproj(CSPROJ)

    def test_leaves_the_license_alone(self):
        assert "<PackageLicenseExpression>MIT</PackageLicenseExpression>" in patch_csproj(
            CSPROJ
        )

    def test_is_idempotent(self):
        once = patch_csproj(CSPROJ)
        assert patch_csproj(once) == once

    def test_rejects_a_non_project_file(self):
        with pytest.raises(PatchError, match="MSBuild project"):
            patch_csproj("just some text")

    def test_rejects_a_template_missing_an_element(self):
        stripped = CSPROJ.replace("<Copyright>No Copyright</Copyright>", "")
        with pytest.raises(PatchError, match="no <Copyright> element"):
            patch_csproj(stripped)


class TestCheckNoGeneratedDefaults:
    def test_unpatched_csproj_is_rejected(self):
        problems = check_no_generated_defaults(CSPROJ)
        assert any("Authors" in p for p in problems)
        assert any("Company" in p for p in problems)
        assert any("Description" in p for p in problems)
        assert any("Copyright" in p for p in problems)

    def test_patched_csproj_is_clean(self):
        assert check_no_generated_defaults(patch_csproj(CSPROJ)) == []

    def test_placeholder_version_is_rejected(self):
        patched = set_property(patch_csproj(CSPROJ), "Version", "0.0.0")
        assert any("0.0.0" in p for p in check_no_generated_defaults(patched))

    def test_empty_field_is_rejected(self):
        patched = set_property(patch_csproj(CSPROJ), "Authors", "")
        assert any("empty" in p for p in check_no_generated_defaults(patched))

    def test_missing_license_is_rejected(self):
        stripped = patch_csproj(CSPROJ).replace(
            "<PackageLicenseExpression>MIT</PackageLicenseExpression>", ""
        )
        assert any("PackageLicenseExpression" in p for p in check_no_generated_defaults(stripped))


class TestMain:
    def test_writes_the_patched_file(self, tmp_path):
        target = tmp_path / "x.csproj"
        target.write_text(CSPROJ, encoding="utf-8")

        assert main([str(target)]) == 0
        assert f"<Authors>{AUTHORS}</Authors>" in target.read_text(encoding="utf-8")

    def test_is_idempotent_on_disk(self, tmp_path):
        target = tmp_path / "x.csproj"
        target.write_text(CSPROJ, encoding="utf-8")
        main([str(target)])
        once = target.read_text(encoding="utf-8")
        main([str(target)])
        assert target.read_text(encoding="utf-8") == once

    def test_check_only_fails_on_an_unpatched_file(self, tmp_path):
        target = tmp_path / "x.csproj"
        target.write_text(CSPROJ, encoding="utf-8")
        assert main([str(target), "--check-only"]) == 1

    def test_check_only_passes_on_a_patched_file(self, tmp_path):
        target = tmp_path / "x.csproj"
        target.write_text(patch_csproj(CSPROJ), encoding="utf-8")
        assert main([str(target), "--check-only"]) == 0

    def test_check_only_does_not_write(self, tmp_path):
        target = tmp_path / "x.csproj"
        target.write_text(CSPROJ, encoding="utf-8")
        main([str(target), "--check-only"])
        assert target.read_text(encoding="utf-8") == CSPROJ

    def test_missing_file_is_an_error(self, tmp_path):
        assert main([str(tmp_path / "nope.csproj")]) == 2

    def test_unrecognised_file_is_an_error(self, tmp_path):
        target = tmp_path / "x.csproj"
        target.write_text("not a project", encoding="utf-8")
        assert main([str(target)]) == 2
