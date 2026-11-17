# ADR 0001: Canonical Content Source

- **Status:** Accepted
- **Date:** 2026-11-18

## Context

Maintaining separate copies of lessons in a repository and a website creates duplication, translation drift, and inconsistent updates.

## Decision

The Git repository is the canonical source for authored content and metadata. Website pages, search indexes, graph views, and other generated outputs are derived from this source.

## Consequences

- Content remains portable and reviewable in Git.
- The website build must preserve IDs, locale state, sources, and version scope.
- Generated output should not be manually edited as a substitute for source changes.
- Build tooling must validate inputs before publication.
