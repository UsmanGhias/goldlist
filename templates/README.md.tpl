<a id="top"></a>

<div align="center">

<img src="assets/banner.svg" alt="GoldList: only the gold" width="100%">

<h3>Only the gold. Everything else is noise.</h3>

<p><b>{{TOTAL}} hand-picked free &amp; open-source resources</b> for finding jobs, winning scholarships, learning,<br>
building, designing and staying safe, sorted into {{CATEGORY_COUNT}} categories and link-checked every week.</p>

[![Entries](https://img.shields.io/badge/entries-{{TOTAL}}-d4af37?style=for-the-badge&labelColor=1f2328)](#contents)
[![Gold picks](https://img.shields.io/badge/gold_picks-{{GOLD_COUNT}}-d4af37?style=for-the-badge&labelColor=1f2328)](#gold-picks)
[![Open source](https://img.shields.io/badge/open_source-{{OPEN_SOURCE_COUNT}}-2ea44f?style=for-the-badge&labelColor=1f2328)](#contents)
<br>
[![Links](https://img.shields.io/github/actions/workflow/status/UsmanGhias/goldlist/links.yml?label=links&style=flat-square)](https://github.com/UsmanGhias/goldlist/actions/workflows/links.yml)
[![Last commit](https://img.shields.io/github/last-commit/UsmanGhias/goldlist?style=flat-square)](https://github.com/UsmanGhias/goldlist/commits/main)
[![PRs welcome](https://img.shields.io/badge/PRs-welcome-brightgreen?style=flat-square)](CONTRIBUTING.md)
[![AI reviewed](https://img.shields.io/badge/PRs_reviewed_by-CodeRabbit-ff570a?style=flat-square)](#how-it-works)
[![License: CC0](https://img.shields.io/badge/license-CC0-lightgrey?style=flat-square)](LICENSE)

{{NAV}}

<sub>⭐ <b>Star this repo</b> to keep it one click away. New gold is added every week.</sub>

</div>

---

## Why GoldList?

You've bookmarked hundreds of "useful tools" and can't find any of them when you need one. Giant awesome-lists have **thousands** of links and no opinion. GoldList is the opposite:

<table>
<tr>
<td width="25%" valign="top"><b>🏆 Curated, not collected</b><br><sub>Every entry earns its place. Categories stay short, so you only see what's worth your time.</sub></td>
<td width="25%" valign="top"><b>🧭 One place for everything</b><br><sub>Jobs, scholarships, courses, dev tools, AI, design, media, research and privacy, all in one list.</sub></td>
<td width="25%" valign="top"><b>✅ Always alive</b><br><sub>A bot checks every link weekly. Every change is reviewed by AI and validated before it merges.</sub></td>
<td width="25%" valign="top"><b>🏷️ Honest labels</b><br><sub>Open source, fully free, or free tier, plus live GitHub stars, so you know exactly what you're getting.</sub></td>
</tr>
</table>

<a id="start-here"></a>

## 🎯 Start Here

| If you are… | Go straight to |
| :--- | :--- |
| 💼 **Hunting for a job** | [Jobs](#jobs) → [Career & Interviews](#career) → [AI Coding](#ai-coding) |
| 🎓 **A student** | [Students](#students) → [Scholarships](#scholarships) → [Learning](#learning) |
| 🌍 **Planning a funded master's or PhD** | [Scholarships](#scholarships) → [Research & Writing](#research) |
| 💻 **Learning to code** | [Learning](#learning) → [Dev Tools](#dev-tools) → [AI Coding](#ai-coding) |
| 🏗️ **Building a product** | [Dev Tools](#dev-tools) → [Startups](#startups) → [Design](#design) |
| 🤖 **Into AI** | [AI Tools](#ai-tools) → [AI Coding](#ai-coding) → [Learning](#learning) |
| 🎨 **A creator** | [Design](#design) → [Media](#media) → [Productivity](#productivity) |
| 🔐 **Privacy-conscious** | [Privacy & Security](#privacy-security) → [Productivity](#productivity) |

<a id="gold-picks"></a>

## 🏆 Gold Picks

The best of the best. If you only open a few links today, make it these.

{{GOLD_PICKS}}

{{RECENT}}
<a id="contents"></a>

## 📑 Contents

{{TOC}}

**Legend:** ![Open source](https://img.shields.io/badge/Open%20source-2ea44f?style=flat-square) source code is public · ![Free](https://img.shields.io/badge/Free-0969da?style=flat-square) free to use · ![Free tier](https://img.shields.io/badge/Free%20tier-bf8700?style=flat-square) generous free plan, paid upgrades · 🏆 gold pick

---

{{CATEGORIES}}

---

<a id="how-it-works"></a>

## ⚙️ How GoldList Stays Gold

Every change goes through the same automated pipeline, so the list stays accurate as it grows.

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

- **Single source of truth:** every entry lives in [`data/*.yaml`](data/). This README, the [JSON API](api/goldlist.json) and the suggestion form are all generated from it.
- **AI review:** [CodeRabbit](https://coderabbit.ai) reviews every pull request against the [quality bar](CONTRIBUTING.md#the-bar).
- **Strict validation:** CI rejects duplicates, broken links, missing fields and over-long descriptions.
- **Self-cleaning:** a weekly job checks every link and opens an issue if anything breaks.

### 📦 Use the data

Building an app, bot or website? Everything is available as JSON:

```bash
curl -s https://raw.githubusercontent.com/UsmanGhias/goldlist/main/api/goldlist.json
```

<a id="contributing"></a>

## 🤝 Contributing

Know something that deserves to be here?

- **30 seconds:** [suggest it with the form](https://github.com/UsmanGhias/goldlist/issues/new?template=suggest.yml). Once a maintainer labels it `accepted`, a bot adds it.
- **Pull request:** add it to [`data/`](data/) and open a PR. CodeRabbit reviews it and it merges automatically when approved. See [CONTRIBUTING.md](CONTRIBUTING.md).

The bar is high on purpose: **free or open source, actively maintained, and clearly the best (or close to it) at what it does.**

## 📈 Star History

<a href="https://star-history.com/#UsmanGhias/goldlist&Date">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=UsmanGhias/goldlist&type=Date&theme=dark">
    <img src="https://api.star-history.com/svg?repos=UsmanGhias/goldlist&type=Date" alt="Star History Chart" width="600">
  </picture>
</a>

---

<div align="center">

**If GoldList saved you time, [give it a ⭐](https://github.com/UsmanGhias/goldlist) and share it with one friend who needs it.**

<sub>Released under [CC0 1.0](LICENSE): public domain, so copy it, share it, build on it.<br>
This README is generated from <code>data/*.yaml</code> by <code>scripts/build.py</code>. Edit the data, not this file.</sub>

<p><a href="#top">↑ Back to top</a></p>

</div>
