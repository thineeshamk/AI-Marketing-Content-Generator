import sys
import os

# Add src to path
sys.path.append(os.path.join(os.getcwd(), 'src'))

from agents.virality_brain import categorize_trend, generate_marketing_strategy

def test_brain():
    print("Testing Virality Brain...")
    
    # Test 1: Categorization
    trend = "Election Results 2025"
    print(f"Testing Categorization for: '{trend}'")
    cat = categorize_trend(trend)
    print(f"-> Category: {cat}")
    
    if cat in ["Politics", "News", "Drama"]:
        print("✅ Categorization seems accurate.")
    else:
        print(f"⚠️ Categorization might be off (Got {cat}), but module is working.")

    # Test 2: Strategy
    product = "Energy Drink"
    print(f"\nTesting Strategy for product: '{product}'")
    strategy = generate_marketing_strategy(product, trend, cat)
    
    if len(strategy) > 50:
        print("✅ Strategy generated:")
        print(strategy[:100] + "...")
    else:
        print("❌ Strategy generation failed or too short.")

if __name__ == "__main__":
    test_brain()
