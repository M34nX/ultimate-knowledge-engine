"""Unit tests for the repository's Markdown-link validator."""

from pathlib import Path
import tempfile
import unittest

from scripts import validate_structure as validator


class InternalMarkdownLinkTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp_dir = tempfile.TemporaryDirectory()
        self.root = Path(self.temp_dir.name)
        self.original_root = validator.ROOT
        self.original_errors = validator.ERRORS
        validator.ROOT = self.root
        validator.ERRORS = []

    def tearDown(self) -> None:
        validator.ROOT = self.original_root
        validator.ERRORS = self.original_errors
        self.temp_dir.cleanup()

    def write(self, relative_path: str, content: str = "") -> Path:
        path = self.root / relative_path
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
        return path

    def test_valid_relative_file_link(self) -> None:
        self.write("README.md", "[Guide](docs/guide.md)\n")
        self.write("docs/guide.md", "# Guide\n")

        checked = validator.validate_internal_links()

        self.assertEqual(checked, 1)
        self.assertEqual(validator.ERRORS, [])

    def test_directory_link_resolves_to_readme(self) -> None:
        self.write("README.md", "[Docs](docs/)\n")
        self.write("docs/README.md", "# Documentation\n")

        checked = validator.validate_internal_links()

        self.assertEqual(checked, 1)
        self.assertEqual(validator.ERRORS, [])

    def test_broken_internal_link_is_reported(self) -> None:
        self.write("README.md", "[Missing](docs/missing.md)\n")

        checked = validator.validate_internal_links()

        self.assertEqual(checked, 1)
        self.assertTrue(any("Broken internal link" in error for error in validator.ERRORS))

    def test_links_cannot_escape_repository_root(self) -> None:
        self.write("docs/page.md", "[Outside](../../outside.md)\n")

        checked = validator.validate_internal_links()

        self.assertEqual(checked, 0)
        self.assertTrue(
            any("Internal link escapes repository" in error for error in validator.ERRORS)
        )

    def test_external_anchor_and_fenced_code_links_are_ignored(self) -> None:
        self.write(
            "README.md",
            "[External](https://example.com) [Anchor](#section)\n"
            "\n```md\n[Example](missing.md)\n```\n",
        )

        checked = validator.validate_internal_links()

        self.assertEqual(checked, 0)
        self.assertEqual(validator.ERRORS, [])


if __name__ == "__main__":
    unittest.main()
