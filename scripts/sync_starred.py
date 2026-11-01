#!/usr/bin/env python3
"""Automatically sync repositories starred by Usman Ghias into GoldList.

Fetches starred repositories via GitHub API / gh CLI, deduplicates against
data/*.yaml, filters out low-signal/archived repos, automatically categorizes,
cleans descriptions to comply with AGENTS.md, and optionally commits & opens PRs.

Usage:
    python scripts/sync_starred.py --dry-run
    python scripts/sync_starred.py --limit 10 --apply
    python scripts/sync_starred.py --limit 10 --create-pr
"""

import argparse
import datetime
import json
import os
import re
import subprocess
import sys
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

import yaml
from build import DATA_DIR, GITHUB_REPO_RE, MAX_DESC, TYPES, load_categories, normalize_url, validate
from add_entry import clean_github, clean_text, clean_url, render_item, yaml_scalar

# Emoji, bracket notes, and hype removal regexes
EMOJI_RE = re.compile(
    r"[\U00010000-\U0010ffff]|[\u2600-\u27ff]|:[a-z0-9_+-]+:",
    flags=re.UNICODE,
)
BRACKET_NOTE_RE = re.compile(r"\[note:.*?\]|\(note:.*?\)", re.I)
TRAILING_CONJ_RE = re.compile(r"\b(and|or|with|to|for|the|a|an|in|on|at|of)\.?$", re.I)

HYPE_PHRASES = [
    re.compile(r"\bworld's first\b", re.I),
    re.compile(r"\bbest and simplest\b", re.I),
    re.compile(r"\bthe most efficient\b", re.I),
    re.compile(r"\bunrestricted\b", re.I),
    re.compile(r"\bnever stop coding\b", re.I),
    re.compile(r"\brevolutionary\b", re.I),
    re.compile(r"\bcutting-edge\b", re.I),
    re.compile(r"\bseamlessly\b", re.I),
    re.compile(r"\bbattle-tested at alibaba's scale\.?", re.I),
]

