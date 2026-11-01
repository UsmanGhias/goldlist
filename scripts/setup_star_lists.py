#!/usr/bin/env python3
"""Create GitHub Star Lists for each GoldList category on UsmanGhias's GitHub profile.

Usage:
    python scripts/setup_star_lists.py
"""

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

from build import load_categories

def get_existing_lists():
    query = """
    query {
      viewer {
        lists(first: 50) {
          nodes {
            id
            name
            description
          }
        }
      }
    }
    """
    cmd = ["gh", "api", "graphql", "-f", f"query={query}"]
    out = subprocess.check_output(cmd)
    data = json.loads(out.decode())
    return {l["name"].lower(): l for l in data.get("data", {}).get("viewer", {}).get("lists", {}).get("nodes", [])}

def create_list(name, description):
    mutation = """
    mutation($name: String!, $description: String!) {
      createUserList(input: {
        name: $name,
        description: $description,
        isPrivate: false
      }) {
        list {
          id
          name
        }
      }
    }
    """
    cmd = [
        "gh", "api", "graphql",
        "-f", f"query={mutation}",
        "-F", f"name={name}",
        "-F", f"description={description}"
    ]
    out = subprocess.check_output(cmd)
    return json.loads(out.decode())

def main():
    print("Checking existing GitHub Star Lists for @UsmanGhias...")
    existing = get_existing_lists()
    print(f"Existing lists ({len(existing)}): {', '.join(existing.keys())}")

    categories = load_categories()
    created = 0
    skipped = 0

    print("\nSetting up Star Lists for GoldList categories:")
    print("-" * 60)
    for cat in categories:
        name = cat["title"]
        desc = cat.get("description", f"Curated {name} from GoldList")[:150]
        if name.lower() in existing:
            print(f"  [SKIP] '{name}' already exists.")
            skipped += 1
            continue

        try:
            res = create_list(name, desc)
            if "errors" in res:
                print(f"  [ERROR] Could not create '{name}': {res['errors']}")
            else:
                print(f"  [CREATED] '{name}'")
                created += 1
        except Exception as e:
            print(f"  [FAIL] '{name}': {e}")

    print("-" * 60)
    print(f"Complete: {created} lists created, {skipped} already existed.")

if __name__ == "__main__":
    main()
