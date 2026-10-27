#!/usr/bin/env python3
"""Write GitHub star counts for every repo on the list to a JSON file used by the website.

Usage: GITHUB_TOKEN=... python scripts/fetch_stars.py _site/stars.json
"""
import datetime
import json
import os
import sys
import urllib.request

from build import REPO, github_repo, load_categories

API = "https://api.github.com/graphql"
BATCH = 80


def query_stars(repos, token):
    stars = {}
    for start in range(0, len(repos), BATCH):
        chunk = repos[start:start + BATCH]
        fields = "\n".join(
            f"r{i}: repository(owner: {json.dumps(r.split('/')[0])}, name: {json.dumps(r.split('/')[1])}) {{ stargazerCount }}"
            for i, r in enumerate(chunk)
        )
        request = urllib.request.Request(
            API,
            data=json.dumps({"query": f"query {{\n{fields}\n}}"}).encode(),
            headers={"Authorization": f"bearer {token}", "Content-Type": "application/json"},
        )
        with urllib.request.urlopen(request, timeout=60) as response:
            data = json.load(response).get("data") or {}
        for i, repo in enumerate(chunk):
            # Missing or renamed repos come back as null: the site just omits their count.
            if data.get(f"r{i}"):
                stars[repo] = data[f"r{i}"]["stargazerCount"]
    return stars


def main():
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    token = os.environ.get("GITHUB_TOKEN")
    if not token:
        sys.exit("GITHUB_TOKEN is not set")
    repos = sorted({github_repo(item) for c in load_categories() for item in c["items"]} - {None} | {REPO})
    stars = query_stars(repos, token)
    payload = {
        "generated": datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds"),
        "repoStars": stars.pop(REPO, 0),
        "stars": stars,
    }
    with open(sys.argv[1], "w", encoding="utf-8") as fh:
        json.dump(payload, fh, indent=1, sort_keys=True)
    print(f"Fetched stars for {len(stars)} of {len(repos) - 1} repos")


if __name__ == "__main__":
    main()
