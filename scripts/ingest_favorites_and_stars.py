#!/usr/bin/env python3
"""Ingest curated standout tools and favorite GitHub repositories into GoldList."""

import datetime
import subprocess
import sys
from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "data"

NEW_ENTRIES = [
    # ai-coding
    {
        "category": "ai-coding",
        "name": "OpenSandbox",
        "url": "https://github.com/opensandbox-group/OpenSandbox",
        "desc": "Secure and lightweight sandbox runtime for autonomous AI coding agents.",
        "type": "open-source",
        "gold": True,
    },
    {
        "category": "ai-coding",
        "name": "OpenShell",
        "url": "https://github.com/NVIDIA/OpenShell",
        "desc": "Safe, private runtime and sandbox for autonomous AI agent execution by NVIDIA.",
        "type": "open-source",
        "gold": True,
    },
    {
        "category": "ai-coding",
        "name": "Eliza",
        "url": "https://github.com/elizaOS/eliza",
        "desc": "Autonomous multi-agent operating system and framework for interactive agents.",
        "type": "open-source",
        "gold": True,
    },
    {
        "category": "ai-coding",
        "name": "Agno",
        "url": "https://github.com/agno-agi/agno",
        "desc": "Lightweight framework for building multi-modal AI agents with memory and tools.",
        "type": "open-source",
    },
    {
        "category": "ai-coding",
        "name": "CopilotKit",
        "url": "https://github.com/CopilotKit/CopilotKit",
        "desc": "Open-source framework to embed custom AI copilots and in-app agent sidebars.",
        "type": "open-source",
    },
    {
        "category": "ai-coding",
        "name": "9Router",
        "url": "https://github.com/decolua/9router",
        "desc": "Multi-provider routing gateway connecting Claude Code, Codex, and Cursor.",
        "type": "open-source",
    },
    {
        "category": "ai-coding",
        "name": "T3 Code",
        "url": "https://github.com/pingdotgg/t3code",
        "desc": "Full-stack web application scaffolding and agentic code generator by Theo.",
        "type": "open-source",
    },

    # agent-skills
    {
        "category": "agent-skills",
        "name": "Claude Ads",
        "url": "https://github.com/AgriciDaniel/claude-ads",
        "desc": "Paid-media operations and ad management skill for Claude Code across 12 platforms.",
        "type": "open-source",
    },
    {
        "category": "agent-skills",
        "name": "Anthropic Cybersecurity Skills",
        "url": "https://github.com/mukul975/Anthropic-Cybersecurity-Skills",
        "desc": "817 structured cybersecurity and penetration testing skills for AI coding agents.",
        "type": "open-source",
        "gold": True,
    },
    {
        "category": "agent-skills",
        "name": "Book to Skill",
        "url": "https://github.com/virgiliojr94/book-to-skill",
        "desc": "Turn any technical book PDF into an indexed Claude Code skill ready for queries.",
        "type": "open-source",
    },
    {
        "category": "agent-skills",
        "name": "I Have ADHD",
        "url": "https://github.com/ayghri/i-have-adhd",
        "desc": "Agent skill that keeps AI coding outputs concise, structured, and slop-free.",
        "type": "open-source",
    },

    # ai-tools
    {
        "category": "ai-tools",
        "name": "Firecrawl",
        "url": "https://github.com/mendableai/firecrawl",
        "desc": "Turn entire websites into clean LLM-ready markdown or structured data with one call.",
        "type": "open-source",
        "gold": True,
    },
    {
        "category": "ai-tools",
        "name": "Jina Reader",
        "url": "https://github.com/jina-ai/reader",
        "desc": "Convert any webpage into clean markdown for LLMs by prefixing r.jina.ai to the URL.",
        "type": "open-source",
    },
    {
        "category": "ai-tools",
        "name": "Strata",
        "url": "https://github.com/Niko1221/Strata",
        "desc": "Run high-performance open LLMs on consumer GPUs with one-click desktop setup.",
        "type": "open-source",
    },

    # dev-tools
    {
        "category": "dev-tools",
        "name": "uv",
        "url": "https://github.com/astral-sh/uv",
        "desc": "Extremely fast Python package installer and resolver written in Rust.",
        "type": "open-source",
        "gold": True,
    },
    {
        "category": "dev-tools",
        "name": "Ruff",
        "url": "https://github.com/astral-sh/ruff",
        "desc": "Extremely fast Python linter and code formatter written in Rust.",
        "type": "open-source",
        "gold": True,
    },
    {
        "category": "dev-tools",
        "name": "PocketBase",
        "url": "https://github.com/pocketbase/pocketbase",
        "desc": "Open source realtime backend in 1 portable Go binary with embedded SQLite.",
        "type": "open-source",
        "gold": True,
    },
    {
        "category": "dev-tools",
        "name": "fd",
        "url": "https://github.com/sharkdp/fd",
        "desc": "Simple, fast, and user-friendly command-line alternative to find.",
        "type": "open-source",
    },
    {
        "category": "dev-tools",
        "name": "FastAPI",
        "url": "https://github.com/fastapi/fastapi",
        "desc": "High-performance web framework for building APIs with Python and type hints.",
        "type": "open-source",
        "gold": True,
    },
    {
        "category": "dev-tools",
        "name": "tRPC",
        "url": "https://github.com/trpc/trpc",
        "desc": "End-to-end typesafe APIs without code generation or runtime schema bloat.",
        "type": "open-source",
    },
    {
        "category": "dev-tools",
        "name": "Biome",
        "url": "https://github.com/biomejs/biome",
        "desc": "Fast toolchain for JavaScript and TypeScript that formats and lints in milliseconds.",
        "type": "open-source",
    },
    {
        "category": "dev-tools",
        "name": "Dokploy",
        "url": "https://github.com/Dokploy/dokploy",
        "desc": "Lightweight self-hostable PaaS alternative to Heroku, Vercel, and Coolify.",
        "type": "open-source",
    },
    {
        "category": "dev-tools",
        "name": "Gum",
        "url": "https://github.com/charmbracelet/gum",
        "desc": "Tool for glamorous interactive shell scripts and terminal prompts.",
        "type": "open-source",
    },
    {
        "category": "dev-tools",
        "name": "Glow",
        "url": "https://github.com/charmbracelet/glow",
        "desc": "Terminal markdown renderer with styled pager, colors, and syntax highlighting.",
        "type": "open-source",
    },
    {
        "category": "dev-tools",
        "name": "Camofox",
        "url": "https://github.com/jo-inc/camofox-browser",
        "desc": "Stealth headless browser for AI agents that bypasses anti-bot detections.",
        "type": "open-source",
    },
    {
        "category": "dev-tools",
        "name": "Check If Email Exists",
        "url": "https://github.com/reacherhq/check-if-email-exists",
        "desc": "Verify email address deliverability in Rust without sending any email.",
        "type": "open-source",
    },
    {
        "category": "dev-tools",
        "name": "Public APIs",
        "url": "https://github.com/marcelscruz/public-apis",
        "desc": "Curated collaborative directory of public APIs for developers across 52 categories.",
        "type": "open-source",
    },
    {
        "category": "dev-tools",
        "name": "API Mega List",
        "url": "https://github.com/cporter202/API-mega-list",
        "desc": "Comprehensive collection of free public APIs for rapid application prototyping.",
        "type": "open-source",
    },
    {
        "category": "dev-tools",
        "name": "ChangeDetection.io",
        "url": "https://github.com/dgtlmoon/changedetection.io",
        "desc": "Self-hosted website change detection, monitoring, and notification service.",
        "type": "open-source",
    },
    {
        "category": "dev-tools",
        "name": "APKEditor",
        "url": "https://github.com/REAndroid/APKEditor",
        "desc": "Android APK reverse engineering and resource modification tool.",
        "type": "open-source",
    },
    {
        "category": "dev-tools",
        "name": "FreeRDP",
        "url": "https://github.com/FreeRDP/FreeRDP",
        "desc": "Free and open-source Remote Desktop Protocol client and library implementation.",
        "type": "open-source",
    },
    {
        "category": "dev-tools",
        "name": "LordOS",
        "url": "https://github.com/lordbasex/LordOS",
        "desc": "Lightweight Debian Linux distribution with Wayland compositor and QuickJS UI.",
        "type": "open-source",
    },

    # design
    {
        "category": "design",
        "name": "tldraw",
        "url": "https://github.com/tldraw/tldraw",
        "desc": "Infinite canvas SDK and collaborative digital whiteboard for React applications.",
        "type": "open-source",
        "gold": True,
    },
    {
        "category": "design",
        "name": "Excalidraw",
        "url": "https://github.com/excalidraw/excalidraw",
        "desc": "Virtual collaborative whiteboard for sketching hand-drawn diagrams and wireframes.",
        "type": "open-source",
        "gold": True,
    },
    {
        "category": "design",
        "name": "Open Design",
        "url": "https://github.com/nexu-io/open-design",
        "desc": "Collaborative local-first AI design agent workspace and canvas.",
        "type": "open-source",
    },
    {
        "category": "design",
        "name": "Text to CAD",
        "url": "https://github.com/earthtojake/text-to-cad",
        "desc": "Generate physical 3D CAD models and mechanical parts from text descriptions.",
        "type": "open-source",
    },
    {
        "category": "design",
        "name": "Scroll World",
        "url": "https://github.com/oso95/scroll-world",
        "desc": "Agent skill that turns any brand into an immersive scrollable 3D world.",
        "type": "open-source",
    },
    {
        "category": "design",
        "name": "Goldie",
        "url": "https://github.com/software-mansion-labs/goldie",
        "desc": "Agentic automated app store screenshot and preview asset generator.",
        "type": "open-source",
    },
    {
        "category": "design",
        "name": "Anidoodle",
        "url": "https://github.com/alexgreensh/anidoodle",
        "desc": "Art, animation, and interactive motion graphics written purely as code.",
        "type": "open-source",
    },

    # media
    {
        "category": "media",
        "name": "Screenity",
        "url": "https://github.com/alyssaxuu/screenity",
        "desc": "Privacy-friendly browser screen recorder and annotation tool with zero limits.",
        "type": "open-source",
        "gold": True,
    },
    {
        "category": "media",
        "name": "Donkey",
        "url": "https://github.com/DonkeyCut/Donkey",
        "desc": "Open-source desktop video editor alternative to CapCut for creator workflows.",
        "type": "open-source",
    },
    {
        "category": "media",
        "name": "PhotoCraft",
        "url": "https://github.com/storytold/photocraft",
        "desc": "Fast photo editor and image manipulation utility written from scratch in pure Rust.",
        "type": "open-source",
    },
    {
        "category": "media",
        "name": "Openverse",
        "url": "https://github.com/WordPress/openverse",
        "desc": "Search engine for over 700 million openly licensed images and audio tracks.",
        "type": "open-source",
    },
    {
        "category": "media",
        "name": "Stickman Video Director",
        "url": "https://github.com/kaomei/stickman-video-director",
        "desc": "Generate multi-style animated stickman explainer videos directly from scripts.",
        "type": "open-source",
    },
    {
        "category": "media",
        "name": "Open Generative AI",
        "url": "https://github.com/Anil-matcha/Open-Generative-AI",
        "desc": "Open-source suite for generative video and image generation pipelines.",
        "type": "open-source",
    },
    {
        "category": "media",
        "name": "Pixelle Video",
        "url": "https://github.com/ATH-MaaS/Pixelle-Video",
        "desc": "Automated engine generating short-form videos with narration and visuals.",
        "type": "open-source",
    },

    # productivity
    {
        "category": "productivity",
        "name": "zoxide",
        "url": "https://github.com/ajeetdsouza/zoxide",
        "desc": "Smarter cd command that learns navigation habits and jumps across folders fast.",
        "type": "open-source",
        "gold": True,
    },
    {
        "category": "productivity",
        "name": "Coucou",
        "url": "https://github.com/Louis-CFM/coucou",
        "desc": "Mac notch and Lock Screen monitor for autonomous coding agents with one-click review.",
        "type": "open-source",
    },
    {
        "category": "productivity",
        "name": "9Drive",
        "url": "https://github.com/zenhosta/9drive",
        "desc": "Virtual storage dashboard aggregating multiple Google Drive accounts seamlessly.",
        "type": "open-source",
    },
    {
        "category": "productivity",
        "name": "PDF Arranger",
        "url": "https://github.com/pdfarranger/pdfarranger",
        "desc": "Lightweight utility to merge, split, rotate, crop, and reorder PDF pages.",
        "type": "open-source",
    },
    {
        "category": "productivity",
        "name": "APITable",
        "url": "https://github.com/apitable/apitable",
        "desc": "API-oriented open-source low-code collaborative spreadsheet and database.",
        "type": "open-source",
    },
    {
        "category": "productivity",
        "name": "Beamer",
        "url": "https://github.com/kalkman-code/beamer",
        "desc": "Share one keyboard and mouse across Mac and Windows PC over local network.",
        "type": "open-source",
    },
    {
        "category": "productivity",
        "name": "OpenGym",
        "url": "https://github.com/DuarteSantos8/openGym",
        "desc": "Open-source privacy-focused workout, bodyweight, and gym routine tracker.",
        "type": "open-source",
    },
    {
        "category": "productivity",
        "name": "No AI Slop",
        "url": "https://github.com/petergyang/no-ai-slop",
        "desc": "CLI and prompt tool that strips 20+ patterns of AI filler and buzzwords from prose.",
        "type": "open-source",
    },

    # startups
    {
        "category": "startups",
        "name": "FinceptTerminal",
        "url": "https://github.com/Fincept-Corporation/FinceptTerminal",
        "desc": "Modern financial analytics terminal offering market data and investment research.",
        "type": "open-source",
        "gold": True,
    },
    {
        "category": "startups",
        "name": "Evershop",
        "url": "https://github.com/evershopcommerce/evershop",
        "desc": "Modern modular open-source TypeScript headless e-commerce platform.",
        "type": "open-source",
    },
    {
        "category": "startups",
        "name": "StoreCraft",
        "url": "https://github.com/store-craft/storecraft",
        "desc": "Rapid headless e-commerce backend framework built with TypeScript and modular storage.",
        "type": "open-source",
    },
    {
        "category": "startups",
        "name": "Open SEO",
        "url": "https://github.com/every-app/open-seo",
        "desc": "Open-source keyword tracking and backlink intelligence alternative to Semrush.",
        "type": "open-source",
    },
    {
        "category": "startups",
        "name": "Roast Room",
        "url": "https://github.com/nateherkai/roast-room",
        "desc": "Live business decision debate simulator with 7 AI advisors in Claude Code.",
        "type": "open-source",
    },
    {
        "category": "startups",
        "name": "Bagisto Mobile App",
        "url": "https://github.com/bagisto/opensource-ecommerce-mobile-app",
        "desc": "Open-source Flutter mobile e-commerce application for the Bagisto ecosystem.",
        "type": "open-source",
    },

    # privacy-security
    {
        "category": "privacy-security",
        "name": "WhatsMyName",
        "url": "https://github.com/WebBreacher/WhatsMyName",
        "desc": "OSINT username reconnaissance tool searching across 700+ websites and platforms.",
        "type": "open-source",
    },

    # learning
    {
        "category": "learning",
        "name": "nanoGPT",
        "url": "https://github.com/karpathy/nanoGPT",
        "desc": "Simplest, fastest repository for training and finetuning medium GPTs by Andrej Karpathy.",
        "type": "open-source",
        "gold": True,
    },
    {
        "category": "learning",
        "name": "Anthropic Courses",
        "url": "https://github.com/anthropics/courses",
        "desc": "Official educational courses and notebooks for prompt engineering and Claude development.",
        "type": "open-source",
        "gold": True,
    },
    {
        "category": "learning",
        "name": "HelloGitHub",
        "url": "https://github.com/521xueweihan/HelloGitHub",
        "desc": "Curated monthly showcase of interesting, entry-level open-source projects.",
        "type": "open-source",
    },
    {
        "category": "learning",
        "name": "Awesome",
        "url": "https://github.com/sindresorhus/awesome",
        "desc": "The definitive curated index of awesome lists covering programming and technology.",
        "type": "open-source",
    },
    {
        "category": "learning",
        "name": "Koodo Reader",
        "url": "https://github.com/koodo-reader/koodo-reader",
        "desc": "Cross-platform open-source ebook manager and reader supporting EPUB, PDF, and MOBI.",
        "type": "open-source",
    },
    {
        "category": "learning",
        "name": "Exercises Dataset",
        "url": "https://github.com/hasaneyldrm/exercises-dataset",
        "desc": "Comprehensive dataset of 1,324 fitness exercises with animated thumbnails.",
        "type": "open-source",
    },

    # research
    {
        "category": "research",
        "name": "Open Notebook",
        "url": "https://github.com/lfnovo/open-notebook",
        "desc": "Open-source implementation of NotebookLM with local-first documents and audio.",
        "type": "open-source",
    },

    # career
    {
        "category": "career",
        "name": "Developer Portfolios",
        "url": "https://github.com/emmabostian/developer-portfolios",
        "desc": "Curated showcase of stellar software developer portfolio websites for inspiration.",
        "type": "open-source",
    },
    {
        "category": "career",
        "name": "Data Science Interview Q&A",
        "url": "https://github.com/youssefHosni/Data-Science-Interview-Questions-Answers",
        "desc": "Curated preparation questions and answers covering data science and machine learning.",
        "type": "open-source",
    },
]

