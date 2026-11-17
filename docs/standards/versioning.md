# Versioning Standard

## Why versioning matters

Language syntax, libraries, frameworks, runtimes, standards, and platform behaviour change over time. A technically correct statement for one release may be incorrect for another.

## Requirements

- Mark claims that depend on a version.
- Prefer explicit version ranges over vague phrases such as “recent versions”.
- Distinguish stable language specifications from implementation-specific behaviour.
- Identify whether an example was tested and with which tool/runtime version.
- Record breaking changes and migration notes.
- Mark content Outdated when its scope can no longer be confirmed.

## Compatibility fields

Use structured fields such as `introduced_in`, `removed_in`, `deprecated_in`, `minimum_version`, `maximum_version`, and `tested_versions` where applicable. Do not invent version data when it is unknown.
