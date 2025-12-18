import streamlit as st
import time
import os
import sys

# Ensure src is in path
sys.path.append(os.path.join(os.getcwd(), 'src'))

from utils.trend_watcher import fetch_top_trends
from agents.virality_brain import categorize_trend, generate_marketing_strategy

# Page Config
st.set_page_config(
    page_title="Marketing AI Agent 🇱🇰",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for Premium Feel
st.markdown("""
<style>
    .stApp {
        background-color: #0e1117;
        color: #fafafa;
    }
    .stButton>button {
        background-color: #FF4B4B;
        color: white;
        border-radius: 20px;
        padding: 10px 24px;
        font-weight: 600;
        border: none;
    }
    .stButton>button:hover {
        background-color: #FF3333;
    }
    .metric-card {
        background-color: #262730;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.5);
    }
    h1, h2, h3 {
        color: #FF4B4B !important;
    }
</style>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/4712/4712035.png", width=50) # Generic AI icon
    st.title("Admin Panel")
    
    api_status = "✅ Active" if os.getenv("GROQ_API_KEY") else "❌ Missing Key"
    st.write(f"LLM Status: {api_status}")
    
    st.markdown("---")
    st.info("Sri Lanka Region (LK) Selected")
    st.markdown("---")
    st.write("v1.0.0 | Built with 🧠")

# Main Content
st.title("🚀 Sri Lanka Marketing AI Agent")
st.markdown("### Capture the Beat of the Nation")

# Tabs
tab1, tab2 = st.tabs(["🔥 Trend Center", "💡 Strategy Lab"])

# Session State for Trends
if "trends_data" not in st.session_state:
    st.session_state.trends_data = []

# --- TAB 1: TREND CENTER ---
with tab1:
    st.header("Real-Time Viral Trends")
    
    col1, col2 = st.columns([3, 1])
    with col2:
        if st.button("🔄 Scan Market"):
            with st.spinner("Scanning Google & Socials..."):
                raw_trends = fetch_top_trends(geo='LK', limit=5)
                
                processed_trends = []
                progress_bar = st.progress(0)
                
                for i, trend in enumerate(raw_trends):
                    cat = categorize_trend(trend)
                    processed_trends.append({"rank": i+1, "topic": trend, "category": cat})
                    progress_bar.progress((i + 1) / len(raw_trends))
                
                st.session_state.trends_data = processed_trends
                st.success("Analysis Complete!")

    with col1:
        if st.session_state.trends_data:
            for item in st.session_state.trends_data:
                with st.container():
                    st.markdown(f"""
                    <div class="metric-card">
                        <h3>#{item['rank']} {item['topic']}</h3>
                        <p style='color: #888;'>Category: <b>{item['category']}</b></p>
                    </div>
                    """, unsafe_allow_html=True)
                    st.write("") # Spacer
        else:
            st.info("Click 'Scan Market' to detect viral trends.")

# --- TAB 2: STRATEGY LAB ---
with tab2:
    st.header("Generate Viral Strategy")
    
    if not st.session_state.trends_data:
        st.warning("Please scan for trends in the 'Trend Center' first.")
    else:
        # Inputs
        col1, col2 = st.columns(2)
        with col1:
            product_name = st.text_input("Product / Service Name", placeholder="e.g., Spicy Kottu Mix")
        with col2:
            trend_options = [t['topic'] for t in st.session_state.trends_data]
            selected_trend_topic = st.selectbox("Piggyback on Trend", trend_options)
        
        if st.button("✨ Generate Campaign"):
            if not product_name:
                st.error("Please enter a product name.")
            else:
                # Find category
                selected_trend_data = next(t for t in st.session_state.trends_data if t['topic'] == selected_trend_topic)
                
                with st.spinner("Brainstorming with AI..."):
                    strategy = generate_marketing_strategy(
                        product=product_name,
                        trend=selected_trend_topic,
                        category=selected_trend_data['category']
                    )
                
                st.markdown("---")
                st.subheader("🎯 Viral Battle Plan")
                st.markdown(strategy)
                st.balloons()
