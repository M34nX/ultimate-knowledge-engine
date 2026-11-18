# Tests and Quality Gates

Tests protect content integrity, not merely application behaviour.

## Run locally

```bash
python -m pip install -r requirements-dev.txt
python -m unittest discover -s tests -p 'test_*.py'
python scripts/validate_structure.py
```

## Automated checks

GitHub Actions runs the validator unit tests before the repository-wide structural validation.

The unit tests currently cover Markdown-link validation:

- Valid relative file links.
- Directory links resolving to `README.md`.
- Broken internal links.
- Links that attempt to escape the repository root.
- External links, fragment-only links, and links inside fenced code blocks.
- Malformed content metadata types (content type, locale, domain, and source IDs) are reported without crashing the validator.

The repository validator checks:

- YAML registry and knowledge-graph files parse successfully.
- All seven JSON Schemas are valid JSON Schema Draft 2020-12 documents.
- Content frontmatter conforms to the relevant schemas.
- Locale, domain, source, language-profile, and knowledge-graph references resolve.
- English and Persian domain landing pages and required project files exist.
- English and Persian content share stable IDs, including structured metadata for all seven Build from Scratch project pairs.
- Relative Markdown links point to files inside this repository.
- Both programming-language workbooks contain exactly 40 examples, consecutive numbering (01–40), a fenced code sample and file extension per entry, matching bilingual headings, and registry coverage.
- All seven Build from Scratch tracks have English/Persian project frontmatter validated against `schemas/project.schema.json`, including objectives, prerequisites, and milestones.

## Not yet automated

- External HTTP link availability and source freshness.
- Execution or compilation of all language examples against pinned toolchain versions.
- Human review of translation accuracy and technical meaning.
- Full anchor-level Markdown link validation.
- Website build, accessibility, responsive layout, and search tests.
- Dependency, secret, and security scanning.

A passing structural check does not mean every code sample has been executed, every factual claim is verified, or every translation is publication-ready. Those states require separate evidence and review.
