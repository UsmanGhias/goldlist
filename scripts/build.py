#!/usr/bin/env python3
"""Validate data/*.yaml and generate README.md, api/goldlist.json and the suggestion form.

Usage:
    python scripts/build.py             # validate + write all generated files
    python scripts/build.py --validate  # validate only (used on pull requests)
    python scripts/build.py --check     # fail if any generated file is out of date
"""
import argparse
import datetime
import json
import re
import sys
from pathlib import Path
from urllib.parse import urlparse

import yaml

ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "data"
TEMPLATE = ROOT / "templates" / "README.md.tpl"
README = ROOT / "README.md"
JSON_OUT = ROOT / "api" / "goldlist.json"
SUGGEST_FORM = ROOT / ".github" / "ISSUE_TEMPLATE" / "suggest.yml"

REPO = "UsmanGhias/goldlist"
TYPES = {
    "open-source": ("Open source", "2ea44f"),
    "free": ("Free", "0969da"),
    "free-tier": ("Free tier", "bf8700"),
}
CATEGORY_KEYS = ("title", "short", "emoji", "description", "items")
ITEM_KEYS = ("name", "url", "desc", "type")
OPTIONAL_ITEM_KEYS = ("gold", "github", "added")
MAX_DESC = 120
RECENT_LIMIT = 10
GITHUB_REPO_RE = re.compile(r"^[\w.-]+/[\w.-]+$")
GITHUB_URL_RE = re.compile(r"^https://github\.com/([\w.-]+/[\w.-]+)/?$")
# Anchors that exist in the template itself rather than per category.
STATIC_ANCHORS = {"top", "start-here", "gold-picks", "recently-added", "contents", "how-it-works", "contributing"}


def load_categories():
    categories = []
    for path in sorted(DATA_DIR.glob("*.yaml")):
        category = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
        category["slug"] = path.stem
        categories.append(category)
    return sorted(categories, key=lambda c: (c.get("order", 99), c["slug"]))


def github_repo(item):
    """owner/repo for an item: explicit `github`, or derived from a GitHub URL."""
    if item.get("github"):
        return item["github"]
    match = GITHUB_URL_RE.match(str(item.get("url", "")))
    return match.group(1) if match else None


def normalize_url(url):
    return str(url).rstrip("/").lower()


def validate(categories):
    errors = []
    seen_urls = {}
    for category in categories:
        slug = category["slug"]
        for key in CATEGORY_KEYS:
            if not category.get(key):
                errors.append(f"{slug}.yaml: missing '{key}'")
        for index, item in enumerate(category.get("items") or []):
            where = f"{slug}.yaml item {index + 1} ({item.get('name', '?')})"
            for key in ITEM_KEYS:
                if not item.get(key):
                    errors.append(f"{where}: missing '{key}'")
            unknown = set(item) - set(ITEM_KEYS) - set(OPTIONAL_ITEM_KEYS)
            if unknown:
                errors.append(f"{where}: unknown field(s) {', '.join(sorted(unknown))}")
            if item.get("type") and item["type"] not in TYPES:
                errors.append(f"{where}: type must be one of {', '.join(TYPES)}")
            url = str(item.get("url", ""))
            if url and not url.startswith("https://"):
                errors.append(f"{where}: url must start with https://")
            if url and normalize_url(url) in seen_urls:
                errors.append(f"{where}: duplicate of {seen_urls[normalize_url(url)]}")
            seen_urls[normalize_url(url)] = where
            desc = str(item.get("desc", ""))
            if len(desc) > MAX_DESC:
                errors.append(f"{where}: desc is {len(desc)} chars (max {MAX_DESC})")
            if desc and not desc.endswith("."):
                errors.append(f"{where}: desc must end with a period")
            if "gold" in item and not isinstance(item["gold"], bool):
                errors.append(f"{where}: gold must be true or false")
            if item.get("github") and not GITHUB_REPO_RE.match(str(item["github"])):
                errors.append(f"{where}: github must look like owner/repo")
            if "added" in item and not isinstance(item["added"], datetime.date):
                errors.append(f"{where}: added must be a date like 2026-10-27")
    errors += validate_template_anchors(categories)
    return errors


def validate_template_anchors(categories):
    known = STATIC_ANCHORS | {c["slug"] for c in categories}
    template = TEMPLATE.read_text(encoding="utf-8")
    return [
        f"templates/README.md.tpl: link to unknown section #{anchor}"
        for anchor in sorted(set(re.findall(r"\]\(#([\w-]+)\)", template)) - known)
    ]


