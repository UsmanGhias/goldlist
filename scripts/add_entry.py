#!/usr/bin/env python3
"""Add one entry to data/<category>.yaml, then validate the whole list.

Usage:
    python scripts/add_entry.py --category ai-tools --name Ollama --url https://ollama.com \\
        --desc "Run open LLMs locally with a single command." --type open-source \\
        [--github ollama/ollama] [--gold] [--dry-run]
    python scripts/add_entry.py --from-issue   # parse the suggestion form in $ISSUE_BODY (CI)

--category accepts the file slug (ai-tools), the title or the short name.
--type accepts open-source | free | free-tier (or the form labels: Open source, Free, Free tier).
"""
import argparse
import datetime
import os
import re
import sys
from urllib.parse import parse_qsl, urlencode, urlparse, urlunparse

import yaml

from build import DATA_DIR, GITHUB_REPO_RE, MAX_DESC, TYPES, load_categories, normalize_url, validate

TRACKING_PARAMS = re.compile(r"^(utm_.*|ref|ref_src|source|fbclid|gclid)$", re.IGNORECASE)
FORM_FIELDS = {
    "Name": "name",
    "Link": "url",
    "Category": "category",
    "Type": "type",
    "One-line description": "desc",
    "GitHub repo (optional)": "github",
}


def parse_issue_form(body):
    """Read the '### Label' sections that GitHub issue forms produce."""
    fields = {}
    for label, value in re.findall(r"^### (.+?)\s*\n(.*?)(?=^### |\Z)", body, re.MULTILINE | re.DOTALL):
        key = FORM_FIELDS.get(label.strip())
        value = value.strip()
        if key and value and value != "_No response_":
            fields[key] = value
    return fields


def clean_text(text):
    return re.sub(r"\s+", " ", str(text)).strip()


def clean_url(url):
    parts = urlparse(clean_text(url))
    query = [(k, v) for k, v in parse_qsl(parts.query, keep_blank_values=True) if not TRACKING_PARAMS.match(k)]
    return urlunparse(parts._replace(query=urlencode(query)))


def clean_github(value):
    value = clean_text(value).removeprefix("https://github.com/").strip("/")
    return "/".join(value.split("/")[:2]) if value else ""


def resolve_category(categories, wanted):
    wanted = clean_text(wanted).lower()
    for category in categories:
        if wanted in (category["slug"], category["title"].lower(), category["short"].lower()):
            return category
    options = ", ".join(c["slug"] for c in categories)
    raise SystemExit(f"Unknown category '{wanted}'. Use one of: {options}")


def resolve_type(wanted):
    wanted = clean_text(wanted).lower()
    for key, (label, _) in TYPES.items():
        if wanted in (key, label.lower()):
            return key
    raise SystemExit(f"Unknown type '{wanted}'. Use one of: {', '.join(TYPES)}")


def yaml_scalar(value):
    """Quote a string only when YAML needs it."""
    return yaml.safe_dump({"v": value}, allow_unicode=True, width=10**6)[3:].rstrip("\n")


def render_item(entry):
    lines = [
        f"  - name: {yaml_scalar(entry['name'])}",
        f"    url: {yaml_scalar(entry['url'])}",
        f"    desc: {yaml_scalar(entry['desc'])}",
        f"    type: {entry['type']}",
    ]
    if entry.get("github"):
        lines.append(f"    github: {entry['github']}")
    if entry.get("gold"):
        lines.append("    gold: true")
    lines.append(f"    added: {entry['added']}")
    return "\n".join(lines) + "\n"


def build_entry(raw, categories):
    for key in ("category", "name", "url", "desc", "type"):
        if not raw.get(key):
            raise SystemExit(f"Missing required field: {key}")
    category = resolve_category(categories, raw["category"])
    desc = clean_text(raw["desc"])
    if not desc.endswith("."):
        desc += "."
    entry = {
        "name": clean_text(raw["name"]),
        "url": clean_url(raw["url"]),
        "desc": desc,
        "type": resolve_type(raw["type"]),
        "github": clean_github(raw.get("github") or ""),
        "gold": bool(raw.get("gold")),
        "added": datetime.date.today().isoformat(),
    }
    if not entry["url"].startswith("https://"):
        raise SystemExit(f"URL must start with https:// (got {entry['url']})")
    if len(desc) > MAX_DESC:
        raise SystemExit(f"Description is {len(desc)} characters; the maximum is {MAX_DESC}.")
    if entry["github"] and not GITHUB_REPO_RE.match(entry["github"]):
        raise SystemExit(f"GitHub repo must look like owner/repo (got {entry['github']})")
    for other in categories:
        for item in other["items"]:
            if normalize_url(item["url"]) == normalize_url(entry["url"]):
                raise SystemExit(f"Already listed: {item['name']} in {other['slug']}.yaml")
    return category, entry


def write_output(**values):
    path = os.environ.get("GITHUB_OUTPUT")
    if path:
        with open(path, "a", encoding="utf-8") as fh:
            for key, value in values.items():
                fh.write(f"{key}={value}\n")


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--from-issue", action="store_true", help="read the issue form from $ISSUE_BODY")
    parser.add_argument("--category")
    parser.add_argument("--name")
    parser.add_argument("--url")
    parser.add_argument("--desc")
    parser.add_argument("--type")
    parser.add_argument("--github")
    parser.add_argument("--gold", action="store_true", help="mark as a gold pick (maintainers only)")
    parser.add_argument("--dry-run", action="store_true", help="print the entry without writing it")
    args = parser.parse_args()

    raw = parse_issue_form(os.environ.get("ISSUE_BODY", "")) if args.from_issue else vars(args)
    categories = load_categories()
    category, entry = build_entry(raw, categories)
    block = render_item(entry)
    if args.dry_run:
        print(f"# would append to data/{category['slug']}.yaml\n{block}", end="")
        return 0

    path = DATA_DIR / f"{category['slug']}.yaml"
    original = path.read_text(encoding="utf-8")
    path.write_text(original.rstrip("\n") + "\n" + block, encoding="utf-8")
    errors = validate(load_categories())
    if errors:
        path.write_text(original, encoding="utf-8")
        print("Entry rejected, file restored:", *errors, sep="\n  - ", file=sys.stderr)
        return 1

    print(f"Added '{entry['name']}' to data/{category['slug']}.yaml")
    write_output(name=entry["name"], category=category["title"], slug=category["slug"])
    return 0


if __name__ == "__main__":
    sys.exit(main())
