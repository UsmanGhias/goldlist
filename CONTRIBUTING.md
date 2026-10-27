# Contributing to GoldList

Thanks for helping keep GoldList the best list on GitHub. 🏆

## The bar

GoldList is **curated, not collected**. An entry must be:

1. **Free**: open source, fully free, or a free tier that's genuinely useful. Never paid-only.
2. **Alive**: actively maintained, and the link works.
3. **Gold**: clearly the best (or close to it) at what it does. "It's nice" isn't enough.
4. **Honest**: no affiliate or referral links, and no self-promotion without disclosure.

If a category already has a great option for the same job, explain why yours is better, or propose a replacement.

## Option 1: Suggest it (30 seconds, no Git needed)

[Open the suggestion form](https://github.com/UsmanGhias/goldlist/issues/new?template=suggest.yml).
When a maintainer labels it `accepted`, a bot adds it to the list and closes the issue.

## Option 2: Open a pull request

`README.md`, `api/goldlist.json` and the suggestion form are **generated**. Only edit `data/`.

```bash
pip install pyyaml
python scripts/add_entry.py --category productivity --name LocalSend --url https://localsend.org \
  --desc "Share files between nearby devices with no internet or account." \
  --type open-source --github localsend/localsend
python scripts/build.py --validate
git add data/ && git commit -m "feat(data): add LocalSend to Productivity"
```

Or edit the right `data/<category>.yaml` by hand:

```yaml
  - name: LocalSend
    url: https://localsend.org
    desc: Share files between nearby devices with no internet or account.
    type: open-source          # open-source | free | free-tier
    github: localsend/localsend   # optional: shows live GitHub stars
```

### What happens next

1. **CodeRabbit** (AI reviewer) reviews your PR within minutes. Answer its comments, or reply with `@coderabbitai`.
2. **CI** validates the schema, checks for duplicates and tests your links.
3. A maintainer approves, and the PR **merges automatically** once checks pass.
4. The README and JSON API regenerate on their own.

### Style rules

- `desc`: one line, ≤ 120 characters, ends with a period, says **why it's useful**. No hype words or unverified numbers.
- `url`: `https://`, the official homepage or repo, no tracking parameters.
- One product, one entry. The build fails on duplicate URLs.

## New categories

Open an issue first with at least 5 strong entries for it. See [AGENTS.md](AGENTS.md#6-adding-a-new-category) for the file format.

## For AI agents

If you're an AI coding agent, follow [AGENTS.md](AGENTS.md).
