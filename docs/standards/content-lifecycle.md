# Content Lifecycle Standard

## States

- **Draft:** authored but not reviewed.
- **Reviewed:** a reviewer checked structure, clarity, and source adequacy.
- **Verified:** technical claims and applicable examples were checked against sources or tests.
- **Published:** approved for the intended audience and locale.
- **Outdated:** needs review because a source, version, or ecosystem may have changed.
- **Deprecated:** intentionally retired; provide a replacement or reason where possible.

## Rules

- Every new page begins as Draft.
- Review and verification are distinct.
- A translation is not Verified just because its source-language page is Verified.
- Version-sensitive content must state its scope.
- Outdated content should show a warning until reviewed or retired.
- Published content should retain review history in Git and metadata.

## Review evidence

For technical claims, record the authoritative source and relevant version. For code examples, record the runtime/tool version and test method where applicable.
