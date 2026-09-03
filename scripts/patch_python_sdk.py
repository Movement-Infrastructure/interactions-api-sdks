#!/usr/bin/env python3
"""Apply the fixes the python generator can't be configured to make.

None of these are reachable through generator config: it exposes packageName,
projectName and packageVersion, and nothing that governs setup() arguments. A
module rather than an inline step because both generate-python-sdk.yml and
python-sdk-tests.yml need it, and because it can then be unit-tested.

Two kinds of patch, because two kinds of target:

Exact anchors
    Generator template text. A miss is fatal rather than a no-op, so a template
    change on a generator upgrade fails the build instead of silently shipping
    a package missing the fix.

Regex
    `long_description` holds the spec's `info.description`, whose text changes
    whenever the API docs are edited upstream. An exact anchor on that prose
    would hard-fail the pipeline on a routine docs edit.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

CERTIFI = "certifi >= 2024.2.2"

CHANGELOG_URL = (
    "https://github.com/Movement-Infrastructure/interactions-api-sdks"
    "/blob/main/sdks/python/v1/CHANGELOG.md"
)

# (relative path, anchor, replacement, already-applied marker)
EXACT_PATCHES = [
    # The template never passes PYTHON_REQUIRES to setup(), so the wheel ships
    # without a Requires-Python and pip will happily install it on 3.7.
    (
        "setup.py",
        "    install_requires=REQUIRES,\n",
        "    python_requires=PYTHON_REQUIRES,\n    install_requires=REQUIRES,\n",
        "python_requires=PYTHON_REQUIRES",
    ),
    # No certifi, while configuration.py defaults ssl_ca_cert to None. HTTPS
    # then dies with CERTIFICATE_VERIFY_FAILED on python.org macOS builds,
    # whose OpenSSL trust store is empty.
    (
        "setup.py",
        '    "typing-extensions >= 4.7.1",\n]',
        f'    "typing-extensions >= 4.7.1",\n    "{CERTIFI}",\n]',
        CERTIFI,
    ),
    (
        "ddx_interactions_api/configuration.py",
        "        self.ssl_ca_cert = ssl_ca_cert\n",
        "        import certifi\n"
        "        self.ssl_ca_cert = ssl_ca_cert if ssl_ca_cert is not None "
        "else certifi.where()\n",
        "certifi.where()",
    ),
    # Shipping CHANGELOG.md in the sdist does not make it visible to anyone --
    # nothing renders sdist contents. PyPI builds its page from metadata, and
    # project_urls is the field it renders as a sidebar link. Keep this URL and
    # the one in templates/python/README.mustache pointing at the same file.
    (
        "setup.py",
        '    packages=find_packages(exclude=["test", "tests"]),\n',
        "    project_urls={\n"
        f'        "Changelog": "{CHANGELOG_URL}",\n'
        "    },\n"
        '    packages=find_packages(exclude=["test", "tests"]),\n',
        "project_urls",
    ),
    # Defines the value the regex patch below points long_description at.
    (
        "setup.py",
        "from setuptools import setup, find_packages  # noqa: H301\n",
        "from pathlib import Path\n\n"
        "from setuptools import setup, find_packages  # noqa: H301\n\n"
        "# Rendered as the whole project page on the package registry.\n"
        "_LONG_DESCRIPTION = (Path(__file__).parent / \"README.md\").read_text(\n"
        '    encoding="utf-8"\n'
        ")\n",
        "_LONG_DESCRIPTION",
    ),
]

# (relative path, pattern, replacement, already-applied marker)
REGEX_PATCHES = [
    # The generator hardcodes long_description to the spec's info.description,
    # so the whole PyPI project page is 30 characters long. Point it at the
    # README instead.
    (
        "setup.py",
        re.compile(r'long_description=""".*?""",(?:[ \t]*# noqa: E501)?', re.DOTALL),
        "long_description=_LONG_DESCRIPTION,",
        "long_description=_LONG_DESCRIPTION",
    ),
]


class PatchError(ValueError):
    """Raised when a generated file is missing or not shaped as expected."""


def apply_exact(text: str, anchor: str, replacement: str, marker: str, where: str) -> str:
    """Apply one exact-anchor patch. Returns `text` unchanged if already applied."""
    if marker in text:
        return text

    found = text.count(anchor)
    if found != 1:
        raise PatchError(
            f"{where}: anchor {anchor!r} matched {found} times, expected 1. "
            f"Generator template changed; update scripts/patch_python_sdk.py."
        )
    return text.replace(anchor, replacement)


def apply_regex(
    text: str, pattern: re.Pattern[str], replacement: str, marker: str, where: str
) -> str:
    """Apply one regex patch. Returns `text` unchanged if already applied."""
    if marker in text:
        return text

    found = len(pattern.findall(text))
    if found != 1:
        raise PatchError(
            f"{where}: pattern {pattern.pattern!r} matched {found} times, expected 1. "
            f"Generator template changed; update scripts/patch_python_sdk.py."
        )
    return pattern.sub(replacement, text, count=1)


def patch_sdk(root: Path) -> list[str]:
    """Patch the generated SDK in `root`. Returns the files it changed."""
    changed: list[str] = []

    by_file: dict[str, list] = {}
    for name, anchor, replacement, marker in EXACT_PATCHES:
        by_file.setdefault(name, []).append(("exact", anchor, replacement, marker))
    for name, pattern, replacement, marker in REGEX_PATCHES:
        by_file.setdefault(name, []).append(("regex", pattern, replacement, marker))

    for name, patches in by_file.items():
        path = root / name
        try:
            text = original = path.read_text(encoding="utf-8")
        except OSError as exc:
            raise PatchError(f"cannot read {path}: {exc}") from exc

        for kind, target, replacement, marker in patches:
            where = str(path)
            if kind == "exact":
                text = apply_exact(text, target, replacement, marker, where)
            else:
                text = apply_regex(text, target, replacement, marker, where)

        if text != original:
            path.write_text(text, encoding="utf-8")
            changed.append(name)

    return changed


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Patch the generated Python SDK in place."
    )
    parser.add_argument(
        "sdk_dir", type=Path, help="The generated SDK directory, e.g. sdks/python/v1."
    )
    args = parser.parse_args(argv)

    try:
        changed = patch_sdk(args.sdk_dir)
    except PatchError as exc:
        print(f"::error::{exc}", file=sys.stderr)
        return 2

    if changed:
        for name in changed:
            print(f"patched: {name}")
    else:
        print("already applied; nothing to change.")
    return 0


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
