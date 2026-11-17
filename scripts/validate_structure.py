#!/usr/bin/env python3
"""Validate UKE registries, content frontmatter, schemas, links, and graph references."""

from __future__ import annotations

import json
import re
import sys
from collections import defaultdict
from pathlib import Path
from urllib.parse import unquote
from typing import Any

import yaml
from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[1]
SCHEMA_NAMES = ("concept", "lesson", "exercise", "reference", "language", "roadmap")
CONTENT_SCHEMAS = {"concept": "concept", "lesson": "lesson", "exercise": "exercise"}
FRONTMATTER = re.compile(r"\A---\s*\n(.*?)\n---\s*(?:\n|\Z)", re.DOTALL)
MARKDOWN_LINK = re.compile(r"(?<!!)\[[^\]]*\]\(([^)\s]+)(?:\s+[^)]*)?\)")


def add_error(message: str) -> None:
    ERRORS.append(message)


ERRORS: list[str] = []


def read_yaml(path: Path) -> Any:
    try:
        return yaml.safe_load(path.read_text(encoding="utf-8"))
    except (OSError, yaml.YAMLError) as exc:
        add_error(f"Invalid YAML {path.relative_to(ROOT)}: {exc}")
        return None


def load_schemas() -> dict[str, Draft202012Validator]:
    validators: dict[str, Draft202012Validator] = {}
    for name in SCHEMA_NAMES:
        path = ROOT / "schemas" / f"{name}.schema.json"
        try:
            schema = json.loads(path.read_text(encoding="utf-8"))
            Draft202012Validator.check_schema(schema)
            validators[name] = Draft202012Validator(schema, format_checker=FormatChecker())
        except Exception as exc:
            add_error(f"Invalid schema {path.relative_to(ROOT)}: {exc}")
    return validators


def validate_content(
    validators: dict[str, Draft202012Validator],
    valid_locales: set[str],
    valid_domains: set[str],
    valid_sources: set[str],
) -> dict[str, set[str]]:
    ids_by_locale: dict[str, set[str]] = defaultdict(set)
    seen: set[tuple[str, str]] = set()

    for path in sorted((ROOT / "content").rglob("*.md")):
        text = path.read_text(encoding="utf-8")
        match = FRONTMATTER.match(text)
        if not match:
            continue

        try:
            metadata = yaml.safe_load(match.group(1))
        except yaml.YAMLError as exc:
            add_error(f"Invalid frontmatter in {path.relative_to(ROOT)}: {exc}")
            continue

        if not isinstance(metadata, dict):
            add_error(f"Frontmatter must be a mapping: {path.relative_to(ROOT)}")
            continue

        schema_name = CONTENT_SCHEMAS.get(metadata.get("content_type"))
        if schema_name is None:
            add_error(f"Unknown content_type in {path.relative_to(ROOT)}")
            continue

        validator = validators.get(schema_name)
        if validator is not None:
            for issue in validator.iter_errors(metadata):
                location = ".".join(str(part) for part in issue.path)
                add_error(f"{path.relative_to(ROOT)} [{location}]: {issue.message}")

        content_id = metadata.get("id")
        locale = metadata.get("locale")
        domain = metadata.get("domain")
        if isinstance(content_id, str) and isinstance(locale, str):
            key = (content_id, locale)
            if key in seen:
                add_error(f"Duplicate content ID/locale pair: {content_id} ({locale})")
            seen.add(key)
            ids_by_locale[locale].add(content_id)

        if locale not in valid_locales:
            add_error(f"Unknown locale in {path.relative_to(ROOT)}: {locale}")
        if domain not in valid_domains:
            add_error(f"Unknown domain in {path.relative_to(ROOT)}: {domain}")

        for source_id in metadata.get("sources", []):
            if source_id not in valid_sources:
                add_error(f"Unknown source ID '{source_id}' in {path.relative_to(ROOT)}")

    return ids_by_locale


