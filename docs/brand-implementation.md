# Brand Implementation Guide

This guide translates the Cyber Blue identity into repeatable repository and product decisions. The canonical values live in `assets/brand/tokens.json`; the CSS reference implementation lives in `assets/brand/tokens.css`.

## Source of truth

1. `docs/brand-system.md` defines the visual principles and design decisions.
2. `assets/brand/tokens.json` is the machine-readable token catalogue.
3. `assets/brand/tokens.css` is the CSS custom-property implementation.
4. `assets/brand/uke-symbol.svg` and `assets/brand/uke-wordmark.svg` are the approved vector marks.

If a token changes, update the JSON and CSS together in the same change. Do not create local, unexplained color values for shared UI components.

## Logo usage

- Use the symbol for compact app icons and navigation.
- Use the wordmark for landing pages, repository introductions, and splash/intro surfaces.
- Preserve the SVG viewBox and aspect ratio.
- Provide meaningful alternative text when the mark conveys identity; use empty alternative text when it is purely decorative beside an equivalent text label.
- Never bake a slogan, version number, or theme color into a raster-only logo variant.

## Repository surfaces

| Surface | Required treatment |
|---|---|
| Root README | Wordmark or symbol, short project description, status, navigation, brand-system link |
| Domain landing pages | Consistent title, scope, content status, next steps |
| Lessons and concepts | Content-first layout; status/version/source metadata remains visible |
| Contribution docs | Same heading, table, code, and link conventions |
| Issue and PR templates | Clear sections and concise checklists; no decorative branding |
| App documentation | Shared tokens, RTL/LTR, accessibility and responsive rules |

GitHub Markdown does not support the full application theme. Keep repository pages readable with native Markdown; use brand artwork and consistent information architecture rather than relying on custom CSS that GitHub will not render.

## Change control

A brand change must include:
- rationale and affected surfaces;
- token JSON and CSS updates;
- updated previews or documentation where needed;
- dark and light mode review;
- Persian RTL and English LTR review;
- keyboard focus and contrast review.

The brand system is a design specification, not proof that a future application has been implemented.
