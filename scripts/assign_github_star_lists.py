#!/usr/bin/env python3
"""Assign all starred repositories of @UsmanGhias into their proper GitHub Star Lists."""

import json
import subprocess
import time
import sys

LIST_IDS = {
    "agent-skills": "UL_kwDOBe6oKc4Aj2JW",       # Claude & Agent Skills
    "ai-coding": "UL_kwDOBe6oKc4Aj2JV",          # AI Coding Agents & Tools
    "ai-tools": "UL_kwDOBe6oKc4Aj2JT",           # AI Tools & Models
    "career": "UL_kwDOBe6oKc4Aj2JM",             # Career & Interviews
    "design": "UL_kwDOBe6oKc4Aj2JZ",             # Design & UI
    "dev-tools": "UL_kwDOBe6oKc4Aj2JS",          # Developer Tools & Free Tiers
    "jobs": "UL_kwDOBe6oKc4Aj2JL",               # Jobs & Freelancing
    "learning": "UL_kwDOBe6oKc4Aj2JQ",           # Learning & Courses
    "mcp": "UL_kwDOBe6oKc4Aj2JY",                # MCP Servers
    "media": "UL_kwDOBe6oKc4Aj2Ja",              # Video, Audio & Media
    "privacy-security": "UL_kwDOBe6oKc4Aj2Je",   # Privacy & Security
    "productivity": "UL_kwDOBe6oKc4Aj2Jb",       # Productivity & Everyday Apps
    "research": "UL_kwDOBe6oKc4Aj2Jc",           # Research & Writing
    "scholarships": "UL_kwDOBe6oKc4Aj2JN",       # Scholarships & Research Funding
    "startups": "UL_kwDOBe6oKc4Aj2Jd",           # Startups & Business
    "students": "UL_kwDOBe6oKc4Aj2JR",           # Students & Programs
}

def classify_repo(r):
    name = r.get("name", "").lower()
    fn = r.get("full_name", "").lower()
    desc = (r.get("description") or "").lower()
    topics = set(t.lower() for t in r.get("topics", []))
    text = f"{name} {fn} {desc} " + " ".join(topics)

    # 1. Agent Skills
    if any(k in text for k in [
        "agent-skills", "agent-skill", "claude-skills", "skill for claude", 
        "design skill", "security-audit-skill", "diagram-design", "hallmark", 
        "impeccable", "adhd", "last30days-skill"
    ]):
        return "agent-skills"

    # 2. MCP Servers
    if "mcp" in topics or name.startswith("mcp-") or "model context protocol" in text or "mcp server" in text:
        if not any(k in text for k in ["crm", "sales os", "video", "capcut"]):
            return "mcp"

    # 3. Media
    if any(k in text for k in [
        "capcut", "video", "videoeditor", "lossless-cut", "opencut", "openmontage", 
        "autoclip", "donkeycut", "screen recorder", "screenity", "youtube", "freetube", 
        "audio", "tts", "text-to-video", "hyperframes", "stickman-video", "upscayl", 
        "image upscaler"
    ]):
        return "media"

    # 4. Privacy & Security
    if any(k in text for k in [
        "security", "pentest", "penetration testing", "osint", "privacy", "vulnerability", 
        "stealth browser", "cloakbrowser", "camofox", "whatsmyname", "maigret", "proxy", 
        "invisiproxy", "wifi", "ruview", "strix", "anti-detect", "lordos"
    ]):
        return "privacy-security"

    # 5. Startups & Business
    if any(k in text for k in [
        "crm", "erp", "ecommerce", "e-commerce", "storecraft", "evershop", "deskcomm", 
        "gauzy", "open-seo", "seo", "invoicing", "billing", "roast-room", "odoo", "djangodoo"
    ]):
        return "startups"

    # 6. Jobs & Career
    if any(k in text for k in ["ai-job-search", "job search", "jobs", "hiring-without-whiteboards", "summer2027-internships"]):
        return "jobs"
    if any(k in text for k in ["interview questions", "developer-portfolios", "career"]):
        return "career"

    # 7. Productivity
    if any(k in text for k in [
        "docusign", "documenso", "meeting note", "meetily", "remote desktop", "freerdp", 
        "rustdesk", "puter", "9drive", "notebook", "notes", "knowledge management", 
        "logseq", "opengym", "beamer", "inlark", "email"
    ]):
        return "productivity"

    # 8. Learning
    if any(k in text for k in ["learning", "course", "tutorial", "exercises-dataset", "dataset", "ebook", "koodo-reader", "hello-github"]):
        return "learning"

    # 9. AI Coding
    if any(k in text for k in [
        "claude-code", "claude code", "ai coding", "coding agent", "code review", 
        "open-code-review", "agentmemory", "openviking", "deepseek-harness", "ponytail", 
        "firstmate", "harness engineering", "builder", "copilot", "cursor", "system prompts", 
        "system_prompts"
    ]):
        return "ai-coding"

    # 10. AI Tools & Models
    if any(k in text for k in [
        "llm", "ai agent", "agents", "opensandbox", "openshell", "openhuman", "airllm", 
        "khoj", "text-to-cad", "fincept", "freellmapi", "arena"
    ]):
        return "ai-tools"

    # 11. Design & UI
    if any(k in text for k in ["design", "ui", "ux", "css", "tailwind", "svg", "figma", "anidoodle", "web art", "icons"]):
        return "design"

    # Default fallback
    return "dev-tools"

def main():
    with open("/tmp/starred_all.json") as f:
        repos = json.load(f)

    print(f"Loaded {len(repos)} starred repositories.")
    success_count = 0
    fail_count = 0

    for i, r in enumerate(repos, start=1):
        full_name = r["full_name"]
        node_id = r["node_id"]
        cat_slug = classify_repo(r)
        list_id = LIST_IDS.get(cat_slug)
        if not list_id:
            print(f"[{i}/{len(repos)}] Unknown category slug: {cat_slug} for {full_name}")
            continue

        query = f"""
        mutation {{
          updateUserListsForItem(input: {{
            itemId: "{node_id}",
            listIds: ["{list_id}"]
          }}) {{
            clientMutationId
          }}
        }}
        """

        cmd = ["gh", "api", "graphql", "-f", f"query={query}"]
        res = subprocess.run(cmd, capture_output=True, text=True)
        if res.returncode == 0:
            success_count += 1
            print(f"[{i:3d}/{len(repos)}] [OK] {full_name:40} -> {cat_slug}")
        else:
            fail_count += 1
            print(f"[{i:3d}/{len(repos)}] [FAIL] {full_name:40}: {res.stderr.strip()[:100]}")

        # Gentle throttle to avoid rate-limiting
        time.sleep(0.08)

    print("\n---------------------------------------------------------")
    print(f"Complete! Successfully categorized {success_count} repositories on GitHub (Failures: {fail_count}).")

if __name__ == "__main__":
    main()
