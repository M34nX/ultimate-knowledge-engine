# Interface Language and Microcopy Standard

## Principles

- Be concise, specific, respectful, and neutral.
- Prefer familiar verbs: Open, Search, Continue, Save, Retry, Cancel.
- Explain what happened and what the user can do next.
- Do not blame the learner for errors.
- Avoid vague labels such as "Submit" when a more specific action is available.
- Do not use urgency, streak loss, or guilt to pressure continued use.

## Status language

Use explicit states consistently:
- Draft — not yet reviewed.
- Reviewed — checked by a reviewer; not necessarily independently verified.
- Verified — passed the defined verification process.
- Published — approved for the intended audience.
- Outdated — retained for history but no longer current.
- Deprecated — no longer recommended.

Never use a visual badge to imply a stronger review state than the content actually has.

## Errors

An error message should include:
1. what failed;
2. whether user input was preserved;
3. a safe next step;
4. a support or diagnostic reference when useful.

Do not expose stack traces, tokens, internal paths, or personal data in user-facing errors.

## Persian and English

- Write idiomatic Persian rather than word-for-word English translations.
- Keep product names, code identifiers, commands, and standard technical abbreviations unchanged where appropriate.
- Maintain one approved glossary per locale.
- Test mixed-direction strings containing Persian, Latin text, numbers, and punctuation.
- Translate meaning and action, not just individual words.
