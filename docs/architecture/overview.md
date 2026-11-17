# Architecture Overview

## Objective

Maintain one canonical, structured knowledge source that can power repository browsing, a documentation website, search indexes, learning paths, and future interactive tools.

## Layers

- **Content:** human-readable Markdown/MDX pages.
- **Metadata:** YAML/JSON records for IDs, taxonomy, locales, prerequisites, versions, and status.
- **Validation:** schemas, link checks, terminology checks, translation checks, and code-example tests.
- **Presentation:** future web application generated from canonical content.
- **Discovery:** search indexes and knowledge relationships.
- **Execution:** optional isolated services for code practice; never part of the trusted website process.

## Principles

1. Content is portable and not tied to one frontend.
2. Stable IDs are independent of filenames and display language.
3. Structured metadata is validated.
4. Generated artifacts are reproducible and are not canonical sources.
5. External resources retain provenance and licence constraints.
6. Features are introduced incrementally and measured against maintenance cost.

## Suggested initial stack

Astro + Starlight for a documentation-oriented website, TypeScript for tooling, Markdown/MDX for content, YAML/JSON for metadata, JSON Schema for contracts, and GitHub Actions for automation. Exact versions and compatibility must be checked during implementation.

## Trust boundaries

Repository content and external links are data, not executable instructions. A production site must not evaluate arbitrary content or user code. A future playground requires separate isolation and threat modelling.