# Curated overrides for well-known repos to ensure gold-standard descriptions
REPOS_METADATA = {
    "opencut-app/opencut": {
        "name": "OpenCut",
        "category": "media",
        "desc": "Open-source CapCut alternative for video editing and timeline composition.",
    },
    "thedaviddias/front-end-checklist": {
        "name": "Front-End Checklist",
        "category": "dev-tools",
        "desc": "Comprehensive checklist of HTML, CSS, performance, and accessibility best practices.",
    },
    "digitalplatdev/freedomain": {
        "name": "FreeDomain",
        "category": "dev-tools",
        "desc": "Guide and directory for free domain registration and hands-on DNS configuration.",
    },
    "cheaper-inference/omniroute": {
        "name": "OmniRoute",
        "category": "ai-coding",
        "desc": "MIT-licensed unified AI proxy routing requests across 375 model endpoints.",
    },
    "tashfeenahmed/freellmapi": {
        "name": "Free LLM API",
        "category": "ai-tools",
        "desc": "Curated index of 34 free LLM providers and quota-free API endpoints.",
    },
    "dgtlmoon/changedetection.io": {
        "name": "ChangeDetection.io",
        "category": "dev-tools",
        "desc": "Self-hosted webpage change detection and notification monitoring system.",
    },
    "alibaba/open-code-review": {
        "name": "Open Code Review",
        "category": "ai-coding",
        "desc": "Automated code review engine that inspects pull requests for security and quality.",
    },
    "usestrix/strix": {
        "name": "Strix",
        "category": "privacy-security",
        "desc": "Open-source autonomous AI penetration testing tool that finds application vulnerabilities.",
    },
    "every-app/open-seo": {
        "name": "Open SEO",
        "category": "startups",
        "desc": "Open-source SEO auditing, backlink analysis, and keyword tracking tool.",
    },
    "evershopcommerce/evershop": {
        "name": "EverShop",
        "category": "startups",
        "desc": "Modular open-source e-commerce platform built with Node.js and React.",
    },
    "marcelscruz/public-apis": {
        "name": "Public APIs",
        "category": "dev-tools",
        "desc": "Collective list of free and public APIs for software developers.",
    },
    "khoj-ai/khoj": {
        "name": "Khoj",
        "category": "ai-tools",
        "desc": "Self-hostable desktop AI personal assistant that searches across your notes and docs.",
    },
    "heyputer/puter": {
        "name": "Puter",
        "category": "productivity",
        "desc": "Open-source desktop operating system in the browser with personal cloud storage.",
    },
    "freetubeapp/freetube": {
        "name": "FreeTube",
        "category": "media",
        "desc": "Privacy-focused open-source desktop YouTube player with no tracking or ads.",
    },
    "soxoj/maigret": {
        "name": "Maigret",
        "category": "privacy-security",
        "desc": "OSINT investigation tool that collects dossiers on usernames across 6,000 websites.",
    },
    "petergyang/no-ai-slop": {
        "name": "No AI Slop",
        "category": "agent-skills",
        "desc": "Writing tool and agent skill that detects and removes corporate AI cliches.",
    },
    "calesthio/openmontage": {
        "name": "OpenMontage",
        "category": "media",
        "desc": "Open-source video production pipeline coordinating TTS, image generation, and FFmpeg.",
    },
    "panniantong/agent-reach": {
        "name": "Agent Reach",
        "category": "agent-skills",
        "desc": "Toolkit giving AI coding agents web and social scraping capabilities.",
    },
    "cloakhq/cloakbrowser": {
        "name": "CloakBrowser",
        "category": "privacy-security",
        "desc": "Anti-detect Chromium browser engine built to pass advanced bot mitigation checks.",
    },
    "zackriya-solutions/meetily": {
        "name": "Meetily",
        "category": "productivity",
        "desc": "Local-first open-source AI meeting transcription and automated note taker.",
    },
    "ever-co/ever-gauzy": {
        "name": "Ever Gauzy",
        "category": "startups",
        "desc": "Open-source ERP, CRM, and human resource management platform for business teams.",
    },
    "ruvnet/ruview": {
        "name": "RuView",
        "category": "privacy-security",
        "desc": "Turns commodity WiFi signals into real-time spatial intelligence and presence detection.",
    },
    "koala73/worldmonitor": {
        "name": "WorldMonitor",
        "category": "mcp",
        "desc": "Real-time global intelligence dashboard with AI news aggregation and OSINT monitoring.",
    },
    "asgeirtj/system_prompts_leaks": {
        "name": "System Prompts Leaks",
        "category": "ai-coding",
        "desc": "Documented system prompts from Anthropic Claude, OpenAI ChatGPT, Gemini, and Cursor.",
    },
    "alishahryar1/free-claude-code": {
        "name": "Free Claude Code",
        "category": "ai-coding",
        "desc": "Setup and routing guide to use Claude Code and agent CLIs with free token providers.",
    },
    "dkhamsing/open-source-ios-apps": {
        "name": "Open Source iOS Apps",
        "category": "dev-tools",
        "desc": "Collaborative catalog of open-source iOS applications across various frameworks.",
    },
    "tinyhumansai/openhuman": {
        "name": "OpenHuman",
        "category": "ai-tools",
        "desc": "Lightweight and fast open-source agent harness designed for autonomous task execution.",
    },
    "lyogavin/airllm": {
        "name": "AirLLM",
        "category": "ai-tools",
        "desc": "Runs 70B+ LLM inference locally on single desktop GPUs with layer-wise memory swapping.",
    },
    "mukul975/anthropic-cybersecurity-skills": {
        "name": "Cybersecurity Skills",
        "category": "agent-skills",
        "desc": "Structured cybersecurity agent skills mapped to MITRE ATT&CK, NIST, and OWASP frameworks.",
    },
    "decolua/9router": {
        "name": "9router",
        "category": "ai-coding",
        "desc": "AI coding proxy connecting Claude Code, Cursor, and Cline to free model providers.",
    },
    "ath-maas/pixelle-video": {
        "name": "Pixelle Video",
        "category": "media",
        "desc": "Automated open-source short video generation engine for storyboarding and social media clips.",
    },
}


def get_authenticated_user():
    """Get the current GitHub username or default to UsmanGhias."""
    try:
        out = subprocess.check_output(["gh", "api", "user", "-q", ".login"], stderr=subprocess.DEVNULL)
        user = out.decode().strip()
        if user:
            return user
    except Exception:
        pass
    return "UsmanGhias"


def fetch_starred_repos(user):
    """Fetch all starred repositories for a user using gh CLI."""
    cmd = ["gh", "api", f"users/{user}/starred", "--paginate"]
    out = subprocess.check_output(cmd)
    return json.loads(out.decode())


