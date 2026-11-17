# Maintenance Scripts

Scripts in this directory support repeatable repository maintenance.

## Available

- `validate_structure.py` — validates registries, JSON Schemas, content frontmatter (including Build from Scratch project metadata), language profiles, knowledge-graph references, required files, relative Markdown links, and the bilingual 40-language workbook contract, and all seven bilingual Build from Scratch project metadata pairs.

Run locally:

```
python -m pip install -r requirements-dev.txt
python scripts/validate_structure.py
```

## Planned

- External-link and source-freshness checks.
- Pinned-toolchain compilation and execution of supported code examples.
- Translation parity and terminology reports beyond heading-level parity.
- Search-index generation.
- Stale-content and version-review reports.

Scripts should be deterministic, documented, safe by default, and usable in local development and CI. Avoid network calls unless explicitly requested by the script's purpose.