def validate_internal_links() -> int:
    checked = 0
    fence = chr(96) * 3
    for path in sorted(ROOT.rglob("*.md")):
        if any(part.startswith(".") for part in path.relative_to(ROOT).parts):
            continue
        text = path.read_text(encoding="utf-8")
        text = re.sub(fence + r".*?" + fence, "", text, flags=re.DOTALL)
        for match in MARKDOWN_LINK.finditer(text):
            target = unquote(match.group(1))
            if target.startswith(("https://", "http://", "mailto:", "tel:", "//")):
                continue
            target = target.split("#", 1)[0].split("?", 1)[0]
            if not target:
                continue
            destination = (ROOT / target.lstrip("/")) if target.startswith("/") else (path.parent / target)
            destination = destination.resolve()
            try:
                destination.relative_to(ROOT.resolve())
            except ValueError:
                add_error(f"Internal link escapes repository in {path.relative_to(ROOT)}: {target}")
                continue
            if destination.is_dir():
                destination = destination / "README.md"
            checked += 1
            if not destination.is_file():
                add_error(f"Broken internal link in {path.relative_to(ROOT)}: {target}")
    return checked



WORKBOOK_PATHS = {
    "en": ROOT / "learning" / "programming-languages" / "40-language-workbook.md",
    "fa": ROOT / "learning" / "programming-languages" / "40-language-workbook.fa.md",
}
WORKBOOK_HEADINGS = re.compile(r"(?m)^###\s+(\d{2})\.\s+(.+?)\s*$")
WORKBOOK_LANGUAGE_IDS = {
    "Python": "python", "JavaScript": "javascript", "TypeScript": "typescript",
    "Java": "java", "C": "c", "C++": "cpp", "C#": "csharp", "Go": "go",
    "Rust": "rust", "PHP": "php", "Ruby": "ruby", "Swift": "swift",
    "Kotlin": "kotlin", "Dart": "dart", "R": "r", "Julia": "julia",
    "MATLAB": "matlab", "Scala": "scala", "Haskell": "haskell",
    "Elixir": "elixir", "Erlang": "erlang", "Clojure": "clojure",
    "OCaml": "ocaml", "F#": "fsharp", "Lua": "lua", "Perl": "perl",
    "Bash": "bash", "PowerShell": "powershell", "Fortran": "fortran",
    "COBOL": "cobol", "Ada": "ada", "Pascal": "pascal", "Groovy": "groovy",
    "Solidity": "solidity", "Move": "move", "Zig": "zig",
    "GDScript": "gdscript", "Vyper": "vyper", "Objective-C": "objective_c",
    "Assembly (x86-64 NASM)": "assembly",
}


def validate_programming_workbooks(language_ids: set[str]) -> int:
    """Check count, numbering, bilingual parity, examples, extensions, and registry coverage."""
    names_by_locale: dict[str, list[str]] = {}
    fence = chr(96) * 3
    marker = chr(96)
    for locale, path in WORKBOOK_PATHS.items():
        if not path.is_file():
            add_error(f"Missing {locale} programming-language workbook: {path.relative_to(ROOT)}")
            continue
        text = path.read_text(encoding="utf-8")
        headings = list(WORKBOOK_HEADINGS.finditer(text))
        numbers = [int(m.group(1)) for m in headings]
        names = [m.group(2).strip() for m in headings]
        names_by_locale[locale] = names
        if len(headings) != 40:
            add_error(f"{path.relative_to(ROOT)} must contain exactly 40 examples; found {len(headings)}.")
        if numbers != list(range(1, 41)):
            add_error(f"{path.relative_to(ROOT)} example numbers must be consecutive from 01 to 40.")
        if len(set(names)) != len(names):
            add_error(f"{path.relative_to(ROOT)} contains duplicate language headings.")
        for index, heading in enumerate(headings):
            end = headings[index + 1].start() if index + 1 < len(headings) else len(text)
            section = text[heading.end():end]
            name = heading.group(2).strip()
            if len(re.findall(r"(?m)^" + re.escape(fence), section)) < 2:
                add_error(f"{path.relative_to(ROOT)} has no complete fenced code sample for {name}.")
            ext_pattern = r"(?m)^\*\*File extension:\*\* " + re.escape(marker) + r"\.[A-Za-z0-9]+" + re.escape(marker) + "$"
            if not re.search(ext_pattern, section):
                add_error(f"{path.relative_to(ROOT)} has no explicit file extension for {name}.")
            lang_id = WORKBOOK_LANGUAGE_IDS.get(name)
            if lang_id is None:
                add_error(f"Unmapped workbook language in {path.relative_to(ROOT)}: {name}")
            elif lang_id not in language_ids:
                add_error(f"Workbook language is missing from registry: {name} ({lang_id})")
    if "en" in names_by_locale and "fa" in names_by_locale and names_by_locale["en"] != names_by_locale["fa"]:
        add_error("English and Persian programming-language workbooks have different language order or headings.")
    return min(len(names_by_locale.get("en", [])), len(names_by_locale.get("fa", [])))


