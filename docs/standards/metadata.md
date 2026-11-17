# Metadata Standard

Metadata supports navigation, validation, translation tracking, search, and future graph generation.

## General rules

- Use stable IDs and predictable field names.
- Use ISO 8601 dates (`YYYY-MM-DD`) for date-only metadata.
- Use BCP 47 locale tags.
- Use controlled values for status, level, and content type.
- Keep metadata factual; do not put prose paragraphs in machine fields.
- Omit inapplicable optional fields instead of inserting misleading placeholders.
- Validate metadata with the schemas in `schemas/`.

## Recommended fields

`id`, `title`, `content_type`, `locale`, `domain`, `level`, `status`, `prerequisites`, `learning_objectives`, `version_scope`, `sources`, `translation_of`, `last_reviewed`.

Templates show examples. Schema files are the validation contract.
