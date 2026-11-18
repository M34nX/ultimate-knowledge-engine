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


    def test_malformed_content_type_is_reported_without_crashing(self) -> None:
        self.write(
            "content/en/programming-languages/example.md",
            "---\ncontent_type: []\nid: sample.lesson\nlocale: en\ndomain: programming-languages\n---\n",
        )

        validator.validate_content({}, {"en"}, {"programming-languages"}, set())

        self.assertTrue(any("Unknown content_type" in error for error in validator.ERRORS))

    def test_malformed_locale_domain_and_source_ids_are_reported(self) -> None:
        self.write(
            "content/en/programming-languages/example.md",
            "---\ncontent_type: lesson\nid: sample.lesson\nlocale: []\ndomain: {}\nsources: [42]\n---\n",
        )

        validator.validate_content({}, {"en"}, {"programming-languages"}, {"known"})

        self.assertTrue(any("Unknown locale" in error for error in validator.ERRORS))
        self.assertTrue(any("Unknown domain" in error for error in validator.ERRORS))
        self.assertTrue(any("Source IDs must be strings" in error for error in validator.ERRORS))

    def test_null_sources_are_reported_without_crashing(self) -> None:
        self.write(
            "content/en/programming-languages/example.md",
            "---\ncontent_type: lesson\nid: sample.lesson\nlocale: en\ndomain: programming-languages\nsources: null\n---\n",
        )

        validator.validate_content({}, {"en"}, {"programming-languages"}, set())

        self.assertTrue(any("Sources must be a list" in error for error in validator.ERRORS))


if __name__ == "__main__":
    unittest.main()
