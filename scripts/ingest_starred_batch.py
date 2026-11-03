#!/usr/bin/env python3
"""Ingest 31 high-impact repositories from @UsmanGhias's stars into GoldList data/*.yaml."""

import datetime
import re
import sys
from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "data"

NEW_ENTRIES = [
    # AI Coding
    {
        "category": "ai-coding",
        "name": "DeepSeek Harness",
        "url": "https://github.com/deepseek-ai/deepseek-harness",
        "desc": "Modular agent execution harness and plugin framework for deep reasoning models.",
        "type": "open-source",
    },
    {
        "category": "ai-coding",
        "name": "Free Claude Code",
        "url": "https://github.com/Alishahryar1/free-claude-code",
        "desc": "Free gateway configuration and prompt routing layer for Claude Code CLI.",
        "type": "open-source",
    },
    {
        "category": "ai-coding",
        "name": "Open Code Review",
        "url": "https://github.com/alibaba/open-code-review",
        "desc": "Hybrid automated code review engine pairing static rules with LLM agents.",
        "type": "open-source",
    },
    {
        "category": "ai-coding",
        "name": "OpenViking",
        "url": "https://github.com/volcengine/OpenViking",
        "desc": "Self-evolving context database and persistent memory engine for AI coding agents.",
        "type": "open-source",
    },
    {
        "category": "ai-coding",
        "name": "AgentMemory",
        "url": "https://github.com/rohitg00/agentmemory",
        "desc": "Persistent memory framework for AI coding agents benchmarked against long contexts.",
        "type": "open-source",
    },
    {
        "category": "ai-coding",
        "name": "FirstMate",
        "url": "https://github.com/kunchenguid/firstmate",
        "desc": "Multi-agent autonomous shipping framework coordinating specialized coding subagents.",
        "type": "open-source",
    },

    # Agent Skills
    {
        "category": "agent-skills",
        "name": "Impeccable",
        "url": "https://github.com/pbakaus/impeccable",
        "desc": "Design vocabulary and editorial polish skill for AI coding agents.",
        "type": "open-source",
    },
    {
        "category": "agent-skills",
        "name": "Diagram Design",
        "url": "https://github.com/cathrynlavery/diagram-design",
        "desc": "Editorial diagram design skill for Claude Code, Codex, and GitHub Copilot.",
        "type": "open-source",
    },
    {
        "category": "agent-skills",
        "name": "Security Audit Skill",
        "url": "https://github.com/cloudflare/security-audit-skill",
        "desc": "Coding-agent skill for multi-phase security audits with verifiable checkpoints.",
        "type": "open-source",
    },
    {
        "category": "agent-skills",
        "name": "Hallmark",
        "url": "https://github.com/Nutlope/hallmark",
        "desc": "Anti-AI-slop design skill for Claude Code, Cursor, and Codex.",
        "type": "open-source",
    },
    {
        "category": "agent-skills",
        "name": "Ponytail",
        "url": "https://github.com/DietrichGebert/ponytail",
        "desc": "Agent skill architecture keeping code generations lean, minimal, and disciplined.",
        "type": "open-source",
    },

    # AI Tools & Models
    {
        "category": "ai-tools",
        "name": "Free LLM API",
        "url": "https://github.com/tashfeenahmed/freellmapi",
        "desc": "Curated index of 34 free LLM providers and 635 free model endpoints under one endpoint.",
        "type": "free",
    },
    {
        "category": "ai-tools",
        "name": "OpenHuman",
        "url": "https://github.com/tinyhumansai/openhuman",
        "desc": "Lightweight, modular agent harness designed for low-latency task execution.",
        "type": "open-source",
    },
    {
        "category": "ai-tools",
        "name": "AirLLM",
        "url": "https://github.com/lyogavin/Anima",
        "desc": "Run 70B+ LLM inference locally on single desktop GPUs via layer-wise memory swapping.",
        "type": "open-source",
    },
    {
        "category": "ai-tools",
        "name": "Khoj",
        "url": "https://github.com/khoj-ai/khoj",
        "desc": "Self-hostable desktop AI assistant searching across local notes and personal documents.",
        "type": "open-source",
    },

    # Developer Tools
    {
        "category": "dev-tools",
        "name": "Scrcpy",
        "url": "https://github.com/Genymobile/scrcpy",
        "desc": "Display and control Android devices over USB or TCP/IP with high performance.",
        "type": "open-source",
    },
    {
        "category": "dev-tools",
        "name": "Open Source iOS Apps",
        "url": "https://github.com/dkhamsing/open-source-ios-apps",
        "desc": "Curated directory of open-source iOS, iPadOS, watchOS, and macOS Swift apps.",
        "type": "open-source",
    },
    {
        "category": "dev-tools",
        "name": "DBX",
        "url": "https://github.com/t8y2/dbx",
        "desc": "25 MB lightweight cross-platform database client supporting 100+ database types.",
        "type": "open-source",
    },
    {
        "category": "dev-tools",
        "name": "Check If Email Exists",
        "url": "https://github.com/reacherhq/check-if-email-exists",
        "desc": "Verify email address deliverability via SMTP handshake without sending an email.",
        "type": "open-source",
    },

    # Productivity
    {
        "category": "productivity",
        "name": "RustDesk",
        "url": "https://github.com/rustdesk/rustdesk",
        "desc": "Open-source virtual and remote desktop infrastructure with full self-hosting.",
        "type": "open-source",
    },
    {
        "category": "productivity",
        "name": "Puter",
        "url": "https://github.com/HeyPuter/puter",
        "desc": "Open-source browser desktop operating system with personal cloud storage.",
        "type": "open-source",
    },
    {
        "category": "productivity",
        "name": "Meetily",
        "url": "https://github.com/Zackriya-Solutions/meetily",
        "desc": "Local-first open-source AI meeting transcription and automated note taker.",
        "type": "open-source",
    },
    {
        "category": "productivity",
        "name": "Documenso",
        "url": "https://github.com/documenso/documenso",
        "desc": "Open-source digital signature alternative for document verification and signing.",
        "type": "open-source",
    },
    {
        "category": "productivity",
        "name": "9Drive",
        "url": "https://github.com/zenhosta/9drive",
        "desc": "Self-hosted storage gateway web application connecting multiple cloud drives.",
        "type": "open-source",
    },

    # Video & Media
    {
        "category": "media",
        "name": "Hyperframes",
        "url": "https://github.com/heygen-com/hyperframes",
        "desc": "Write HTML, CSS, and SVG code to render programmatic video for agent workflows.",
        "type": "open-source",
    },
    {
        "category": "media",
        "name": "AutoClip",
        "url": "https://github.com/zhouxiaoka/autoclip",
        "desc": "Desktop AI tool that slices long podcasts and interviews into captioned short clips.",
        "type": "open-source",
    },
    {
        "category": "media",
        "name": "DonkeyCut",
        "url": "https://github.com/DonkeyCut/Donkey",
        "desc": "Open-source timeline video editor alternative to CapCut.",
        "type": "open-source",
    },
    {
        "category": "media",
        "name": "FreeTube",
        "url": "https://github.com/FreeTubeApp/FreeTube",
        "desc": "Privacy-focused open-source desktop YouTube player with no tracking or telemetry.",
        "type": "open-source",
    },

    # Privacy & Security
    {
        "category": "privacy-security",
        "name": "Maigret",
        "url": "https://github.com/soxoj/maigret",
        "desc": "OSINT username dossier collector querying accounts across 6,000 public platforms.",
        "type": "open-source",
    },
    {
        "category": "privacy-security",
        "name": "CloakBrowser",
        "url": "https://github.com/CloakHQ/CloakBrowser",
        "desc": "Anti-detect Chromium browser engine built to pass advanced bot mitigation checks.",
        "type": "open-source",
    },

    # Startups & Business
    {
        "category": "startups",
        "name": "Ever Gauzy",
        "url": "https://github.com/ever-co/ever-gauzy",
        "desc": "Open-source enterprise business management platform with ERP, CRM, and HRM.",
        "type": "open-source",
    },
    {
        "category": "startups",
        "name": "Deskcomm CRM",
        "url": "https://github.com/melgarafael/DeskcommCRM",
        "desc": "Self-hosted AI sales OS and CRM with native multi-agent chat integrations.",
        "type": "open-source",
    },

    # Jobs
    {
        "category": "jobs",
        "name": "AI Job Search",
        "url": "https://github.com/ai-job-search-dev/ai-job-search",
        "desc": "Local-first AI agent framework that searches job boards and prepares applications.",
        "type": "open-source",
    },
]

