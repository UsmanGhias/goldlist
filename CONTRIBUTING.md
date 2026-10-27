# Contributing to GoldList

Thanks for helping keep GoldList the best list on GitHub. 🏆

## The bar

GoldList is **curated, not collected**. An entry must be:

1. **Free**: open source, fully free, or a free tier that's genuinely useful.
2. **Alive**: actively maintained, and the link works.
3. **Gold**: clearly the best (or close to it) at what it does. "It's nice" isn't enough.
4. **Honest**: no affiliate or referral links, no self-promotion without disclosure.

Categories stay short on purpose. If a category is full, propose **replacing** a weaker entry and say why.

## The quick way

[Open a suggestion](https://github.com/UsmanGhias/goldlist/issues/new?template=suggest.yml) and fill in the form. A maintainer will add it.

## The PR way

`README.md` is **generated**. Don't edit it directly.

1. Add your entry to the right file in [`data/`](data/):

   ```yaml
   - name: LocalSend
     url: https://localsend.org
     desc: Share files between nearby devices with no internet or account.
     type: open-source   # open-source | free | free-tier
     gold: true          # optional, best in category only (maintainers decide)
   ```

2. Validate (optional, CI does it too):

   ```bash
   pip install pyyaml
   python scripts/build.py --validate
   ```

3. Open a PR. Once it's merged, the README regenerates automatically.

### Style rules

- `desc`: one line, ≤ 120 characters, ends with a period, says **why it's useful** rather than just what it is.
- `url`: `https://`, the official homepage or repo, with no tracking parameters.
- No duplicates. The build fails if the same URL appears twice.

## New categories

Open an issue first with at least 5 strong entries for the category.