def cell(text):
    return str(text).replace("|", "\\|").strip()


def icon_url(item):
    repo = GITHUB_URL_RE.match(item["url"])
    if repo:
        return f"https://github.com/{repo.group(1).split('/')[0]}.png?size=64"
    return f"https://www.google.com/s2/favicons?domain={urlparse(item['url']).netloc}&sz=64"


def type_badge(item):
    label, color = TYPES[item["type"]]
    return f"![{label}](https://img.shields.io/badge/{label.replace(' ', '%20')}-{color}?style=flat-square)"


def stars_badge(item):
    repo = github_repo(item)
    if not repo:
        return ""
    return (
        f"[![GitHub stars](https://img.shields.io/github/stars/{repo}"
        f"?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/{repo})"
    )


def render_nav(categories):
    return " · ".join(f"[{c['emoji']} {c['short']}](#{c['slug']})" for c in categories)


def render_gold_picks(categories, columns=3):
    picks = [(c, item) for c in categories for item in c["items"] if item.get("gold")]
    rows = []
    for start in range(0, len(picks), columns):
        cells = []
        for category, item in picks[start:start + columns]:
            cells.append(
                f'<td width="33%" valign="top">\n'
                f'<img src="{icon_url(item)}" width="16" height="16"> '
                f'<b><a href="{item["url"]}">{item["name"]}</a></b><br>\n'
                f'<sub>{item["desc"]}</sub><br>\n'
                f'<sub><a href="#{category["slug"]}">{category["emoji"]} {category["short"]}</a></sub>\n'
                f"</td>"
            )
        rows.append("<tr>\n" + "\n".join(cells) + "\n</tr>")
    return "<table>\n" + "\n".join(rows) + "\n</table>"


def render_recent(categories):
    recent = sorted(
        ((item["added"], c, item) for c in categories for item in c["items"] if "added" in item),
        key=lambda entry: entry[0],
        reverse=True,
    )[:RECENT_LIMIT]
    if not recent:
        return ""
    lines = ['<a id="recently-added"></a>', "", "## 🆕 Recently Added", ""]
    for added, category, item in recent:
        lines.append(
            f"- **[{cell(item['name'])}]({item['url']})**: {cell(item['desc'])} "
            f"<sub>[{category['emoji']} {category['short']}](#{category['slug']}) · {added.isoformat()}</sub>"
        )
    return "\n".join(lines) + "\n"


def render_toc(categories):
    rows = ["| | Category | What's inside | Picks |", "| :-: | :--- | :--- | :-: |"]
    for c in categories:
        rows.append(
            f"| {c['emoji']} | **[{c['title']}](#{c['slug']})** | {cell(c['description'])} | {len(c['items'])} |"
        )
    return "\n".join(rows)


def render_categories(categories):
    blocks = []
    for category in categories:
        gold_count = sum(1 for item in category["items"] if item.get("gold"))
        rows = [
            f'<a id="{category["slug"]}"></a>',
            "",
            f"## {category['emoji']} {category['title']}",
            "",
            f"> {category['description']}<br>",
            f"> <sub>{len(category['items'])} picks · {gold_count} gold</sub>",
            "",
            "| | Resource | Why it's gold | Type | GitHub |",
            "| :-: | :--- | :--- | :-- | :-- |",
        ]
        for item in category["items"]:
            name = f"**[{cell(item['name'])}]({item['url']})**"
            if item.get("gold"):
                name += " 🏆"
            rows.append(
                f'| <img src="{icon_url(item)}" width="20" height="20"> | {name} '
                f"| {cell(item['desc'])} | {type_badge(item)} | {stars_badge(item)} |"
            )
        rows += ["", '<p align="right"><a href="#top">↑ Back to top</a></p>']
        blocks.append("\n".join(rows))
    return "\n\n".join(blocks)


def render_readme(categories):
    items = [item for c in categories for item in c["items"]]
    replacements = {
        "{{TOTAL}}": str(len(items)),
        "{{CATEGORY_COUNT}}": str(len(categories)),
        "{{OPEN_SOURCE_COUNT}}": str(sum(1 for i in items if i["type"] == "open-source")),
        "{{GOLD_COUNT}}": str(sum(1 for i in items if i.get("gold"))),
        "{{NAV}}": render_nav(categories),
        "{{GOLD_PICKS}}": render_gold_picks(categories),
        "{{RECENT}}": render_recent(categories),
        "{{TOC}}": render_toc(categories),
        "{{CATEGORIES}}": render_categories(categories),
    }
    output = TEMPLATE.read_text(encoding="utf-8")
    for placeholder, value in replacements.items():
        output = output.replace(placeholder, value)
    return output


