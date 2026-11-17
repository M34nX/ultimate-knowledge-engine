# Knowledge Graph

The knowledge graph records meaningful relationships between stable UKE content IDs.

## Files

- `concepts.yaml`: nodes and their metadata.
- `relationships.yaml`: typed, directed links between nodes.

## Rules

- Every referenced ID must exist in the node registry or be explicitly marked as an external entity.
- Use typed relationships rather than vague links.
- Prerequisites must reflect genuine learning dependencies.
- Do not infer equivalence from similar names.
- Add a short rationale for non-obvious relationships.
- Keep graph data reviewable in Git and validate it before generating visualisations.

The graph is an index over content, not a replacement for the explanations themselves.
