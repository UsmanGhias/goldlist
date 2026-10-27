# AGENTS.md: Guide for AI agents working on GoldList

This file tells AI coding agents (Antigravity, Gemini CLI, Claude Code, Codex, Cursor and others)
everything they need to add resources to GoldList correctly. **Read it fully before changing anything.**

## 1. What GoldList is

GoldList (<https://github.com/UsmanGhias/goldlist>, website <https://usmanghias.github.io/goldlist/>) is a curated "best of the best" list of **free and
open-source** resources: jobs, career, scholarships, learning, dev tools, AI, design, media,
productivity, research, startups and privacy. Its value is **curation, not size**. Every entry must
be clearly among the best at what it does. When in doubt, leave it out.

## 2. Repository map

| Path | What it is | Edit by hand? |
| --- | --- | --- |
| `data/<slug>.yaml` | One file per category. **The single source of truth.** | ✅ Yes, this is where you work |
| `scripts/add_entry.py` | CLI that adds one entry safely (cleans, dedupes, validates) | Only to improve tooling |
| `scripts/build.py` | Validates data and generates the files below | Only to improve tooling |
| `scripts/fetch_stars.py` | Fetches live GitHub stars for the website (CI only) | Only to improve tooling |
| `site/` | Website (GitHub Pages) that reads `goldlist.json` | For website changes |
| `templates/README.md.tpl` | README layout with `{{PLACEHOLDERS}}` | For layout changes |
| `README.md` | **Generated** | ❌ Never |
| `api/goldlist.json` | **Generated** JSON API for apps and websites | ❌ Never |
| `.github/ISSUE_TEMPLATE/suggest.yml` | **Generated** suggestion form (categories come from data) | ❌ Never |
| `.github/workflows/` | Automation (see section 7) | Only when asked |
| `.coderabbit.yaml` | CodeRabbit AI review rules | Only when asked |
| `lychee.toml` | Link checker config | Only when asked |

## 3. Categories

| Slug (file) | Title |
| --- | --- |
| `jobs` | Jobs & Freelancing |
| `career` | Career & Interviews |
| `scholarships` | Scholarships & Research Funding |
| `learning` | Learning & Courses |
| `students` | Students & Programs |
| `dev-tools` | Developer Tools & Free Tiers |
| `ai-tools` | AI Tools & Models |
| `ai-coding` | AI Coding Agents & Tools |
| `agent-skills` | Claude & Agent Skills |
| `mcp` | MCP Servers |
| `design` | Design & UI |
| `media` | Video, Audio & Media |
| `productivity` | Productivity & Everyday Apps |
| `research` | Research & Writing |
| `startups` | Startups & Business |
| `privacy-security` | Privacy & Security |

Run `ls data/` for the live list. Categories can be added (see section 6).

## 4. Entry schema

```yaml
  - name: LocalSend                      # required: official product name
    url: https://localsend.org           # required: official homepage or repo, https, no tracking params
    desc: Share files between nearby devices with no internet or account.   # required, see rules
    type: open-source                    # required: open-source | free | free-tier
    github: localsend/localsend          # optional: owner/repo, shows live GitHub stars
    gold: true                           # optional: only the 1-3 best in a category
    added: 2026-10-27                    # set automatically by add_entry.py (feeds "Recently Added")
```

Rules (CI enforces the mechanical ones, CodeRabbit reviews the judgment ones):

- **`type`**
  - `open-source`: source code is public under an open license.
  - `free`: free to use, but the code isn't open.
  - `free-tier`: a useful free plan with paid upgrades. Paid-only tools are **never** allowed.
- **`desc`**: one line, **max 120 characters**, ends with a period. Say **why it's useful**, not just
  what it is. Keep it factual: no hype ("revolutionary", "best ever"), no numbers you haven't
  verified, no first person.
- **`url`**: the official site or repo. No affiliate, referral or `utm_` links, and no duplicates.
  CI fails on duplicate URLs.
- **`github`**: only if the project has a real public repo. For entries whose `url` is already a
  GitHub repo, leave it out; it's derived automatically.
- **`gold`**: rare by design. Don't add `gold: true` unless the owner asks.
- Don't add archived or abandoned projects. Check with `gh api repos/OWNER/REPO -q .archived`.

## 5. How to add a resource (the standard workflow)

```bash
# 0. Setup (once)
pip install pyyaml

# 1. Start from a fresh branch
git checkout main && git pull
git checkout -b add/<short-name>

# 2. Verify before adding
#    - Open the URL and confirm it works and is the official site.
#    - Check it isn't already listed:
grep -ri "<name or domain>" data/
#    - For GitHub projects, check it's alive and get the canonical owner/repo:
gh api repos/OWNER/REPO -q '"\(.full_name) archived=\(.archived) pushed=\(.pushed_at)"'

# 3. Add it with the CLI (cleans the URL, dedupes, validates, sets `added`)
python scripts/add_entry.py --category ai-tools --name "Ollama" --url https://ollama.com \
  --desc "Run open LLMs locally with a single command." --type open-source --github ollama/ollama
#    Use --dry-run first to preview. Repeat step 3 for each resource.

# 4. Validate and preview (optional: CI regenerates everything after merge)
python scripts/build.py --validate
python scripts/build.py            # regenerates README.md locally so you can preview it

# 5. Commit ONLY the data files (generated files are rebuilt on main automatically)
git add data/
git commit -m "feat(data): add Ollama to AI Tools"
git push -u origin HEAD

# 6. Open the pull request
gh pr create --fill
```

Then:

1. **CodeRabbit** reviews the PR automatically within a few minutes.
2. If CodeRabbit **requests changes**, fix them on the same branch and push. Reply in the PR thread
   with `@coderabbitai` if you disagree, giving a reason.
3. When CodeRabbit **approves** and the `validate` check passes, the PR is **squash-merged
   automatically** and the README is rebuilt. You don't need to do anything else.
4. If the owner wants to skip the AI gate, they add the `approved` label to the PR.

Commit message style (Conventional Commits): `feat(data): add X to <Category>`,
`fix(data): update X link`, `chore(data): remove archived X`, `feat(data): add <category> category`.

Several related entries can go in one PR (e.g. "add 5 design tools"), but keep a PR to one theme.

## 6. Adding a new category

1. Create `data/<slug>.yaml` (lowercase, hyphens). The slug becomes the README anchor `#<slug>`.

   ```yaml
   title: Open-Source Alternatives      # full section title
   short: Alternatives                  # short label for the nav bar
   emoji: 🔁
   order: 17                            # position in the README (existing: 1-16)
   description: One line saying what's inside and who it's for.
   items:
     - name: ...
   ```

2. Add at least **5 strong entries**.
3. Optionally link it from the "Start Here" table in `templates/README.md.tpl`. The build fails if a
   template link points to a section that doesn't exist.
4. Run `python scripts/build.py --validate`, then follow section 5 to open a PR.
   The suggestion form's category dropdown updates automatically.

## 7. Automation (what happens without you)

| Workflow | Trigger | What it does |
| --- | --- | --- |
| `validate.yml` | every PR | Schema, duplicates and template-link validation, plus a link check of changed data files. Must pass before merge. |
| CodeRabbit (GitHub App) | every PR | AI review against the rules in `.coderabbit.yaml`. Approves when satisfied. |
| `automerge.yml` | CodeRabbit approval (owner PRs) or `approved` label | Waits for checks, squash-merges, deletes the branch, rebuilds the README. |
| `build.yml` | push to main, daily, manual | Regenerates README.md, api/goldlist.json and the suggestion form, then commits them. |
| `accept-suggestion.yml` | `accepted` label on a suggestion issue | Parses the issue form, adds the entry, rebuilds, closes the issue. |
| `pages.yml` | push to main, daily, after bot merges | Builds and deploys the website at <https://usmanghias.github.io/goldlist/> with fresh star counts. |
| `links.yml` | weekly (Monday) | Checks every link and opens a `broken-link` issue if any are dead. |
| Dependabot | monthly | Opens PRs to update GitHub Actions versions. |

`main` is protected against force-pushes and deletion. Always change it through a pull request,
so that CodeRabbit and `validate` check every change before it lands.

## 8. Fixing a broken-link issue

1. Read the issue and find each failing URL in `data/`.
2. If the site moved, update `url` (and `github` if the repo was renamed).
3. If the project is dead or archived, remove the whole entry.
4. If the site works in a browser but blocks bots, add it to `exclude` in `lychee.toml` with a comment.
5. Open a PR with `fix(data): ...` and reference the issue (`Fixes #N`).

## 9. Never do this

- ❌ Edit `README.md`, `api/goldlist.json` or `.github/ISSUE_TEMPLATE/suggest.yml` by hand.
- ❌ Push directly to `main`. Always use a branch and a PR.
- ❌ Add paid-only tools, affiliate or referral links, or archived projects.
- ❌ Invent facts in descriptions (star counts, user numbers, features you didn't verify).
- ❌ Add `gold: true` without the owner asking.
- ❌ Change workflows, `.coderabbit.yaml` or the ruleset unless explicitly asked.

## 10. Pre-PR checklist

- [ ] Each URL opens and is the official site or repo.
- [ ] `grep -ri` found no existing entry for the same product.
- [ ] `type` is accurate, and `desc` is ≤120 characters, factual and ends with a period.
- [ ] GitHub projects are not archived and use the canonical `owner/repo`.
- [ ] `python scripts/build.py --validate` prints `OK`.
- [ ] Only `data/` files are committed. The branch is pushed and the PR is opened with `gh pr create --fill`.
