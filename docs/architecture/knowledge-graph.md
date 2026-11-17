# Knowledge Graph Design

## Purpose

Represent relationships between concepts so learners can understand prerequisites, alternatives, related ideas, and cross-language equivalents.

## Relationship vocabulary

- `prerequisite_of`
- `related_to`
- `part_of`
- `implements`
- `contrasts_with`
- `alternative_to`
- `introduced_in`
- `removed_in`
- `has_translation`
- `implemented_by`

## Quality rules

Relationships must be meaningful, typed, and traceable. Avoid adding edges merely to make the graph look dense. Prerequisites should represent genuine learning dependencies, not loose associations.

## Initial storage

Begin with validated YAML/JSON records in the repository. A graph database is not required until scale and query patterns justify it. Generated graph views are derived artefacts, not canonical records.
