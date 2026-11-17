# Tests and Quality Gates

Tests protect content integrity, not merely application behaviour.

## Planned test layers

- **Structure:** required files, directories, and navigation references.
- **Metadata:** YAML frontmatter and JSON Schema validation.
- **Links:** internal anchors, local paths, and external-link health.
- **Content:** required fields, IDs, duplicate detection, and taxonomy references.
- **Translations:** locale parity, stale-source detection, and glossary consistency.
- **Code:** language-specific syntax checks and reproducible example tests.
- **Website:** build, accessibility, responsive layout, and search.
- **Security:** dependency review, secret scanning, and content trust boundaries.

## Current automated check

`python scripts/validate_structure.py` checks the minimum foundation and parses the JSON Schema files using Python's standard library. It does not yet validate YAML, Markdown frontmatter, external links, translations, or executable examples.
