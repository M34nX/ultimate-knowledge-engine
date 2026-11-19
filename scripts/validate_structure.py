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
SCHEMA_NAMES = ("concept", "lesson", "exercise", "reference", "language", "roadmap", "project")
CONTENT_SCHEMAS = {"concept": "concept", "lesson": "lesson", "exercise": "exercise", "project": "project"}
FRONTMATTER = re.compile(r"\A---\s*\n(.*?)\n---\s*(?:\n|\Z)", re.DOTALL)
MARKDOWN_LINK = re.compile(r"(?<!!)\[[^\]]*\]\(([^)\s]+)(?:\s+[^)]*)?\)")


def add_error(message: str) -> None:
    ERRORS.append(message)


ERRORS: list[str] = []


def read_text(path: Path) -> str | None:
    try:
        return path.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as exc:
        add_error(f"Unable to read {path.relative_to(ROOT)}: {exc}")
        return None


def read_yaml(path: Path) -> Any:
    text = read_text(path)
    if text is None:
        return None
    try:
        return yaml.safe_load(text)
    except yaml.YAMLError as exc:
        add_error(f"Invalid YAML {path.relative_to(ROOT)}: {exc}")
        return None


def read_mapping(path: Path) -> dict[str, Any]:
    value = read_yaml(path)
    if value is None:
        return {}
    if not isinstance(value, dict):
        add_error(f"Top-level YAML must be a mapping: {path.relative_to(ROOT)}")
        return {}
    return value


def read_mapping_list(data: dict[str, Any], key: str, path: Path) -> list[dict[str, Any]]:
    value = data.get(key)
    if not isinstance(value, list):
        add_error(f"Registry field '{key}' must be a list: {path.relative_to(ROOT)}")
        return []
    mappings: list[dict[str, Any]] = []
    for index, item in enumerate(value):
        if not isinstance(item, dict):
            add_error(f"Registry field '{key}' entry {index} must be a mapping: {path.relative_to(ROOT)}")
            continue
        mappings.append(item)
    return mappings


def string_values(items: list[dict[str, Any]], key: str, path: Path, label: str) -> list[str]:
    values: list[str] = []
    for index, item in enumerate(items):
        value = item.get(key)
        if not isinstance(value, str) or not value.strip():
            add_error(f"{label} entry {index} must contain a non-empty string '{key}': {path.relative_to(ROOT)}")
            continue
        values.append(value)
    return values


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

    content_roots = (ROOT / "content", ROOT / "learning" / "build-from-scratch")
    for content_root in content_roots:
        for path in sorted(content_root.rglob("*.md")):
            text = read_text(path)
            if text is None:
                continue
            match = FRONTMATTER.match(text)
            if not match:
                try:
                    track_relative = path.relative_to(ROOT / "learning" / "build-from-scratch")
                except ValueError:
                    track_relative = None
                if track_relative is not None and len(track_relative.parts) == 2 and path.name in ("README.md", "README.fa.md"):
                    add_error(f"Missing project metadata in {path.relative_to(ROOT)}")
                continue

            try:
                metadata = yaml.safe_load(match.group(1))
            except yaml.YAMLError as exc:
                add_error(f"Invalid frontmatter in {path.relative_to(ROOT)}: {exc}")
                continue
    
            if not isinstance(metadata, dict):
                add_error(f"Frontmatter must be a mapping: {path.relative_to(ROOT)}")
                continue
    
            content_type = metadata.get("content_type")
            schema_name = CONTENT_SCHEMAS.get(content_type) if isinstance(content_type, str) else None
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

            if not isinstance(locale, str) or locale not in valid_locales:
                add_error(f"Unknown locale in {path.relative_to(ROOT)}: {locale}")
            if not isinstance(domain, str) or domain not in valid_domains:
                add_error(f"Unknown domain in {path.relative_to(ROOT)}: {domain}")

            source_ids = metadata.get("sources", [])
            if not isinstance(source_ids, list):
                add_error(f"Sources must be a list in {path.relative_to(ROOT)}")
                source_ids = []
            for source_id in source_ids:
                if not isinstance(source_id, str):
                    add_error(f"Source IDs must be strings in {path.relative_to(ROOT)}")
                elif source_id not in valid_sources:
                    add_error(f"Unknown source ID '{source_id}' in {path.relative_to(ROOT)}")
    
    return ids_by_locale


