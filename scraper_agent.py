import json
from typing import Dict, List, Any
from strands import Agent   # keep Agent base class
import logging
import feedparser

class WebScraperAgent(Agent):
    """
    A web scraping agent that extracts structured data from a specified website.
    Uses feedparser to fetch and parse RSS feeds, returning JSON output.
    """

    def __init__(self, site_name: str, base_url: str):
        super().__init__()
        self.site_name = site_name
        self.base_url = base_url
        self.logger = logging.getLogger(__name__)

    async def run(self) -> Dict[str, Any]:
        """Execute the web scraping process."""
        try:
            scraped_data = await self.scrape_website()
            return self.format_output(scraped_data)
        except Exception as e:
            print(f"Error during web scraping: {str(e)}")
            return {"error": "Failed to scrape website", "details": str(e)}

    async def scrape_website(self) -> List[Dict[str, Any]]:
        """Scrape the RSS feed and extract relevant information."""
        scraped_data = []
        try:
            feed = feedparser.parse(self.base_url)
            for entry in feed.entries:
                scraped_item = {
                    'headline': entry.title,
                    'url': entry.link,
                    'snippet': entry.summary if 'summary' in entry else '',
                    'date': entry.published if 'published' in entry else ''
                }
                scraped_data.append(scraped_item)
        except Exception as e:
            print(f"Error scraping website: {str(e)}")
            return [{"error": str(e)}]

        return scraped_data

    def format_output(self, scraped_data: List[Dict[str, Any]]) -> Dict[str, Any]:
        return {
            "site": self.site_name,
            "scraped_data": scraped_data
        }

    async def scrape_step(self) -> Dict[str, Any]:
        """Run the scraper and return JSON output."""
        try:
            result = await self.run()
            return result
        except Exception as e:
            print(f"Error in scrape_step: {str(e)}")
            return {"error": str(e)}