def main():
    today = datetime.date.today()
    added_count = 0
    skipped_count = 0

    # Build map of existing URLs
    existing_urls = set()
    for yaml_path in DATA_DIR.glob("*.yaml"):
        data = yaml.safe_load(yaml_path.read_text(encoding="utf-8")) or {}
        for it in data.get("items", []):
            existing_urls.add(str(it.get("url", "")).rstrip("/").lower())

    # Group new entries by category
    by_category = {}
    for e in NEW_ENTRIES:
        cat = e["category"]
        by_category.setdefault(cat, []).append(e)

    for cat_slug, items in by_category.items():
        yaml_path = DATA_DIR / f"{cat_slug}.yaml"
        if not yaml_path.exists():
            print(f"Skipping unknown category: {cat_slug}")
            continue

        raw = yaml.safe_load(yaml_path.read_text(encoding="utf-8")) or {}
        existing_items = raw.get("items", [])

        modified = False
        for it in items:
            u = it["url"].rstrip("/").lower()
            if u in existing_urls:
                print(f"  [SKIP] Already present: {it['name']} ({it['url']})")
                skipped_count += 1
                continue

            entry = {
                "name": it["name"],
                "url": it["url"],
                "desc": it["desc"],
                "type": it["type"],
                "added": today,
            }
            if it.get("gold"):
                entry["gold"] = True

            existing_items.append(entry)
            existing_urls.add(u)
            added_count += 1
            modified = True
            print(f"  [ADD] {cat_slug}: {it['name']}")

        if modified:
            raw["items"] = existing_items
            yaml_path.write_text(yaml.safe_dump(raw, sort_keys=False, allow_unicode=True), encoding="utf-8")

    print(f"\nDone: Added {added_count} items, skipped {skipped_count} items.")

if __name__ == "__main__":
    main()
