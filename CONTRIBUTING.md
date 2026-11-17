# Contributing

Thank you for helping build a rigorous, accessible, multilingual knowledge resource.

## Before you start

- Search existing issues and content to avoid duplication.
- Open an issue before large or architectural changes.
- Do not copy material unless its licence clearly permits the intended reuse.
- Never add secrets, credentials, personal data, or unsafe executable payloads.

## Useful contributions

- Correct factual or technical errors.
- Add lessons, concepts, exercises, and language profiles.
- Add authoritative references.
- Improve translations and terminology.
- Improve schemas, validation, accessibility, or tooling.
- Report outdated links, versions, and examples.

## Content requirements

A content contribution should include, where applicable: stable ID, title, locale, domain, target level, prerequisites, measurable objectives, sources, version scope, translation status, and known limitations. Use the templates in `templates/`.

Follow the [writing standard](docs/standards/writing-style.md), [source standard](docs/standards/citations-and-sources.md), and [editorial policy](docs/editorial-policy.md).

## Code examples

- Prefer small examples that demonstrate one idea.
- State required language/runtime versions.
- Show expected output where useful.
- Avoid secrets, destructive operations, and environment-specific assumptions.
- Test executable examples in a disposable, restricted environment before marking them Verified.

## Translation contributions

Preserve the stable content ID. Translate meaning and pedagogical intent, not word order. Keep code identifiers and compiler output unchanged unless localisation is the topic. Machine-assisted translations remain unreviewed until a qualified human reviewer checks them.

## Pull requests

Keep PRs focused. Explain what changed and why, link related issues, include sources, and add tests or explain why they are not applicable. Do not claim verification that has not happened.

Maintainers may request revisions or decline work that is unsupported, legally unclear, unsafe, inaccessible, or outside scope.