def clean_repo_desc(raw_desc, name=""):
    """Clean and compress repo description to <= MAX_DESC ending with a period."""
    if not raw_desc:
        return f"Open-source tool for developers."

    # Remove bracket notes
    text = BRACKET_NOTE_RE.sub("", raw_desc)
    
    # Remove emojis and shortcodes
    text = EMOJI_RE.sub("", text)
    
    # If text contains non-ASCII and has English sentences, extract English portion
    if re.search(r"[\u4e00-\u9fff\u3040-\u30ff]", text):
        eng_match = re.search(r"([A-Z][^。！？\n\r]+)", text)
        if eng_match:
            text = eng_match.group(1)

    # Replace em-dashes and en-dashes with comma or space
    text = text.replace("—", ", ").replace("–", "-")
    
    # Strip hype phrases
    for pat in HYPE_PHRASES:
        text = pat.sub("", text)
    
    text = clean_text(text)
    
    # Remove leading dots, colons, or punctuation
    text = re.sub(r"^[:\s,.-]+", "", text)
    
    if not text:
        text = f"Open-source {name} utility."

    # Capitalize first letter
    text = text[0].upper() + text[1:]
    
    # Trim to MAX_DESC - 1 to leave room for terminal period
    if len(text) > MAX_DESC - 1:
        cutoff = text[: MAX_DESC - 2].rfind(" ")
        if cutoff > 20:
            text = text[:cutoff].rstrip(" ,;:-")
        else:
            text = text[: MAX_DESC - 2].rstrip(" ,;:-")
            
    # Remove trailing conjunctions or prepositions (e.g. 'and', 'with')
    text = TRAILING_CONJ_RE.sub("", text).strip(" ,;:-")
            
    if not text.endswith("."):
        text += "."
        
    return text


def categorize_repo(repo):
    """Assign repo to one of GoldList's 16 categories based on topics, name, and description."""
    full_name = repo.get("full_name", "").lower()
    if full_name in REPOS_METADATA:
        return REPOS_METADATA[full_name]["category"]

    topics = set(t.lower() for t in repo.get("topics", []))
    desc = (repo.get("description") or "").lower()
    name = repo.get("name", "").lower()
    
    # 1. Agent Skills
    if "agent-skills" in topics or "agent-skill" in topics or "claude-skills" in topics or "skill-md" in topics or name.endswith("-skill"):
        return "agent-skills"

    # 2. MCP Servers
    if "mcp" in topics or "mcp-server" in topics or name.startswith("mcp-"):
        return "mcp"
        
    # 3. AI Coding (coding agents, proxies, code review, prompts)
    ai_coding_kw = {"claude-code", "copilot", "cursor", "cline", "ai-gateway", "code-review", "ai-coding", "system-prompts", "token-saver"}
    if topics & ai_coding_kw or any(kw in desc for kw in ["code review", "ai gateway", "ai coding", "claude code", "system prompts"]):
        return "ai-coding"
        
    # 4. Media (video, audio, media generation)
    media_kw = {"video", "capcut", "videoeditor", "audio", "video-generation", "remotion", "tts", "text-to-video", "text-to-speech", "ffmpeg", "video-production", "youtube"}
    if topics & media_kw or any(kw in desc for kw in ["video editor", "short video engine", "video production", "youtube app"]):
        return "media"
        
    # 5. Privacy & Security
    sec_kw = {"security", "pentest", "penetration-testing", "osint", "privacy", "cybersecurity", "vulnerability", "ethical-hacking", "bug-bounty", "wifi-security", "tor", "two-factor-auth"}
    if topics & sec_kw or any(kw in desc for kw in ["penetration testing", "dossier on a person", "bot detection", "two-factor", "wifi signals"]):
        return "privacy-security"
        
    # 6. Startups & Business (E-commerce, ERP, CRM, SEO, Marketing)
    startup_kw = {"ecommerce", "crm", "erp", "business", "startup", "saas", "seo", "invoicing", "billing", "marketing", "growth-marketing"}
    if topics & startup_kw or any(kw in desc for kw in ["e-commerce", "crm", "erp", "semrush", "ahrefs", "sales os"]):
        return "startups"
        
    # 7. Productivity & Everyday Apps
    prod_kw = {"productivity", "notes", "note-taking", "meeting", "desktop", "remote-desktop"}
    if topics & prod_kw or any(kw in desc for kw in ["meeting note", "operating system", "remote desktop protocol", "second brain"]):
        return "productivity"
        
    # 8. Design & UI
    design_kw = {"design", "ui", "ux", "icons", "css", "tailwind", "svg", "figma"}
    if topics & design_kw:
        return "design"
        
    # 9. Learning & Interviews
    learn_kw = {"learning", "course", "cheatsheet", "tutorial", "education", "interview-questions", "book", "dataset"}
    if topics & learn_kw or any(kw in desc for kw in ["interview questions", "learning resources", "dataset"]):
        return "learning"
        
    # 10. Jobs & Career
    jobs_kw = {"jobs", "hiring", "interview", "resume", "internships", "portfolio", "portfolios"}
    if topics & jobs_kw or any(kw in desc for kw in ["developer portfolios", "hiring without"]):
        return "career"
        
    # 11. AI Tools & Models
    ai_kw = {"ai", "ai-agent", "agents", "llm", "llms", "machine-learning", "rag", "nlp", "inference"}
    if topics & ai_kw or any(kw in desc for kw in ["llm inference", "free llm", "ai agent", "spatial intelligence"]):
        return "ai-tools"
        
    # 12. Dev Tools (default fallback for code/infrastructure)
    return "dev-tools"