def validate_internal_links() -> int:
    checked = 0
    fence = chr(96) * 3
    for path in sorted(ROOT.rglob("*.md")):
        if any(part.startswith(".") for part in path.relative_to(ROOT).parts):
            continue
        text = read_text(path)
        if text is None:
            continue
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



BUILD_FROM_SCRATCH_TRACKS = (
    "ai-model",
    "game-development",
    "operating-systems",
    "database-engine",
    "compiler",
    "network-server",
    "search-engine",
)


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
        text = read_text(path)
        if text is None:
            continue
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

    domains_path = ROOT / "registry" / "domains.yaml"
    languages_path = ROOT / "registry" / "languages.yaml"
    locales_path = ROOT / "registry" / "locales.yaml"
    resources_path = ROOT / "registry" / "resources.yaml"
    graph_nodes_path = ROOT / "knowledge-graph" / "concepts.yaml"
    graph_edges_path = ROOT / "knowledge-graph" / "relationships.yaml"

    domains_data = read_mapping(domains_path)
    languages_data = read_mapping(languages_path)
    locales_data = read_mapping(locales_path)
    resources_data = read_mapping(resources_path)
    graph_nodes_data = read_mapping(graph_nodes_path)
    graph_edges_data = read_mapping(graph_edges_path)

    domains = read_mapping_list(domains_data, "domains", domains_path)
    languages = read_mapping_list(languages_data, "entries", languages_path)
    initial_locales = read_mapping_list(locales_data, "initial_locales", locales_path)
    planned_locales = read_mapping_list(locales_data, "planned_locales", locales_path)
    resources = read_mapping_list(resources_data, "resources", resources_path)
    nodes = read_mapping_list(graph_nodes_data, "nodes", graph_nodes_path)
    edges = read_mapping_list(graph_edges_data, "relationships", graph_edges_path)

    domain_slugs = set(string_values(domains, "slug", domains_path, "Domain"))
    locale_items = [*initial_locales, *planned_locales]
    locale_tags = set(string_values(locale_items, "tag", locales_path, "Locale"))
    source_ids = set(string_values(resources, "id", resources_path, "Resource"))
    language_ids = string_values(languages, "id", languages_path, "Language")
    node_ids = set(string_values(nodes, "id", graph_nodes_path, "Knowledge graph node"))

    if len(domain_slugs) != len(domains):
        add_error("Domain slugs are missing or duplicated.")
    if len(locale_tags) != len(locale_items):
        add_error("Locale tags are missing or duplicated.")
    if len(set(language_ids)) != len(languages):
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
        for endpoint, label in (("from", "source"), ("to", "target")):
            value = edge.get(endpoint)
            if not isinstance(value, str) or value not in node_ids:
                add_error(f"Unknown graph {label} node: {value}")

    for relative in (
        "README.md", "START-HERE.md", "CONTRIBUTING.md",
        "docs/architecture/overview.md", "docs/roadmap.md",
        "content/en/README.md", "content/fa/README.md",
    ):
        if not (ROOT / relative).is_file():
            add_error(f"Missing required file: {relative}")

    ids_by_locale = validate_content(validators, locale_tags, domain_slugs, source_ids)
    build_from_scratch_ids = {
        locale: {
            item for item in ids_by_locale.get(locale, set())
            if item.startswith("build-from-scratch.")
        }
        for locale in ("en", "fa")
    }
    if build_from_scratch_ids["en"] != build_from_scratch_ids["fa"]:
        missing_fa = sorted(build_from_scratch_ids["en"] - build_from_scratch_ids["fa"])
        missing_en = sorted(build_from_scratch_ids["fa"] - build_from_scratch_ids["en"])
        add_error(f"Build from Scratch translation ID mismatch; missing in fa: {missing_fa}; missing in en: {missing_en}.")

    for track in BUILD_FROM_SCRATCH_TRACKS:
        for locale, filename in (("en", "README.md"), ("fa", "README.fa.md")):
            track_page = ROOT / "learning" / "build-from-scratch" / track / filename
            if not track_page.is_file():
                add_error(f"Missing {locale} Build from Scratch track page: {track}/{filename}")

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
