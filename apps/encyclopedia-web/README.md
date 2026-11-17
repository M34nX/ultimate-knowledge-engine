# Encyclopedia Web Application

## Purpose

A future multilingual website generated from the canonical repository content. The repository remains the source of truth; the site must not maintain a parallel hand-edited copy of lessons.

## Product identity

The future interface follows the [UKE Cyber Blue brand system](../../docs/brand-system.md), uses the shared [design tokens](../../assets/brand/tokens.css), and follows the [interface guidelines](../../docs/interface-guidelines.md).

## Initial implementation direction

- Astro + Starlight for documentation-oriented navigation.
- TypeScript for content loading and build-time validation.
- Markdown/MDX as the presentation source for authored pages.
- Pagefind or an equivalent static index for the first search implementation.

## Required milestones

1. Load validated content and stable IDs.
2. Support locale-aware navigation and RTL/LTR layouts.
3. Apply canonical design tokens with dark and light themes.
4. Display source, version, and publication status.
5. Provide keyboard-accessible search and navigation.
6. Add responsive and accessibility testing.
7. Add richer semantic search only after the basic index is dependable.

## Non-negotiable security boundary

The website must never execute arbitrary user code in its own process. A future code playground must be an isolated, separately secured service with strict CPU, memory, time, filesystem, and network controls.

This directory contains architecture notes only; the application has not yet been implemented.
