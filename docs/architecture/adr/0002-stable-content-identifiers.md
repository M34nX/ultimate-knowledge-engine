# ADR 0002: Stable Content Identifiers

- **Status:** Accepted
- **Date:** 2026-11-18

## Context

Titles, filenames, and translations change. Links and graph relationships need a stable identity.

## Decision

Each concept and reusable content entity receives a stable ID independent of locale and display title.

## Consequences

- Translation files share the same conceptual ID.
- Renames do not automatically change the content identity.
- Split, merged, and superseded content requires explicit migration or redirect metadata.
- IDs must never be silently reused for unrelated concepts.
