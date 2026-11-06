<a id="top"></a>

<div align="center">

<img src="assets/banner.svg" alt="GoldList: only the gold" width="100%">

<br><br>

<code>// the catalogue, today</code>

<h3>Only the gold. Everything else is noise.</h3>

<p>
  <b>481 hand-picked free and open-source resources</b> for finding jobs, AI coding, winning scholarships,<br>
  learning, building products, and staying secure. Sorted across 16 categories and verified every week.
</p>

[![Entries](https://img.shields.io/badge/entries-481-d4af37?style=flat-square&labelColor=24292f)](#contents)
[![Gold picks](https://img.shields.io/badge/gold_picks-70-d4af37?style=flat-square&labelColor=24292f)](#gold-picks)
[![Open source](https://img.shields.io/badge/open_source-349-2ea44f?style=flat-square&labelColor=24292f)](#contents)
[![Web Directory](https://img.shields.io/badge/web_directory-live-d4af37?style=flat-square&logo=googlechrome&logoColor=ffffff&labelColor=24292f)](https://goldlist-seven.vercel.app/)
[![Weekly Check](https://img.shields.io/github/actions/workflow/status/UsmanGhias/goldlist/links.yml?label=links&style=flat-square&labelColor=24292f)](https://github.com/UsmanGhias/goldlist/actions/workflows/links.yml)
[![Stars](https://img.shields.io/github/stars/UsmanGhias/goldlist?style=flat-square&logo=github&labelColor=24292f&color=d4af37)](https://github.com/UsmanGhias/goldlist/stargazers)
[![PRs welcome](https://img.shields.io/badge/PRs-welcome-brightgreen?style=flat-square&labelColor=24292f)](CONTRIBUTING.md)
[![AI reviewed](https://img.shields.io/badge/reviewed_by-CodeRabbit-ff570a?style=flat-square&labelColor=24292f)](#how-it-works)
[![XERJ Corpus Hub](https://hub.xerj.org/contributors/UsmanGhias/badge.svg)](https://hub.xerj.org/contributors/UsmanGhias)
[![License: CC0](https://img.shields.io/badge/license-CC0-lightgrey?style=flat-square&labelColor=24292f)](LICENSE)

<br>

<table>
<tr>
<td align="center" width="25%"><h3>481</h3><sub>verified resources</sub></td>
<td align="center" width="25%"><h3>16</h3><sub>curated topics</sub></td>
<td align="center" width="25%"><h3>349</h3><sub>open-source repos</sub></td>
<td align="center" width="25%"><h3>70</h3><sub>elite gold picks</sub></td>
</tr>
</table>

<br>

[💼 Jobs](#jobs) · [🧭 Career](#career) · [🎓 Scholarships](#scholarships) · [📚 Learning](#learning) · [🧑‍🎓 Students](#students) · [🛠️ Dev Tools](#dev-tools) · [🤖 AI Tools](#ai-tools) · [🧠 AI Coding](#ai-coding) · [🧩 Skills](#agent-skills) · [🔌 MCP](#mcp) · [🎨 Design](#design) · [🎬 Media](#media) · [⚡ Productivity](#productivity) · [🔬 Research](#research) · [🚀 Startups](#startups) · [🔒 Privacy](#privacy-security)

<br><br>

**[🔎 Search &amp; filter all 481 resources on the live website →](https://goldlist-seven.vercel.app/)**

<sub>⭐ <b>Star this repository</b> to keep it one click away. Updated weekly.</sub>

</div>

---

## ⚡ Why GoldList?

Giant awesome-lists drown you in thousands of stale links with zero point of view. GoldList is curated with strict discipline:

- **Curated, not collected:** Every entry earns its place. Categories stay focused so you only see what is worth your time.
- **One clean directory:** Jobs, scholarships, dev tools, Claude skills, MCP servers, and privacy in one unified place.
- **100% active links:** Automated weekly CI checks sweep every single URL. Dead links are caught and resolved immediately.
- **Honest labels:** Explicit open-source licenses, generous free tiers, and live GitHub stars with zero promotional hype.

---

<a id="start-here"></a>

## 🎯 Start Here

| If you are… | Go straight to |
| :--- | :--- |
| 💼 **Hunting for a job** | [Jobs](#jobs) → [Career & Interviews](#career) → [AI Coding](#ai-coding) |
| 🎓 **A student** | [Students](#students) → [Scholarships](#scholarships) → [Learning](#learning) |
| 🌍 **Planning a funded master's or PhD** | [Scholarships](#scholarships) → [Research & Writing](#research) |
| 💻 **Learning to code** | [Learning](#learning) → [Dev Tools](#dev-tools) → [AI Coding](#ai-coding) |
| 🏗️ **Building a product** | [Dev Tools](#dev-tools) → [Startups](#startups) → [Design](#design) |
| 🧩 **Supercharging Claude Code or AI agents** | [Skills](#agent-skills) → [MCP Servers](#mcp) → [AI Coding](#ai-coding) |
| 🤖 **Exploring modern AI** | [AI Tools](#ai-tools) → [AI Coding](#ai-coding) → [Learning](#learning) |
| 🎨 **A creator or designer** | [Design](#design) → [Media](#media) → [Productivity](#productivity) |
| 🔐 **Privacy-conscious** | [Privacy & Security](#privacy-security) → [Productivity](#productivity) |

---

<a id="take-it-with-you"></a>

## 📦 Take It With You

GoldList is machine-readable and agent-ready. Consume it in your terminal, pipe it into AI agents, or show your badge.

<table>
<tr>
<td width="50%" valign="top">

### 💻 Terminal &amp; JSON API
Query the full live dataset from your command line:

```bash
# Stream the raw JSON
curl -sL https://raw.githubusercontent.com/UsmanGhias/goldlist/main/api/goldlist.json | jq .

# List all open-source AI coding tools
curl -sL https://raw.githubusercontent.com/UsmanGhias/goldlist/main/api/goldlist.json \
  | jq '.categories[] | select(.slug=="ai-coding") | .items[] | select(.type=="open-source") | .name'
```

</td>
<td width="50%" valign="top">

### 🤖 AI Agent &amp; Claude Code
GoldList works natively with Claude Code, Antigravity, and Cursor.

Prompt your coding agent:
> *"Fetch the top tools from `https://raw.githubusercontent.com/UsmanGhias/goldlist/main/api/goldlist.json` before recommending libraries."*

All entries include verified URLs, descriptions, and licenses.

</td>
</tr>
</table>

### 🏅 Featured on GoldList Badge

If your tool or open-source project is featured on GoldList, showcase it with pride:

```markdown
[![Featured on GoldList](https://img.shields.io/badge/featured%20on-GoldList-d4af37?style=flat-square&logo=github&labelColor=1f2328)](https://github.com/UsmanGhias/goldlist)
```

**Preview:** [![Featured on GoldList](https://img.shields.io/badge/featured%20on-GoldList-d4af37?style=flat-square&logo=github&labelColor=1f2328)](https://github.com/UsmanGhias/goldlist)

---

<a id="gold-picks"></a>

## 🏆 Gold Picks

The best of the best. If you only open a few links today, make it these.

<table>
<tr>
<td width="33%" valign="top">
<img src="https://www.google.com/s2/favicons?domain=clivora.io&sz=64" width="16" height="16"> <b><a href="https://clivora.io">Clivora Web</a></b><br>
<sub>Free open-source freelance OS for clients and freelancers with portals, contracts, escrow, and invoicing.</sub><br>
<sub><a href="#jobs">💼 Jobs</a></sub>
</td>
<td width="33%" valign="top">
<img src="https://github.com/UsmanGhias.png?size=64" width="16" height="16"> <b><a href="https://github.com/UsmanGhias/clivora">Clivora App</a></b><br>
<sub>Free open-source offline-first mobile app for freelance client portals, contracts, and milestone invoicing.</sub><br>
<sub><a href="#jobs">💼 Jobs</a></sub>
</td>
<td width="33%" valign="top">
<img src="https://www.google.com/s2/favicons?domain=freehire.me&sz=64" width="16" height="16"> <b><a href="https://freehire.me">freehire</a></b><br>
<sub>IT job postings from many boards in one search, each linked back to the original posting.</sub><br>
<sub><a href="#jobs">💼 Jobs</a></sub>
</td>
</tr>
<tr>
<td width="33%" valign="top">
<img src="https://www.google.com/s2/favicons?domain=news.ycombinator.com&sz=64" width="16" height="16"> <b><a href="https://news.ycombinator.com/submitted?id=whoishiring">Hacker News: Who is Hiring</a></b><br>
<sub>Monthly thread where startups post real openings, often remote and often from founders directly.</sub><br>
<sub><a href="#jobs">💼 Jobs</a></sub>
</td>
<td width="33%" valign="top">
<img src="https://github.com/SimplifyJobs.png?size=64" width="16" height="16"> <b><a href="https://github.com/SimplifyJobs/Summer2027-Internships">Simplify Summer 2027 Internships</a></b><br>
<sub>Daily-updated list of tech internships in the US, Canada and remote.</sub><br>
<sub><a href="#jobs">💼 Jobs</a></sub>
</td>
<td width="33%" valign="top">
<img src="https://www.google.com/s2/favicons?domain=www.techinterviewhandbook.org&sz=64" width="16" height="16"> <b><a href="https://www.techinterviewhandbook.org">Tech Interview Handbook</a></b><br>
<sub>Concise interview prep covering algorithm cheatsheets, behavioral questions and resume tips.</sub><br>
<sub><a href="#career">🧭 Career</a></sub>
</td>
</tr>
<tr>
<td width="33%" valign="top">
<img src="https://github.com/donnemartin.png?size=64" width="16" height="16"> <b><a href="https://github.com/donnemartin/system-design-primer">System Design Primer</a></b><br>
<sub>The classic guide to designing large-scale systems, with Anki flashcards.</sub><br>
<sub><a href="#career">🧭 Career</a></sub>
</td>
<td width="33%" valign="top">
<img src="https://www.google.com/s2/favicons?domain=rxresu.me&sz=64" width="16" height="16"> <b><a href="https://rxresu.me">Reactive Resume</a></b><br>
<sub>Open-source resume builder with no ads or tracking, exporting to PDF.</sub><br>
<sub><a href="#career">🧭 Career</a></sub>
</td>
<td width="33%" valign="top">
<img src="https://www.google.com/s2/favicons?domain=www.eacea.ec.europa.eu&sz=64" width="16" height="16"> <b><a href="https://www.eacea.ec.europa.eu/scholarships/erasmus-mundus-catalogue_en">Erasmus Mundus Catalogue</a></b><br>
<sub>Fully funded joint master's programmes taught across several European universities.</sub><br>
<sub><a href="#scholarships">🎓 Scholarships</a></sub>
</td>
</tr>
<tr>
<td width="33%" valign="top">
<img src="https://www.google.com/s2/favicons?domain=www2.daad.de&sz=64" width="16" height="16"> <b><a href="https://www2.daad.de/deutschland/stipendium/datenbank/en/21148-scholarship-database/">DAAD Scholarship Database</a></b><br>
<sub>Search funding for studying or doing research in Germany.</sub><br>
<sub><a href="#scholarships">🎓 Scholarships</a></sub>
</td>
<td width="33%" valign="top">
<img src="https://www.google.com/s2/favicons?domain=www.freecodecamp.org&sz=64" width="16" height="16"> <b><a href="https://www.freecodecamp.org">freeCodeCamp</a></b><br>
<sub>Full-stack curriculum with free certifications and thousands of exercises.</sub><br>
<sub><a href="#learning">📚 Learning</a></sub>
</td>
<td width="33%" valign="top">
<img src="https://www.google.com/s2/favicons?domain=cs50.harvard.edu&sz=64" width="16" height="16"> <b><a href="https://cs50.harvard.edu/x/">CS50x</a></b><br>
<sub>Harvard's famous intro to computer science, free online.</sub><br>
<sub><a href="#learning">📚 Learning</a></sub>
</td>
</tr>
<tr>
<td width="33%" valign="top">
<img src="https://www.google.com/s2/favicons?domain=roadmap.sh&sz=64" width="16" height="16"> <b><a href="https://roadmap.sh">roadmap.sh</a></b><br>
<sub>Step-by-step learning roadmaps for every developer role and technology.</sub><br>
<sub><a href="#learning">📚 Learning</a></sub>
</td>
<td width="33%" valign="top">
<img src="https://www.google.com/s2/favicons?domain=developer.mozilla.org&sz=64" width="16" height="16"> <b><a href="https://developer.mozilla.org">MDN Web Docs</a></b><br>
<sub>The reference for HTML, CSS, JavaScript and web APIs.</sub><br>
<sub><a href="#learning">📚 Learning</a></sub>
</td>
<td width="33%" valign="top">
<img src="https://github.com/rasbt.png?size=64" width="16" height="16"> <b><a href="https://github.com/rasbt/LLMs-from-scratch">LLMs from Scratch</a></b><br>
<sub>Build a ChatGPT-like LLM in PyTorch step by step.</sub><br>
<sub><a href="#learning">📚 Learning</a></sub>
</td>
</tr>
<tr>
<td width="33%" valign="top">
<img src="https://github.com/karpathy.png?size=64" width="16" height="16"> <b><a href="https://github.com/karpathy/nanoGPT">nanoGPT</a></b><br>
<sub>Simplest, fastest repository for training and finetuning medium GPTs by Andrej Karpathy.</sub><br>
<sub><a href="#learning">📚 Learning</a></sub>
</td>
<td width="33%" valign="top">
<img src="https://github.com/anthropics.png?size=64" width="16" height="16"> <b><a href="https://github.com/anthropics/courses">Anthropic Courses</a></b><br>
<sub>Official educational courses and notebooks for prompt engineering and Claude development.</sub><br>
<sub><a href="#learning">📚 Learning</a></sub>
</td>
<td width="33%" valign="top">
<img src="https://www.google.com/s2/favicons?domain=education.github.com&sz=64" width="16" height="16"> <b><a href="https://education.github.com/pack">GitHub Student Developer Pack</a></b><br>
<sub>Free access to dozens of paid developer tools while you study.</sub><br>
<sub><a href="#students">🧑‍🎓 Students</a></sub>
</td>
</tr>
<tr>
<td width="33%" valign="top">
<img src="https://www.google.com/s2/favicons?domain=summerofcode.withgoogle.com&sz=64" width="16" height="16"> <b><a href="https://summerofcode.withgoogle.com">Google Summer of Code</a></b><br>
<sub>Paid, mentored program for contributing to open-source projects.</sub><br>
<sub><a href="#students">🧑‍🎓 Students</a></sub>
</td>
<td width="33%" valign="top">
<img src="https://github.com/ripienaar.png?size=64" width="16" height="16"> <b><a href="https://github.com/ripienaar/free-for-dev">free-for-dev</a></b><br>
<sub>Hundreds of SaaS, PaaS and IaaS services with free tiers for developers.</sub><br>
<sub><a href="#dev-tools">🛠️ Dev Tools</a></sub>
</td>
<td width="33%" valign="top">
<img src="https://github.com/public-apis.png?size=64" width="16" height="16"> <b><a href="https://github.com/public-apis/public-apis">public-apis</a></b><br>
<sub>Collective list of free APIs to build projects on.</sub><br>
<sub><a href="#dev-tools">🛠️ Dev Tools</a></sub>
</td>
</tr>
<tr>
<td width="33%" valign="top">
<img src="https://www.google.com/s2/favicons?domain=supabase.com&sz=64" width="16" height="16"> <b><a href="https://supabase.com">Supabase</a></b><br>
<sub>Open-source Postgres backend with auth, storage and realtime, plus a free tier.</sub><br>
<sub><a href="#dev-tools">🛠️ Dev Tools</a></sub>
</td>
<td width="33%" valign="top">
<img src="https://github.com/jesseduffield.png?size=64" width="16" height="16"> <b><a href="https://github.com/jesseduffield/lazygit">lazygit</a></b><br>
<sub>Terminal UI for git that makes staging, rebasing and stashing painless.</sub><br>
<sub><a href="#dev-tools">🛠️ Dev Tools</a></sub>
</td>
<td width="33%" valign="top">
<img src="https://github.com/astral-sh.png?size=64" width="16" height="16"> <b><a href="https://github.com/astral-sh/uv">uv</a></b><br>
<sub>Extremely fast Python package installer and resolver written in Rust.</sub><br>
<sub><a href="#dev-tools">🛠️ Dev Tools</a></sub>
</td>
</tr>
<tr>
<td width="33%" valign="top">
<img src="https://github.com/astral-sh.png?size=64" width="16" height="16"> <b><a href="https://github.com/astral-sh/ruff">Ruff</a></b><br>
<sub>Extremely fast Python linter and code formatter written in Rust.</sub><br>
<sub><a href="#dev-tools">🛠️ Dev Tools</a></sub>
</td>
<td width="33%" valign="top">
<img src="https://github.com/pocketbase.png?size=64" width="16" height="16"> <b><a href="https://github.com/pocketbase/pocketbase">PocketBase</a></b><br>
<sub>Open source realtime backend in 1 portable Go binary with embedded SQLite.</sub><br>
<sub><a href="#dev-tools">🛠️ Dev Tools</a></sub>
</td>
<td width="33%" valign="top">
<img src="https://github.com/fastapi.png?size=64" width="16" height="16"> <b><a href="https://github.com/fastapi/fastapi">FastAPI</a></b><br>
<sub>High-performance web framework for building APIs with Python and type hints.</sub><br>
<sub><a href="#dev-tools">🛠️ Dev Tools</a></sub>
</td>
</tr>
<tr>
<td width="33%" valign="top">
<img src="https://www.google.com/s2/favicons?domain=caniuse.com&sz=64" width="16" height="16"> <b><a href="https://caniuse.com">Can I use</a></b><br>
<sub>Up-to-date browser feature support tables for modern HTML, CSS, JavaScript, and Web APIs.</sub><br>
<sub><a href="#dev-tools">🛠️ Dev Tools</a></sub>
</td>
<td width="33%" valign="top">
<img src="https://www.google.com/s2/favicons?domain=jsoncrack.com&sz=64" width="16" height="16"> <b><a href="https://jsoncrack.com">JSON Crack</a></b><br>
<sub>Interactive visual graph and hierarchical tree viewer for complex JSON structures.</sub><br>
<sub><a href="#dev-tools">🛠️ Dev Tools</a></sub>
</td>
<td width="33%" valign="top">
<img src="https://www.google.com/s2/favicons?domain=ollama.com&sz=64" width="16" height="16"> <b><a href="https://ollama.com">Ollama</a></b><br>
<sub>Run open LLMs locally with a single command.</sub><br>
<sub><a href="#ai-tools">🤖 AI Tools</a></sub>
</td>
</tr>
<tr>
<td width="33%" valign="top">
<img src="https://www.google.com/s2/favicons?domain=aistudio.google.com&sz=64" width="16" height="16"> <b><a href="https://aistudio.google.com">Google AI Studio</a></b><br>
<sub>Try Gemini models and get a free API key in minutes.</sub><br>
<sub><a href="#ai-tools">🤖 AI Tools</a></sub>
</td>
<td width="33%" valign="top">
<img src="https://www.google.com/s2/favicons?domain=browser-use.com&sz=64" width="16" height="16"> <b><a href="https://browser-use.com">Browser Use</a></b><br>
<sub>Let AI agents control a real web browser to finish tasks.</sub><br>
<sub><a href="#ai-tools">🤖 AI Tools</a></sub>
</td>
<td width="33%" valign="top">
<img src="https://github.com/microsoft.png?size=64" width="16" height="16"> <b><a href="https://github.com/microsoft/markitdown">MarkItDown</a></b><br>
<sub>Convert PDFs, Office files and more to Markdown for LLMs.</sub><br>
<sub><a href="#ai-tools">🤖 AI Tools</a></sub>
</td>
</tr>
<tr>
<td width="33%" valign="top">
<img src="https://github.com/mendableai.png?size=64" width="16" height="16"> <b><a href="https://github.com/mendableai/firecrawl">Firecrawl</a></b><br>
<sub>Turn entire websites into clean LLM-ready markdown or structured data with one call.</sub><br>
<sub><a href="#ai-tools">🤖 AI Tools</a></sub>
</td>
<td width="33%" valign="top">
<img src="https://github.com/google-gemini.png?size=64" width="16" height="16"> <b><a href="https://github.com/google-gemini/gemini-cli">Gemini CLI</a></b><br>
<sub>Google's open-source AI agent for the terminal, with a generous free tier.</sub><br>
<sub><a href="#ai-coding">🧠 AI Coding</a></sub>
</td>
<td width="33%" valign="top">
<img src="https://github.com/github.png?size=64" width="16" height="16"> <b><a href="https://github.com/github/spec-kit">Spec Kit</a></b><br>
<sub>GitHub's toolkit for spec-driven development that turns specs into plans and tasks for agents.</sub><br>
<sub><a href="#ai-coding">🧠 AI Coding</a></sub>
</td>
</tr>
<tr>
<td width="33%" valign="top">
<img src="https://www.google.com/s2/favicons?domain=cline.bot&sz=64" width="16" height="16"> <b><a href="https://cline.bot">Cline</a></b><br>
<sub>Autonomous coding agent inside VS Code that plans, edits and runs commands.</sub><br>
<sub><a href="#ai-coding">🧠 AI Coding</a></sub>
</td>
<td width="33%" valign="top">
<img src="https://github.com/opensandbox-group.png?size=64" width="16" height="16"> <b><a href="https://github.com/opensandbox-group/OpenSandbox">OpenSandbox</a></b><br>
<sub>Secure and lightweight sandbox runtime for autonomous AI coding agents.</sub><br>
<sub><a href="#ai-coding">🧠 AI Coding</a></sub>
</td>
<td width="33%" valign="top">
<img src="https://github.com/NVIDIA.png?size=64" width="16" height="16"> <b><a href="https://github.com/NVIDIA/OpenShell">OpenShell</a></b><br>
<sub>Safe, private runtime and sandbox for autonomous AI agent execution by NVIDIA.</sub><br>
<sub><a href="#ai-coding">🧠 AI Coding</a></sub>
</td>
</tr>
<tr>
<td width="33%" valign="top">
<img src="https://github.com/elizaOS.png?size=64" width="16" height="16"> <b><a href="https://github.com/elizaOS/eliza">Eliza</a></b><br>
<sub>Autonomous multi-agent operating system and framework for interactive agents.</sub><br>
<sub><a href="#ai-coding">🧠 AI Coding</a></sub>
</td>
<td width="33%" valign="top">
<img src="https://github.com/DietrichGebert.png?size=64" width="16" height="16"> <b><a href="https://github.com/DietrichGebert/ponytail">Ponytail</a></b><br>
<sub>Makes your coding agent favor the simplest working solution and write less, leaner code.</sub><br>
<sub><a href="#agent-skills">🧩 Skills</a></sub>
</td>
<td width="33%" valign="top">
<img src="https://github.com/obra.png?size=64" width="16" height="16"> <b><a href="https://github.com/obra/superpowers">Superpowers</a></b><br>
<sub>Skills framework that gives agents a disciplined workflow of brainstorming, planning, TDD and review.</sub><br>
<sub><a href="#agent-skills">🧩 Skills</a></sub>
</td>
</tr>
<tr>
<td width="33%" valign="top">
<img src="https://github.com/nextlevelbuilder.png?size=64" width="16" height="16"> <b><a href="https://github.com/nextlevelbuilder/ui-ux-pro-max-skill">UI UX Pro Max Skill</a></b><br>
<sub>Design-intelligence skill that helps AI coding agents build polished, professional UI.</sub><br>
<sub><a href="#agent-skills">🧩 Skills</a></sub>
</td>
<td width="33%" valign="top">
<img src="https://github.com/mukul975.png?size=64" width="16" height="16"> <b><a href="https://github.com/mukul975/Anthropic-Cybersecurity-Skills">Anthropic Cybersecurity Skills</a></b><br>
<sub>817 structured cybersecurity and penetration testing skills for AI coding agents.</sub><br>
<sub><a href="#agent-skills">🧩 Skills</a></sub>
</td>
<td width="33%" valign="top">
<img src="https://github.com/modelcontextprotocol.png?size=64" width="16" height="16"> <b><a href="https://github.com/modelcontextprotocol/servers">MCP Reference Servers</a></b><br>
<sub>Reference Model Context Protocol servers that connect AI agents to tools and data.</sub><br>
<sub><a href="#mcp">🔌 MCP</a></sub>
</td>
</tr>
<tr>
<td width="33%" valign="top">
<img src="https://github.com/upstash.png?size=64" width="16" height="16"> <b><a href="https://github.com/upstash/context7">Context7</a></b><br>
<sub>Feeds your agent up-to-date, version-specific library docs so it stops guessing APIs.</sub><br>
<sub><a href="#mcp">🔌 MCP</a></sub>
</td>
<td width="33%" valign="top">
<img src="https://github.com/microsoft.png?size=64" width="16" height="16"> <b><a href="https://github.com/microsoft/playwright-mcp">Playwright MCP</a></b><br>
<sub>Lets agents drive a real browser to test, click through and read web pages.</sub><br>
<sub><a href="#mcp">🔌 MCP</a></sub>
</td>
<td width="33%" valign="top">
<img src="https://github.com/ChromeDevTools.png?size=64" width="16" height="16"> <b><a href="https://github.com/ChromeDevTools/chrome-devtools-mcp">Chrome DevTools MCP</a></b><br>
<sub>Let agents debug, profile and test pages in a live Chrome.</sub><br>
<sub><a href="#mcp">🔌 MCP</a></sub>
</td>
</tr>
<tr>
<td width="33%" valign="top">
<img src="https://www.google.com/s2/favicons?domain=penpot.app&sz=64" width="16" height="16"> <b><a href="https://penpot.app">Penpot</a></b><br>
<sub>Open-source design and prototyping tool, an alternative to Figma.</sub><br>
<sub><a href="#design">🎨 Design</a></sub>
</td>
<td width="33%" valign="top">
<img src="https://www.google.com/s2/favicons?domain=ui.shadcn.com&sz=64" width="16" height="16"> <b><a href="https://ui.shadcn.com">shadcn/ui</a></b><br>
<sub>Beautiful, accessible React components you copy into your project.</sub><br>
<sub><a href="#design">🎨 Design</a></sub>
</td>
<td width="33%" valign="top">
<img src="https://github.com/tldraw.png?size=64" width="16" height="16"> <b><a href="https://github.com/tldraw/tldraw">tldraw</a></b><br>
<sub>Infinite canvas SDK and collaborative digital whiteboard for React applications.</sub><br>
<sub><a href="#design">🎨 Design</a></sub>
</td>
</tr>
<tr>
<td width="33%" valign="top">
<img src="https://github.com/excalidraw.png?size=64" width="16" height="16"> <b><a href="https://github.com/excalidraw/excalidraw">Excalidraw</a></b><br>
<sub>Virtual collaborative whiteboard for sketching hand-drawn diagrams and wireframes.</sub><br>
<sub><a href="#design">🎨 Design</a></sub>
</td>
<td width="33%" valign="top">
<img src="https://www.google.com/s2/favicons?domain=www.blackmagicdesign.com&sz=64" width="16" height="16"> <b><a href="https://www.blackmagicdesign.com/products/davinciresolve">DaVinci Resolve</a></b><br>
<sub>Hollywood-grade video editing and color grading, with a very capable free version.</sub><br>
<sub><a href="#media">🎬 Media</a></sub>
</td>
<td width="33%" valign="top">
<img src="https://www.google.com/s2/favicons?domain=obsproject.com&sz=64" width="16" height="16"> <b><a href="https://obsproject.com">OBS Studio</a></b><br>
<sub>Screen recording and live streaming.</sub><br>
<sub><a href="#media">🎬 Media</a></sub>
</td>
</tr>
<tr>
<td width="33%" valign="top">
<img src="https://www.google.com/s2/favicons?domain=ffmpeg.org&sz=64" width="16" height="16"> <b><a href="https://ffmpeg.org">FFmpeg</a></b><br>
<sub>The Swiss Army knife for converting and editing audio and video.</sub><br>
<sub><a href="#media">🎬 Media</a></sub>
</td>
<td width="33%" valign="top">
<img src="https://www.google.com/s2/favicons?domain=immich.app&sz=64" width="16" height="16"> <b><a href="https://immich.app">Immich</a></b><br>
<sub>Self-hosted Google Photos alternative with mobile backup.</sub><br>
<sub><a href="#media">🎬 Media</a></sub>
</td>
<td width="33%" valign="top">
<img src="https://github.com/alyssaxuu.png?size=64" width="16" height="16"> <b><a href="https://github.com/alyssaxuu/screenity">Screenity</a></b><br>
<sub>Privacy-friendly browser screen recorder and annotation tool with zero limits.</sub><br>
<sub><a href="#media">🎬 Media</a></sub>
</td>
</tr>
<tr>
<td width="33%" valign="top">
<img src="https://www.google.com/s2/favicons?domain=obsidian.md&sz=64" width="16" height="16"> <b><a href="https://obsidian.md">Obsidian</a></b><br>
<sub>Local-first markdown notes with backlinks and a huge plugin ecosystem.</sub><br>
<sub><a href="#productivity">⚡ Productivity</a></sub>
</td>
<td width="33%" valign="top">
<img src="https://www.google.com/s2/favicons?domain=localsend.org&sz=64" width="16" height="16"> <b><a href="https://localsend.org">LocalSend</a></b><br>
<sub>Share files between nearby devices with no internet or account.</sub><br>
<sub><a href="#productivity">⚡ Productivity</a></sub>
</td>
<td width="33%" valign="top">
<img src="https://www.google.com/s2/favicons?domain=www.stirlingpdf.com&sz=64" width="16" height="16"> <b><a href="https://www.stirlingpdf.com">Stirling-PDF</a></b><br>
<sub>Self-hosted toolkit to merge, split, sign, OCR and edit PDFs.</sub><br>
<sub><a href="#productivity">⚡ Productivity</a></sub>
</td>
</tr>
<tr>
<td width="33%" valign="top">
<img src="https://github.com/ajeetdsouza.png?size=64" width="16" height="16"> <b><a href="https://github.com/ajeetdsouza/zoxide">zoxide</a></b><br>
<sub>Smarter cd command that learns navigation habits and jumps across folders fast.</sub><br>
<sub><a href="#productivity">⚡ Productivity</a></sub>
</td>
<td width="33%" valign="top">
<img src="https://www.google.com/s2/favicons?domain=www.zotero.org&sz=64" width="16" height="16"> <b><a href="https://www.zotero.org">Zotero</a></b><br>
<sub>Collect, organize and cite research papers, with one-click capture from your browser.</sub><br>
<sub><a href="#research">🔬 Research</a></sub>
</td>
<td width="33%" valign="top">
<img src="https://www.google.com/s2/favicons?domain=www.overleaf.com&sz=64" width="16" height="16"> <b><a href="https://www.overleaf.com">Overleaf</a></b><br>
<sub>Collaborative LaTeX editor in the browser for papers and theses.</sub><br>
<sub><a href="#research">🔬 Research</a></sub>
</td>
</tr>
<tr>
<td width="33%" valign="top">
<img src="https://www.google.com/s2/favicons?domain=colab.research.google.com&sz=64" width="16" height="16"> <b><a href="https://colab.research.google.com">Google Colab</a></b><br>
<sub>Free Jupyter notebooks in the cloud with GPU access.</sub><br>
<sub><a href="#research">🔬 Research</a></sub>
</td>
<td width="33%" valign="top">
<img src="https://www.google.com/s2/favicons?domain=www.startupschool.org&sz=64" width="16" height="16"> <b><a href="https://www.startupschool.org">YC Startup School</a></b><br>
<sub>Y Combinator's free course on how to start a startup, plus co-founder matching.</sub><br>
<sub><a href="#startups">🚀 Startups</a></sub>
</td>
<td width="33%" valign="top">
<img src="https://www.google.com/s2/favicons?domain=posthog.com&sz=64" width="16" height="16"> <b><a href="https://posthog.com">PostHog</a></b><br>
<sub>Open-source product analytics, session replay and feature flags with a big free tier.</sub><br>
<sub><a href="#startups">🚀 Startups</a></sub>
</td>
</tr>
<tr>
<td width="33%" valign="top">
<img src="https://github.com/Fincept-Corporation.png?size=64" width="16" height="16"> <b><a href="https://github.com/Fincept-Corporation/FinceptTerminal">FinceptTerminal</a></b><br>
<sub>Modern financial analytics terminal offering market data and investment research.</sub><br>
<sub><a href="#startups">🚀 Startups</a></sub>
</td>
<td width="33%" valign="top">
<img src="https://www.google.com/s2/favicons?domain=bitwarden.com&sz=64" width="16" height="16"> <b><a href="https://bitwarden.com">Bitwarden</a></b><br>
<sub>Open-source password manager with a free plan on every device.</sub><br>
<sub><a href="#privacy-security">🔒 Privacy</a></sub>
</td>
<td width="33%" valign="top">
<img src="https://github.com/gorhill.png?size=64" width="16" height="16"> <b><a href="https://github.com/gorhill/uBlock">uBlock Origin</a></b><br>
<sub>Efficient, lightweight ad and tracker blocker.</sub><br>
<sub><a href="#privacy-security">🔒 Privacy</a></sub>
</td>
</tr>
<tr>
<td width="33%" valign="top">
<img src="https://www.google.com/s2/favicons?domain=portswigger.net&sz=64" width="16" height="16"> <b><a href="https://portswigger.net/web-security">PortSwigger Web Security Academy</a></b><br>
<sub>Free hands-on labs for every major web vulnerability.</sub><br>
<sub><a href="#privacy-security">🔒 Privacy</a></sub>
</td>
</tr>
</table>

<a id="recently-added"></a>

## 🆕 Recently Added

- **[Can I use](https://caniuse.com)**: Up-to-date browser feature support tables for modern HTML, CSS, JavaScript, and Web APIs. <sub>[🛠️ Dev Tools](#dev-tools) · 2026-11-05</sub>
- **[Crontab.guru](https://crontab.guru)**: Interactive cron schedule expression editor with human-readable plain English definitions. <sub>[🛠️ Dev Tools](#dev-tools) · 2026-11-05</sub>
- **[JSON Crack](https://jsoncrack.com)**: Interactive visual graph and hierarchical tree viewer for complex JSON structures. <sub>[🛠️ Dev Tools](#dev-tools) · 2026-11-05</sub>
- **[Ray.so](https://ray.so)**: Generate beautiful code snippet screenshots with syntax themes, padding, and dark mode. <sub>[🛠️ Dev Tools](#dev-tools) · 2026-11-05</sub>
- **[Bundlephobia](https://bundlephobia.com)**: Find the bundle size and download impact of npm packages before adding them to projects. <sub>[🛠️ Dev Tools](#dev-tools) · 2026-11-05</sub>
- **[Anyps5](https://boykopovar.github.io/AnyPS5/)**: Tool for automatic PS5 executables porting to Linux and Windows. <sub>[🛠️ Dev Tools](#dev-tools) · 2026-11-05</sub>
- **[Mathmodelagent](https://mathmodel.top/home)**: Agent & skills ,自动完成数学建模，生成一份完整的可以直接提交的论文. <sub>[🤖 AI Tools](#ai-tools) · 2026-11-05</sub>
- **[Openmed](https://openmed.life/)**: Local-first healthcare AI: clinical NER and HIPAA PII de-identification on hardware you control. 2,200+ medical. <sub>[🤖 AI Tools](#ai-tools) · 2026-11-05</sub>
- **[Cleanyourtv](https://cleanyour.tv)**: Debloat any Android or Google TV over Wi-Fi and get an Apple TV-style home. <sub>[🧠 AI Coding](#ai-coding) · 2026-11-05</sub>
- **[SVG Repo](https://www.svgrepo.com)**: Search and download 500,000+ free vector SVG icons and illustrations with CC0 license. <sub>[🎨 Design](#design) · 2026-11-05</sub>

<a id="contents"></a>

## 📑 Catalogue Contents

| | Category | What's inside | Picks |
| :-: | :--- | :--- | :-: |
| 💼 | **[Jobs & Freelancing](#jobs)** | Where real openings get posted first, from remote boards to curated GitHub lists. | 22 |
| 🧭 | **[Career & Interviews](#career)** | Resumes, interview prep and salary data to land the offer and negotiate it. | 17 |
| 🎓 | **[Scholarships & Research Funding](#scholarships)** | Funded master's, PhDs and fellowships, so you can study without paying for it. | 22 |
| 📚 | **[Learning & Courses](#learning)** | Free courses and books that are as good as paid ones, often better. | 36 |
| 🧑‍🎓 | **[Students & Programs](#students)** | Free licenses, credits and paid programs available only while you're a student or newcomer. | 16 |
| 🛠️ | **[Developer Tools & Free Tiers](#dev-tools)** | Build, host and ship without a credit card. | 58 |
| 🤖 | **[AI Tools & Models](#ai-tools)** | Run models locally, build AI apps and automate your work. | 37 |
| 🧠 | **[AI Coding Agents & Tools](#ai-coding)** | Terminal coding agents, spec-driven workflows and the tools that make Claude Code better. | 42 |
| 🧩 | **[Claude & Agent Skills](#agent-skills)** | Drop-in skills and plugins that give Claude Code, Codex, Gemini CLI and Antigravity new abilities. | 35 |
| 🔌 | **[MCP Servers](#mcp)** | Model Context Protocol servers that plug your AI agent into docs, browsers, GitHub, design files and databases. | 21 |
| 🎨 | **[Design & UI](#design)** | Icons, fonts, photos and design tools that look premium and cost nothing. | 33 |
| 🎬 | **[Video, Audio & Media](#media)** | Studio-grade editing, recording and stock media at zero cost. | 31 |
| ⚡ | **[Productivity & Everyday Apps](#productivity)** | Notes, office apps and utilities, mostly open-source alternatives to paid apps. | 35 |
| 🔬 | **[Research & Writing](#research)** | Find papers, manage references and write better, for students and researchers. | 19 |
| 🚀 | **[Startups & Business](#startups)** | Launch and run a product, with free credits, analytics, CRM and support tools. | 28 |
| 🔒 | **[Privacy & Security](#privacy-security)** | Protect your accounts, data and devices, and learn security hands-on. | 29 |

**Legend:** ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) source code is public · ![Free](https://img.shields.io/badge/Free-0969da?style=flat-square) free to use · ![Free tier](https://img.shields.io/badge/Free%20tier-bf8700?style=flat-square) generous free tier, paid upgrades · 🏆 gold pick

---

<a id="jobs"></a>

## 💼 Jobs & Freelancing

> Where real openings get posted first, from remote boards to curated GitHub lists.<br>
> <sub>22 picks · 5 gold</sub>

| | Resource | Why it's gold | Type | GitHub |
| :-: | :--- | :--- | :-- | :-- |
| <img src="https://www.google.com/s2/favicons?domain=clivora.io&sz=64" width="20" height="20"> | **[Clivora Web](https://clivora.io)** 🏆 | Free open-source freelance OS for clients and freelancers with portals, contracts, escrow, and invoicing. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/UsmanGhias/clivora-web?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/UsmanGhias/clivora-web) |
| <img src="https://github.com/UsmanGhias.png?size=64" width="20" height="20"> | **[Clivora App](https://github.com/UsmanGhias/clivora)** 🏆 | Free open-source offline-first mobile app for freelance client portals, contracts, and milestone invoicing. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/UsmanGhias/clivora?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/UsmanGhias/clivora) |
| <img src="https://www.google.com/s2/favicons?domain=freehire.me&sz=64" width="20" height="20"> | **[freehire](https://freehire.me)** 🏆 | IT job postings from many boards in one search, each linked back to the original posting. | ![Free](https://img.shields.io/badge/Free-0969da?style=flat-square) |  |
| <img src="https://www.google.com/s2/favicons?domain=news.ycombinator.com&sz=64" width="20" height="20"> | **[Hacker News: Who is Hiring](https://news.ycombinator.com/submitted?id=whoishiring)** 🏆 | Monthly thread where startups post real openings, often remote and often from founders directly. | ![Free](https://img.shields.io/badge/Free-0969da?style=flat-square) |  |
| <img src="https://github.com/SimplifyJobs.png?size=64" width="20" height="20"> | **[Simplify Summer 2027 Internships](https://github.com/SimplifyJobs/Summer2027-Internships)** 🏆 | Daily-updated list of tech internships in the US, Canada and remote. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/SimplifyJobs/Summer2027-Internships?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/SimplifyJobs/Summer2027-Internships) |
| <img src="https://github.com/SimplifyJobs.png?size=64" width="20" height="20"> | **[Simplify New Grad Positions](https://github.com/SimplifyJobs/New-Grad-Positions)** | Daily-updated list of new-grad software, data and engineering roles. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/SimplifyJobs/New-Grad-Positions?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/SimplifyJobs/New-Grad-Positions) |
| <img src="https://www.google.com/s2/favicons?domain=www.workatastartup.com&sz=64" width="20" height="20"> | **[Work at a Startup](https://www.workatastartup.com)** | Y Combinator's job board, where one profile lets you apply to hundreds of YC startups. | ![Free](https://img.shields.io/badge/Free-0969da?style=flat-square) |  |
| <img src="https://github.com/remoteintech.png?size=64" width="20" height="20"> | **[remote-jobs](https://github.com/remoteintech/remote-jobs)** | Community-maintained list of remote-friendly tech companies, with regions and tech stacks. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/remoteintech/remote-jobs?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/remoteintech/remote-jobs) |
| <img src="https://github.com/poteto.png?size=64" width="20" height="20"> | **[Hiring Without Whiteboards](https://github.com/poteto/hiring-without-whiteboards)** | Companies that skip whiteboard puzzles and hire through practical take-homes and pairing. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/poteto/hiring-without-whiteboards?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/poteto/hiring-without-whiteboards) |
| <img src="https://github.com/speedyapply.png?size=64" width="20" height="20"> | **[JobSpy](https://github.com/speedyapply/JobSpy)** | Python library that scrapes LinkedIn, Indeed, Glassdoor and more into one clean table. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/speedyapply/JobSpy?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/speedyapply/JobSpy) |
| <img src="https://www.google.com/s2/favicons?domain=weworkremotely.com&sz=64" width="20" height="20"> | **[We Work Remotely](https://weworkremotely.com)** | One of the largest remote-only job boards, covering dev, design, support and more. | ![Free](https://img.shields.io/badge/Free-0969da?style=flat-square) |  |
| <img src="https://www.google.com/s2/favicons?domain=remoteok.com&sz=64" width="20" height="20"> | **[Remote OK](https://remoteok.com)** | Remote job board with salary ranges and tag-based filters. | ![Free](https://img.shields.io/badge/Free-0969da?style=flat-square) |  |
| <img src="https://www.google.com/s2/favicons?domain=remotive.com&sz=64" width="20" height="20"> | **[Remotive](https://remotive.com)** | Curated remote tech jobs plus a job-alert newsletter. | ![Free](https://img.shields.io/badge/Free-0969da?style=flat-square) |  |
| <img src="https://www.google.com/s2/favicons?domain=himalayas.app&sz=64" width="20" height="20"> | **[Himalayas](https://himalayas.app)** | Remote job board with detailed company profiles and salary info, free for job seekers. | ![Free](https://img.shields.io/badge/Free-0969da?style=flat-square) |  |
| <img src="https://www.google.com/s2/favicons?domain=wellfound.com&sz=64" width="20" height="20"> | **[Wellfound](https://wellfound.com)** | Startup jobs (formerly AngelList Talent) with salary and equity shown upfront. | ![Free](https://img.shields.io/badge/Free-0969da?style=flat-square) |  |
| <img src="https://www.google.com/s2/favicons?domain=contra.com&sz=64" width="20" height="20"> | **[Contra](https://contra.com)** | Commission-free platform where freelancers get hired and paid. | ![Free](https://img.shields.io/badge/Free-0969da?style=flat-square) |  |
| <img src="https://www.google.com/s2/favicons?domain=www.workingnomads.com&sz=64" width="20" height="20"> | **[Working Nomads](https://www.workingnomads.com)** | Curated remote jobs by category, delivered as an email digest. | ![Free](https://img.shields.io/badge/Free-0969da?style=flat-square) |  |
| <img src="https://github.com/career-ops-hq.png?size=64" width="20" height="20"> | **[career-ops](https://github.com/career-ops-hq/career-ops)** | AI job-search agent that scores jobs against your CV and tailors your resume and cover letter. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/career-ops-hq/career-ops?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/career-ops-hq/career-ops) |
| <img src="https://github.com/lukasz-madon.png?size=64" width="20" height="20"> | **[Awesome Remote Job](https://github.com/lukasz-madon/awesome-remote-job)** | Curated list of remote job boards, companies and resources. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/lukasz-madon/awesome-remote-job?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/lukasz-madon/awesome-remote-job) |
| <img src="https://www.google.com/s2/favicons?domain=www.welcometothejungle.com&sz=64" width="20" height="20"> | **[Welcome to the Jungle](https://www.welcometothejungle.com)** | Tech jobs with real salary ranges and company insights (formerly Otta). | ![Free](https://img.shields.io/badge/Free-0969da?style=flat-square) |  |
| <img src="https://www.google.com/s2/favicons?domain=www.remoterocketship.com&sz=64" width="20" height="20"> | **[Remote Rocketship](https://www.remoterocketship.com)** | Remote jobs pulled straight from company career pages. | ![Free](https://img.shields.io/badge/Free-0969da?style=flat-square) |  |
| <img src="https://github.com/ai-job-search-dev.png?size=64" width="20" height="20"> | **[AI Job Search](https://github.com/ai-job-search-dev/ai-job-search)** | Local-first AI agent framework that searches job boards and prepares applications. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/ai-job-search-dev/ai-job-search?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/ai-job-search-dev/ai-job-search) |

<p align="right"><a href="#top">↑ Back to top</a></p>

<a id="career"></a>

## 🧭 Career & Interviews

> Resumes, interview prep and salary data to land the offer and negotiate it.<br>
> <sub>17 picks · 3 gold</sub>

| | Resource | Why it's gold | Type | GitHub |
| :-: | :--- | :--- | :-- | :-- |
| <img src="https://www.google.com/s2/favicons?domain=www.techinterviewhandbook.org&sz=64" width="20" height="20"> | **[Tech Interview Handbook](https://www.techinterviewhandbook.org)** 🏆 | Concise interview prep covering algorithm cheatsheets, behavioral questions and resume tips. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/yangshun/tech-interview-handbook?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/yangshun/tech-interview-handbook) |
| <img src="https://github.com/donnemartin.png?size=64" width="20" height="20"> | **[System Design Primer](https://github.com/donnemartin/system-design-primer)** 🏆 | The classic guide to designing large-scale systems, with Anki flashcards. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/donnemartin/system-design-primer?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/donnemartin/system-design-primer) |
| <img src="https://www.google.com/s2/favicons?domain=rxresu.me&sz=64" width="20" height="20"> | **[Reactive Resume](https://rxresu.me)** 🏆 | Open-source resume builder with no ads or tracking, exporting to PDF. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/reactive-resume/reactive-resume?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/reactive-resume/reactive-resume) |
| <img src="https://www.google.com/s2/favicons?domain=www.techinterviewhandbook.org&sz=64" width="20" height="20"> | **[Grind 75](https://www.techinterviewhandbook.org/grind75)** | Customizable week-by-week LeetCode study plan from the author of Blind 75. | ![Free](https://img.shields.io/badge/Free-0969da?style=flat-square) |  |
| <img src="https://github.com/jwasham.png?size=64" width="20" height="20"> | **[Coding Interview University](https://github.com/jwasham/coding-interview-university)** | Multi-month self-study plan for becoming a software engineer. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/jwasham/coding-interview-university?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/jwasham/coding-interview-university) |
| <img src="https://www.google.com/s2/favicons?domain=neetcode.io&sz=64" width="20" height="20"> | **[NeetCode](https://neetcode.io)** | Structured LeetCode roadmap with free video explanations for every problem. | ![Free tier](https://img.shields.io/badge/Free%20tier-bf8700?style=flat-square) |  |
| <img src="https://www.google.com/s2/favicons?domain=leetcode.com&sz=64" width="20" height="20"> | **[LeetCode](https://leetcode.com)** | The standard platform for practicing coding interview problems. | ![Free tier](https://img.shields.io/badge/Free%20tier-bf8700?style=flat-square) |  |
| <img src="https://github.com/srbhr.png?size=64" width="20" height="20"> | **[Resume Matcher](https://github.com/srbhr/Resume-Matcher)** | Compares your resume with a job description and suggests keywords to improve your match. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/srbhr/Resume-Matcher?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/srbhr/Resume-Matcher) |
| <img src="https://www.google.com/s2/favicons?domain=jsonresume.org&sz=64" width="20" height="20"> | **[JSON Resume](https://jsonresume.org)** | Open standard for writing your resume as JSON, with themes to render it. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) |  |
| <img src="https://www.google.com/s2/favicons?domain=www.overleaf.com&sz=64" width="20" height="20"> | **[Overleaf CV Templates](https://www.overleaf.com/latex/templates/tagged/cv)** | Professional LaTeX CV templates you can edit right in the browser. | ![Free tier](https://img.shields.io/badge/Free%20tier-bf8700?style=flat-square) |  |
| <img src="https://www.google.com/s2/favicons?domain=www.bigocheatsheet.com&sz=64" width="20" height="20"> | **[Big-O Cheat Sheet](https://www.bigocheatsheet.com)** | Time and space complexity of common algorithms and data structures on one page. | ![Free](https://img.shields.io/badge/Free-0969da?style=flat-square) |  |
| <img src="https://www.google.com/s2/favicons?domain=www.levels.fyi&sz=64" width="20" height="20"> | **[Levels.fyi](https://www.levels.fyi)** | Crowdsourced compensation data by company, level and location. | ![Free](https://img.shields.io/badge/Free-0969da?style=flat-square) |  |
| <img src="https://github.com/ashishps1.png?size=64" width="20" height="20"> | **[Awesome System Design Resources](https://github.com/ashishps1/awesome-system-design-resources)** | Free resources to learn system design concepts and prep interviews. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/ashishps1/awesome-system-design-resources?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/ashishps1/awesome-system-design-resources) |
| <img src="https://github.com/TheAlgorithms.png?size=64" width="20" height="20"> | **[The Algorithms (Python)](https://github.com/TheAlgorithms/Python)** | Every classic algorithm implemented in Python. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/TheAlgorithms/Python?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/TheAlgorithms/Python) |
| <img src="https://github.com/trekhleb.png?size=64" width="20" height="20"> | **[JavaScript Algorithms](https://github.com/trekhleb/javascript-algorithms)** | Algorithms and data structures in JavaScript with explanations. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/trekhleb/javascript-algorithms?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/trekhleb/javascript-algorithms) |
| <img src="https://github.com/emmabostian.png?size=64" width="20" height="20"> | **[Developer Portfolios](https://github.com/emmabostian/developer-portfolios)** | Curated showcase of stellar software developer portfolio websites for inspiration. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/emmabostian/developer-portfolios?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/emmabostian/developer-portfolios) |
| <img src="https://github.com/youssefHosni.png?size=64" width="20" height="20"> | **[Data Science Interview Q&A](https://github.com/youssefHosni/Data-Science-Interview-Questions-Answers)** | Curated preparation questions and answers covering data science and machine learning. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/youssefHosni/Data-Science-Interview-Questions-Answers?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/youssefHosni/Data-Science-Interview-Questions-Answers) |

<p align="right"><a href="#top">↑ Back to top</a></p>

<a id="scholarships"></a>

## 🎓 Scholarships & Research Funding

> Funded master's, PhDs and fellowships, so you can study without paying for it.<br>
> <sub>22 picks · 2 gold</sub>

| | Resource | Why it's gold | Type | GitHub |
| :-: | :--- | :--- | :-- | :-- |
| <img src="https://www.google.com/s2/favicons?domain=www.eacea.ec.europa.eu&sz=64" width="20" height="20"> | **[Erasmus Mundus Catalogue](https://www.eacea.ec.europa.eu/scholarships/erasmus-mundus-catalogue_en)** 🏆 | Fully funded joint master's programmes taught across several European universities. | ![Free](https://img.shields.io/badge/Free-0969da?style=flat-square) |  |
| <img src="https://www.google.com/s2/favicons?domain=www2.daad.de&sz=64" width="20" height="20"> | **[DAAD Scholarship Database](https://www2.daad.de/deutschland/stipendium/datenbank/en/21148-scholarship-database/)** 🏆 | Search funding for studying or doing research in Germany. | ![Free](https://img.shields.io/badge/Free-0969da?style=flat-square) |  |
| <img src="https://www.google.com/s2/favicons?domain=euraxess.ec.europa.eu&sz=64" width="20" height="20"> | **[EURAXESS](https://euraxess.ec.europa.eu)** | EU portal for research jobs, PhD positions and fellowships. | ![Free](https://img.shields.io/badge/Free-0969da?style=flat-square) |  |
| <img src="https://www.google.com/s2/favicons?domain=www.findaphd.com&sz=64" width="20" height="20"> | **[FindAPhD](https://www.findaphd.com)** | Search funded PhD projects worldwide by subject and country. | ![Free](https://img.shields.io/badge/Free-0969da?style=flat-square) |  |
| <img src="https://www.google.com/s2/favicons?domain=academicpositions.com&sz=64" width="20" height="20"> | **[Academic Positions](https://academicpositions.com)** | PhD, postdoc and faculty openings, mostly in Europe. | ![Free](https://img.shields.io/badge/Free-0969da?style=flat-square) |  |
| <img src="https://www.google.com/s2/favicons?domain=marie-sklodowska-curie-actions.ec.europa.eu&sz=64" width="20" height="20"> | **[Marie Skłodowska-Curie Actions](https://marie-sklodowska-curie-actions.ec.europa.eu)** | EU funding for doctoral networks and postdoctoral fellowships. | ![Free](https://img.shields.io/badge/Free-0969da?style=flat-square) |  |
| <img src="https://www.google.com/s2/favicons?domain=ellis.eu&sz=64" width="20" height="20"> | **[ELLIS PhD & Postdoc Program](https://ellis.eu/phd-postdoc)** | Europe-wide machine learning PhD program with co-supervision across countries. | ![Free](https://img.shields.io/badge/Free-0969da?style=flat-square) |  |
| <img src="https://www.google.com/s2/favicons?domain=research.google&sz=64" width="20" height="20"> | **[Google PhD Fellowship](https://research.google/programs-and-events/phd-fellowship/)** | Funding and Google mentorship for PhD students in computer science. | ![Free](https://img.shields.io/badge/Free-0969da?style=flat-square) |  |
| <img src="https://www.google.com/s2/favicons?domain=foreign.fulbrightonline.org&sz=64" width="20" height="20"> | **[Fulbright Foreign Student Program](https://foreign.fulbrightonline.org)** | Funded graduate study in the United States for international students. | ![Free](https://img.shields.io/badge/Free-0969da?style=flat-square) |  |
| <img src="https://www.google.com/s2/favicons?domain=www.chevening.org&sz=64" width="20" height="20"> | **[Chevening](https://www.chevening.org)** | UK government-funded one-year master's scholarships. | ![Free](https://img.shields.io/badge/Free-0969da?style=flat-square) |  |
| <img src="https://www.google.com/s2/favicons?domain=cscuk.fcdo.gov.uk&sz=64" width="20" height="20"> | **[Commonwealth Scholarships](https://cscuk.fcdo.gov.uk)** | UK-funded master's and PhD scholarships for Commonwealth citizens. | ![Free](https://img.shields.io/badge/Free-0969da?style=flat-square) |  |
| <img src="https://www.google.com/s2/favicons?domain=si.se&sz=64" width="20" height="20"> | **[Swedish Institute Scholarships](https://si.se/en/apply/scholarships/)** | Scholarships covering tuition and living costs for master's study in Sweden. | ![Free](https://img.shields.io/badge/Free-0969da?style=flat-square) |  |
| <img src="https://www.google.com/s2/favicons?domain=stipendiumhungaricum.hu&sz=64" width="20" height="20"> | **[Stipendium Hungaricum](https://stipendiumhungaricum.hu)** | Hungarian government scholarships for bachelor's, master's and PhD study. | ![Free](https://img.shields.io/badge/Free-0969da?style=flat-square) |  |
| <img src="https://www.google.com/s2/favicons?domain=www.turkiyeburslari.gov.tr&sz=64" width="20" height="20"> | **[Türkiye Scholarships](https://www.turkiyeburslari.gov.tr)** | Turkish government scholarships covering tuition, housing and a monthly stipend. | ![Free](https://img.shields.io/badge/Free-0969da?style=flat-square) |  |
| <img src="https://www.google.com/s2/favicons?domain=www.scholars4dev.com&sz=64" width="20" height="20"> | **[Scholars4Dev](https://www.scholars4dev.com)** | International scholarships for students from developing countries. | ![Free](https://img.shields.io/badge/Free-0969da?style=flat-square) |  |
| <img src="https://www.google.com/s2/favicons?domain=www.gatescambridge.org&sz=64" width="20" height="20"> | **[Gates Cambridge Scholarship](https://www.gatescambridge.org)** | Full-cost postgraduate scholarships at the University of Cambridge. | ![Free](https://img.shields.io/badge/Free-0969da?style=flat-square) |  |
| <img src="https://www.google.com/s2/favicons?domain=knight-hennessy.stanford.edu&sz=64" width="20" height="20"> | **[Knight-Hennessy Scholars](https://knight-hennessy.stanford.edu)** | Fully funded graduate study at Stanford for any program. | ![Free](https://img.shields.io/badge/Free-0969da?style=flat-square) |  |
| <img src="https://www.google.com/s2/favicons?domain=www.rhodeshouse.ox.ac.uk&sz=64" width="20" height="20"> | **[Rhodes Scholarship](https://www.rhodeshouse.ox.ac.uk)** | Fully funded postgraduate study at the University of Oxford. | ![Free](https://img.shields.io/badge/Free-0969da?style=flat-square) |  |
| <img src="https://www.google.com/s2/favicons?domain=www.studyinjapan.go.jp&sz=64" width="20" height="20"> | **[MEXT Scholarship](https://www.studyinjapan.go.jp/en/smap-stopj-applications-research.html)** | Japanese government scholarship for research and degree study. | ![Free](https://img.shields.io/badge/Free-0969da?style=flat-square) |  |
| <img src="https://www.google.com/s2/favicons?domain=www.sbfi.admin.ch&sz=64" width="20" height="20"> | **[Swiss Government Excellence Scholarships](https://www.sbfi.admin.ch/sbfi/en/home/education/scholarships-and-grants/swiss-government-excellence-scholarships.html)** | Research and PhD scholarships for foreign scholars in Switzerland. | ![Free](https://img.shields.io/badge/Free-0969da?style=flat-square) |  |
| <img src="https://www.google.com/s2/favicons?domain=www.campusfrance.org&sz=64" width="20" height="20"> | **[Eiffel Excellence Scholarship](https://www.campusfrance.org/en/eiffel-scholarship-program-of-excellence)** | French government scholarship for master's and PhD students. | ![Free](https://img.shields.io/badge/Free-0969da?style=flat-square) |  |
| <img src="https://www.google.com/s2/favicons?domain=admissions.kaust.edu.sa&sz=64" width="20" height="20"> | **[KAUST Fellowship](https://admissions.kaust.edu.sa)** | Fully funded MS and PhD fellowships in Saudi Arabia with a stipend. | ![Free](https://img.shields.io/badge/Free-0969da?style=flat-square) |  |

<p align="right"><a href="#top">↑ Back to top</a></p>

<a id="learning"></a>

## 📚 Learning & Courses

> Free courses and books that are as good as paid ones, often better.<br>
> <sub>36 picks · 7 gold</sub>

| | Resource | Why it's gold | Type | GitHub |
| :-: | :--- | :--- | :-- | :-- |
| <img src="https://www.google.com/s2/favicons?domain=www.freecodecamp.org&sz=64" width="20" height="20"> | **[freeCodeCamp](https://www.freecodecamp.org)** 🏆 | Full-stack curriculum with free certifications and thousands of exercises. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/freeCodeCamp/freeCodeCamp?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/freeCodeCamp/freeCodeCamp) |
| <img src="https://www.google.com/s2/favicons?domain=cs50.harvard.edu&sz=64" width="20" height="20"> | **[CS50x](https://cs50.harvard.edu/x/)** 🏆 | Harvard's famous intro to computer science, free online. | ![Free](https://img.shields.io/badge/Free-0969da?style=flat-square) |  |
| <img src="https://www.google.com/s2/favicons?domain=roadmap.sh&sz=64" width="20" height="20"> | **[roadmap.sh](https://roadmap.sh)** 🏆 | Step-by-step learning roadmaps for every developer role and technology. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/nilbuild/developer-roadmap?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/nilbuild/developer-roadmap) |
| <img src="https://www.google.com/s2/favicons?domain=www.theodinproject.com&sz=64" width="20" height="20"> | **[The Odin Project](https://www.theodinproject.com)** | Project-based full-stack web development path from zero to job-ready. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/TheOdinProject/curriculum?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/TheOdinProject/curriculum) |
| <img src="https://www.google.com/s2/favicons?domain=fullstackopen.com&sz=64" width="20" height="20"> | **[Full Stack Open](https://fullstackopen.com)** | University of Helsinki's modern web development course covering React, Node and GraphQL. | ![Free](https://img.shields.io/badge/Free-0969da?style=flat-square) |  |
| <img src="https://github.com/ossu.png?size=64" width="20" height="20"> | **[OSSU Computer Science](https://github.com/ossu/computer-science)** | A complete computer science degree path built from free online courses. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/ossu/computer-science?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/ossu/computer-science) |
| <img src="https://www.google.com/s2/favicons?domain=missing.csail.mit.edu&sz=64" width="20" height="20"> | **[The Missing Semester](https://missing.csail.mit.edu)** | MIT's course on the tools nobody teaches, like the shell, Git, editors and debugging. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/missing-semester/missing-semester?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/missing-semester/missing-semester) |
| <img src="https://github.com/codecrafters-io.png?size=64" width="20" height="20"> | **[build-your-own-x](https://github.com/codecrafters-io/build-your-own-x)** | Learn by rebuilding Git, Redis, Docker, databases and more from scratch. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/codecrafters-io/build-your-own-x?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/codecrafters-io/build-your-own-x) |
| <img src="https://github.com/practical-tutorials.png?size=64" width="20" height="20"> | **[project-based-learning](https://github.com/practical-tutorials/project-based-learning)** | Curated project tutorials sorted by programming language. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/practical-tutorials/project-based-learning?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/practical-tutorials/project-based-learning) |
| <img src="https://www.google.com/s2/favicons?domain=exercism.org&sz=64" width="20" height="20"> | **[Exercism](https://exercism.org)** | Coding exercises in 70+ languages with free human mentoring. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) |  |
| <img src="https://www.google.com/s2/favicons?domain=learngitbranching.js.org&sz=64" width="20" height="20"> | **[Learn Git Branching](https://learngitbranching.js.org)** | Interactive visual game that finally makes Git branching click. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/pcottle/learnGitBranching?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/pcottle/learnGitBranching) |
| <img src="https://www.google.com/s2/favicons?domain=ocw.mit.edu&sz=64" width="20" height="20"> | **[MIT OpenCourseWare](https://ocw.mit.edu)** | Lecture notes, videos and exams from thousands of MIT courses. | ![Free](https://img.shields.io/badge/Free-0969da?style=flat-square) |  |
| <img src="https://github.com/EbookFoundation.png?size=64" width="20" height="20"> | **[free-programming-books](https://github.com/EbookFoundation/free-programming-books)** | Huge list of free programming books in many languages. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/EbookFoundation/free-programming-books?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/EbookFoundation/free-programming-books) |
| <img src="https://www.google.com/s2/favicons?domain=karpathy.ai&sz=64" width="20" height="20"> | **[Neural Networks: Zero to Hero](https://karpathy.ai/zero-to-hero.html)** | Andrej Karpathy builds neural networks and GPT from scratch, step by step. | ![Free](https://img.shields.io/badge/Free-0969da?style=flat-square) |  |
| <img src="https://www.google.com/s2/favicons?domain=course.fast.ai&sz=64" width="20" height="20"> | **[Practical Deep Learning (fast.ai)](https://course.fast.ai)** | Hands-on deep learning course for people who already code. | ![Free](https://img.shields.io/badge/Free-0969da?style=flat-square) |  |
| <img src="https://www.google.com/s2/favicons?domain=huggingface.co&sz=64" width="20" height="20"> | **[Hugging Face Learn](https://huggingface.co/learn)** | Free courses on LLMs, AI agents, diffusion models and more. | ![Free](https://img.shields.io/badge/Free-0969da?style=flat-square) |  |
| <img src="https://www.google.com/s2/favicons?domain=developers.google.com&sz=64" width="20" height="20"> | **[Google Machine Learning Crash Course](https://developers.google.com/machine-learning/crash-course)** | Fast-paced, practical intro to machine learning with interactive exercises. | ![Free](https://img.shields.io/badge/Free-0969da?style=flat-square) |  |
| <img src="https://www.google.com/s2/favicons?domain=www.kaggle.com&sz=64" width="20" height="20"> | **[Kaggle Learn](https://www.kaggle.com/learn)** | Short, hands-on micro-courses in Python, SQL, pandas and machine learning. | ![Free](https://img.shields.io/badge/Free-0969da?style=flat-square) |  |
| <img src="https://www.google.com/s2/favicons?domain=www.khanacademy.org&sz=64" width="20" height="20"> | **[Khan Academy](https://www.khanacademy.org)** | Maths, science and computing lessons for every level. | ![Free](https://img.shields.io/badge/Free-0969da?style=flat-square) |  |
| <img src="https://www.google.com/s2/favicons?domain=javascript.info&sz=64" width="20" height="20"> | **[javascript.info](https://javascript.info)** | The modern JavaScript tutorial, from basics to advanced topics. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/javascript-tutorial/en.javascript.info?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/javascript-tutorial/en.javascript.info) |
| <img src="https://www.google.com/s2/favicons?domain=developer.mozilla.org&sz=64" width="20" height="20"> | **[MDN Web Docs](https://developer.mozilla.org)** 🏆 | The reference for HTML, CSS, JavaScript and web APIs. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/mdn/content?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/mdn/content) |
| <img src="https://github.com/rasbt.png?size=64" width="20" height="20"> | **[LLMs from Scratch](https://github.com/rasbt/LLMs-from-scratch)** 🏆 | Build a ChatGPT-like LLM in PyTorch step by step. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/rasbt/LLMs-from-scratch?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/rasbt/LLMs-from-scratch) |
| <img src="https://github.com/microsoft.png?size=64" width="20" height="20"> | **[ML for Beginners](https://github.com/microsoft/ML-For-Beginners)** | Microsoft's 12-week, 26-lesson classic machine learning curriculum. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/microsoft/ML-For-Beginners?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/microsoft/ML-For-Beginners) |
| <img src="https://github.com/microsoft.png?size=64" width="20" height="20"> | **[Generative AI for Beginners](https://github.com/microsoft/generative-ai-for-beginners)** | Microsoft's 21-lesson course on building generative AI apps. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/microsoft/generative-ai-for-beginners?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/microsoft/generative-ai-for-beginners) |
| <img src="https://github.com/microsoft.png?size=64" width="20" height="20"> | **[AI Agents for Beginners](https://github.com/microsoft/ai-agents-for-beginners)** | Microsoft's lessons on building AI agents from the ground up. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/microsoft/ai-agents-for-beginners?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/microsoft/ai-agents-for-beginners) |
| <img src="https://github.com/microsoft.png?size=64" width="20" height="20"> | **[Web Dev for Beginners](https://github.com/microsoft/Web-Dev-For-Beginners)** | Microsoft's 12-week, 24-lesson web development curriculum. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/microsoft/Web-Dev-For-Beginners?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/microsoft/Web-Dev-For-Beginners) |
| <img src="https://www.google.com/s2/favicons?domain=teachyourselfcs.com&sz=64" width="20" height="20"> | **[Teach Yourself CS](https://teachyourselfcs.com)** | The best books and lectures to learn computer science on your own. | ![Free](https://img.shields.io/badge/Free-0969da?style=flat-square) |  |
| <img src="https://www.google.com/s2/favicons?domain=www.promptingguide.ai&sz=64" width="20" height="20"> | **[Prompt Engineering Guide](https://www.promptingguide.ai)** | Guides, papers and techniques for prompting LLMs and agents. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/dair-ai/Prompt-Engineering-Guide?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/dair-ai/Prompt-Engineering-Guide) |
| <img src="https://github.com/anthropics.png?size=64" width="20" height="20"> | **[Claude Cookbooks](https://github.com/anthropics/claude-cookbooks)** | Copy-ready notebooks for building with Claude. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/anthropics/claude-cookbooks?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/anthropics/claude-cookbooks) |
| <img src="https://www.google.com/s2/favicons?domain=apps.ankiweb.net&sz=64" width="20" height="20"> | **[Anki](https://apps.ankiweb.net)** | Spaced-repetition flashcards that make anything you learn stick, synced across devices. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/ankitects/anki?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/ankitects/anki) |
| <img src="https://github.com/karpathy.png?size=64" width="20" height="20"> | **[nanoGPT](https://github.com/karpathy/nanoGPT)** 🏆 | Simplest, fastest repository for training and finetuning medium GPTs by Andrej Karpathy. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/karpathy/nanoGPT?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/karpathy/nanoGPT) |
| <img src="https://github.com/anthropics.png?size=64" width="20" height="20"> | **[Anthropic Courses](https://github.com/anthropics/courses)** 🏆 | Official educational courses and notebooks for prompt engineering and Claude development. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/anthropics/courses?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/anthropics/courses) |
| <img src="https://github.com/521xueweihan.png?size=64" width="20" height="20"> | **[HelloGitHub](https://github.com/521xueweihan/HelloGitHub)** | Curated monthly showcase of interesting, entry-level open-source projects. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/521xueweihan/HelloGitHub?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/521xueweihan/HelloGitHub) |
| <img src="https://github.com/sindresorhus.png?size=64" width="20" height="20"> | **[Awesome](https://github.com/sindresorhus/awesome)** | The definitive curated index of awesome lists covering programming and technology. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/sindresorhus/awesome?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/sindresorhus/awesome) |
| <img src="https://github.com/koodo-reader.png?size=64" width="20" height="20"> | **[Koodo Reader](https://github.com/koodo-reader/koodo-reader)** | Cross-platform open-source ebook manager and reader supporting EPUB, PDF, and MOBI. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/koodo-reader/koodo-reader?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/koodo-reader/koodo-reader) |
| <img src="https://github.com/hasaneyldrm.png?size=64" width="20" height="20"> | **[Exercises Dataset](https://github.com/hasaneyldrm/exercises-dataset)** | Comprehensive dataset of 1,324 fitness exercises with animated thumbnails. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/hasaneyldrm/exercises-dataset?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/hasaneyldrm/exercises-dataset) |

<p align="right"><a href="#top">↑ Back to top</a></p>

<a id="students"></a>

## 🧑‍🎓 Students & Programs

> Free licenses, credits and paid programs available only while you're a student or newcomer.<br>
> <sub>16 picks · 2 gold</sub>

| | Resource | Why it's gold | Type | GitHub |
| :-: | :--- | :--- | :-- | :-- |
| <img src="https://www.google.com/s2/favicons?domain=education.github.com&sz=64" width="20" height="20"> | **[GitHub Student Developer Pack](https://education.github.com/pack)** 🏆 | Free access to dozens of paid developer tools while you study. | ![Free](https://img.shields.io/badge/Free-0969da?style=flat-square) |  |
| <img src="https://www.google.com/s2/favicons?domain=summerofcode.withgoogle.com&sz=64" width="20" height="20"> | **[Google Summer of Code](https://summerofcode.withgoogle.com)** 🏆 | Paid, mentored program for contributing to open-source projects. | ![Free](https://img.shields.io/badge/Free-0969da?style=flat-square) |  |
| <img src="https://www.google.com/s2/favicons?domain=www.outreachy.org&sz=64" width="20" height="20"> | **[Outreachy](https://www.outreachy.org)** | Paid remote open-source internships for people underrepresented in tech. | ![Free](https://img.shields.io/badge/Free-0969da?style=flat-square) |  |
| <img src="https://www.google.com/s2/favicons?domain=mentorship.lfx.linuxfoundation.org&sz=64" width="20" height="20"> | **[LFX Mentorship](https://mentorship.lfx.linuxfoundation.org)** | Paid mentorships on Linux Foundation and CNCF open-source projects. | ![Free](https://img.shields.io/badge/Free-0969da?style=flat-square) |  |
| <img src="https://www.google.com/s2/favicons?domain=fellowship.mlh.io&sz=64" width="20" height="20"> | **[MLH Fellowship](https://fellowship.mlh.io)** | Remote fellowship programs in open source and software engineering. | ![Free](https://img.shields.io/badge/Free-0969da?style=flat-square) |  |
| <img src="https://www.google.com/s2/favicons?domain=mlh.io&sz=64" width="20" height="20"> | **[MLH Hackathons](https://mlh.io)** | Student hackathons around the world, in person and online. | ![Free](https://img.shields.io/badge/Free-0969da?style=flat-square) |  |
| <img src="https://www.google.com/s2/favicons?domain=devpost.com&sz=64" width="20" height="20"> | **[Devpost](https://devpost.com)** | Find online hackathons with real prizes and build your portfolio. | ![Free](https://img.shields.io/badge/Free-0969da?style=flat-square) |  |
| <img src="https://www.google.com/s2/favicons?domain=hacktoberfest.com&sz=64" width="20" height="20"> | **[Hacktoberfest](https://hacktoberfest.com)** | Yearly October event that rewards your first open-source contributions. | ![Free](https://img.shields.io/badge/Free-0969da?style=flat-square) |  |
| <img src="https://www.google.com/s2/favicons?domain=www.jetbrains.com&sz=64" width="20" height="20"> | **[JetBrains Educational Licenses](https://www.jetbrains.com/community/education/)** | Free JetBrains IDEs for students and teachers. | ![Free](https://img.shields.io/badge/Free-0969da?style=flat-square) |  |
| <img src="https://www.google.com/s2/favicons?domain=azure.microsoft.com&sz=64" width="20" height="20"> | **[Azure for Students](https://azure.microsoft.com/en-us/free/students)** | Azure cloud credit for students, with no credit card required. | ![Free](https://img.shields.io/badge/Free-0969da?style=flat-square) |  |
| <img src="https://www.google.com/s2/favicons?domain=www.figma.com&sz=64" width="20" height="20"> | **[Figma for Education](https://www.figma.com/education/)** | Free Figma Education plan for students and educators. | ![Free](https://img.shields.io/badge/Free-0969da?style=flat-square) |  |
| <img src="https://www.google.com/s2/favicons?domain=mvp.microsoft.com&sz=64" width="20" height="20"> | **[Microsoft Learn Student Ambassadors](https://mvp.microsoft.com/studentambassadors)** | Microsoft's student community with perks, mentoring and certifications. | ![Free](https://img.shields.io/badge/Free-0969da?style=flat-square) |  |
| <img src="https://www.google.com/s2/favicons?domain=aws.amazon.com&sz=64" width="20" height="20"> | **[AWS Educate](https://aws.amazon.com/education/awseducate/)** | Free cloud courses and hands-on labs, no credit card required. | ![Free](https://img.shields.io/badge/Free-0969da?style=flat-square) |  |
| <img src="https://www.google.com/s2/favicons?domain=www.notion.com&sz=64" width="20" height="20"> | **[Notion for Education](https://www.notion.com/product/notion-for-education)** | Free Notion Plus plan for students with a school email. | ![Free](https://img.shields.io/badge/Free-0969da?style=flat-square) |  |
| <img src="https://www.google.com/s2/favicons?domain=education.github.com&sz=64" width="20" height="20"> | **[GitHub Campus Experts](https://education.github.com/experts)** | Training program for student community leaders. | ![Free](https://img.shields.io/badge/Free-0969da?style=flat-square) |  |
| <img src="https://www.google.com/s2/favicons?domain=www.coursera.support&sz=64" width="20" height="20"> | **[Coursera Financial Aid](https://www.coursera.support/s/article/209819033-Apply-for-Financial-Aid-or-a-Scholarship)** | Get Coursera courses and certificates free with financial aid. | ![Free](https://img.shields.io/badge/Free-0969da?style=flat-square) |  |

<p align="right"><a href="#top">↑ Back to top</a></p>

<a id="dev-tools"></a>

## 🛠️ Developer Tools & Free Tiers

> Build, host and ship without a credit card.<br>
> <sub>58 picks · 10 gold</sub>

| | Resource | Why it's gold | Type | GitHub |
| :-: | :--- | :--- | :-- | :-- |
| <img src="https://github.com/ripienaar.png?size=64" width="20" height="20"> | **[free-for-dev](https://github.com/ripienaar/free-for-dev)** 🏆 | Hundreds of SaaS, PaaS and IaaS services with free tiers for developers. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/ripienaar/free-for-dev?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/ripienaar/free-for-dev) |
| <img src="https://github.com/public-apis.png?size=64" width="20" height="20"> | **[public-apis](https://github.com/public-apis/public-apis)** 🏆 | Collective list of free APIs to build projects on. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/public-apis/public-apis?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/public-apis/public-apis) |
| <img src="https://www.google.com/s2/favicons?domain=code.visualstudio.com&sz=64" width="20" height="20"> | **[VS Code](https://code.visualstudio.com)** | Free code editor with a huge extension ecosystem. | ![Free](https://img.shields.io/badge/Free-0969da?style=flat-square) |  |
| <img src="https://www.google.com/s2/favicons?domain=zed.dev&sz=64" width="20" height="20"> | **[Zed](https://zed.dev)** | Very fast open-source code editor with built-in collaboration and AI. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/zed-industries/zed?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/zed-industries/zed) |
| <img src="https://www.google.com/s2/favicons?domain=supabase.com&sz=64" width="20" height="20"> | **[Supabase](https://supabase.com)** 🏆 | Open-source Postgres backend with auth, storage and realtime, plus a free tier. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/supabase/supabase?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/supabase/supabase) |
| <img src="https://www.google.com/s2/favicons?domain=appwrite.io&sz=64" width="20" height="20"> | **[Appwrite](https://appwrite.io)** | Open-source backend for web and mobile apps, self-hosted or in the cloud. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/appwrite/appwrite?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/appwrite/appwrite) |
| <img src="https://www.google.com/s2/favicons?domain=neon.tech&sz=64" width="20" height="20"> | **[Neon](https://neon.tech)** | Serverless Postgres with database branching and a free plan. | ![Free tier](https://img.shields.io/badge/Free%20tier-bf8700?style=flat-square) |  |
| <img src="https://www.google.com/s2/favicons?domain=pages.cloudflare.com&sz=64" width="20" height="20"> | **[Cloudflare Pages](https://pages.cloudflare.com)** | Deploy static sites and frontends for free on a global CDN. | ![Free tier](https://img.shields.io/badge/Free%20tier-bf8700?style=flat-square) |  |
| <img src="https://www.google.com/s2/favicons?domain=vercel.com&sz=64" width="20" height="20"> | **[Vercel](https://vercel.com)** | Push-to-deploy hosting for frontends and Next.js, with a free Hobby plan. | ![Free tier](https://img.shields.io/badge/Free%20tier-bf8700?style=flat-square) |  |
| <img src="https://www.google.com/s2/favicons?domain=coolify.io&sz=64" width="20" height="20"> | **[Coolify](https://coolify.io)** | Self-hosted alternative to Heroku and Vercel for your own server. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/coollabsio/coolify?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/coollabsio/coolify) |
| <img src="https://www.google.com/s2/favicons?domain=hoppscotch.io&sz=64" width="20" height="20"> | **[Hoppscotch](https://hoppscotch.io)** | Lightweight open-source API client, an alternative to Postman. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/hoppscotch/hoppscotch?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/hoppscotch/hoppscotch) |
| <img src="https://www.google.com/s2/favicons?domain=www.usebruno.com&sz=64" width="20" height="20"> | **[Bruno](https://www.usebruno.com)** | Offline-first API client that stores collections as plain files in your Git repo. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/usebruno/bruno?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/usebruno/bruno) |
| <img src="https://www.google.com/s2/favicons?domain=dbeaver.io&sz=64" width="20" height="20"> | **[DBeaver](https://dbeaver.io)** | Universal database client for Postgres, MySQL, SQLite and dozens more. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/dbeaver/dbeaver?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/dbeaver/dbeaver) |
| <img src="https://www.google.com/s2/favicons?domain=sentry.io&sz=64" width="20" height="20"> | **[Sentry](https://sentry.io)** | Error tracking and performance monitoring with a free developer plan. | ![Free tier](https://img.shields.io/badge/Free%20tier-bf8700?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/getsentry/sentry?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/getsentry/sentry) |
| <img src="https://www.google.com/s2/favicons?domain=devdocs.io&sz=64" width="20" height="20"> | **[DevDocs](https://devdocs.io)** | API documentation for hundreds of languages and frameworks, searchable and offline. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/freeCodeCamp/devdocs?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/freeCodeCamp/devdocs) |
| <img src="https://www.google.com/s2/favicons?domain=regex101.com&sz=64" width="20" height="20"> | **[regex101](https://regex101.com)** | Build, test and debug regular expressions with live explanations. | ![Free](https://img.shields.io/badge/Free-0969da?style=flat-square) |  |
| <img src="https://www.google.com/s2/favicons?domain=letsencrypt.org&sz=64" width="20" height="20"> | **[Let's Encrypt](https://letsencrypt.org)** | Free, automated HTTPS certificates for any website. | ![Free](https://img.shields.io/badge/Free-0969da?style=flat-square) |  |
| <img src="https://www.google.com/s2/favicons?domain=ohmyz.sh&sz=64" width="20" height="20"> | **[Oh My Zsh](https://ohmyz.sh)** | Framework that makes your terminal far more pleasant, with hundreds of plugins and themes. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/ohmyzsh/ohmyzsh?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/ohmyzsh/ohmyzsh) |
| <img src="https://github.com/awesome-selfhosted.png?size=64" width="20" height="20"> | **[awesome-selfhosted](https://github.com/awesome-selfhosted/awesome-selfhosted)** | Free software you can host yourself, sorted by category. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/awesome-selfhosted/awesome-selfhosted?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/awesome-selfhosted/awesome-selfhosted) |
| <img src="https://www.google.com/s2/favicons?domain=neovim.io&sz=64" width="20" height="20"> | **[Neovim](https://neovim.io)** | Hyperextensible Vim-based editor with Lua plugins and built-in LSP. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/neovim/neovim?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/neovim/neovim) |
| <img src="https://github.com/junegunn.png?size=64" width="20" height="20"> | **[fzf](https://github.com/junegunn/fzf)** | Fuzzy finder for the terminal: files, history, processes, anything. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/junegunn/fzf?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/junegunn/fzf) |
| <img src="https://github.com/BurntSushi.png?size=64" width="20" height="20"> | **[ripgrep](https://github.com/BurntSushi/ripgrep)** | Blazing-fast recursive search that respects your .gitignore. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/BurntSushi/ripgrep?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/BurntSushi/ripgrep) |
| <img src="https://github.com/jesseduffield.png?size=64" width="20" height="20"> | **[lazygit](https://github.com/jesseduffield/lazygit)** 🏆 | Terminal UI for git that makes staging, rebasing and stashing painless. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/jesseduffield/lazygit?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/jesseduffield/lazygit) |
| <img src="https://www.google.com/s2/favicons?domain=starship.rs&sz=64" width="20" height="20"> | **[Starship](https://starship.rs)** | Fast, minimal, customizable prompt for any shell. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/starship/starship?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/starship/starship) |
| <img src="https://github.com/louislam.png?size=64" width="20" height="20"> | **[Uptime Kuma](https://github.com/louislam/uptime-kuma)** | Self-hosted uptime monitoring with status pages and alerts. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/louislam/uptime-kuma?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/louislam/uptime-kuma) |
| <img src="https://www.google.com/s2/favicons?domain=tldr.sh&sz=64" width="20" height="20"> | **[tldr pages](https://tldr.sh)** | Community cheat sheets with practical examples for console commands. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/tldr-pages/tldr?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/tldr-pages/tldr) |
| <img src="https://www.google.com/s2/favicons?domain=bun.sh&sz=64" width="20" height="20"> | **[Bun](https://bun.sh)** | All-in-one JavaScript runtime, bundler, test runner and package manager. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/oven-sh/bun?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/oven-sh/bun) |
| <img src="https://www.google.com/s2/favicons?domain=ghostty.org&sz=64" width="20" height="20"> | **[Ghostty](https://ghostty.org)** | Fast, native, GPU-accelerated terminal emulator. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/ghostty-org/ghostty?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/ghostty-org/ghostty) |
| <img src="https://www.google.com/s2/favicons?domain=www.netlify.com&sz=64" width="20" height="20"> | **[Netlify](https://www.netlify.com)** | Deploy static sites and serverless functions with a generous free plan. | ![Free tier](https://img.shields.io/badge/Free%20tier-bf8700?style=flat-square) |  |
| <img src="https://www.google.com/s2/favicons?domain=dashboard.digitalplat.org&sz=64" width="20" height="20"> | **[FreeDomain](https://dashboard.digitalplat.org)** | Guide and directory for free domain registration and hands-on DNS configuration. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/DigitalPlatDev/FreeDomain?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/DigitalPlatDev/FreeDomain) |
| <img src="https://www.google.com/s2/favicons?domain=frontendchecklist.io&sz=64" width="20" height="20"> | **[Front-End Checklist](https://frontendchecklist.io)** | Comprehensive checklist of HTML, CSS, performance, and accessibility best practices. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/thedaviddias/Front-End-Checklist?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/thedaviddias/Front-End-Checklist) |
| <img src="https://github.com/dkhamsing.png?size=64" width="20" height="20"> | **[Open Source iOS Apps](https://github.com/dkhamsing/open-source-ios-apps)** | Collaborative catalog of open-source iOS applications across various frameworks. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/dkhamsing/open-source-ios-apps?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/dkhamsing/open-source-ios-apps) |
| <img src="https://github.com/Genymobile.png?size=64" width="20" height="20"> | **[Scrcpy](https://github.com/Genymobile/scrcpy)** | Display and control Android devices over USB or TCP/IP with high performance. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/Genymobile/scrcpy?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/Genymobile/scrcpy) |
| <img src="https://github.com/t8y2.png?size=64" width="20" height="20"> | **[DBX](https://github.com/t8y2/dbx)** | 25 MB lightweight cross-platform database client supporting 100+ database types. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/t8y2/dbx?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/t8y2/dbx) |
| <img src="https://github.com/reacherhq.png?size=64" width="20" height="20"> | **[Check If Email Exists](https://github.com/reacherhq/check-if-email-exists)** | Verify email address deliverability via SMTP handshake without sending an email. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/reacherhq/check-if-email-exists?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/reacherhq/check-if-email-exists) |
| <img src="https://github.com/astral-sh.png?size=64" width="20" height="20"> | **[uv](https://github.com/astral-sh/uv)** 🏆 | Extremely fast Python package installer and resolver written in Rust. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/astral-sh/uv?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/astral-sh/uv) |
| <img src="https://github.com/astral-sh.png?size=64" width="20" height="20"> | **[Ruff](https://github.com/astral-sh/ruff)** 🏆 | Extremely fast Python linter and code formatter written in Rust. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/astral-sh/ruff?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/astral-sh/ruff) |
| <img src="https://github.com/pocketbase.png?size=64" width="20" height="20"> | **[PocketBase](https://github.com/pocketbase/pocketbase)** 🏆 | Open source realtime backend in 1 portable Go binary with embedded SQLite. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/pocketbase/pocketbase?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/pocketbase/pocketbase) |
| <img src="https://github.com/sharkdp.png?size=64" width="20" height="20"> | **[fd](https://github.com/sharkdp/fd)** | Simple, fast, and user-friendly command-line alternative to find. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/sharkdp/fd?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/sharkdp/fd) |
| <img src="https://github.com/fastapi.png?size=64" width="20" height="20"> | **[FastAPI](https://github.com/fastapi/fastapi)** 🏆 | High-performance web framework for building APIs with Python and type hints. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/fastapi/fastapi?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/fastapi/fastapi) |
| <img src="https://github.com/trpc.png?size=64" width="20" height="20"> | **[tRPC](https://github.com/trpc/trpc)** | End-to-end typesafe APIs without code generation or runtime schema bloat. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/trpc/trpc?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/trpc/trpc) |
| <img src="https://github.com/biomejs.png?size=64" width="20" height="20"> | **[Biome](https://github.com/biomejs/biome)** | Fast toolchain for JavaScript and TypeScript that formats and lints in milliseconds. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/biomejs/biome?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/biomejs/biome) |
| <img src="https://github.com/Dokploy.png?size=64" width="20" height="20"> | **[Dokploy](https://github.com/Dokploy/dokploy)** | Lightweight self-hostable PaaS alternative to Heroku, Vercel, and Coolify. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/Dokploy/dokploy?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/Dokploy/dokploy) |
| <img src="https://github.com/charmbracelet.png?size=64" width="20" height="20"> | **[Gum](https://github.com/charmbracelet/gum)** | Tool for glamorous interactive shell scripts and terminal prompts. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/charmbracelet/gum?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/charmbracelet/gum) |
| <img src="https://github.com/charmbracelet.png?size=64" width="20" height="20"> | **[Glow](https://github.com/charmbracelet/glow)** | Terminal markdown renderer with styled pager, colors, and syntax highlighting. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/charmbracelet/glow?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/charmbracelet/glow) |
| <img src="https://github.com/jo-inc.png?size=64" width="20" height="20"> | **[Camofox](https://github.com/jo-inc/camofox-browser)** | Stealth headless browser for AI agents that bypasses anti-bot detections. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/jo-inc/camofox-browser?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/jo-inc/camofox-browser) |
| <img src="https://github.com/marcelscruz.png?size=64" width="20" height="20"> | **[Public APIs](https://github.com/marcelscruz/public-apis)** | Curated collaborative directory of public APIs for developers across 52 categories. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/marcelscruz/public-apis?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/marcelscruz/public-apis) |
| <img src="https://github.com/cporter202.png?size=64" width="20" height="20"> | **[API Mega List](https://github.com/cporter202/API-mega-list)** | Comprehensive collection of free public APIs for rapid application prototyping. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/cporter202/API-mega-list?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/cporter202/API-mega-list) |
| <img src="https://github.com/dgtlmoon.png?size=64" width="20" height="20"> | **[ChangeDetection.io](https://github.com/dgtlmoon/changedetection.io)** | Self-hosted website change detection, monitoring, and notification service. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/dgtlmoon/changedetection.io?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/dgtlmoon/changedetection.io) |
| <img src="https://github.com/REAndroid.png?size=64" width="20" height="20"> | **[APKEditor](https://github.com/REAndroid/APKEditor)** | Android APK reverse engineering and resource modification tool. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/REAndroid/APKEditor?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/REAndroid/APKEditor) |
| <img src="https://github.com/FreeRDP.png?size=64" width="20" height="20"> | **[FreeRDP](https://github.com/FreeRDP/FreeRDP)** | Free and open-source Remote Desktop Protocol client and library implementation. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/FreeRDP/FreeRDP?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/FreeRDP/FreeRDP) |
| <img src="https://github.com/lordbasex.png?size=64" width="20" height="20"> | **[LordOS](https://github.com/lordbasex/LordOS)** | Lightweight Debian Linux distribution with Wayland compositor and QuickJS UI. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/lordbasex/LordOS?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/lordbasex/LordOS) |
| <img src="https://www.google.com/s2/favicons?domain=caniuse.com&sz=64" width="20" height="20"> | **[Can I use](https://caniuse.com)** 🏆 | Up-to-date browser feature support tables for modern HTML, CSS, JavaScript, and Web APIs. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/fyrd/caniuse?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/fyrd/caniuse) |
| <img src="https://www.google.com/s2/favicons?domain=crontab.guru&sz=64" width="20" height="20"> | **[Crontab.guru](https://crontab.guru)** | Interactive cron schedule expression editor with human-readable plain English definitions. | ![Free](https://img.shields.io/badge/Free-0969da?style=flat-square) |  |
| <img src="https://www.google.com/s2/favicons?domain=jsoncrack.com&sz=64" width="20" height="20"> | **[JSON Crack](https://jsoncrack.com)** 🏆 | Interactive visual graph and hierarchical tree viewer for complex JSON structures. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/AykutSarac/jsoncrack.com?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/AykutSarac/jsoncrack.com) |
| <img src="https://www.google.com/s2/favicons?domain=ray.so&sz=64" width="20" height="20"> | **[Ray.so](https://ray.so)** | Generate beautiful code snippet screenshots with syntax themes, padding, and dark mode. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/raycast/ray-so?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/raycast/ray-so) |
| <img src="https://www.google.com/s2/favicons?domain=bundlephobia.com&sz=64" width="20" height="20"> | **[Bundlephobia](https://bundlephobia.com)** | Find the bundle size and download impact of npm packages before adding them to projects. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/pastelsky/bundlephobia?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/pastelsky/bundlephobia) |
| <img src="https://www.google.com/s2/favicons?domain=boykopovar.github.io&sz=64" width="20" height="20"> | **[Anyps5](https://boykopovar.github.io/AnyPS5/)** | Tool for automatic PS5 executables porting to Linux and Windows. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/boykopovar/AnyPS5?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/boykopovar/AnyPS5) |

<p align="right"><a href="#top">↑ Back to top</a></p>

<a id="ai-tools"></a>

## 🤖 AI Tools & Models

> Run models locally, build AI apps and automate your work.<br>
> <sub>37 picks · 5 gold</sub>

| | Resource | Why it's gold | Type | GitHub |
| :-: | :--- | :--- | :-- | :-- |
| <img src="https://www.google.com/s2/favicons?domain=ollama.com&sz=64" width="20" height="20"> | **[Ollama](https://ollama.com)** 🏆 | Run open LLMs locally with a single command. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/ollama/ollama?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/ollama/ollama) |
| <img src="https://www.google.com/s2/favicons?domain=aistudio.google.com&sz=64" width="20" height="20"> | **[Google AI Studio](https://aistudio.google.com)** 🏆 | Try Gemini models and get a free API key in minutes. | ![Free tier](https://img.shields.io/badge/Free%20tier-bf8700?style=flat-square) |  |
| <img src="https://www.google.com/s2/favicons?domain=notebooklm.google&sz=64" width="20" height="20"> | **[NotebookLM](https://notebooklm.google)** | Upload your sources and get grounded answers, summaries and audio overviews. | ![Free tier](https://img.shields.io/badge/Free%20tier-bf8700?style=flat-square) |  |
| <img src="https://github.com/open-webui.png?size=64" width="20" height="20"> | **[Open WebUI](https://github.com/open-webui/open-webui)** | Self-hosted ChatGPT-style interface for local and API models. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/open-webui/open-webui?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/open-webui/open-webui) |
| <img src="https://www.google.com/s2/favicons?domain=lmstudio.ai&sz=64" width="20" height="20"> | **[LM Studio](https://lmstudio.ai)** | Desktop app to discover, download and chat with local LLMs. | ![Free](https://img.shields.io/badge/Free-0969da?style=flat-square) |  |
| <img src="https://github.com/ggml-org.png?size=64" width="20" height="20"> | **[llama.cpp](https://github.com/ggml-org/llama.cpp)** | Fast LLM inference in C/C++ that runs on almost any hardware. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/ggml-org/llama.cpp?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/ggml-org/llama.cpp) |
| <img src="https://github.com/vllm-project.png?size=64" width="20" height="20"> | **[vLLM](https://github.com/vllm-project/vllm)** | High-throughput engine for serving LLMs in production. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/vllm-project/vllm?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/vllm-project/vllm) |
| <img src="https://www.google.com/s2/favicons?domain=huggingface.co&sz=64" width="20" height="20"> | **[Hugging Face](https://huggingface.co)** | Hub of open models, datasets and live demo apps. | ![Free tier](https://img.shields.io/badge/Free%20tier-bf8700?style=flat-square) |  |
| <img src="https://github.com/unslothai.png?size=64" width="20" height="20"> | **[Unsloth](https://github.com/unslothai/unsloth)** | Fine-tune open LLMs faster and with much less GPU memory. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/unslothai/unsloth?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/unslothai/unsloth) |
| <img src="https://github.com/langgenius.png?size=64" width="20" height="20"> | **[Dify](https://github.com/langgenius/dify)** | Visual platform for building LLM apps, RAG pipelines and agents. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/langgenius/dify?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/langgenius/dify) |
| <img src="https://github.com/Mintplex-Labs.png?size=64" width="20" height="20"> | **[AnythingLLM](https://github.com/Mintplex-Labs/anything-llm)** | Private all-in-one app for chatting with your documents using any LLM. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/Mintplex-Labs/anything-llm?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/Mintplex-Labs/anything-llm) |
| <img src="https://github.com/n8n-io.png?size=64" width="20" height="20"> | **[n8n](https://github.com/n8n-io/n8n)** | Fair-code workflow automation with AI agents, free to self-host as the Community Edition. | ![Free](https://img.shields.io/badge/Free-0969da?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/n8n-io/n8n?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/n8n-io/n8n) |
| <img src="https://github.com/Comfy-Org.png?size=64" width="20" height="20"> | **[ComfyUI](https://github.com/Comfy-Org/ComfyUI)** | Node-based interface for image and video generation models. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/Comfy-Org/ComfyUI?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/Comfy-Org/ComfyUI) |
| <img src="https://github.com/openai.png?size=64" width="20" height="20"> | **[Whisper](https://github.com/openai/whisper)** | OpenAI's open-source multilingual speech-to-text model. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/openai/whisper?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/openai/whisper) |
| <img src="https://github.com/Shubhamsaboo.png?size=64" width="20" height="20"> | **[awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps)** | 100+ open-source AI agent, RAG and LLM app examples you can run and learn from. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/Shubhamsaboo/awesome-llm-apps?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/Shubhamsaboo/awesome-llm-apps) |
| <img src="https://www.google.com/s2/favicons?domain=www.langchain.com&sz=64" width="20" height="20"> | **[LangChain](https://www.langchain.com)** | The most used framework for building LLM apps and agents. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/langchain-ai/langchain?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/langchain-ai/langchain) |
| <img src="https://www.google.com/s2/favicons?domain=www.llamaindex.ai&sz=64" width="20" height="20"> | **[LlamaIndex](https://www.llamaindex.ai)** | Data framework for connecting your documents to LLMs (RAG). | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/run-llama/llama_index?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/run-llama/llama_index) |
| <img src="https://www.google.com/s2/favicons?domain=jan.ai&sz=64" width="20" height="20"> | **[Jan](https://jan.ai)** | Offline ChatGPT alternative that runs models 100% on your computer. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/janhq/jan?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/janhq/jan) |
| <img src="https://www.google.com/s2/favicons?domain=www.langflow.org&sz=64" width="20" height="20"> | **[Langflow](https://www.langflow.org)** | Visual drag-and-drop builder for AI agents and RAG flows. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/langflow-ai/langflow?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/langflow-ai/langflow) |
| <img src="https://www.google.com/s2/favicons?domain=browser-use.com&sz=64" width="20" height="20"> | **[Browser Use](https://browser-use.com)** 🏆 | Let AI agents control a real web browser to finish tasks. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/browser-use/browser-use?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/browser-use/browser-use) |
| <img src="https://www.google.com/s2/favicons?domain=www.firecrawl.dev&sz=64" width="20" height="20"> | **[Firecrawl](https://www.firecrawl.dev)** | Turn any website into clean, LLM-ready markdown or data. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/firecrawl/firecrawl?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/firecrawl/firecrawl) |
| <img src="https://www.google.com/s2/favicons?domain=crewai.com&sz=64" width="20" height="20"> | **[CrewAI](https://crewai.com)** | Framework for orchestrating teams of role-playing AI agents. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/crewAIInc/crewAI?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/crewAIInc/crewAI) |
| <img src="https://www.google.com/s2/favicons?domain=www.litellm.ai&sz=64" width="20" height="20"> | **[LiteLLM](https://www.litellm.ai)** | Call 100+ LLM APIs in the OpenAI format, with a proxy and cost tracking. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/BerriAI/litellm?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/BerriAI/litellm) |
| <img src="https://www.google.com/s2/favicons?domain=ragflow.io&sz=64" width="20" height="20"> | **[RAGFlow](https://ragflow.io)** | RAG engine with deep document understanding for reliable answers. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/infiniflow/ragflow?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/infiniflow/ragflow) |
| <img src="https://github.com/microsoft.png?size=64" width="20" height="20"> | **[MarkItDown](https://github.com/microsoft/markitdown)** 🏆 | Convert PDFs, Office files and more to Markdown for LLMs. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/microsoft/markitdown?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/microsoft/markitdown) |
| <img src="https://www.google.com/s2/favicons?domain=lobehub.com&sz=64" width="20" height="20"> | **[LobeHub](https://lobehub.com)** | Open-source AI workspace for chats and teams of agents across many model providers. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/lobehub/lobehub?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/lobehub/lobehub) |
| <img src="https://www.google.com/s2/favicons?domain=openrouter.ai&sz=64" width="20" height="20"> | **[OpenRouter](https://openrouter.ai)** | One API for hundreds of models, including many free ones. | ![Free tier](https://img.shields.io/badge/Free%20tier-bf8700?style=flat-square) |  |
| <img src="https://www.google.com/s2/favicons?domain=freellmapi.co&sz=64" width="20" height="20"> | **[Free LLM API](https://freellmapi.co)** | Curated index of 34 free LLM providers and quota-free API endpoints. | ![Free](https://img.shields.io/badge/Free-0969da?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/tashfeenahmed/freellmapi?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/tashfeenahmed/freellmapi) |
| <img src="https://www.google.com/s2/favicons?domain=tinyhumans.ai&sz=64" width="20" height="20"> | **[OpenHuman](https://tinyhumans.ai/openhuman)** | Lightweight and fast open-source agent harness designed for autonomous task execution. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/tinyhumansai/openhuman?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/tinyhumansai/openhuman) |
| <img src="https://github.com/lyogavin.png?size=64" width="20" height="20"> | **[AirLLM](https://github.com/lyogavin/airllm)** | Runs 70B+ LLM inference locally on single desktop GPUs with layer-wise memory swapping. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/lyogavin/airllm?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/lyogavin/airllm) |
| <img src="https://www.google.com/s2/favicons?domain=khoj.dev&sz=64" width="20" height="20"> | **[Khoj](https://khoj.dev)** | Self-hostable desktop AI personal assistant that searches across your notes and docs. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/khoj-ai/khoj?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/khoj-ai/khoj) |
| <img src="https://github.com/ashishpatel26.png?size=64" width="20" height="20"> | **[500 Ai Machine Learning Deep Learning Computer Vision Nlp Projects With Code](https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code)** | 500 AI Machine learning Deep learning Computer vision NLP Projects with code. | ![Free](https://img.shields.io/badge/Free-0969da?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code) |
| <img src="https://github.com/mendableai.png?size=64" width="20" height="20"> | **[Firecrawl](https://github.com/mendableai/firecrawl)** 🏆 | Turn entire websites into clean LLM-ready markdown or structured data with one call. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/mendableai/firecrawl?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/mendableai/firecrawl) |
| <img src="https://github.com/jina-ai.png?size=64" width="20" height="20"> | **[Jina Reader](https://github.com/jina-ai/reader)** | Convert any webpage into clean markdown for LLMs by prefixing r.jina.ai to the URL. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/jina-ai/reader?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/jina-ai/reader) |
| <img src="https://github.com/Niko1221.png?size=64" width="20" height="20"> | **[Strata](https://github.com/Niko1221/Strata)** | Run high-performance open LLMs on consumer GPUs with one-click desktop setup. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/Niko1221/Strata?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/Niko1221/Strata) |
| <img src="https://www.google.com/s2/favicons?domain=mathmodel.top&sz=64" width="20" height="20"> | **[Mathmodelagent](https://mathmodel.top/home)** | Agent & skills ,自动完成数学建模，生成一份完整的可以直接提交的论文. | ![Free](https://img.shields.io/badge/Free-0969da?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/jihe520/MathModelAgent?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/jihe520/MathModelAgent) |
| <img src="https://www.google.com/s2/favicons?domain=openmed.life&sz=64" width="20" height="20"> | **[Openmed](https://openmed.life/)** | Local-first healthcare AI: clinical NER and HIPAA PII de-identification on hardware you control. 2,200+ medical. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/maziyarpanahi/openmed?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/maziyarpanahi/openmed) |

<p align="right"><a href="#top">↑ Back to top</a></p>

<a id="ai-coding"></a>

## 🧠 AI Coding Agents & Tools

> Terminal coding agents, spec-driven workflows and the tools that make Claude Code better.<br>
> <sub>42 picks · 6 gold</sub>

| | Resource | Why it's gold | Type | GitHub |
| :-: | :--- | :--- | :-- | :-- |
| <img src="https://github.com/google-gemini.png?size=64" width="20" height="20"> | **[Gemini CLI](https://github.com/google-gemini/gemini-cli)** 🏆 | Google's open-source AI agent for the terminal, with a generous free tier. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/google-gemini/gemini-cli?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/google-gemini/gemini-cli) |
| <img src="https://github.com/openai.png?size=64" width="20" height="20"> | **[Codex CLI](https://github.com/openai/codex)** | OpenAI's open-source coding agent that runs in your terminal. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/openai/codex?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/openai/codex) |
| <img src="https://github.com/Aider-AI.png?size=64" width="20" height="20"> | **[Aider](https://github.com/Aider-AI/aider)** | AI pair programming in your terminal that edits your Git repo directly. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/Aider-AI/aider?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/Aider-AI/aider) |
| <img src="https://github.com/continuedev.png?size=64" width="20" height="20"> | **[Continue](https://github.com/continuedev/continue)** | Open-source AI code assistant for VS Code and JetBrains, using any model. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/continuedev/continue?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/continuedev/continue) |
| <img src="https://github.com/OpenHands.png?size=64" width="20" height="20"> | **[OpenHands](https://github.com/OpenHands/OpenHands)** | Open-source autonomous software engineering agent. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/OpenHands/OpenHands?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/OpenHands/OpenHands) |
| <img src="https://github.com/github.png?size=64" width="20" height="20"> | **[Spec Kit](https://github.com/github/spec-kit)** 🏆 | GitHub's toolkit for spec-driven development that turns specs into plans and tasks for agents. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/github/spec-kit?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/github/spec-kit) |
| <img src="https://github.com/bmad-code-org.png?size=64" width="20" height="20"> | **[BMAD Method](https://github.com/bmad-code-org/BMAD-METHOD)** | Agile AI-driven development method with specialized agents for planning, architecture and delivery. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/bmad-code-org/BMAD-METHOD?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/bmad-code-org/BMAD-METHOD) |
| <img src="https://github.com/davila7.png?size=64" width="20" height="20"> | **[Claude Code Templates](https://github.com/davila7/claude-code-templates)** | CLI for configuring and monitoring Claude Code, with ready-made agents, commands and hooks. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/davila7/claude-code-templates?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/davila7/claude-code-templates) |
| <img src="https://github.com/jarrodwatts.png?size=64" width="20" height="20"> | **[Claude HUD](https://github.com/jarrodwatts/claude-hud)** | Claude Code plugin showing context usage, active tools, running agents and todo progress. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/jarrodwatts/claude-hud?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/jarrodwatts/claude-hud) |
| <img src="https://github.com/ccusage.png?size=64" width="20" height="20"> | **[ccusage](https://github.com/ccusage/ccusage)** | Analyze Claude Code token usage and costs from your local logs. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/ccusage/ccusage?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/ccusage/ccusage) |
| <img src="https://github.com/BloopAI.png?size=64" width="20" height="20"> | **[Vibe Kanban](https://github.com/BloopAI/vibe-kanban)** | Kanban board for planning and running Claude Code, Codex and other coding agents. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/BloopAI/vibe-kanban?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/BloopAI/vibe-kanban) |
| <img src="https://github.com/farion1231.png?size=64" width="20" height="20"> | **[CC Switch](https://github.com/farion1231/cc-switch)** | Desktop app to manage providers and settings for Claude Code, Codex and other CLI agents. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/farion1231/cc-switch?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/farion1231/cc-switch) |
| <img src="https://github.com/musistudio.png?size=64" width="20" height="20"> | **[Claude Code Router](https://github.com/musistudio/claude-code-router)** | Route Claude Code requests to the models and providers you choose. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/musistudio/claude-code-router?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/musistudio/claude-code-router) |
| <img src="https://github.com/luongnv89.png?size=64" width="20" height="20"> | **[Claude How-To](https://github.com/luongnv89/claude-howto)** | Visual, example-driven guide to Claude Code with copy-paste templates. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/luongnv89/claude-howto?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/luongnv89/claude-howto) |
| <img src="https://github.com/shareAI-lab.png?size=64" width="20" height="20"> | **[Learn Claude Code](https://github.com/shareAI-lab/learn-claude-code)** | Build a nano Claude Code-style agent harness from scratch to learn how it works. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/shareAI-lab/learn-claude-code?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/shareAI-lab/learn-claude-code) |
| <img src="https://github.com/hesreallyhim.png?size=64" width="20" height="20"> | **[awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code)** | Hand-picked skills, agents, hooks, status lines and tooling for Claude Code. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/hesreallyhim/awesome-claude-code?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/hesreallyhim/awesome-claude-code) |
| <img src="https://www.google.com/s2/favicons?domain=cline.bot&sz=64" width="20" height="20"> | **[Cline](https://cline.bot)** 🏆 | Autonomous coding agent inside VS Code that plans, edits and runs commands. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/cline/cline?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/cline/cline) |
| <img src="https://www.google.com/s2/favicons?domain=goose-docs.ai&sz=64" width="20" height="20"> | **[Goose](https://goose-docs.ai)** | Local, extensible AI agent that installs, runs, edits and tests code with any LLM. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/aaif-goose/goose?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/aaif-goose/goose) |
| <img src="https://www.google.com/s2/favicons?domain=opencode.ai&sz=64" width="20" height="20"> | **[OpenCode](https://opencode.ai)** | Open-source AI coding agent built for the terminal, any model. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/anomalyco/opencode?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/anomalyco/opencode) |
| <img src="https://www.google.com/s2/favicons?domain=www.tabbyml.com&sz=64" width="20" height="20"> | **[Tabby](https://www.tabbyml.com)** | Self-hosted AI coding assistant, an open alternative to Copilot. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/TabbyML/tabby?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/TabbyML/tabby) |
| <img src="https://github.com/stackblitz-labs.png?size=64" width="20" height="20"> | **[bolt.diy](https://github.com/stackblitz-labs/bolt.diy)** | Prompt, run and edit full-stack web apps in the browser, any LLM. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/stackblitz-labs/bolt.diy?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/stackblitz-labs/bolt.diy) |
| <img src="https://www.google.com/s2/favicons?domain=repomix.com&sz=64" width="20" height="20"> | **[Repomix](https://repomix.com)** | Pack a whole repository into one AI-friendly file. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/yamadashy/repomix?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/yamadashy/repomix) |
| <img src="https://www.google.com/s2/favicons?domain=gitingest.com&sz=64" width="20" height="20"> | **[Gitingest](https://gitingest.com)** | Turn any GitHub repo into a prompt-ready text digest. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/coderamp-labs/gitingest?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/coderamp-labs/gitingest) |
| <img src="https://github.com/charmbracelet.png?size=64" width="20" height="20"> | **[Crush](https://github.com/charmbracelet/crush)** | Glamorous terminal AI coding agent from Charm. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/charmbracelet/crush?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/charmbracelet/crush) |
| <img src="https://github.com/anthropics.png?size=64" width="20" height="20"> | **[Claude Code Action](https://github.com/anthropics/claude-code-action)** | Run Claude Code in GitHub Actions to review PRs and fix issues. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/anthropics/claude-code-action?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/anthropics/claude-code-action) |
| <img src="https://www.google.com/s2/favicons?domain=www.omniroute.online&sz=64" width="20" height="20"> | **[OmniRoute](https://www.omniroute.online/)** | MIT-licensed unified AI proxy routing requests across 375 model providers. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/cheaper-inference/OmniRoute?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/cheaper-inference/OmniRoute) |
| <img src="https://github.com/asgeirtj.png?size=64" width="20" height="20"> | **[System Prompts Leaks](https://github.com/asgeirtj/system_prompts_leaks)** | Documented system prompts from Anthropic Claude, OpenAI ChatGPT, Gemini, and Cursor. | ![Free](https://img.shields.io/badge/Free-0969da?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/asgeirtj/system_prompts_leaks?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/asgeirtj/system_prompts_leaks) |
| <img src="https://github.com/Alishahryar1.png?size=64" width="20" height="20"> | **[Free Claude Code](https://github.com/Alishahryar1/free-claude-code)** | Setup and routing guide to use Claude Code and agent CLIs with free token providers. | ![Free](https://img.shields.io/badge/Free-0969da?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/Alishahryar1/free-claude-code?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/Alishahryar1/free-claude-code) |
| <img src="https://www.google.com/s2/favicons?domain=open-codereview.ai&sz=64" width="20" height="20"> | **[Open Code Review](https://open-codereview.ai)** | Automated code review engine that inspects pull requests for security and quality. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/alibaba/open-code-review?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/alibaba/open-code-review) |
| <img src="https://github.com/deepseek-ai.png?size=64" width="20" height="20"> | **[DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness)** | Modular agent execution harness and plugin framework for deep reasoning models. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/deepseek-ai/deepseek-harness?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/deepseek-ai/deepseek-harness) |
| <img src="https://github.com/alibaba.png?size=64" width="20" height="20"> | **[Open Code Review](https://github.com/alibaba/open-code-review)** | Hybrid automated code review engine pairing static rules with LLM agents. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/alibaba/open-code-review?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/alibaba/open-code-review) |
| <img src="https://github.com/volcengine.png?size=64" width="20" height="20"> | **[OpenViking](https://github.com/volcengine/OpenViking)** | Self-evolving context database and persistent memory engine for AI coding agents. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/volcengine/OpenViking?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/volcengine/OpenViking) |
| <img src="https://github.com/rohitg00.png?size=64" width="20" height="20"> | **[AgentMemory](https://github.com/rohitg00/agentmemory)** | Persistent memory framework for AI coding agents benchmarked against long contexts. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/rohitg00/agentmemory?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/rohitg00/agentmemory) |
| <img src="https://github.com/kunchenguid.png?size=64" width="20" height="20"> | **[FirstMate](https://github.com/kunchenguid/firstmate)** | Multi-agent autonomous shipping framework coordinating specialized coding subagents. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/kunchenguid/firstmate?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/kunchenguid/firstmate) |
| <img src="https://github.com/opensandbox-group.png?size=64" width="20" height="20"> | **[OpenSandbox](https://github.com/opensandbox-group/OpenSandbox)** 🏆 | Secure and lightweight sandbox runtime for autonomous AI coding agents. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/opensandbox-group/OpenSandbox?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/opensandbox-group/OpenSandbox) |
| <img src="https://github.com/NVIDIA.png?size=64" width="20" height="20"> | **[OpenShell](https://github.com/NVIDIA/OpenShell)** 🏆 | Safe, private runtime and sandbox for autonomous AI agent execution by NVIDIA. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/NVIDIA/OpenShell?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/NVIDIA/OpenShell) |
| <img src="https://github.com/elizaOS.png?size=64" width="20" height="20"> | **[Eliza](https://github.com/elizaOS/eliza)** 🏆 | Autonomous multi-agent operating system and framework for interactive agents. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/elizaOS/eliza?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/elizaOS/eliza) |
| <img src="https://github.com/agno-agi.png?size=64" width="20" height="20"> | **[Agno](https://github.com/agno-agi/agno)** | Lightweight framework for building multi-modal AI agents with memory and tools. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/agno-agi/agno?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/agno-agi/agno) |
| <img src="https://github.com/CopilotKit.png?size=64" width="20" height="20"> | **[CopilotKit](https://github.com/CopilotKit/CopilotKit)** | Open-source framework to embed custom AI copilots and in-app agent sidebars. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/CopilotKit/CopilotKit?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/CopilotKit/CopilotKit) |
| <img src="https://github.com/decolua.png?size=64" width="20" height="20"> | **[9Router](https://github.com/decolua/9router)** | Multi-provider routing gateway connecting Claude Code, Codex, and Cursor. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/decolua/9router?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/decolua/9router) |
| <img src="https://github.com/pingdotgg.png?size=64" width="20" height="20"> | **[T3 Code](https://github.com/pingdotgg/t3code)** | Full-stack web application scaffolding and agentic code generator by Theo. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/pingdotgg/t3code?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/pingdotgg/t3code) |
| <img src="https://www.google.com/s2/favicons?domain=cleanyour.tv&sz=64" width="20" height="20"> | **[Cleanyourtv](https://cleanyour.tv)** | Debloat any Android or Google TV over Wi-Fi and get an Apple TV-style home. | ![Free](https://img.shields.io/badge/Free-0969da?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/Gathin23/cleanyourtv?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/Gathin23/cleanyourtv) |

<p align="right"><a href="#top">↑ Back to top</a></p>

<a id="agent-skills"></a>

## 🧩 Claude & Agent Skills

> Drop-in skills and plugins that give Claude Code, Codex, Gemini CLI and Antigravity new abilities.<br>
> <sub>35 picks · 4 gold</sub>

| | Resource | Why it's gold | Type | GitHub |
| :-: | :--- | :--- | :-- | :-- |
| <img src="https://github.com/DietrichGebert.png?size=64" width="20" height="20"> | **[Ponytail](https://github.com/DietrichGebert/ponytail)** 🏆 | Makes your coding agent favor the simplest working solution and write less, leaner code. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/DietrichGebert/ponytail?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/DietrichGebert/ponytail) |
| <img src="https://github.com/obra.png?size=64" width="20" height="20"> | **[Superpowers](https://github.com/obra/superpowers)** 🏆 | Skills framework that gives agents a disciplined workflow of brainstorming, planning, TDD and review. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/obra/superpowers?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/obra/superpowers) |
| <img src="https://github.com/nextlevelbuilder.png?size=64" width="20" height="20"> | **[UI UX Pro Max Skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill)** 🏆 | Design-intelligence skill that helps AI coding agents build polished, professional UI. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/nextlevelbuilder/ui-ux-pro-max-skill?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) |
| <img src="https://github.com/anthropics.png?size=64" width="20" height="20"> | **[Anthropic Agent Skills](https://github.com/anthropics/skills)** | Official example skills for Claude covering documents, design and development. | ![Free](https://img.shields.io/badge/Free-0969da?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/anthropics/skills?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/anthropics/skills) |
| <img src="https://github.com/VoltAgent.png?size=64" width="20" height="20"> | **[awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills)** | 1,000+ agent skills for Claude Code, Codex, Cursor and other agents. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/VoltAgent/awesome-agent-skills?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/VoltAgent/awesome-agent-skills) |
| <img src="https://github.com/affaan-m.png?size=64" width="20" height="20"> | **[ECC](https://github.com/affaan-m/ECC)** | Agent harness optimization system with skills, memory, security checks and research-first workflows. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/affaan-m/ECC?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/affaan-m/ECC) |
| <img src="https://github.com/garrytan.png?size=64" width="20" height="20"> | **[gstack](https://github.com/garrytan/gstack)** | Garry Tan's Claude Code setup, with opinionated tools that act as CEO, designer, eng manager and QA. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/garrytan/gstack?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/garrytan/gstack) |
| <img src="https://github.com/addyosmani.png?size=64" width="20" height="20"> | **[Agent Skills by Addy Osmani](https://github.com/addyosmani/agent-skills)** | Production-grade engineering skills for AI coding agents. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/addyosmani/agent-skills?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/addyosmani/agent-skills) |
| <img src="https://github.com/anthropics.png?size=64" width="20" height="20"> | **[Claude Code Plugins (Official)](https://github.com/anthropics/claude-plugins-official)** | Anthropic-managed directory of high-quality Claude Code plugins. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/anthropics/claude-plugins-official?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/anthropics/claude-plugins-official) |
| <img src="https://github.com/Leonxlnx.png?size=64" width="20" height="20"> | **[Taste Skill](https://github.com/Leonxlnx/taste-skill)** | Gives coding agents design taste through art direction, reference images and a browser check. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/Leonxlnx/taste-skill?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/Leonxlnx/taste-skill) |
| <img src="https://github.com/Nutlope.png?size=64" width="20" height="20"> | **[Hallmark](https://github.com/Nutlope/hallmark)** | Anti-AI-slop design skill for Claude Code, Cursor and Codex. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/Nutlope/hallmark?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/Nutlope/hallmark) |
| <img src="https://github.com/thedotmack.png?size=64" width="20" height="20"> | **[claude-mem](https://github.com/thedotmack/claude-mem)** | Captures what your agent does and feeds the relevant context back into future sessions. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/thedotmack/claude-mem?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/thedotmack/claude-mem) |
| <img src="https://github.com/OthmanAdi.png?size=64" width="20" height="20"> | **[Planning with Files](https://github.com/OthmanAdi/planning-with-files)** | Persistent markdown plans that survive /clear and compaction during long-running agent tasks. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/OthmanAdi/planning-with-files?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/OthmanAdi/planning-with-files) |
| <img src="https://github.com/EveryInc.png?size=64" width="20" height="20"> | **[Compound Engineering](https://github.com/EveryInc/compound-engineering-plugin)** | Every's plan, build and review plugin, where each finished task makes the next one easier. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/EveryInc/compound-engineering-plugin?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/EveryInc/compound-engineering-plugin) |
| <img src="https://github.com/tt-a1i.png?size=64" width="20" height="20"> | **[Archify](https://github.com/tt-a1i/archify)** | Turns any idea, plan or codebase into an interactive diagram. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/tt-a1i/archify?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/tt-a1i/archify) |
| <img src="https://github.com/mvanhorn.png?size=64" width="20" height="20"> | **[last30days](https://github.com/mvanhorn/last30days-skill)** | Researches any topic across Reddit, X, YouTube, HN and the web, then writes a grounded summary. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/mvanhorn/last30days-skill?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/mvanhorn/last30days-skill) |
| <img src="https://github.com/blader.png?size=64" width="20" height="20"> | **[Humanizer](https://github.com/blader/humanizer)** | Removes the telltale signs of AI-generated writing from text. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/blader/humanizer?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/blader/humanizer) |
| <img src="https://github.com/coreyhaines31.png?size=64" width="20" height="20"> | **[Marketing Skills](https://github.com/coreyhaines31/marketingskills)** | Skills for CRO, copywriting, SEO, analytics and growth engineering. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/coreyhaines31/marketingskills?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/coreyhaines31/marketingskills) |
| <img src="https://github.com/K-Dense-AI.png?size=64" width="20" height="20"> | **[Scientific Agent Skills](https://github.com/K-Dense-AI/scientific-agent-skills)** | Ready-to-use skills and scientific databases for biology, chemistry, medicine and drug discovery. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/K-Dense-AI/scientific-agent-skills?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/K-Dense-AI/scientific-agent-skills) |
| <img src="https://github.com/kepano.png?size=64" width="20" height="20"> | **[Obsidian Skills](https://github.com/kepano/obsidian-skills)** | Skills from Obsidian's CEO that teach agents the Obsidian CLI and formats like Bases and JSON Canvas. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/kepano/obsidian-skills?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/kepano/obsidian-skills) |
| <img src="https://github.com/cloudflare.png?size=64" width="20" height="20"> | **[Security Audit Skill](https://github.com/cloudflare/security-audit-skill)** | Cloudflare's multi-phase security audit skill with independently verified, machine-readable findings. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/cloudflare/security-audit-skill?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/cloudflare/security-audit-skill) |
| <img src="https://github.com/vercel-labs.png?size=64" width="20" height="20"> | **[Vercel Agent Skills](https://github.com/vercel-labs/agent-skills)** | Vercel's official collection of agent skills. | ![Free](https://img.shields.io/badge/Free-0969da?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/vercel-labs/agent-skills?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/vercel-labs/agent-skills) |
| <img src="https://github.com/google.png?size=64" width="20" height="20"> | **[Google Skills](https://github.com/google/skills)** | Official agent skills for Google products and technologies. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/google/skills?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/google/skills) |
| <img src="https://github.com/wshobson.png?size=64" width="20" height="20"> | **[Agents Plugin Marketplace](https://github.com/wshobson/agents)** | Plugin marketplace of agents and skills for Claude Code, Codex, Cursor, Copilot and Antigravity. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/wshobson/agents?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/wshobson/agents) |
| <img src="https://github.com/VoltAgent.png?size=64" width="20" height="20"> | **[Claude Code Subagents](https://github.com/VoltAgent/awesome-claude-code-subagents)** | 100+ specialized subagents for Claude Code across many development use cases. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/VoltAgent/awesome-claude-code-subagents?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/VoltAgent/awesome-claude-code-subagents) |
| <img src="https://github.com/vercel-labs.png?size=64" width="20" height="20"> | **[skills CLI](https://github.com/vercel-labs/skills)** | Install and manage agent skills from the open ecosystem with npx skills. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/vercel-labs/skills?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/vercel-labs/skills) |
| <img src="https://github.com/NVIDIA.png?size=64" width="20" height="20"> | **[SkillSpector](https://github.com/NVIDIA/SkillSpector)** | Scans agent skills for prompt injection, data exfiltration and supply-chain risks before you install. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/NVIDIA/SkillSpector?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/NVIDIA/SkillSpector) |
| <img src="https://github.com/ComposioHQ.png?size=64" width="20" height="20"> | **[awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills)** | Curated list of Claude Skills, resources and tools. | ![Free](https://img.shields.io/badge/Free-0969da?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/ComposioHQ/awesome-claude-skills?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/ComposioHQ/awesome-claude-skills) |
| <img src="https://github.com/Panniantong.png?size=64" width="20" height="20"> | **[Agent Reach](https://github.com/Panniantong/Agent-Reach)** | Toolkit giving AI coding agents web and social scraping capabilities. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/Panniantong/Agent-Reach?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/Panniantong/Agent-Reach) |
| <img src="https://github.com/pbakaus.png?size=64" width="20" height="20"> | **[Impeccable](https://github.com/pbakaus/impeccable)** | Design vocabulary and editorial polish skill for AI coding agents. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/pbakaus/impeccable?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/pbakaus/impeccable) |
| <img src="https://github.com/cathrynlavery.png?size=64" width="20" height="20"> | **[Diagram Design](https://github.com/cathrynlavery/diagram-design)** | Editorial diagram design skill for Claude Code, Codex, and GitHub Copilot. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/cathrynlavery/diagram-design?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/cathrynlavery/diagram-design) |
| <img src="https://github.com/AgriciDaniel.png?size=64" width="20" height="20"> | **[Claude Ads](https://github.com/AgriciDaniel/claude-ads)** | Paid-media operations and ad management skill for Claude Code across 12 platforms. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/AgriciDaniel/claude-ads?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/AgriciDaniel/claude-ads) |
| <img src="https://github.com/mukul975.png?size=64" width="20" height="20"> | **[Anthropic Cybersecurity Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills)** 🏆 | 817 structured cybersecurity and penetration testing skills for AI coding agents. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/mukul975/Anthropic-Cybersecurity-Skills?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) |
| <img src="https://github.com/virgiliojr94.png?size=64" width="20" height="20"> | **[Book to Skill](https://github.com/virgiliojr94/book-to-skill)** | Turn any technical book PDF into an indexed Claude Code skill ready for queries. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/virgiliojr94/book-to-skill?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/virgiliojr94/book-to-skill) |
| <img src="https://github.com/ayghri.png?size=64" width="20" height="20"> | **[I Have ADHD](https://github.com/ayghri/i-have-adhd)** | Agent skill that keeps AI coding outputs concise, structured, and slop-free. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/ayghri/i-have-adhd?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/ayghri/i-have-adhd) |

<p align="right"><a href="#top">↑ Back to top</a></p>

<a id="mcp"></a>

## 🔌 MCP Servers

> Model Context Protocol servers that plug your AI agent into docs, browsers, GitHub, design files and databases.<br>
> <sub>21 picks · 4 gold</sub>

| | Resource | Why it's gold | Type | GitHub |
| :-: | :--- | :--- | :-- | :-- |
| <img src="https://github.com/modelcontextprotocol.png?size=64" width="20" height="20"> | **[MCP Reference Servers](https://github.com/modelcontextprotocol/servers)** 🏆 | Reference Model Context Protocol servers that connect AI agents to tools and data. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/modelcontextprotocol/servers?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/modelcontextprotocol/servers) |
| <img src="https://github.com/upstash.png?size=64" width="20" height="20"> | **[Context7](https://github.com/upstash/context7)** 🏆 | Feeds your agent up-to-date, version-specific library docs so it stops guessing APIs. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/upstash/context7?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/upstash/context7) |
| <img src="https://github.com/microsoft.png?size=64" width="20" height="20"> | **[Playwright MCP](https://github.com/microsoft/playwright-mcp)** 🏆 | Lets agents drive a real browser to test, click through and read web pages. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/microsoft/playwright-mcp?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/microsoft/playwright-mcp) |
| <img src="https://github.com/github.png?size=64" width="20" height="20"> | **[GitHub MCP Server](https://github.com/github/github-mcp-server)** | GitHub's official MCP server for issues, pull requests, code and Actions. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/github/github-mcp-server?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/github/github-mcp-server) |
| <img src="https://github.com/oraios.png?size=64" width="20" height="20"> | **[Serena](https://github.com/oraios/serena)** | Semantic code search and editing tools that work like an IDE for your agent. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/oraios/serena?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/oraios/serena) |
| <img src="https://github.com/GLips.png?size=64" width="20" height="20"> | **[Figma Context MCP](https://github.com/GLips/Figma-Context-MCP)** | Gives coding agents Figma layout data so they implement designs accurately. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/GLips/Figma-Context-MCP?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/GLips/Figma-Context-MCP) |
| <img src="https://github.com/googleapis.png?size=64" width="20" height="20"> | **[MCP Toolbox for Databases](https://github.com/googleapis/mcp-toolbox)** | Google's open-source MCP server for connecting agents to your databases. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/googleapis/mcp-toolbox?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/googleapis/mcp-toolbox) |
| <img src="https://github.com/PrefectHQ.png?size=64" width="20" height="20"> | **[FastMCP](https://github.com/PrefectHQ/fastmcp)** | The fast, Pythonic way to build MCP servers and clients. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/PrefectHQ/fastmcp?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/PrefectHQ/fastmcp) |
| <img src="https://github.com/modelcontextprotocol.png?size=64" width="20" height="20"> | **[MCP Inspector](https://github.com/modelcontextprotocol/inspector)** | Visual tool for testing and debugging MCP servers. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/modelcontextprotocol/inspector?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/modelcontextprotocol/inspector) |
| <img src="https://github.com/microsoft.png?size=64" width="20" height="20"> | **[MCP for Beginners](https://github.com/microsoft/mcp-for-beginners)** | Microsoft's free MCP curriculum with examples in Python, TypeScript, .NET, Java and Rust. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/microsoft/mcp-for-beginners?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/microsoft/mcp-for-beginners) |
| <img src="https://github.com/punkpeye.png?size=64" width="20" height="20"> | **[awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers)** | Large community directory of MCP servers, sorted by category. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/punkpeye/awesome-mcp-servers?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/punkpeye/awesome-mcp-servers) |
| <img src="https://github.com/ChromeDevTools.png?size=64" width="20" height="20"> | **[Chrome DevTools MCP](https://github.com/ChromeDevTools/chrome-devtools-mcp)** 🏆 | Let agents debug, profile and test pages in a live Chrome. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/ChromeDevTools/chrome-devtools-mcp?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/ChromeDevTools/chrome-devtools-mcp) |
| <img src="https://github.com/wonderwhy-er.png?size=64" width="20" height="20"> | **[Desktop Commander](https://github.com/wonderwhy-er/DesktopCommanderMCP)** | MCP server for terminal commands, file search and edits on your machine. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/wonderwhy-er/DesktopCommanderMCP?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/wonderwhy-er/DesktopCommanderMCP) |
| <img src="https://github.com/makenotion.png?size=64" width="20" height="20"> | **[Notion MCP Server](https://github.com/makenotion/notion-mcp-server)** | Official MCP server for the Notion API. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/makenotion/notion-mcp-server?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/makenotion/notion-mcp-server) |
| <img src="https://www.google.com/s2/favicons?domain=supabase.com&sz=64" width="20" height="20"> | **[Supabase MCP](https://supabase.com/mcp)** | Connect agents to your Supabase projects, tables and logs. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/supabase/mcp?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/supabase/mcp) |
| <img src="https://github.com/exa-labs.png?size=64" width="20" height="20"> | **[Exa MCP](https://github.com/exa-labs/exa-mcp-server)** | Real-time web search and crawling for agents via Exa. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/exa-labs/exa-mcp-server?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/exa-labs/exa-mcp-server) |
| <img src="https://github.com/firecrawl.png?size=64" width="20" height="20"> | **[Firecrawl MCP](https://github.com/firecrawl/firecrawl-mcp-server)** | Scrape, crawl and search the web from any MCP client. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/firecrawl/firecrawl-mcp-server?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/firecrawl/firecrawl-mcp-server) |
| <img src="https://github.com/ahujasid.png?size=64" width="20" height="20"> | **[Blender MCP](https://github.com/ahujasid/mcp-for-blender)** | Community plugin that lets Claude and other LLMs control Blender 3D. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/ahujasid/mcp-for-blender?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/ahujasid/mcp-for-blender) |
| <img src="https://github.com/modelcontextprotocol.png?size=64" width="20" height="20"> | **[MCP TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk)** | Official TypeScript SDK for building MCP servers and clients. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/modelcontextprotocol/typescript-sdk?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/modelcontextprotocol/typescript-sdk) |
| <img src="https://github.com/modelcontextprotocol.png?size=64" width="20" height="20"> | **[MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk)** | Official Python SDK for building MCP servers and clients. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/modelcontextprotocol/python-sdk?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/modelcontextprotocol/python-sdk) |
| <img src="https://www.google.com/s2/favicons?domain=worldmonitor.app&sz=64" width="20" height="20"> | **[WorldMonitor](https://worldmonitor.app)** | Real-time global intelligence dashboard with AI news aggregation and OSINT monitoring. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/koala73/worldmonitor?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/koala73/worldmonitor) |

<p align="right"><a href="#top">↑ Back to top</a></p>

<a id="design"></a>

## 🎨 Design & UI

> Icons, fonts, photos and design tools that look premium and cost nothing.<br>
> <sub>33 picks · 4 gold</sub>

| | Resource | Why it's gold | Type | GitHub |
| :-: | :--- | :--- | :-- | :-- |
| <img src="https://www.google.com/s2/favicons?domain=penpot.app&sz=64" width="20" height="20"> | **[Penpot](https://penpot.app)** 🏆 | Open-source design and prototyping tool, an alternative to Figma. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/penpot/penpot?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/penpot/penpot) |
| <img src="https://www.google.com/s2/favicons?domain=ui.shadcn.com&sz=64" width="20" height="20"> | **[shadcn/ui](https://ui.shadcn.com)** 🏆 | Beautiful, accessible React components you copy into your project. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/shadcn-ui/ui?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/shadcn-ui/ui) |
| <img src="https://www.google.com/s2/favicons?domain=tailwindcss.com&sz=64" width="20" height="20"> | **[Tailwind CSS](https://tailwindcss.com)** | Utility-first CSS framework for building any design without leaving your HTML. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/tailwindlabs/tailwindcss?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/tailwindlabs/tailwindcss) |
| <img src="https://www.google.com/s2/favicons?domain=excalidraw.com&sz=64" width="20" height="20"> | **[Excalidraw](https://excalidraw.com)** | Hand-drawn style whiteboard for diagrams and sketches. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/excalidraw/excalidraw?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/excalidraw/excalidraw) |
| <img src="https://www.google.com/s2/favicons?domain=inkscape.org&sz=64" width="20" height="20"> | **[Inkscape](https://inkscape.org)** | Professional vector graphics editor, an alternative to Illustrator. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) |  |
| <img src="https://www.google.com/s2/favicons?domain=www.gimp.org&sz=64" width="20" height="20"> | **[GIMP](https://www.gimp.org)** | Powerful raster image editor, an alternative to Photoshop. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) |  |
| <img src="https://www.google.com/s2/favicons?domain=krita.org&sz=64" width="20" height="20"> | **[Krita](https://krita.org)** | Digital painting app made by artists, for artists. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) |  |
| <img src="https://www.google.com/s2/favicons?domain=www.photopea.com&sz=64" width="20" height="20"> | **[Photopea](https://www.photopea.com)** | Photoshop-like image editor that runs in the browser. | ![Free](https://img.shields.io/badge/Free-0969da?style=flat-square) |  |
| <img src="https://www.google.com/s2/favicons?domain=lucide.dev&sz=64" width="20" height="20"> | **[Lucide](https://lucide.dev)** | Clean, consistent open-source icon set. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/lucide-icons/lucide?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/lucide-icons/lucide) |
| <img src="https://www.google.com/s2/favicons?domain=heroicons.com&sz=64" width="20" height="20"> | **[Heroicons](https://heroicons.com)** | Hand-crafted SVG icons from the makers of Tailwind CSS. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/tailwindlabs/heroicons?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/tailwindlabs/heroicons) |
| <img src="https://www.google.com/s2/favicons?domain=phosphoricons.com&sz=64" width="20" height="20"> | **[Phosphor Icons](https://phosphoricons.com)** | Flexible icon family with six weights, from thin to duotone. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) |  |
| <img src="https://www.google.com/s2/favicons?domain=fonts.google.com&sz=64" width="20" height="20"> | **[Google Fonts](https://fonts.google.com)** | Large library of free, openly licensed fonts. | ![Free](https://img.shields.io/badge/Free-0969da?style=flat-square) |  |
| <img src="https://www.google.com/s2/favicons?domain=undraw.co&sz=64" width="20" height="20"> | **[unDraw](https://undraw.co)** | Customizable illustrations with no attribution required. | ![Free](https://img.shields.io/badge/Free-0969da?style=flat-square) |  |
| <img src="https://www.google.com/s2/favicons?domain=unsplash.com&sz=64" width="20" height="20"> | **[Unsplash](https://unsplash.com)** | Free high-resolution photos for any project. | ![Free](https://img.shields.io/badge/Free-0969da?style=flat-square) |  |
| <img src="https://www.google.com/s2/favicons?domain=coolors.co&sz=64" width="20" height="20"> | **[Coolors](https://coolors.co)** | Generate and explore color palettes in seconds. | ![Free tier](https://img.shields.io/badge/Free%20tier-bf8700?style=flat-square) |  |
| <img src="https://www.google.com/s2/favicons?domain=www.realtimecolors.com&sz=64" width="20" height="20"> | **[Realtime Colors](https://www.realtimecolors.com)** | Preview your color palette and fonts on a real website layout instantly. | ![Free](https://img.shields.io/badge/Free-0969da?style=flat-square) |  |
| <img src="https://www.google.com/s2/favicons?domain=haikei.app&sz=64" width="20" height="20"> | **[Haikei](https://haikei.app)** | Generate unique SVG waves, blobs and backgrounds for your designs. | ![Free](https://img.shields.io/badge/Free-0969da?style=flat-square) |  |
| <img src="https://www.google.com/s2/favicons?domain=squoosh.app&sz=64" width="20" height="20"> | **[Squoosh](https://squoosh.app)** | Compress and convert images in the browser while comparing quality side by side. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/GoogleChromeLabs/squoosh?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/GoogleChromeLabs/squoosh) |
| <img src="https://www.google.com/s2/favicons?domain=tabler.io&sz=64" width="20" height="20"> | **[Tabler Icons](https://tabler.io/icons)** | Thousands of free, pixel-perfect MIT-licensed SVG icons. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/tabler/tabler-icons?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/tabler/tabler-icons) |
| <img src="https://www.google.com/s2/favicons?domain=iconify.design&sz=64" width="20" height="20"> | **[Iconify](https://iconify.design)** | 200,000+ open-source icons from 150+ sets in one framework. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/iconify/iconify?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/iconify/iconify) |
| <img src="https://www.google.com/s2/favicons?domain=www.radix-ui.com&sz=64" width="20" height="20"> | **[Radix Primitives](https://www.radix-ui.com)** | Unstyled, accessible React components for design systems. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/radix-ui/primitives?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/radix-ui/primitives) |
| <img src="https://www.google.com/s2/favicons?domain=daisyui.com&sz=64" width="20" height="20"> | **[daisyUI](https://daisyui.com)** | Component classes for Tailwind CSS: cleaner markup, themes built in. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/saadeghi/daisyui?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/saadeghi/daisyui) |
| <img src="https://www.google.com/s2/favicons?domain=motion.dev&sz=64" width="20" height="20"> | **[Motion](https://motion.dev)** | Production-grade animation library for React and JavaScript. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/motiondivision/motion?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/motiondivision/motion) |
| <img src="https://github.com/danielgatis.png?size=64" width="20" height="20"> | **[rembg](https://github.com/danielgatis/rembg)** | Remove image backgrounds locally with one command. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/danielgatis/rembg?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/danielgatis/rembg) |
| <img src="https://www.google.com/s2/favicons?domain=www.fontshare.com&sz=64" width="20" height="20"> | **[Fontshare](https://www.fontshare.com)** | Quality fonts from Indian Type Foundry, free for commercial use. | ![Free](https://img.shields.io/badge/Free-0969da?style=flat-square) |  |
| <img src="https://github.com/tldraw.png?size=64" width="20" height="20"> | **[tldraw](https://github.com/tldraw/tldraw)** 🏆 | Infinite canvas SDK and collaborative digital whiteboard for React applications. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/tldraw/tldraw?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/tldraw/tldraw) |
| <img src="https://github.com/excalidraw.png?size=64" width="20" height="20"> | **[Excalidraw](https://github.com/excalidraw/excalidraw)** 🏆 | Virtual collaborative whiteboard for sketching hand-drawn diagrams and wireframes. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/excalidraw/excalidraw?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/excalidraw/excalidraw) |
| <img src="https://github.com/nexu-io.png?size=64" width="20" height="20"> | **[Open Design](https://github.com/nexu-io/open-design)** | Collaborative local-first AI design agent workspace and canvas. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/nexu-io/open-design?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/nexu-io/open-design) |
| <img src="https://github.com/earthtojake.png?size=64" width="20" height="20"> | **[Text to CAD](https://github.com/earthtojake/text-to-cad)** | Generate physical 3D CAD models and mechanical parts from text descriptions. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/earthtojake/text-to-cad?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/earthtojake/text-to-cad) |
| <img src="https://github.com/oso95.png?size=64" width="20" height="20"> | **[Scroll World](https://github.com/oso95/scroll-world)** | Agent skill that turns any brand into an immersive scrollable 3D world. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/oso95/scroll-world?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/oso95/scroll-world) |
| <img src="https://github.com/software-mansion-labs.png?size=64" width="20" height="20"> | **[Goldie](https://github.com/software-mansion-labs/goldie)** | Agentic automated app store screenshot and preview asset generator. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/software-mansion-labs/goldie?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/software-mansion-labs/goldie) |
| <img src="https://github.com/alexgreensh.png?size=64" width="20" height="20"> | **[Anidoodle](https://github.com/alexgreensh/anidoodle)** | Art, animation, and interactive motion graphics written purely as code. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/alexgreensh/anidoodle?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/alexgreensh/anidoodle) |
| <img src="https://www.google.com/s2/favicons?domain=www.svgrepo.com&sz=64" width="20" height="20"> | **[SVG Repo](https://www.svgrepo.com)** | Search and download 500,000+ free vector SVG icons and illustrations with CC0 license. | ![Free](https://img.shields.io/badge/Free-0969da?style=flat-square) |  |

<p align="right"><a href="#top">↑ Back to top</a></p>

<a id="media"></a>

## 🎬 Video, Audio & Media

> Studio-grade editing, recording and stock media at zero cost.<br>
> <sub>31 picks · 5 gold</sub>

| | Resource | Why it's gold | Type | GitHub |
| :-: | :--- | :--- | :-- | :-- |
| <img src="https://www.google.com/s2/favicons?domain=www.blackmagicdesign.com&sz=64" width="20" height="20"> | **[DaVinci Resolve](https://www.blackmagicdesign.com/products/davinciresolve)** 🏆 | Hollywood-grade video editing and color grading, with a very capable free version. | ![Free](https://img.shields.io/badge/Free-0969da?style=flat-square) |  |
| <img src="https://www.google.com/s2/favicons?domain=obsproject.com&sz=64" width="20" height="20"> | **[OBS Studio](https://obsproject.com)** 🏆 | Screen recording and live streaming. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/obsproject/obs-studio?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/obsproject/obs-studio) |
| <img src="https://www.google.com/s2/favicons?domain=kdenlive.org&sz=64" width="20" height="20"> | **[Kdenlive](https://kdenlive.org)** | Full-featured open-source video editor for Linux, Windows and macOS. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) |  |
| <img src="https://www.google.com/s2/favicons?domain=shotcut.org&sz=64" width="20" height="20"> | **[Shotcut](https://shotcut.org)** | Simple cross-platform video editor that supports hundreds of formats. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/mltframework/shotcut?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/mltframework/shotcut) |
| <img src="https://www.google.com/s2/favicons?domain=www.audacityteam.org&sz=64" width="20" height="20"> | **[Audacity](https://www.audacityteam.org)** | Record and edit audio, from podcasts to voice-overs. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/audacity/audacity?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/audacity/audacity) |
| <img src="https://www.google.com/s2/favicons?domain=handbrake.fr&sz=64" width="20" height="20"> | **[HandBrake](https://handbrake.fr)** | Convert and compress videos to any format. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/HandBrake/HandBrake?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/HandBrake/HandBrake) |
| <img src="https://www.google.com/s2/favicons?domain=www.blender.org&sz=64" width="20" height="20"> | **[Blender](https://www.blender.org)** | Complete 3D suite for modeling, animation, rendering and video editing. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) |  |
| <img src="https://www.google.com/s2/favicons?domain=www.videolan.org&sz=64" width="20" height="20"> | **[VLC](https://www.videolan.org/vlc/)** | Media player that plays practically any file. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) |  |
| <img src="https://github.com/yt-dlp.png?size=64" width="20" height="20"> | **[yt-dlp](https://github.com/yt-dlp/yt-dlp)** | Command-line downloader for audio and video from thousands of sites. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/yt-dlp/yt-dlp?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/yt-dlp/yt-dlp) |
| <img src="https://www.google.com/s2/favicons?domain=www.canva.com&sz=64" width="20" height="20"> | **[Canva](https://www.canva.com)** | Drag-and-drop design for social posts, slides and thumbnails, with a strong free plan. | ![Free tier](https://img.shields.io/badge/Free%20tier-bf8700?style=flat-square) |  |
| <img src="https://www.google.com/s2/favicons?domain=www.pexels.com&sz=64" width="20" height="20"> | **[Pexels](https://www.pexels.com)** | Free stock photos and videos you can use without attribution. | ![Free](https://img.shields.io/badge/Free-0969da?style=flat-square) |  |
| <img src="https://www.google.com/s2/favicons?domain=freesound.org&sz=64" width="20" height="20"> | **[Freesound](https://freesound.org)** | Huge library of Creative Commons sound effects and samples. | ![Free](https://img.shields.io/badge/Free-0969da?style=flat-square) |  |
| <img src="https://www.google.com/s2/favicons?domain=ffmpeg.org&sz=64" width="20" height="20"> | **[FFmpeg](https://ffmpeg.org)** 🏆 | The Swiss Army knife for converting and editing audio and video. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/FFmpeg/FFmpeg?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/FFmpeg/FFmpeg) |
| <img src="https://www.google.com/s2/favicons?domain=immich.app&sz=64" width="20" height="20"> | **[Immich](https://immich.app)** 🏆 | Self-hosted Google Photos alternative with mobile backup. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/immich-app/immich?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/immich-app/immich) |
| <img src="https://www.google.com/s2/favicons?domain=jellyfin.org&sz=64" width="20" height="20"> | **[Jellyfin](https://jellyfin.org)** | Free media server to stream your movies, shows and music. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/jellyfin/jellyfin?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/jellyfin/jellyfin) |
| <img src="https://www.google.com/s2/favicons?domain=upscayl.org&sz=64" width="20" height="20"> | **[Upscayl](https://upscayl.org)** | Upscale images with AI on your own computer. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/upscayl/upscayl?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/upscayl/upscayl) |
| <img src="https://github.com/mifi.png?size=64" width="20" height="20"> | **[LosslessCut](https://github.com/mifi/lossless-cut)** | Cut and trim video and audio instantly without re-encoding. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/mifi/lossless-cut?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/mifi/lossless-cut) |
| <img src="https://www.google.com/s2/favicons?domain=newpipe.net&sz=64" width="20" height="20"> | **[NewPipe](https://newpipe.net)** | Lightweight YouTube client for Android without ads or tracking. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/TeamNewPipe/NewPipe?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/TeamNewPipe/NewPipe) |
| <img src="https://www.google.com/s2/favicons?domain=cobalt.tools&sz=64" width="20" height="20"> | **[cobalt](https://cobalt.tools)** | Save videos and audio from many sites with no ads or tracking. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/imputnet/cobalt?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/imputnet/cobalt) |
| <img src="https://github.com/OpenCut-app.png?size=64" width="20" height="20"> | **[OpenCut](https://github.com/OpenCut-app/OpenCut)** | Open-source CapCut alternative for video editing and timeline composition. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/OpenCut-app/OpenCut?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/OpenCut-app/OpenCut) |
| <img src="https://www.google.com/s2/favicons?domain=www.openmontage.video&sz=64" width="20" height="20"> | **[OpenMontage](https://www.openmontage.video/)** | Open-source video production pipeline coordinating TTS, image generation, and FFmpeg. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/calesthio/OpenMontage?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/calesthio/OpenMontage) |
| <img src="https://github.com/heygen-com.png?size=64" width="20" height="20"> | **[Hyperframes](https://github.com/heygen-com/hyperframes)** | Write HTML, CSS, and SVG code to render programmatic video for agent workflows. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/heygen-com/hyperframes?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/heygen-com/hyperframes) |
| <img src="https://github.com/zhouxiaoka.png?size=64" width="20" height="20"> | **[AutoClip](https://github.com/zhouxiaoka/autoclip)** | Desktop AI tool that slices long podcasts and interviews into captioned short clips. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/zhouxiaoka/autoclip?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/zhouxiaoka/autoclip) |
| <img src="https://github.com/DonkeyCut.png?size=64" width="20" height="20"> | **[DonkeyCut](https://github.com/DonkeyCut/Donkey)** | Open-source timeline video editor alternative to CapCut. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/DonkeyCut/Donkey?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/DonkeyCut/Donkey) |
| <img src="https://github.com/FreeTubeApp.png?size=64" width="20" height="20"> | **[FreeTube](https://github.com/FreeTubeApp/FreeTube)** | Privacy-focused open-source desktop YouTube player with no tracking or telemetry. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/FreeTubeApp/FreeTube?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/FreeTubeApp/FreeTube) |
| <img src="https://github.com/alyssaxuu.png?size=64" width="20" height="20"> | **[Screenity](https://github.com/alyssaxuu/screenity)** 🏆 | Privacy-friendly browser screen recorder and annotation tool with zero limits. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/alyssaxuu/screenity?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/alyssaxuu/screenity) |
| <img src="https://github.com/storytold.png?size=64" width="20" height="20"> | **[PhotoCraft](https://github.com/storytold/photocraft)** | Fast photo editor and image manipulation utility written from scratch in pure Rust. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/storytold/photocraft?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/storytold/photocraft) |
| <img src="https://github.com/WordPress.png?size=64" width="20" height="20"> | **[Openverse](https://github.com/WordPress/openverse)** | Search engine for over 700 million openly licensed images and audio tracks. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/WordPress/openverse?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/WordPress/openverse) |
| <img src="https://github.com/kaomei.png?size=64" width="20" height="20"> | **[Stickman Video Director](https://github.com/kaomei/stickman-video-director)** | Generate multi-style animated stickman explainer videos directly from scripts. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/kaomei/stickman-video-director?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/kaomei/stickman-video-director) |
| <img src="https://github.com/Anil-matcha.png?size=64" width="20" height="20"> | **[Open Generative AI](https://github.com/Anil-matcha/Open-Generative-AI)** | Open-source suite for generative video and image generation pipelines. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/Anil-matcha/Open-Generative-AI?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/Anil-matcha/Open-Generative-AI) |
| <img src="https://github.com/ATH-MaaS.png?size=64" width="20" height="20"> | **[Pixelle Video](https://github.com/ATH-MaaS/Pixelle-Video)** | Automated engine generating short-form videos with narration and visuals. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/ATH-MaaS/Pixelle-Video?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/ATH-MaaS/Pixelle-Video) |

<p align="right"><a href="#top">↑ Back to top</a></p>

<a id="productivity"></a>

## ⚡ Productivity & Everyday Apps

> Notes, office apps and utilities, mostly open-source alternatives to paid apps.<br>
> <sub>35 picks · 4 gold</sub>

| | Resource | Why it's gold | Type | GitHub |
| :-: | :--- | :--- | :-- | :-- |
| <img src="https://www.google.com/s2/favicons?domain=obsidian.md&sz=64" width="20" height="20"> | **[Obsidian](https://obsidian.md)** 🏆 | Local-first markdown notes with backlinks and a huge plugin ecosystem. | ![Free](https://img.shields.io/badge/Free-0969da?style=flat-square) |  |
| <img src="https://www.google.com/s2/favicons?domain=localsend.org&sz=64" width="20" height="20"> | **[LocalSend](https://localsend.org)** 🏆 | Share files between nearby devices with no internet or account. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/localsend/localsend?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/localsend/localsend) |
| <img src="https://www.google.com/s2/favicons?domain=logseq.com&sz=64" width="20" height="20"> | **[Logseq](https://logseq.com)** | Open-source outliner for notes, journals and knowledge graphs. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/logseq/logseq?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/logseq/logseq) |
| <img src="https://www.google.com/s2/favicons?domain=joplinapp.org&sz=64" width="20" height="20"> | **[Joplin](https://joplinapp.org)** | Open-source note app with end-to-end encrypted sync. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/laurent22/joplin?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/laurent22/joplin) |
| <img src="https://www.google.com/s2/favicons?domain=appflowy.io&sz=64" width="20" height="20"> | **[AppFlowy](https://appflowy.io)** | Open-source alternative to Notion that you can self-host. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/AppFlowy-IO/AppFlowy?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/AppFlowy-IO/AppFlowy) |
| <img src="https://www.google.com/s2/favicons?domain=super-productivity.com&sz=64" width="20" height="20"> | **[Super Productivity](https://super-productivity.com)** | To-do list with time tracking, timeboxing and Jira/GitHub integration. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/super-productivity/super-productivity?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/super-productivity/super-productivity) |
| <img src="https://www.google.com/s2/favicons?domain=www.libreoffice.org&sz=64" width="20" height="20"> | **[LibreOffice](https://www.libreoffice.org)** | Full office suite for documents, spreadsheets and slides. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) |  |
| <img src="https://www.google.com/s2/favicons?domain=www.thunderbird.net&sz=64" width="20" height="20"> | **[Thunderbird](https://www.thunderbird.net)** | Email, calendar and contacts in one open-source app. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) |  |
| <img src="https://www.google.com/s2/favicons?domain=syncthing.net&sz=64" width="20" height="20"> | **[Syncthing](https://syncthing.net)** | Sync folders between your devices privately, with no cloud in between. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/syncthing/syncthing?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/syncthing/syncthing) |
| <img src="https://www.google.com/s2/favicons?domain=espanso.org&sz=64" width="20" height="20"> | **[Espanso](https://espanso.org)** | Cross-platform text expander that saves you from typing the same things again. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/espanso/espanso?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/espanso/espanso) |
| <img src="https://www.google.com/s2/favicons?domain=flameshot.org&sz=64" width="20" height="20"> | **[Flameshot](https://flameshot.org)** | Screenshot tool with instant annotation, arrows and blur. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/flameshot-org/flameshot?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/flameshot-org/flameshot) |
| <img src="https://www.google.com/s2/favicons?domain=getsharex.com&sz=64" width="20" height="20"> | **[ShareX](https://getsharex.com)** | Windows power tool for screenshots, screen recording and instant sharing. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/ShareX/ShareX?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/ShareX/ShareX) |
| <img src="https://www.google.com/s2/favicons?domain=rectangleapp.com&sz=64" width="20" height="20"> | **[Rectangle](https://rectangleapp.com)** | Snap and arrange macOS windows with keyboard shortcuts. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/rxhanson/Rectangle?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/rxhanson/Rectangle) |
| <img src="https://github.com/microsoft.png?size=64" width="20" height="20"> | **[PowerToys](https://github.com/microsoft/PowerToys)** | Microsoft's power-user utilities for Windows. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/microsoft/PowerToys?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/microsoft/PowerToys) |
| <img src="https://www.google.com/s2/favicons?domain=www.7-zip.org&sz=64" width="20" height="20"> | **[7-Zip](https://www.7-zip.org)** | File archiver with a high compression ratio that opens almost any archive. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) |  |
| <img src="https://www.google.com/s2/favicons?domain=affine.pro&sz=64" width="20" height="20"> | **[AFFiNE](https://affine.pro)** | Docs, whiteboards and databases in one, a Notion + Miro alternative. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/toeverything/AFFiNE?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/toeverything/AFFiNE) |
| <img src="https://www.google.com/s2/favicons?domain=anytype.io&sz=64" width="20" height="20"> | **[Anytype](https://anytype.io)** | Local-first, encrypted, everything app for notes and knowledge. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/anyproto/anytype-ts?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/anyproto/anytype-ts) |
| <img src="https://www.google.com/s2/favicons?domain=www.stirlingpdf.com&sz=64" width="20" height="20"> | **[Stirling-PDF](https://www.stirlingpdf.com)** 🏆 | Self-hosted toolkit to merge, split, sign, OCR and edit PDFs. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/Stirling-Tools/Stirling-PDF?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/Stirling-Tools/Stirling-PDF) |
| <img src="https://www.google.com/s2/favicons?domain=www.raycast.com&sz=64" width="20" height="20"> | **[Raycast](https://www.raycast.com)** | Fast launcher for Mac with extensions, clipboard history and snippets. | ![Free](https://img.shields.io/badge/Free-0969da?style=flat-square) |  |
| <img src="https://www.google.com/s2/favicons?domain=www.voidtools.com&sz=64" width="20" height="20"> | **[Everything](https://www.voidtools.com)** | Find any file on Windows instantly by name. | ![Free](https://img.shields.io/badge/Free-0969da?style=flat-square) |  |
| <img src="https://www.google.com/s2/favicons?domain=nextcloud.com&sz=64" width="20" height="20"> | **[Nextcloud](https://nextcloud.com)** | Self-hosted cloud for files, calendar, contacts and office. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/nextcloud/server?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/nextcloud/server) |
| <img src="https://www.google.com/s2/favicons?domain=puter.com&sz=64" width="20" height="20"> | **[Puter](https://puter.com)** | Open-source desktop operating system in the browser with personal cloud storage. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/HeyPuter/puter?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/HeyPuter/puter) |
| <img src="https://www.google.com/s2/favicons?domain=calibre-ebook.com&sz=64" width="20" height="20"> | **[Calibre](https://calibre-ebook.com)** | Manage, convert and read your entire ebook library, and sync it to any e-reader. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/kovidgoyal/calibre?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/kovidgoyal/calibre) |
| <img src="https://github.com/rustdesk.png?size=64" width="20" height="20"> | **[RustDesk](https://github.com/rustdesk/rustdesk)** | Open-source virtual and remote desktop infrastructure with full self-hosting. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/rustdesk/rustdesk?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/rustdesk/rustdesk) |
| <img src="https://github.com/HeyPuter.png?size=64" width="20" height="20"> | **[Puter](https://github.com/HeyPuter/puter)** | Open-source browser desktop operating system with personal cloud storage. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/HeyPuter/puter?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/HeyPuter/puter) |
| <img src="https://github.com/Zackriya-Solutions.png?size=64" width="20" height="20"> | **[Meetily](https://github.com/Zackriya-Solutions/meetily)** | Local-first open-source AI meeting transcription and automated note taker. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/Zackriya-Solutions/meetily?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/Zackriya-Solutions/meetily) |
| <img src="https://github.com/documenso.png?size=64" width="20" height="20"> | **[Documenso](https://github.com/documenso/documenso)** | Open-source digital signature alternative for document verification and signing. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/documenso/documenso?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/documenso/documenso) |
| <img src="https://github.com/zenhosta.png?size=64" width="20" height="20"> | **[9Drive](https://github.com/zenhosta/9drive)** | Self-hosted storage gateway web application connecting multiple cloud drives. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/zenhosta/9drive?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/zenhosta/9drive) |
| <img src="https://github.com/ajeetdsouza.png?size=64" width="20" height="20"> | **[zoxide](https://github.com/ajeetdsouza/zoxide)** 🏆 | Smarter cd command that learns navigation habits and jumps across folders fast. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/ajeetdsouza/zoxide?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/ajeetdsouza/zoxide) |
| <img src="https://github.com/Louis-CFM.png?size=64" width="20" height="20"> | **[Coucou](https://github.com/Louis-CFM/coucou)** | Mac notch and Lock Screen monitor for autonomous coding agents with one-click review. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/Louis-CFM/coucou?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/Louis-CFM/coucou) |
| <img src="https://github.com/pdfarranger.png?size=64" width="20" height="20"> | **[PDF Arranger](https://github.com/pdfarranger/pdfarranger)** | Lightweight utility to merge, split, rotate, crop, and reorder PDF pages. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/pdfarranger/pdfarranger?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/pdfarranger/pdfarranger) |
| <img src="https://github.com/apitable.png?size=64" width="20" height="20"> | **[APITable](https://github.com/apitable/apitable)** | API-oriented open-source low-code collaborative spreadsheet and database. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/apitable/apitable?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/apitable/apitable) |
| <img src="https://github.com/kalkman-code.png?size=64" width="20" height="20"> | **[Beamer](https://github.com/kalkman-code/beamer)** | Share one keyboard and mouse across Mac and Windows PC over local network. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/kalkman-code/beamer?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/kalkman-code/beamer) |
| <img src="https://github.com/DuarteSantos8.png?size=64" width="20" height="20"> | **[OpenGym](https://github.com/DuarteSantos8/openGym)** | Open-source privacy-focused workout, bodyweight, and gym routine tracker. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/DuarteSantos8/openGym?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/DuarteSantos8/openGym) |
| <img src="https://github.com/petergyang.png?size=64" width="20" height="20"> | **[No AI Slop](https://github.com/petergyang/no-ai-slop)** | CLI and prompt tool that strips 20+ patterns of AI filler and buzzwords from prose. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/petergyang/no-ai-slop?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/petergyang/no-ai-slop) |

<p align="right"><a href="#top">↑ Back to top</a></p>

<a id="research"></a>

## 🔬 Research & Writing

> Find papers, manage references and write better, for students and researchers.<br>
> <sub>19 picks · 3 gold</sub>

| | Resource | Why it's gold | Type | GitHub |
| :-: | :--- | :--- | :-- | :-- |
| <img src="https://www.google.com/s2/favicons?domain=www.zotero.org&sz=64" width="20" height="20"> | **[Zotero](https://www.zotero.org)** 🏆 | Collect, organize and cite research papers, with one-click capture from your browser. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/zotero/zotero?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/zotero/zotero) |
| <img src="https://www.google.com/s2/favicons?domain=www.overleaf.com&sz=64" width="20" height="20"> | **[Overleaf](https://www.overleaf.com)** 🏆 | Collaborative LaTeX editor in the browser for papers and theses. | ![Free tier](https://img.shields.io/badge/Free%20tier-bf8700?style=flat-square) |  |
| <img src="https://www.google.com/s2/favicons?domain=typst.app&sz=64" width="20" height="20"> | **[Typst](https://typst.app)** | Modern typesetting system that's much easier to learn than LaTeX. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/typst/typst?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/typst/typst) |
| <img src="https://www.google.com/s2/favicons?domain=arxiv.org&sz=64" width="20" height="20"> | **[arXiv](https://arxiv.org)** | Open-access archive of preprints in CS, physics, maths and more. | ![Free](https://img.shields.io/badge/Free-0969da?style=flat-square) |  |
| <img src="https://www.google.com/s2/favicons?domain=www.semanticscholar.org&sz=64" width="20" height="20"> | **[Semantic Scholar](https://www.semanticscholar.org)** | AI-powered search engine for academic papers. | ![Free](https://img.shields.io/badge/Free-0969da?style=flat-square) |  |
| <img src="https://www.google.com/s2/favicons?domain=scholar.google.com&sz=64" width="20" height="20"> | **[Google Scholar](https://scholar.google.com)** | Search scholarly literature and track citations. | ![Free](https://img.shields.io/badge/Free-0969da?style=flat-square) |  |
| <img src="https://www.google.com/s2/favicons?domain=www.connectedpapers.com&sz=64" width="20" height="20"> | **[Connected Papers](https://www.connectedpapers.com)** | Visual graph of papers related to the one you're reading. | ![Free tier](https://img.shields.io/badge/Free%20tier-bf8700?style=flat-square) |  |
| <img src="https://www.google.com/s2/favicons?domain=unpaywall.org&sz=64" width="20" height="20"> | **[Unpaywall](https://unpaywall.org)** | Find legal, free versions of paywalled research papers. | ![Free](https://img.shields.io/badge/Free-0969da?style=flat-square) |  |
| <img src="https://www.google.com/s2/favicons?domain=elicit.com&sz=64" width="20" height="20"> | **[Elicit](https://elicit.com)** | AI research assistant that finds papers and extracts key findings. | ![Free tier](https://img.shields.io/badge/Free%20tier-bf8700?style=flat-square) |  |
| <img src="https://www.google.com/s2/favicons?domain=languagetool.org&sz=64" width="20" height="20"> | **[LanguageTool](https://languagetool.org)** | Grammar and style checker for 30+ languages. | ![Free tier](https://img.shields.io/badge/Free%20tier-bf8700?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/languagetool-org/languagetool?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/languagetool-org/languagetool) |
| <img src="https://www.google.com/s2/favicons?domain=hemingwayapp.com&sz=64" width="20" height="20"> | **[Hemingway Editor](https://hemingwayapp.com)** | Highlights long, hard-to-read sentences so your writing gets clear and bold. | ![Free](https://img.shields.io/badge/Free-0969da?style=flat-square) |  |
| <img src="https://www.google.com/s2/favicons?domain=www.researchrabbit.ai&sz=64" width="20" height="20"> | **[ResearchRabbit](https://www.researchrabbit.ai)** | Discover related papers and authors through citation maps. | ![Free](https://img.shields.io/badge/Free-0969da?style=flat-square) |  |
| <img src="https://www.google.com/s2/favicons?domain=openalex.org&sz=64" width="20" height="20"> | **[OpenAlex](https://openalex.org)** | Free, open index of 250M+ scholarly works, authors and institutions. | ![Free](https://img.shields.io/badge/Free-0969da?style=flat-square) |  |
| <img src="https://www.google.com/s2/favicons?domain=core.ac.uk&sz=64" width="20" height="20"> | **[CORE](https://core.ac.uk)** | Millions of free full-text open access research papers. | ![Free](https://img.shields.io/badge/Free-0969da?style=flat-square) |  |
| <img src="https://www.google.com/s2/favicons?domain=www.jabref.org&sz=64" width="20" height="20"> | **[JabRef](https://www.jabref.org)** | Reference manager built around BibTeX and BibLaTeX. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/JabRef/jabref?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/JabRef/jabref) |
| <img src="https://www.google.com/s2/favicons?domain=quarto.org&sz=64" width="20" height="20"> | **[Quarto](https://quarto.org)** | Publish papers, reports and sites from Python, R and Markdown. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/quarto-dev/quarto-cli?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/quarto-dev/quarto-cli) |
| <img src="https://www.google.com/s2/favicons?domain=jupyter.org&sz=64" width="20" height="20"> | **[Jupyter](https://jupyter.org)** | Interactive notebooks for code, data and narrative. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/jupyterlab/jupyterlab?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/jupyterlab/jupyterlab) |
| <img src="https://www.google.com/s2/favicons?domain=colab.research.google.com&sz=64" width="20" height="20"> | **[Google Colab](https://colab.research.google.com)** 🏆 | Free Jupyter notebooks in the cloud with GPU access. | ![Free tier](https://img.shields.io/badge/Free%20tier-bf8700?style=flat-square) |  |
| <img src="https://github.com/lfnovo.png?size=64" width="20" height="20"> | **[Open Notebook](https://github.com/lfnovo/open-notebook)** | Open-source implementation of NotebookLM with local-first documents and audio. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/lfnovo/open-notebook?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/lfnovo/open-notebook) |

<p align="right"><a href="#top">↑ Back to top</a></p>

<a id="startups"></a>

## 🚀 Startups & Business

> Launch and run a product, with free credits, analytics, CRM and support tools.<br>
> <sub>28 picks · 3 gold</sub>

| | Resource | Why it's gold | Type | GitHub |
| :-: | :--- | :--- | :-- | :-- |
| <img src="https://www.google.com/s2/favicons?domain=www.startupschool.org&sz=64" width="20" height="20"> | **[YC Startup School](https://www.startupschool.org)** 🏆 | Y Combinator's free course on how to start a startup, plus co-founder matching. | ![Free](https://img.shields.io/badge/Free-0969da?style=flat-square) |  |
| <img src="https://www.google.com/s2/favicons?domain=www.ycombinator.com&sz=64" width="20" height="20"> | **[YC Library](https://www.ycombinator.com/library)** | Y Combinator's essays, videos and advice for founders. | ![Free](https://img.shields.io/badge/Free-0969da?style=flat-square) |  |
| <img src="https://www.google.com/s2/favicons?domain=aws.amazon.com&sz=64" width="20" height="20"> | **[AWS Activate](https://aws.amazon.com/activate/)** | AWS credits and support for early-stage startups. | ![Free](https://img.shields.io/badge/Free-0969da?style=flat-square) |  |
| <img src="https://www.google.com/s2/favicons?domain=cloud.google.com&sz=64" width="20" height="20"> | **[Google for Startups Cloud Program](https://cloud.google.com/startup)** | Google Cloud credits and technical support for startups. | ![Free](https://img.shields.io/badge/Free-0969da?style=flat-square) |  |
| <img src="https://www.google.com/s2/favicons?domain=posthog.com&sz=64" width="20" height="20"> | **[PostHog](https://posthog.com)** 🏆 | Open-source product analytics, session replay and feature flags with a big free tier. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/PostHog/posthog?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/PostHog/posthog) |
| <img src="https://www.google.com/s2/favicons?domain=umami.is&sz=64" width="20" height="20"> | **[Umami](https://umami.is)** | Simple, privacy-friendly website analytics, an alternative to Google Analytics. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/umami-software/umami?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/umami-software/umami) |
| <img src="https://www.google.com/s2/favicons?domain=listmonk.app&sz=64" width="20" height="20"> | **[Listmonk](https://listmonk.app)** | Self-hosted newsletter and mailing list manager. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/knadh/listmonk?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/knadh/listmonk) |
| <img src="https://www.google.com/s2/favicons?domain=www.chatwoot.com&sz=64" width="20" height="20"> | **[Chatwoot](https://www.chatwoot.com)** | Open-source customer support inbox for chat, email and social. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/chatwoot/chatwoot?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/chatwoot/chatwoot) |
| <img src="https://www.google.com/s2/favicons?domain=twenty.com&sz=64" width="20" height="20"> | **[Twenty](https://twenty.com)** | Modern open-source CRM, an alternative to Salesforce. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/twentyhq/twenty?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/twentyhq/twenty) |
| <img src="https://github.com/odoo.png?size=64" width="20" height="20"> | **[Odoo Community](https://github.com/odoo/odoo)** | Open-source ERP covering CRM, sales, inventory, accounting and website. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/odoo/odoo?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/odoo/odoo) |
| <img src="https://www.google.com/s2/favicons?domain=cal.diy&sz=64" width="20" height="20"> | **[Cal.diy](https://cal.diy)** | Open-source, self-hostable scheduling from the Cal.com team, a Calendly alternative. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/calcom/cal.diy?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/calcom/cal.diy) |
| <img src="https://www.google.com/s2/favicons?domain=plausible.io&sz=64" width="20" height="20"> | **[Plausible](https://plausible.io)** | Simple, privacy-friendly Google Analytics alternative. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/plausible/analytics?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/plausible/analytics) |
| <img src="https://www.google.com/s2/favicons?domain=documenso.com&sz=64" width="20" height="20"> | **[Documenso](https://documenso.com)** | Open-source DocuSign alternative for signing documents. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/documenso/documenso?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/documenso/documenso) |
| <img src="https://www.google.com/s2/favicons?domain=ghost.org&sz=64" width="20" height="20"> | **[Ghost](https://ghost.org)** | Publishing platform for blogs and paid newsletters. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/TryGhost/Ghost?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/TryGhost/Ghost) |
| <img src="https://www.google.com/s2/favicons?domain=plane.so&sz=64" width="20" height="20"> | **[Plane](https://plane.so)** | Project management for tasks, sprints and roadmaps, a Jira alternative. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/makeplane/plane?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/makeplane/plane) |
| <img src="https://www.google.com/s2/favicons?domain=formbricks.com&sz=64" width="20" height="20"> | **[Formbricks](https://formbricks.com)** | Open-source survey and experience management platform. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/formbricks/formbricks?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/formbricks/formbricks) |
| <img src="https://www.google.com/s2/favicons?domain=strapi.io&sz=64" width="20" height="20"> | **[Strapi](https://strapi.io)** | Leading open-source headless CMS in JavaScript and TypeScript. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/strapi/strapi?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/strapi/strapi) |
| <img src="https://www.google.com/s2/favicons?domain=medusajs.com&sz=64" width="20" height="20"> | **[Medusa](https://medusajs.com)** | Open-source commerce platform for building custom stores. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/medusajs/medusa?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/medusajs/medusa) |
| <img src="https://www.google.com/s2/favicons?domain=www.microsoft.com&sz=64" width="20" height="20"> | **[Microsoft for Startups](https://www.microsoft.com/en-us/startups)** | Free Azure credits and tools for early-stage founders. | ![Free](https://img.shields.io/badge/Free-0969da?style=flat-square) |  |
| <img src="https://github.com/ever-co.png?size=64" width="20" height="20"> | **[Ever Gauzy](https://github.com/ever-co/ever-gauzy)** | Open-source enterprise business management platform with ERP, CRM, and HRM. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/ever-co/ever-gauzy?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/ever-co/ever-gauzy) |
| <img src="https://github.com/melgarafael.png?size=64" width="20" height="20"> | **[Deskcomm CRM](https://github.com/melgarafael/DeskcommCRM)** | Self-hosted AI sales OS and CRM with native multi-agent chat integrations. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/melgarafael/DeskcommCRM?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/melgarafael/DeskcommCRM) |
| <img src="https://github.com/Fincept-Corporation.png?size=64" width="20" height="20"> | **[FinceptTerminal](https://github.com/Fincept-Corporation/FinceptTerminal)** 🏆 | Modern financial analytics terminal offering market data and investment research. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/Fincept-Corporation/FinceptTerminal?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/Fincept-Corporation/FinceptTerminal) |
| <img src="https://github.com/evershopcommerce.png?size=64" width="20" height="20"> | **[Evershop](https://github.com/evershopcommerce/evershop)** | Modern modular open-source TypeScript headless e-commerce platform. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/evershopcommerce/evershop?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/evershopcommerce/evershop) |
| <img src="https://github.com/store-craft.png?size=64" width="20" height="20"> | **[StoreCraft](https://github.com/store-craft/storecraft)** | Rapid headless e-commerce backend framework built with TypeScript and modular storage. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/store-craft/storecraft?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/store-craft/storecraft) |
| <img src="https://github.com/every-app.png?size=64" width="20" height="20"> | **[Open SEO](https://github.com/every-app/open-seo)** | Open-source keyword tracking and backlink intelligence alternative to Semrush. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/every-app/open-seo?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/every-app/open-seo) |
| <img src="https://github.com/nateherkai.png?size=64" width="20" height="20"> | **[Roast Room](https://github.com/nateherkai/roast-room)** | Live business decision debate simulator with 7 AI advisors in Claude Code. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/nateherkai/roast-room?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/nateherkai/roast-room) |
| <img src="https://github.com/bagisto.png?size=64" width="20" height="20"> | **[Bagisto Mobile App](https://github.com/bagisto/opensource-ecommerce-mobile-app)** | Open-source Flutter mobile e-commerce application for the Bagisto ecosystem. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/bagisto/opensource-ecommerce-mobile-app?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/bagisto/opensource-ecommerce-mobile-app) |
| <img src="https://github.com/HeyPuter.png?size=64" width="20" height="20"> | **[Everything](https://github.com/HeyPuter/everything)** | We're rebuilding and open-sourcing the world’s software from scratch. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/HeyPuter/everything?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/HeyPuter/everything) |

<p align="right"><a href="#top">↑ Back to top</a></p>

<a id="privacy-security"></a>

## 🔒 Privacy & Security

> Protect your accounts, data and devices, and learn security hands-on.<br>
> <sub>29 picks · 3 gold</sub>

| | Resource | Why it's gold | Type | GitHub |
| :-: | :--- | :--- | :-- | :-- |
| <img src="https://www.google.com/s2/favicons?domain=bitwarden.com&sz=64" width="20" height="20"> | **[Bitwarden](https://bitwarden.com)** 🏆 | Open-source password manager with a free plan on every device. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/bitwarden/clients?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/bitwarden/clients) |
| <img src="https://github.com/gorhill.png?size=64" width="20" height="20"> | **[uBlock Origin](https://github.com/gorhill/uBlock)** 🏆 | Efficient, lightweight ad and tracker blocker. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/gorhill/uBlock?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/gorhill/uBlock) |
| <img src="https://www.google.com/s2/favicons?domain=www.mozilla.org&sz=64" width="20" height="20"> | **[Firefox](https://www.mozilla.org/firefox/)** | Independent open-source browser with strong tracking protection. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) |  |
| <img src="https://www.google.com/s2/favicons?domain=signal.org&sz=64" width="20" height="20"> | **[Signal](https://signal.org)** | End-to-end encrypted messaging and calls. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) |  |
| <img src="https://www.google.com/s2/favicons?domain=keepassxc.org&sz=64" width="20" height="20"> | **[KeePassXC](https://keepassxc.org)** | Offline open-source password manager. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/keepassxreboot/keepassxc?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/keepassxreboot/keepassxc) |
| <img src="https://www.google.com/s2/favicons?domain=ente.io&sz=64" width="20" height="20"> | **[Ente Auth](https://ente.io/auth/)** | Open-source 2FA authenticator with end-to-end encrypted backups. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/ente/ente?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/ente/ente) |
| <img src="https://www.google.com/s2/favicons?domain=getaegis.app&sz=64" width="20" height="20"> | **[Aegis Authenticator](https://getaegis.app)** | Secure open-source 2FA app for Android with encrypted backups. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/beemdevelopment/Aegis?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/beemdevelopment/Aegis) |
| <img src="https://www.google.com/s2/favicons?domain=www.veracrypt.fr&sz=64" width="20" height="20"> | **[VeraCrypt](https://www.veracrypt.fr)** | Encrypt whole drives or create encrypted containers for sensitive files. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/veracrypt/VeraCrypt?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/veracrypt/VeraCrypt) |
| <img src="https://www.google.com/s2/favicons?domain=tailscale.com&sz=64" width="20" height="20"> | **[Tailscale](https://tailscale.com)** | Zero-config private network between your devices, free for personal use. | ![Free tier](https://img.shields.io/badge/Free%20tier-bf8700?style=flat-square) |  |
| <img src="https://www.google.com/s2/favicons?domain=proton.me&sz=64" width="20" height="20"> | **[Proton Mail](https://proton.me/mail)** | Encrypted email with a free plan. | ![Free tier](https://img.shields.io/badge/Free%20tier-bf8700?style=flat-square) |  |
| <img src="https://www.google.com/s2/favicons?domain=haveibeenpwned.com&sz=64" width="20" height="20"> | **[Have I Been Pwned](https://haveibeenpwned.com)** | Check whether your email address appeared in a data breach. | ![Free](https://img.shields.io/badge/Free-0969da?style=flat-square) |  |
| <img src="https://www.google.com/s2/favicons?domain=www.privacyguides.org&sz=64" width="20" height="20"> | **[Privacy Guides](https://www.privacyguides.org)** | Independent, non-profit recommendations for privacy tools. | ![Free](https://img.shields.io/badge/Free-0969da?style=flat-square) |  |
| <img src="https://www.google.com/s2/favicons?domain=owasp.org&sz=64" width="20" height="20"> | **[OWASP Top 10](https://owasp.org/www-project-top-ten/)** | The most critical web application security risks every developer should know. | ![Free](https://img.shields.io/badge/Free-0969da?style=flat-square) |  |
| <img src="https://www.google.com/s2/favicons?domain=tryhackme.com&sz=64" width="20" height="20"> | **[TryHackMe](https://tryhackme.com)** | Learn cybersecurity through guided, hands-on labs in the browser. | ![Free tier](https://img.shields.io/badge/Free%20tier-bf8700?style=flat-square) |  |
| <img src="https://www.google.com/s2/favicons?domain=overthewire.org&sz=64" width="20" height="20"> | **[OverTheWire Wargames](https://overthewire.org/wargames/)** | Learn Linux and security concepts through progressively harder games. | ![Free](https://img.shields.io/badge/Free-0969da?style=flat-square) |  |
| <img src="https://github.com/trimstray.png?size=64" width="20" height="20"> | **[The Book of Secret Knowledge](https://github.com/trimstray/the-book-of-secret-knowledge)** | Huge collection of sysadmin, security and command-line cheatsheets. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/trimstray/the-book-of-secret-knowledge?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/trimstray/the-book-of-secret-knowledge) |
| <img src="https://www.google.com/s2/favicons?domain=www.wireshark.org&sz=64" width="20" height="20"> | **[Wireshark](https://www.wireshark.org)** | The standard tool to capture and inspect network traffic. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/wireshark/wireshark?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/wireshark/wireshark) |
| <img src="https://www.google.com/s2/favicons?domain=pi-hole.net&sz=64" width="20" height="20"> | **[Pi-hole](https://pi-hole.net)** | Network-wide ad and tracker blocking via your own DNS. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/pi-hole/pi-hole?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/pi-hole/pi-hole) |
| <img src="https://github.com/dani-garcia.png?size=64" width="20" height="20"> | **[Vaultwarden](https://github.com/dani-garcia/vaultwarden)** | Lightweight self-hosted server compatible with Bitwarden apps. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/dani-garcia/vaultwarden?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/dani-garcia/vaultwarden) |
| <img src="https://www.google.com/s2/favicons?domain=portswigger.net&sz=64" width="20" height="20"> | **[PortSwigger Web Security Academy](https://portswigger.net/web-security)** 🏆 | Free hands-on labs for every major web vulnerability. | ![Free](https://img.shields.io/badge/Free-0969da?style=flat-square) |  |
| <img src="https://www.google.com/s2/favicons?domain=gchq.github.io&sz=64" width="20" height="20"> | **[CyberChef](https://gchq.github.io/CyberChef/)** | The cyber Swiss Army knife for encoding, decoding and analysis. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/gchq/CyberChef?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/gchq/CyberChef) |
| <img src="https://www.google.com/s2/favicons?domain=ghidra-sre.org&sz=64" width="20" height="20"> | **[Ghidra](https://ghidra-sre.org)** | NSA's software reverse engineering suite. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/NationalSecurityAgency/ghidra?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/NationalSecurityAgency/ghidra) |
| <img src="https://github.com/swisskyrepo.png?size=64" width="20" height="20"> | **[PayloadsAllTheThings](https://github.com/swisskyrepo/PayloadsAllTheThings)** | Payloads and bypasses for web application security testing. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/swisskyrepo/PayloadsAllTheThings?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/swisskyrepo/PayloadsAllTheThings) |
| <img src="https://github.com/projectdiscovery.png?size=64" width="20" height="20"> | **[Nuclei](https://github.com/projectdiscovery/nuclei)** | Fast, template-based vulnerability scanner. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/projectdiscovery/nuclei?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/projectdiscovery/nuclei) |
| <img src="https://www.google.com/s2/favicons?domain=Cognitum.One&sz=64" width="20" height="20"> | **[RuView](https://Cognitum.One/RuView)** | Turns commodity WiFi signals into real-time spatial intelligence and presence detection. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/ruvnet/RuView?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/ruvnet/RuView) |
| <img src="https://www.google.com/s2/favicons?domain=www.strix.ai&sz=64" width="20" height="20"> | **[Strix](https://www.strix.ai/)** | Open-source autonomous AI penetration testing tool that finds application vulnerabilities. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/usestrix/strix?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/usestrix/strix) |
| <img src="https://www.google.com/s2/favicons?domain=maigret.app&sz=64" width="20" height="20"> | **[Maigret](https://maigret.app/gh)** | OSINT investigation tool that collects dossiers on usernames across 6,000 websites. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/soxoj/maigret?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/soxoj/maigret) |
| <img src="https://github.com/CloakHQ.png?size=64" width="20" height="20"> | **[CloakBrowser](https://github.com/CloakHQ/CloakBrowser)** | Anti-detect Chromium browser engine built to pass advanced bot mitigation checks. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/CloakHQ/CloakBrowser?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/CloakHQ/CloakBrowser) |
| <img src="https://github.com/WebBreacher.png?size=64" width="20" height="20"> | **[WhatsMyName](https://github.com/WebBreacher/WhatsMyName)** | OSINT username reconnaissance tool searching across 700+ websites and platforms. | ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) | [![GitHub stars](https://img.shields.io/github/stars/WebBreacher/WhatsMyName?style=flat-square&logo=github&label=&labelColor=1f2328&color=d4af37)](https://github.com/WebBreacher/WhatsMyName) |

<p align="right"><a href="#top">↑ Back to top</a></p>

---

<a id="how-it-works"></a>

## ⚙️ How GoldList Stays Gold

Every change goes through an automated pipeline, so the catalog stays accurate and fresh.

```mermaid
flowchart LR
    A["💡 Suggestion<br/>issue form or PR"] --> B["🤖 CodeRabbit<br/>AI review"]
    A --> C["✅ Validation<br/>schema · duplicates · links"]
    B --> D{"Approved?"}
    C --> D
    D -- yes --> E["🔀 Auto-merge"]
    E --> F["📄 README + JSON API<br/>regenerated"]
    F --> G["🔍 Weekly<br/>dead-link sweep"]
```

- **Single source of truth:** every entry lives in [`data/*.yaml`](data/). This README, the [JSON API](api/goldlist.json), and the suggestion form are generated from it.
- **AI review:** [CodeRabbit](https://coderabbit.ai) reviews every pull request against the [quality bar](CONTRIBUTING.md#the-bar).
- **Strict validation:** CI rejects duplicates, broken links, missing fields, and over-long descriptions.
- **Self-cleaning:** a weekly job checks every link and opens an issue if anything breaks.
- **Interactive web directory:** [goldlist-seven.vercel.app](https://goldlist-seven.vercel.app/) is rebuilt from the same data on every change.
- **AI agent reference memory:** indexed in the [XERJ Corpus Hub](https://hub.xerj.org/corpus/usmanghias--goldlist) as a verified, pinned reference corpus for AI coding agents.

---

<a id="contributing"></a>

## 🤝 Contributing

Know a resource that deserves a spot?

- **30 seconds:** [suggest it with the form](https://github.com/UsmanGhias/goldlist/issues/new?template=suggest.yml). Once a maintainer labels it `accepted`, a bot adds it.
- **Pull request:** add it to [`data/`](data/) and open a PR. CodeRabbit reviews it and it merges automatically when approved. See [CONTRIBUTING.md](CONTRIBUTING.md).

The bar is high on purpose: **free or open source, actively maintained, and clearly the best (or close to it) at what it does.**

---

## 📈 Star History

<a href="https://star-history.com/#UsmanGhias/goldlist&Date">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=UsmanGhias/goldlist&type=Date&theme=dark">
    <img src="https://api.star-history.com/svg?repos=UsmanGhias/goldlist&type=Date" alt="Star History Chart" width="600">
  </picture>
</a>

---

<div align="center">

**If GoldList saved you time, [give it a ⭐](https://github.com/UsmanGhias/goldlist) and share it with someone who needs it.**

<br>

<sub>Curated by <a href="https://usmanghias.co.uk">Usman Ghias</a>. Released under <a href="LICENSE">CC0 1.0 Universal</a>: public domain, so copy it, share it, build on it.<br>
This README is generated from <code>data/*.yaml</code> by <code>scripts/build.py</code>. Edit the data, not this file.</sub>

<br>

<p><a href="#top">↑ Back to top</a></p>

</div>