def render_yaml_item(item):
    lines = [
        f"  - name: {item['name']}\n",
        f"    url: {item['url']}\n",
        f"    desc: {item['desc']}\n",
        f"    type: {item['type']}\n",
        f"    added: {datetime.date.today().isoformat()}\n",
    ]
    return "".join(lines)

def main():
    # Load existing URLs to avoid duplicates
    existing_urls = set()
    for p in DATA_DIR.glob("*.yaml"):
        cat = yaml.safe_load(p.read_text()) or {}
        for it in cat.get("items", []):
            if "url" in it:
                existing_urls.add(it["url"].rstrip("/").lower())

    by_cat = {}
    added_count = 0
    skipped_count = 0

    for entry in NEW_ENTRIES:
        url_norm = entry["url"].rstrip("/").lower()
        if url_norm in existing_urls:
            print(f"Skipping duplicate: {entry['name']} ({entry['url']})")
            skipped_count += 1
            continue
        existing_urls.add(url_norm)
        by_cat.setdefault(entry["category"], []).append(entry)
        added_count += 1

    for cat_slug, items in by_cat.items():
        path = DATA_DIR / f"{cat_slug}.yaml"
        content = path.read_text(encoding="utf-8").rstrip("\n") + "\n"
        blocks = [render_yaml_item(it) for it in items]
        path.write_text(content + "".join(blocks), encoding="utf-8")
        print(f"Added {len(items)} items to data/{cat_slug}.yaml")

    print(f"\nIngestion summary: {added_count} added, {skipped_count} skipped.")

if __name__ == "__main__":
    main()
