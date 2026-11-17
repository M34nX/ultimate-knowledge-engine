# Validation Pipeline

The foundation validator is intended to catch structural errors before content is published.

## Local setup

Install the development dependencies:

    python -m pip install -r requirements-dev.txt

Run the checks:

    python scripts/validate_structure.py

## Current automated checks

- JSON Schema syntax and draft compatibility.
- YAML parsing for registries and graph records.
- Markdown frontmatter validation for concepts, lessons, and exercises.
- Language-profile validation.
- Unique domain slugs, locale tags, language IDs, and graph node IDs.
- Domain landing-page presence for English and Persian.
- Source ID references in authored content.
- Knowledge-graph edge references.
- Shared stable IDs between the initial English and Persian sample content.
- Relative Markdown links that resolve inside the repository.

## Known limitations

This is an initial foundation validator, not a complete editorial review. It does not currently verify external-link availability, technical correctness of prose, translation quality, code-example behaviour, every graph semantic, or conformance of the website to accessibility standards. Those checks require dedicated tooling and, in several cases, human review.

A green CI result means these automated checks passed. It does not mean all project content is complete, verified, or publication-ready.
