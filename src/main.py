import os
import time
import chromadb
from chromadb.utils import embedding_functions
from dotenv import load_dotenv

# Import our modules
from utils.trend_watcher import fetch_top_trends
from agents.virality_brain import categorize_trend, generate_marketing_strategy

# Load environment variables
load_dotenv()

def main():
    print("=======================================")
    print("   SRI LANKA MARKETING AI AGENT 🇱🇰   ")
    print("=======================================")
    
    # 1. Setup ChromaDB (Local Vector Store)
    # We will use a simple collection to store trends we've seen
    try:
        chroma_client = chromadb.PersistentClient(path="data/chroma_db")
        collection = chroma_client.get_or_create_collection(name="sri_lanka_trends")
        print("[*] ChromaDB initialized.")
    except Exception as e:
        print(f"[!] Warning: ChromaDB init failed: {e}. Continuing without persistence.")
        collection = None

    # 2. Fetch Trends
    trends = fetch_top_trends(geo='LK', limit=5)
    
    if not trends:
        print("[!] No trends found. Exiting.")
        return

    print("\n[*] Detected Trends:")
    analyzed_trends = []
    
    # 3. Process & Categorize Trends
    for i, trend in enumerate(trends):
        print(f"    {i+1}. {trend}", end="... ")
        category = categorize_trend(trend)
        print(f"[{category}]")
        
        trend_data = {
            "id": f"trend_{int(time.time())}_{i}",
            "topic": trend,
            "category": category
        }
        analyzed_trends.append(trend_data)
        
        # Store in RAG (ChromaDB)
        if collection:
            collection.add(
                documents=[f"Trend: {trend}, Category: {category}"],
                metadatas=[{"category": category, "timestamp": int(time.time())}],
                ids=[trend_data["id"]]
            )

    print("\n" + "="*40)
    
    # 4. Interactive Product Matching
    while True:
        product = input("\n[?] Enter your product/service (or 'q' to quit): ").strip()
        if product.lower() == 'q':
            break
            
        print(f"\n[*] Analyzing best strategy for '{product}'...")
        
        # Simple matchmaking logic: Just pick the first trend for now
        # In a real RAG system, we would query ChromaDB for the "closest" trend context
        # But for this V1, let's let the user pick or auto-pick the top trend
        
        # Let's auto-match functionality using the LLM in a more advanced version, 
        # but here we'll iterate through the top trend to show immediate value.
        
        best_trend = analyzed_trends[0] # Pick top trend
        
        print(f"[*] Pairing with Top Trend: {best_trend['topic']} ({best_trend['category']})")
        
        strategy = generate_marketing_strategy(
            product=product,
            trend=best_trend['topic'],
            category=best_trend['category']
        )
        
        print("\n" + "-"*40)
        print(strategy)
        print("-"*40)

if __name__ == "__main__":
    main()
