<a id="top"></a>

<div align="center">

<img src="assets/banner.svg" alt="GoldList: only the gold" width="100%">

<br><br>

<code>// the catalogue, today</code>

<h3>Only the gold. Everything else is noise.</h3>

<p>
  <b>{{TOTAL}} hand-picked free and open-source resources</b> for finding jobs, AI coding, winning scholarships,<br>
  learning, building products, and staying secure. Sorted across {{CATEGORY_COUNT}} categories and verified every week.
</p>

[![Entries](https://img.shields.io/badge/entries-{{TOTAL}}-d4af37?style=flat-square&labelColor=24292f)](#contents)
[![Gold picks](https://img.shields.io/badge/gold_picks-{{GOLD_COUNT}}-d4af37?style=flat-square&labelColor=24292f)](#gold-picks)
[![Open source](https://img.shields.io/badge/open_source-{{OPEN_SOURCE_COUNT}}-2ea44f?style=flat-square&labelColor=24292f)](#contents)
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
<td align="center" width="25%"><h3>{{TOTAL}}</h3><sub>verified resources</sub></td>
<td align="center" width="25%"><h3>{{CATEGORY_COUNT}}</h3><sub>curated topics</sub></td>
<td align="center" width="25%"><h3>{{OPEN_SOURCE_COUNT}}</h3><sub>open-source repos</sub></td>
<td align="center" width="25%"><h3>{{GOLD_COUNT}}</h3><sub>elite gold picks</sub></td>
</tr>
</table>

<br>

{{NAV}}

<br><br>

**[🔎 Search &amp; filter all {{TOTAL}} resources on the live website →](https://goldlist-seven.vercel.app/)**

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

{{GOLD_PICKS}}

{{RECENT}}
<a id="contents"></a>

## 📑 Catalogue Contents

{{TOC}}

**Legend:** ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) source code is public · ![Free](https://img.shields.io/badge/Free-0969da?style=flat-square) free to use · ![Free tier](https://img.shields.io/badge/Free%20tier-bf8700?style=flat-square) generous free tier, paid upgrades · 🏆 gold pick

---

{{CATEGORIES}}

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