def render_json(categories):
    payload = {
        "name": "GoldList",
        "repository": f"https://github.com/{REPO}",
        "total": sum(len(c["items"]) for c in categories),
        "categories": [
            {
                "slug": c["slug"],
                "title": c["title"],
                "short": c["short"],
                "emoji": c["emoji"],
                "description": c["description"],
                "items": [
                    {
                        "name": item["name"],
                        "url": item["url"],
                        "description": item["desc"],
                        "type": item["type"],
                        "gold": bool(item.get("gold")),
                        "github": github_repo(item),
                        "added": item["added"].isoformat() if "added" in item else None,
                    }
                    for item in c["items"]
                ],
            }
            for c in categories
        ],
    }
    return json.dumps(payload, ensure_ascii=False, indent=2) + "\n"


def render_suggest_form(categories):
    form = {
        "name": "⭐ Suggest a resource",
        "description": "Something free or open source that belongs on GoldList",
        "title": "[Suggest] ",
        "labels": ["suggestion"],
        "body": [
            {"type": "markdown", "attributes": {"value": (
                "Thanks for helping! A maintainer reviews every suggestion. Once it's labeled "
                "`accepted`, a bot adds it to the list automatically."
            )}},
            {"type": "input", "id": "name", "attributes": {"label": "Name", "placeholder": "e.g. LocalSend"},
             "validations": {"required": True}},
            {"type": "input", "id": "url", "attributes": {"label": "Link", "placeholder": "https://..."},
             "validations": {"required": True}},
            {"type": "dropdown", "id": "category", "attributes": {
                "label": "Category", "options": [c["title"] for c in categories]},
             "validations": {"required": True}},
            {"type": "dropdown", "id": "type", "attributes": {
                "label": "Type", "options": [label for label, _ in TYPES.values()]},
             "validations": {"required": True}},
            {"type": "input", "id": "desc", "attributes": {
                "label": "One-line description",
                "description": f"Why it's useful, at most {MAX_DESC} characters, ending with a period.",
                "placeholder": "Share files between nearby devices with no internet or account."},
             "validations": {"required": True}},
            {"type": "input", "id": "github", "attributes": {
                "label": "GitHub repo (optional)",
                "description": "owner/repo, used to show live GitHub stars.",
                "placeholder": "localsend/localsend"}},
            {"type": "textarea", "id": "why", "attributes": {
                "label": "Why is it gold?",
                "description": "What makes it the best (or close to it) at what it does?"},
             "validations": {"required": True}},
            {"type": "checkboxes", "id": "checks", "attributes": {"label": "Checklist", "options": [
                {"label": "It is free, open source, or has a genuinely useful free tier", "required": True},
                {"label": "I searched the list and it is not already on it", "required": True},
            ]}},
        ],
    }
    header = "# Generated by scripts/build.py from data/*.yaml. Do not edit by hand.\n"
    return header + yaml.safe_dump(form, allow_unicode=True, sort_keys=False, width=1000)


def generated_files(categories):
    return {
        README: render_readme(categories),
        JSON_OUT: render_json(categories),
        SUGGEST_FORM: render_suggest_form(categories),
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--validate", action="store_true", help="validate data only")
    mode.add_argument("--check", action="store_true", help="fail if generated files are stale")
    args = parser.parse_args()

    categories = load_categories()
    errors = validate(categories)
    if errors:
        print("Validation failed:", *errors, sep="\n  - ", file=sys.stderr)
        return 1
    total = sum(len(c["items"]) for c in categories)
    print(f"OK: {total} entries in {len(categories)} categories")
    if args.validate:
        return 0

    stale = []
    for path, content in generated_files(categories).items():
        current = path.read_text(encoding="utf-8") if path.exists() else ""
        if current == content:
            continue
        stale.append(path)
        if not args.check:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding="utf-8")
            print(f"Wrote {path.relative_to(ROOT)}")
    if args.check and stale:
        names = ", ".join(str(p.relative_to(ROOT)) for p in stale)
        print(f"Out of date: {names}. Run: python scripts/build.py", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
