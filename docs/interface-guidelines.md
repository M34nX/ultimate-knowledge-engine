# UKE Interface Guidelines

These guidelines apply to future UKE websites and applications. They do not claim that the interface is already implemented.

## Layout

- Design mobile-first; support narrow phones, tablets, laptops, and wide displays.
- Use a readable content measure and avoid stretching long-form lessons across the full viewport.
- Keep primary navigation stable and make the current location clear.
- Use consistent spacing based on the 4 px token unit.
- Prefer surface contrast and borders over large shadows or decorative gradients.

## Core surfaces

- **Page:** `--uke-bg`
- **Card/panel:** `--uke-surface`
- **Raised panel:** `--uke-surface-raised`
- **Primary action:** `--uke-primary`
- **Focus/knowledge accent:** `--uke-accent`
- **Body text:** `--uke-text`
- **Secondary text:** `--uke-text-muted`

Do not use accent cyan for large blocks of body text. Reserve it for focus, selected relationships, and concise highlights.

## Component behavior

| Component | Rule |
|---|---|
| Buttons | Clear verb labels; distinguish primary, secondary, and destructive actions |
| Inputs | Persistent labels, helpful errors, keyboard support |
| Navigation | Current item is indicated by text and shape, not color alone |
| Cards | Use only when content forms a meaningful group |
| Tables | Provide headers, captions when needed, and mobile overflow handling |
| Code | Preserve whitespace, identify language, allow copying without losing selectable text |
| Alerts | State the issue and the next action; do not rely on color alone |
| Progress | Pair visual progress with a readable value or description |
| Dialogs | Manage focus, provide an accessible name, and support Escape when appropriate |

## Theme and direction

- Dark Cyber Blue is the default design reference; light mode is equally supported.
- Respect system theme on first visit and provide a persistent explicit choice when an application exists.
- Set document language and direction per locale.
- Persian uses RTL for prose and navigation; code, file paths, URLs, and technical identifiers remain LTR and isolated from surrounding text.
- Do not reverse mathematical notation or code syntax as a side effect of RTL layout.

## Motion

Use motion only to communicate state changes or spatial relationships. Keep transitions short and support `prefers-reduced-motion`. Avoid parallax, flashing, and attention-seeking animation.

## Responsive navigation

On small screens, navigation may collapse behind a clearly labelled control. Keep search, locale switching, and theme switching discoverable. Touch targets should preferably be at least 44 × 44 CSS pixels.

## Content-first principle

The interface must not obscure the learning material. Avoid gamification that pressures learners, noisy dashboards, excessive badges, or auto-playing media. Learning progress should be informative and optional.
