import os
import sys

from serpcheap import SerpCheap, SerpCheapError


def main():
    api_key = os.environ.get("SERPCHEAP_API_KEY")
    if not api_key:
        print("Set SERPCHEAP_API_KEY to your serp.cheap API key and try again.")
        sys.exit(1)

    client = SerpCheap(api_key)

    try:
        res = client.search(q="best running shoes", gl="us")
    except SerpCheapError as e:
        print(f"[{e.code}] {e}")
        sys.exit(1)

    for r in res.organic:
        print(f"{r.position}. {r.title} — {r.link}")

    s = res.stats
    print(f"stats: cost={s.cost} balance={s.balance} cached={s.cached}")


if __name__ == "__main__":
    main()
