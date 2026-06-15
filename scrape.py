import os
import sys

from serpcheap import ScrapeOptions, SerpCheap, SerpCheapError


def main():
    api_key = os.environ.get("SERPCHEAP_API_KEY")
    if not api_key:
        print("Set SERPCHEAP_API_KEY to your serp.cheap API key and try again.")
        sys.exit(1)

    client = SerpCheap(api_key)

    try:
        res = client.search(
            q="best running shoes",
            gl="us",
            scrape=ScrapeOptions(render_js=True, screenshot=True, top_n=3),
        )
    except SerpCheapError as e:
        print(f"[{e.code}] {e}")
        sys.exit(1)

    for r in res.organic:
        print(f"{r.position}. {r.title} — {r.link}")
        if r.scrape_error:
            print(f"   scrape failed: {r.scrape_error}")
            continue
        if r.content:
            print(f"   content ({len(r.content)} chars): {r.content[:200]}")
        if r.screenshot_url:
            print(f"   screenshot: {r.screenshot_url}")

    s = res.stats
    print(f"stats: cost={s.cost} balance={s.balance} cached={s.cached}")


if __name__ == "__main__":
    main()
