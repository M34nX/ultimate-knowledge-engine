# Web Encyclopedia Architecture

## Goal

Generate the public learning and reference website from repository content. The site must not maintain a parallel hand-edited copy of canonical lessons.

## Initial recommendation

Astro with Starlight is a strong initial fit for structured technical documentation. TypeScript can power content ingestion and validation. Pagefind may provide static search initially; richer semantic search can be evaluated later.

## Required capabilities

- locale-aware navigation and page switching;
- right-to-left and left-to-right layout support;
- accessible headings, landmarks, contrast, and keyboard navigation;
- structured metadata and canonical URLs;
- search by title, alias, term, and language;
- visible content status and version scope;
- source citations and last-reviewed details;
- responsive layouts and print-friendly pages;
- selected-page offline support, if practical.

## First-release non-goals

Do not build accounts, adaptive learning, AI chat, or code execution before the content pipeline and basic site are reliable.

## Security

Treat content, user input, embeds, and external links as untrusted. Avoid arbitrary HTML where possible. Do not run user code inside the web server or main site context.
