# serp.cheap Python example

Minimal example that runs a real Google search through the official
[`serpcheap`](https://github.com/SerpCheap/serpcheap-py) Python SDK.

## Quickstart

```bash
python3 -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt

SERPCHEAP_API_KEY=your-key-here python main.py
```

Get an API key at [serp.cheap](https://serp.cheap).

## Scraping page content

`scrape.py` runs the same search but also fetches the page content of the top
organic results by passing a `ScrapeOptions`. Each scraped page prints its
extracted markdown `content` and, when `screenshot=True`, a presigned
`screenshot_url`.

```bash
SERPCHEAP_API_KEY=your-key-here python scrape.py
```

`ScrapeOptions(render_js=True, screenshot=True, top_n=3)` renders each page with a
headless browser, captures a full-page screenshot, and scrapes the top 3 results.
Each scraped page is billed on top of the search.

> Note: scraping requires the `serpcheap` SDK version with scrape support, which
> is not yet published to PyPI. Until then, `requirements.txt` installs the SDK
> straight from the GitHub `main` branch, which tracks this API.
