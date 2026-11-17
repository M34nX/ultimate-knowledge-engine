# Multilingual Architecture

## Model

A concept has one stable identity and multiple locale-specific representations. Translation files must not create new concept IDs merely because the display language changes.

## Locale identifiers

Use BCP 47 language tags where appropriate, such as `en`, `fa`, `es`, `fr`, `de`, `pt-BR`, `zh-CN`, `zh-TW`, `ja`, `ko`, `ru`, `tr`, `ar`, and `hi`.

The initial catalogue is in `registry/locales.yaml`. Add regional variants only when there is a real editorial or audience need.

## Reference locale

English is the initial technical reference locale. Persian is a first-class initial publication locale. A reference locale does not make other languages secondary in accuracy or pedagogy.

## Translation states

Recommended states: missing, draft, machine-assisted, reviewed, verified, published, outdated. The application must show incomplete states honestly.

## Direction and typography

RTL and LTR are page-level presentation concerns. Do not reverse code, filenames, command-line snippets, URLs, or identifiers. Use locale-aware date, number, and typography formatting.

## Search

Future search should index localised titles, aliases, canonical English terms, synonyms, and transliterations while returning results in the selected locale where available.