def main() -> int:
    validators = load_schemas()
    domains_data = read_yaml(ROOT / "registry" / "domains.yaml") or {}
    languages_data = read_yaml(ROOT / "registry" / "languages.yaml") or {}
    locales_data = read_yaml(ROOT / "registry" / "locales.yaml") or {}
    resources_data = read_yaml(ROOT / "registry" / "resources.yaml") or {}
    graph_nodes = read_yaml(ROOT / "knowledge-graph" / "concepts.yaml") or {}
    graph_edges = read_yaml(ROOT / "knowledge-graph" / "relationships.yaml") or {}

    domains = domains_data.get("domains", [])
    languages = languages_data.get("entries", [])
    initial_locales = locales_data.get("initial_locales", [])
    planned_locales = locales_data.get("planned_locales", [])
    resources = resources_data.get("resources", [])
    nodes = graph_nodes.get("nodes", [])
    edges = graph_edges.get("relationships", [])

    domain_slugs = {item.get("slug") for item in domains if isinstance(item, dict)}
    locale_tags = {item.get("tag") for item in [*initial_locales, *planned_locales] if isinstance(item, dict)}
    source_ids = {item.get("id") for item in resources if isinstance(item, dict)}
    language_ids = [item.get("id") for item in languages if isinstance(item, dict)]
    node_ids = {item.get("id") for item in nodes if isinstance(item, dict)}

    if len(domain_slugs) != len(domains):
        add_error("Domain slugs are missing or duplicated.")
    if len(locale_tags) != len(initial_locales) + len(planned_locales):
        add_error("Locale tags are missing or duplicated.")
    if len(language_ids) != len(languages):
        add_error("Language IDs are missing or duplicated.")
    if len(node_ids) != len(nodes):
        add_error("Knowledge graph node IDs are missing or duplicated.")

    for locale in ("en", "fa"):
        for slug in domain_slugs:
            landing = ROOT / "content" / locale / slug / "README.md"
            if not landing.is_file():
                add_error(f"Missing {locale} domain landing page: {slug}")

    for path in sorted((ROOT / "content").rglob("language-profile.yaml")):
        metadata = read_yaml(path)
        if isinstance(metadata, dict) and "language" in validators:
            for issue in validators["language"].iter_errors(metadata):
                add_error(f"{path.relative_to(ROOT)}: {issue.message}")
            if metadata.get("id") not in set(language_ids):
                add_error(f"Language profile not present in registry: {metadata.get('id')}")

    for edge in edges:
        if not isinstance(edge, dict):
            add_error("Knowledge graph relationship must be a mapping.")
            continue
        if edge.get("from") not in node_ids:
            add_error(f"Unknown graph source node: {edge.get('from')}")
        if edge.get("to") not in node_ids:
            add_error(f"Unknown graph target node: {edge.get('to')}")

    for relative in (
        "README.md", "START-HERE.md", "CONTRIBUTING.md",
        "docs/architecture/overview.md", "docs/roadmap.md",
        "content/en/README.md", "content/fa/README.md",
    ):
        if not (ROOT / relative).is_file():
            add_error(f"Missing required file: {relative}")

    ids_by_locale = validate_content(validators, locale_tags, domain_slugs, source_ids)
    shared = ids_by_locale.get("en", set()) & ids_by_locale.get("fa", set())
    if not shared:
        add_error("No shared stable content IDs found between en and fa.")

    checked_links = validate_internal_links()
    validated_workbook_examples = validate_programming_workbooks(set(language_ids))
    if ERRORS:
        print("UKE validation failed:")
        for item in ERRORS:
            print(f" - {item}")
        return 1

    print("UKE validation passed.")
    print(f" - {len(domains)} knowledge domains with English and Persian landing pages")
    print(f" - {len(languages)} language/technology registry entries")
    print(f" - {len(locale_tags)} initial/planned locales")
    print(f" - {len(nodes)} knowledge graph nodes and {len(edges)} relationships")
    print(f" - {len(shared)} shared English/Persian content IDs")
    print(f" - {checked_links} internal Markdown links checked")
    print(f" - {validated_workbook_examples} examples checked in each programming-language workbook")
    return 0


if __name__ == "__main__":
    sys.exit(main())
