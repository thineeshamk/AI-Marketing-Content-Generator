import sys
import os

# Add src to path
sys.path.append(os.path.join(os.getcwd(), 'src'))

from utils.trend_watcher import fetch_top_trends

def test_fetch_trends():
    print("Testing Trend Watcher...")
    trends = fetch_top_trends(geo='LK', limit=3)
    
    if trends and len(trends) > 0:
        print(f"✅ Success: Fetched {len(trends)} trends.")
        print(f"   Sample: {trends}")
    else:
        print("❌ Failure: No trends returned.")

if __name__ == "__main__":
    test_fetch_trends()