def curate_candidates(starred_repos, categories, min_stars=20):
    """Filter and prepare candidate entries from starred repos."""
    existing_urls = set()
    existing_githubs = set()
    for cat in categories:
        for item in cat.get("items", []):
            if "url" in item:
                existing_urls.add(normalize_url(item["url"]))
            if "github" in item:
                existing_githubs.add(item["github"].lower())
                
    candidates = []
    for r in starred_repos:
        full_name = r["full_name"].strip()
        fn_lower = full_name.lower()
        html_url = r["html_url"].strip()
        stars = r.get("stargazers_count", 0)
        archived = r.get("archived", False)
        homepage = r.get("homepage")
        
        # Deduplication
        if fn_lower in existing_githubs or normalize_url(html_url) in existing_urls:
            continue
        if homepage and normalize_url(homepage) in existing_urls:
            continue
            
        # Quality filters
        if archived:
            continue
        if stars < min_stars:
            continue
        # Exclude meta-awesome lists since GoldList is its own curated list
        if fn_lower in ("sindresorhus/awesome", "521xueweihan/hellogithub"):
            continue
            
        category_slug = categorize_repo(r)
        
        # Meta overrides or auto-cleaning
        if fn_lower in REPOS_METADATA:
            name = REPOS_METADATA[fn_lower]["name"]
            category_slug = REPOS_METADATA[fn_lower]["category"]
            desc = REPOS_METADATA[fn_lower]["desc"]
        else:
            name = r.get("name", "").replace("-", " ").replace("_", " ").title()
            desc = clean_repo_desc(r.get("description"), name)

        # URL: prefer homepage if valid https, else html_url
        url = homepage if homepage and homepage.startswith("https://") and "github.com" not in homepage else html_url
        if not url.startswith("https://"):
            url = html_url
        
        entry = {
            "name": name,
            "url": clean_url(url),
            "desc": desc,
            "type": "open-source",
            "github": full_name,
            "added": datetime.date.today().isoformat(),
            "_stars": stars,
            "_category": category_slug,
        }
        candidates.append(entry)
        
    candidates.sort(key=lambda x: x["_stars"], reverse=True)
    return candidates


def apply_entries(entries, categories):
    """Append entries to their respective data/<slug>.yaml files."""
    by_category = {}
    for entry in entries:
        cat_slug = entry["_category"]
        by_category.setdefault(cat_slug, []).append(entry)
        
    for cat_slug, items in by_category.items():
        path = DATA_DIR / f"{cat_slug}.yaml"
        original = path.read_text(encoding="utf-8")
        blocks = []
        for item in items:
            clean_item = {k: v for k, v in item.items() if not k.startswith("_")}
            if clean_item.get("github") and normalize_url(clean_item["url"]) == f"https://github.com/{clean_item['github'].lower()}":
                clean_item.pop("github", None)
            blocks.append(render_item(clean_item))
        path.write_text(original.rstrip("\n") + "\n" + "".join(blocks), encoding="utf-8")
        print(f"Appended {len(items)} item(s) to data/{cat_slug}.yaml")


