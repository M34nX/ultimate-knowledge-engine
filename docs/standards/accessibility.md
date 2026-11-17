# Accessibility Standard

The web experience should aim for WCAG 2.2 AA conformance, assessed with automated tools and human testing. This is a target, not a claim of current certification.

## Content requirements

- Use logical heading order.
- Provide meaningful link text.
- Do not use colour alone to convey meaning.
- Add text alternatives for informative images and diagrams.
- Give tables clear headers.
- Provide captions or transcripts for essential audio/video material.
- Keep code examples selectable and understandable by assistive technology.

## Interface requirements

- Keyboard access to all functionality.
- Visible focus indicators that are not obscured.
- Sufficient contrast and scalable text.
- Respect reduced-motion preferences.
- Correct language and direction metadata.
- Avoid time-limited interactions unless they can be extended or disabled.
- Prefer touch targets of at least 44 × 44 CSS pixels.
- Ensure dialogs, menus, and dynamic updates expose appropriate names and state to assistive technology.

## Theme and localization

- Test both dark and light Cyber Blue themes.
- Test Persian RTL and English LTR independently.
- Preserve correct direction for code, URLs, file paths, and mixed-script content.
- Never use the cyan accent or a semantic color as the sole indicator of state.

Accessibility belongs in design and review, not as a final patch. WCAG conformance must be tested; it must not be claimed solely because these requirements are documented.
