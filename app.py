from fastapi import FastAPI
from pydantic import BaseModel
from crawl4ai import AsyncWebCrawler
from crawl4ai.async_configs import BrowserConfig, CrawlerRunConfig

app = FastAPI()

class CrawlRequest(BaseModel):
    url: str

@app.post("/crawl")
async def crawl_url(data: CrawlRequest):
    config = BrowserConfig(stealth=True)
    run = CrawlerRunConfig(magic_mode=True, css_selector="body")

    async with AsyncWebCrawler(config=config) as crawler:
        result = await crawler.arun(url=data.url, config=run)
        return {
            "success": result.success,
            "markdown": result.markdown,
            "html": result.html
        }
