import asyncio
from scraper_agent import WebScraperAgent
import json
async def main():
    agent = WebScraperAgent(
        site_name="Google News - Holiday Shopping",
        base_url="https://news.google.com/rss/search?q=Christmas+New+Year+shopping+trends"
        # "https://news.google.com/rss/search?q=Christmas+New+Year+shopping+trends"
    )
    result = await agent.scrape_step()
    # print(result)
    with open("scraped_news.json", "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=4)

    print("Data saved to scraped_news.json")


if __name__ == "__main__":
    asyncio.run(main())