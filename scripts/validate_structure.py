#!/usr/bin/env python3
"""Validate the minimum UKE repository foundation using only Python's standard library."""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_PATHS = (
    "README.md",
    "START-HERE.md",
    "CONTRIBUTING.md",
    "PROJECT-STATUS.md",
    "docs/architecture/overview.md",
    "docs/roadmap.md",
    "registry/domains.yaml",
    "registry/languages.yaml",
    "registry/locales.yaml",
    "schemas/concept.schema.json",
    "schemas/lesson.schema.json",
    "content/en/README.md",
    "content/fa/README.md",
)

SCHEMA_FILES = (
    "schemas/concept.schema.json",
    "schemas/lesson.schema.json",
    "schemas/exercise.schema.json",
    "schemas/reference.schema.json",
)


def main() -> int:
    errors: list[str] = []

    for relative in REQUIRED_PATHS:
        if not (ROOT / relative).is_file():
            errors.append(f"Missing required file: {relative}")

    for relative in SCHEMA_FILES:
        path = ROOT / relative
        if not path.is_file():
            continue
        try:
            with path.open("r", encoding="utf-8") as handle:
                schema = json.load(handle)
            if not isinstance(schema, dict) or schema.get("type") != "object":
                errors.append(f"Schema must be a JSON object schema: {relative}")
        except (OSError, json.JSONDecodeError) as exc:
            errors.append(f"Invalid JSON schema {relative}: {exc}")

    if errors:
        print("UKE foundation validation failed:")
        for error in errors:
            print(f" - {error}")
        return 1

    print("UKE foundation structure and JSON schemas are valid.")
    print("Note: YAML parsing, frontmatter validation, links, translations, and code examples")
    print("require additional validators and are not checked by this lightweight script.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
