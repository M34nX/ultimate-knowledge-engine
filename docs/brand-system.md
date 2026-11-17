# UKE Brand System — Cyber Blue

**Status:** Selected visual direction  
**Theme:** Cyber Blue  
**Applies to:** Repository identity, documentation, and the future UKE application  
**Version:** 1.0

## 1. Brand idea

UKE should feel like a precise, modern knowledge instrument: technical without looking hostile, futuristic without visual noise, and academic without feeling dated.

The Cyber Blue direction uses a deep navy foundation, electric blue as the primary action color, and cyan as a restrained signal color. A connected-node / circuit motif represents structured knowledge and relationships between concepts.

**Brand attributes:** precise · connected · curious · trustworthy · engineered

## 2. Color tokens

### Core palette

| Token | Hex | Use |
|---|---|---|
| Ink 950 | `#071426` | Main dark background |
| Ink 900 | `#0B1F36` | Elevated dark surfaces |
| Ink 800 | `#12304F` | Cards, navigation, panels |
| Blue 600 | `#1677FF` | Primary actions and links |
| Blue 500 | `#368BFF` | Hover and active emphasis |
| Cyan 400 | `#35D6F2` | Knowledge links, highlights, focus accents |
| Ice 100 | `#EAF4FF` | Light text on dark surfaces |
| Slate 500 | `#71839A` | Secondary text |
| Light 50 | `#F4F8FC` | Light-mode page background |
| Light 0 | `#FFFFFF` | Light-mode cards |
| Text 900 | `#102033` | Main light-mode text |
| Border | `#D9E4F0` | Light-mode separators |

### Semantic colors

| Meaning | Color | Hex |
|---|---|---|
| Success | Green | `#20A878` |
| Warning | Amber | `#E7A23B` |
| Error | Red | `#D94B59` |
| Information | Cyan | `#35BFD8` |

Semantic colors are reserved for status and feedback; they must not replace the primary brand blue.

## 3. Theme behavior

- **Default application theme:** Dark Cyber Blue.
- **Alternative:** Light mode using Light 50 / Light 0 surfaces and Text 900 typography.
- Respect the operating-system preference on first launch, then allow an explicit user choice.
- Keep the same semantic token names in both modes; change token values, not component logic.
- Avoid pure black backgrounds and large saturated-blue panels.
- Use cyan sparingly for focus, selected knowledge relationships, and small indicators.

## 4. Typography

- **Latin:** Inter; fallback: system-ui, sans-serif.
- **Persian:** Vazirmatn; fallback: Tahoma, sans-serif.
- **Code:** JetBrains Mono; fallback: ui-monospace, monospace.
- Headings use semibold or bold weights. Body text should prioritize legibility over density.
- Persian pages must use correct RTL direction while keeping code, paths, and technical identifiers LTR.
- Do not mix Persian and Latin punctuation carelessly; isolate inline code and identifiers where needed.

## 5. Logo and symbol

The UKE symbol is a compact network of connected nodes enclosed by a subtle geometric frame. It communicates a knowledge graph, not a literal brain or a generic robot.

- Use the supplied SVG symbol on dark or light backgrounds.
- Keep clear space around the mark equal to at least the diameter of one outer node.
- Do not stretch, rotate, add glow effects, or recolor individual nodes arbitrarily.
- Preferred lockup: symbol followed by **UKE**; full name may appear below or alongside it.
- Minimum symbol size in application navigation: 24 × 24 CSS pixels.

## 6. Shape, spacing, and depth

- Use a 12-column responsive layout for wide screens and a single-column flow on mobile.
- Base spacing unit: 4 px. Common spacing: 8, 12, 16, 24, 32, 48 px.
- Cards: 14–18 px radius. Inputs and compact controls: 10–12 px radius.
- Borders should be subtle. Use elevation sparingly; prefer surface contrast over heavy shadows.
- Motion should be short and functional (roughly 140–220 ms). Respect reduced-motion preferences.

## 7. Component rules

| Component | Direction |
|---|---|
| Primary button | Blue 600 fill, white text; clear focus ring |
| Secondary button | Transparent or Ink 800 surface with a visible border |
| Links | Blue 500 on light surfaces; Cyan 400 or Blue 500 on dark surfaces, with underline on hover |
| Navigation | Ink 900 surface; selected item uses a blue-tinted background and a clear indicator |
| Cards | Ink 900 / Ink 800 in dark mode; white in light mode |
| Search | Prominent field with a small cyan focus accent |
| Progress | Blue track with cyan endpoint/highlight |
| Code blocks | Deep navy surface, readable syntax contrast, copy action |
| Status labels | Semantic colors only when communicating a real state |

## 8. Knowledge visual language

- Use connected dots and thin lines to represent prerequisites, concept relations, and learning paths.
- Use diagrams to explain relationships, not as decoration.
- Keep diagrams low-noise: navy/neutral surfaces, blue for the active path, cyan for the current node.
- Never rely on color alone to communicate graph state; include labels, shape, or line-style differences.

## 9. Accessibility

- Maintain WCAG 2.2 AA contrast for normal text and interactive controls.
- Provide visible keyboard focus and sufficiently large touch targets (prefer 44 × 44 px).
- Do not communicate success, warning, or errors by color alone.
- Support keyboard navigation, screen readers, zoom, and reduced motion.
- Test both Persian RTL and English LTR layouts.

## 10. Repository presentation

- README headings and tables remain simple and readable; avoid decorative emoji overload.
- Use the SVG mark at the top of the README and link to this document as the source of truth.
- Screenshots and future app previews should use the same palette, typography, and component rules.
- Do not imply that planned application screens or features are already implemented.

## 11. Implementation tokens

The following CSS custom properties are the canonical starting point for the future application:

```css
:root {
  color-scheme: dark;
  --uke-bg: #071426;
  --uke-surface: #0B1F36;
  --uke-surface-raised: #12304F;
  --uke-primary: #1677FF;
  --uke-primary-hover: #368BFF;
  --uke-accent: #35D6F2;
  --uke-text: #EAF4FF;
  --uke-text-muted: #9AAEC4;
  --uke-border: #24415F;
  --uke-success: #20A878;
  --uke-warning: #E7A23B;
  --uke-danger: #D94B59;
  --uke-radius-card: 16px;
  --uke-radius-control: 11px;
  --uke-space-unit: 4px;
}

[data-theme="light"] {
  color-scheme: light;
  --uke-bg: #F4F8FC;
  --uke-surface: #FFFFFF;
  --uke-surface-raised: #EAF4FF;
  --uke-primary: #1268E8;
  --uke-primary-hover: #075ACB;
  --uke-accent: #087F9A;
  --uke-text: #102033;
  --uke-text-muted: #52677F;
  --uke-border: #D9E4F0;
}
```

These tokens define the design direction; they are not yet wired into an application stylesheet.
