#!/usr/bin/env python3
"""Validate data/*.yaml and render README.md from templates/README.md.tpl.

Usage:
    python scripts/build.py             # validate + write README.md
    python scripts/build.py --validate  # validate only (used on pull requests)
    python scripts/build.py --check     # fail if README.md is out of date
"""
import argparse
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "data"
TEMPLATE = ROOT / "templates" / "README.md.tpl"
README = ROOT / "README.md"

TYPES = {
    "open-source": "🔓 Open source",
    "free": "🆓 Free",
    "free-tier": "💳 Free tier",
}
CATEGORY_KEYS = ("title", "emoji", "description", "items")
ITEM_KEYS = ("name", "url", "desc", "type")
MAX_DESC = 120


def load_categories():
    categories = []
    for path in sorted(DATA_DIR.glob("*.yaml")):
        category = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
        category["slug"] = path.stem
        categories.append(category)
    return sorted(categories, key=lambda c: (c.get("order", 99), c["slug"]))


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
            if item.get("type") and item["type"] not in TYPES:
                errors.append(f"{where}: type must be one of {', '.join(TYPES)}")
            url = str(item.get("url", ""))
            if url and not url.startswith("https://"):
                errors.append(f"{where}: url must start with https://")
            key = url.rstrip("/").lower()
            if key in seen_urls:
                errors.append(f"{where}: duplicate of {seen_urls[key]}")
            seen_urls[key] = where
            desc = str(item.get("desc", ""))
            if len(desc) > MAX_DESC:
                errors.append(f"{where}: desc is {len(desc)} chars (max {MAX_DESC})")
            if desc and not desc.endswith("."):
                errors.append(f"{where}: desc must end with a period")
    return errors


def cell(text):
    return str(text).replace("|", "\\|").strip()


def render_gold_picks(categories):
    lines = []
    for category in categories:
        for item in category["items"]:
            if item.get("gold"):
                lines.append(
                    f"- **[{cell(item['name'])}]({item['url']})**: {cell(item['desc'])} "
                    f"<sub>[{category['emoji']} {category['title']}](#{category['slug']})</sub>"
                )
    return "\n".join(lines)


def render_toc(categories):
    return "\n".join(
        f"- [{c['emoji']} {c['title']}](#{c['slug']}) <sub>({len(c['items'])})</sub>"
        for c in categories
    )


def render_categories(categories):
    blocks = []
    for category in categories:
        rows = [
            f'<a id="{category["slug"]}"></a>',
            "",
            f"## {category['emoji']} {category['title']}",
            "",
            f"_{category['description']}_",
            "",
            "| Name | Why it's gold | Type |",
            "| :--- | :--- | :--- |",
        ]
        for item in category["items"]:
            star = " ⭐" if item.get("gold") else ""
            rows.append(
                f"| [{cell(item['name'])}]({item['url']}){star} "
                f"| {cell(item['desc'])} | {TYPES[item['type']]} |"
            )
        rows += ["", "<div align=\"right\"><a href=\"#top\">⬆ back to top</a></div>"]
        blocks.append("\n".join(rows))
    return "\n\n".join(blocks)


def render(categories):
    total = sum(len(c["items"]) for c in categories)
    replacements = {
        "{{TOTAL}}": str(total),
        "{{CATEGORY_COUNT}}": str(len(categories)),
        "{{GOLD_PICKS}}": render_gold_picks(categories),
        "{{TOC}}": render_toc(categories),
        "{{CATEGORIES}}": render_categories(categories),
    }
    output = TEMPLATE.read_text(encoding="utf-8")
    for placeholder, value in replacements.items():
        output = output.replace(placeholder, value)
    return output


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--validate", action="store_true", help="validate data only")
    mode.add_argument("--check", action="store_true", help="fail if README.md is stale")
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

    output = render(categories)
    if args.check:
        current = README.read_text(encoding="utf-8") if README.exists() else ""
        if current != output:
            print("README.md is out of date. Run: python scripts/build.py", file=sys.stderr)
            return 1
        return 0

    README.write_text(output, encoding="utf-8")
    print(f"Wrote {README.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
