from fastapi import FastAPI
from pydantic import BaseModel
from crawl4ai import AsyncWebCrawler
from crawl4ai.async_configs import BrowserConfig, CrawlerRunConfig

app = FastAPI()  # ← You were missing this line

class CrawlRequest(BaseModel):
    url: str

@app.post("/crawl")
async def crawl_url(data: CrawlRequest):
    config = BrowserConfig()
    run = CrawlerRunConfig(
        magic_mode=True,
        css_selector="body",
        stealth=True,
        headless=True
    )

    async with AsyncWebCrawler(config=config) as crawler:
        result = await crawler.arun(url=data.url, config=run)
        return {
            "success": result.success,
            "markdown": result.markdown,
            "html": result.html
        }
