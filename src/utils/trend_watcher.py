import os
from pytrends.request import TrendReq
import pandas as pd

def fetch_top_trends(geo='LK', limit=5):
    """
    Fetches the top trending searches for a given geometry (default: Sri Lanka 'LK').
    
    Args:
        geo (str): The geolocation code (default 'LK' for Sri Lanka).
        limit (int): Number of trends to return.
        
    Returns:
        list: A list of trending search queries (strings).
    """
    print(f"[*] Fetching real-time trends for {geo}...")
    try:
        # Initialize pytrends
        # hl='en-US' (language), tz=360 (TimeZone offset)
        pytrends = TrendReq(hl='en-US', tz=330) # Sri Lanka is UTC+5:30 (330 mins)
        
        # Get trending searches (Daily Search Trends)
        # Note: 'daily' trends are often more robust for getting specific topics than 'today'
        trending_searches_df = pytrends.trending_searches(pn='sri_lanka') # pn for country name in some versions, or use trending_searches(pn='sri_lanka')
        
        # If trending_searches() simply returns a dataframe with one column
        if not trending_searches_df.empty:
             # The column name is usually 0
            trends = trending_searches_df.iloc[:, 0].head(limit).tolist()
            return trends
            
    except Exception as e:
        print(f"[!] PyTrends failed: {e}. Trying fallback RSS...")
        try:
            import requests
            import xml.etree.ElementTree as ET
            
            # Fallback: Google Trends RSS for Sri Lanka
            rss_url = "https://trends.google.com/trends/trendingsearches/daily/rss?geo=LK"
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
            }
            response = requests.get(rss_url, headers=headers)
            if response.status_code == 200:
                root = ET.fromstring(response.content)
                # Parse items
                # Structure: channel -> item -> title
                trends = []
                for item in root.findall('.//item'):
                    title = item.find('title').text
                    trends.append(title)
                    if len(trends) >= limit:
                        break
                if trends:
                    print(f"[*] Success: Fetched {len(trends)} trends from RSS.")
                    return trends
            else:
                print(f"[!] RSS failed with status code: {response.status_code}")
        except Exception as rss_e:
             print(f"[!] RSS Fallback failed: {rss_e}")

        # Fallback 2: Playwright Scraper (Subprocess to avoid Streamlit AsyncIO conflicts)
        print("[*] Trying Playwright Scraper for Real-Time Data...")
        try:
            import subprocess
            import json
            import sys
            
            # Path to the separate script
            script_path = os.path.join(os.path.dirname(__file__), 'scraper_subprocess.py')
            
            # Run independent python process
            result = subprocess.run(
                [sys.executable, script_path], 
                capture_output=True, 
                text=True, 
                timeout=90
            )
            
            if result.returncode == 0:
                trends = json.loads(result.stdout)
                if trends:
                    print(f"[*] Success: Scraped {len(trends)} trends via Subprocess.")
                    return trends
            else:
                print(f"[!] Subprocess failed: {result.stderr}")
                
        except Exception as pw_e:
            print(f"[!] Playwright Scraper failed: {pw_e}")

        return []

if __name__ == "__main__":
    # Test run
    trends = fetch_top_trends()
    print("Top Trends:", trends)
