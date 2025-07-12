from crawl4ai import AsyncWebCrawler
from crawl4ai.async_configs import BrowserConfig, CrawlerRunConfig

@app.post("/crawl")
async def crawl_url(data: CrawlRequest):
    # Just basic browser config (no stealth here anymore)
    config = BrowserConfig()

    # Stealth, magic mode, etc now go here:
    run = CrawlerRunConfig(
        magic_mode=True,
        css_selector="body",
        stealth=True,         # ← moved here
        headless=True         # ← optional, also safer on server
    )

    async with AsyncWebCrawler(config=config) as crawler:
        result = await crawler.arun(url=data.url, config=run)
        return {
            "success": result.success,
            "markdown": result.markdown,
            "html": result.html
        }