def create_pr_workflow(entries, date_str):
    """Run validation, commit data changes on a fresh branch, push, and open PR."""
    branch = f"add/sync-starred-{date_str}"
    print(f"Creating Git branch: {branch}")
    # Ensure starting clean
    subprocess.check_call(["git", "checkout", "-b", branch], cwd=ROOT)
    
    # Run validation
    errors = validate(load_categories())
    if errors:
        print("Validation errors detected:", file=sys.stderr)
        for err in errors:
            print(f"  - {err}", file=sys.stderr)
        sys.exit(1)
        
    # Stage ONLY data/
    subprocess.check_call(["git", "add", "data/"], cwd=ROOT)
    commit_msg = f"feat(data): add {len(entries)} starred open-source tools\n\nAutomated ingestion of top starred repositories:\n" + "\n".join(f"- {e['name']} ({e['github']}) -> {e['_category']}" for e in entries)
    subprocess.check_call(["git", "commit", "-m", commit_msg], cwd=ROOT)
    
    print("Pushing branch to origin...")
    subprocess.check_call(["git", "push", "-u", "origin", branch], cwd=ROOT)
    
    print("Opening Pull Request...")
    pr_body = (
        f"### Summary\n\n"
        f"Automated synchronization of {len(entries)} top-tier repositories starred by @UsmanGhias.\n\n"
        f"### Added Resources\n\n"
        + "\n".join(f"- **[{e['name']}]({e['url']})** (`{e['github']}`): {e['desc']} [Category: `{e['_category']}`, Stars: {e['_stars']:,}]" for e in entries)
        + f"\n\n- Validated via `python scripts/build.py --validate`.\n"
        f"- Strict adherence to AGENTS.md schema and description rules.\n"
    )
    cmd = [
        "gh", "pr", "create",
        "--title", f"feat(data): add {len(entries)} starred open-source tools",
        "--body", pr_body,
        "--base", "main",
        "--head", branch,
    ]
    subprocess.check_call(cmd, cwd=ROOT)
    print("Pull request opened successfully!")


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--user", default="", help="GitHub user to fetch stars from (defaults to authenticated user)")
    parser.add_argument("--min-stars", type=int, default=20, help="Minimum star threshold for inclusion")
    parser.add_argument("--limit", type=int, default=10, help="Max candidates to process")
    parser.add_argument("--dry-run", action="store_true", help="Print preview without changing files")
    parser.add_argument("--apply", action="store_true", help="Apply entries directly to data/*.yaml")
    parser.add_argument("--create-pr", action="store_true", help="Apply, validate, commit, push branch, and open PR")
    parser.add_argument("--category", default="", help="Filter candidates to specific category slug")
    args = parser.parse_args()

    user = args.user or get_authenticated_user()
    print(f"Fetching starred repositories for @{user}...")
    starred = fetch_starred_repos(user)
    print(f"Found {len(starred)} starred repositories on GitHub.")

    categories = load_categories()
    candidates = curate_candidates(starred, categories, min_stars=args.min_stars)

    if args.category:
        candidates = [c for c in candidates if c["_category"] == args.category]

    print(f"Identified {len(candidates)} uncurated high-quality candidate tools.")
    selected = candidates[: args.limit]

    if not selected:
        print("No candidates available for ingestion.")
        return 0

    print("\nSelected Repositories for Ingestion:")
    print("-" * 80)
    for i, item in enumerate(selected, 1):
        print(f"{i:2d}. [{item['_category']:<16}] {item['name']:<20} ({item['_stars']:>7,} ★) -> {item['desc']}")
    print("-" * 80)

    if args.dry_run or (not args.apply and not args.create_pr):
        print("\nDry-run complete. Run with --apply to write to data/*.yaml, or --create-pr to submit a PR.")
        return 0

    today_str = datetime.date.today().isoformat()
    if args.create_pr:
        apply_entries(selected, categories)
        create_pr_workflow(selected, today_str)
    elif args.apply:
        apply_entries(selected, categories)
        print("\nRunning validation check...")
        errors = validate(load_categories())
        if errors:
            print("Validation failed:", *errors, sep="\n  - ", file=sys.stderr)
            return 1
        print("Validation OK! You can now commit or preview with python scripts/build.py")

    return 0


if __name__ == "__main__":
    sys.exit(main())
