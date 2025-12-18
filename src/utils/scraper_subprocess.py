import sys
import json
from playwright.sync_api import sync_playwright

def scrape_trends(limit=5):
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            context = browser.new_context(
                user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
            )
            page = context.new_page()
            
            # Using the validated selector
            url = "https://trends.google.com/trends/trending?geo=LK&hl=en-GB"
            page.goto(url, timeout=60000)
            
            # Wait for content
            try:
                page.wait_for_selector('div.mZ3RIc', timeout=20000)
                titles = page.locator('div.mZ3RIc').all_inner_texts()
            except:
                titles = []

            browser.close()
            
            valid_trends = [t.strip() for t in titles if t.strip()][:limit]
            return valid_trends
    except Exception as e:
        return []

if __name__ == "__main__":
    trends = scrape_trends()
    # Print JSON for the caller to parse
    print(json.dumps(trends))
