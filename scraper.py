
"""Scrape quotes from quotes.toscrape.com and export them in four formats."""

import time

import requests
from bs4 import BeautifulSoup

from datetime import datetime
from urllib.parse import urljoin

# Configuration constants
BASE_URL = "https://quotes.toscrape.com/"
REQUEST_TIMEOUT = 10
REQUEST_DELAY = 1.5
MAX_RETRIES = 2
RETRY_DELAY = 2


HEADERS = {
    "User-Agent": "DATA430-Project3-Educational-WebScraper/1.0"
}



def fetch_page(url):
    """Fetch a webpage, retrying failed requests twice."""
    for attempt in range(MAX_RETRIES + 1):
        try:
            response = requests.get(
                url,
                headers=HEADERS,
                timeout=REQUEST_TIMEOUT,
            )
            response.raise_for_status()
            return response.text

        except requests.RequestException as error:
            print(
                f"Request failed (attempt {attempt + 1} "
                f"of {MAX_RETRIES + 1}): {error}"
            )

            if attempt < MAX_RETRIES:
                print(f"Retrying in {RETRY_DELAY} seconds...")
                time.sleep(RETRY_DELAY)

    print(f"Unable to retrieve {url} after all attempts.")
    return None




def parse_quotes(soup, page_number, scraped_at):
    """Extract quote text, author, tags, page number, and timestamp."""
    extracted_quotes = []

    for quote_container in soup.select("div.quote"):
        quote_text = quote_container.select_one("span.text").get_text(
            strip=True
        )

        quote_text = quote_text.strip('“”"')

        author = quote_container.select_one("small.author").get_text(
            strip=True
        )

        tags = [
            tag.get_text(strip=True)
            for tag in quote_container.select("a.tag")
        ]

        extracted_quotes.append(
            {
                "quote": quote_text,
                "author": author,
                "tags": tags,
                "page": page_number,
                "scraped_at": scraped_at,
            }
        )

    return extracted_quotes



def main():
    """Scrape quotes from all available pages."""
    print("Starting DATA 430 Project 3 scraper...")

    all_quotes = []
    current_url = BASE_URL
    page_number = 1
    pages_fetched = 0
    scraped_at = datetime.now().isoformat(timespec="seconds")

    while current_url:
        print(f"Fetching page {page_number}...")

        html = fetch_page(current_url)

        if html is None:
            print(f"Stopping: unable to fetch page {page_number}.")
            break

        pages_fetched += 1

        soup = BeautifulSoup(html, "html.parser")

        page_quotes = parse_quotes(
            soup,
            page_number,
            scraped_at,
        )

        all_quotes.extend(page_quotes)

        print(f"Extracted {len(page_quotes)} quotes.")

        # Find the Next link instead of hardcoding page count.
        next_link = soup.select_one("li.next a")

        if next_link is None:
            print("No more pages found.")
            break

        current_url = urljoin(
            current_url,
            next_link["href"],
        )

        page_number += 1

        # Be polite to the server between requests.
        time.sleep(REQUEST_DELAY)

    print("\nScraping summary:")
    print(f"Pages fetched: {pages_fetched}")
    print(f"Quotes extracted: {len(all_quotes)}")


if __name__ == "__main__":
    main()
