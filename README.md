# 🇱🇰 AI Marketing Content Generator

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![LangChain](https://img.shields.io/badge/AI-LangChain-1C3C3C?style=for-the-badge&logo=langchain&logoColor=white)
![OpenAI](https://img.shields.io/badge/Powered%20By-OpenAI%20%2F%20Groq-412991?style=for-the-badge&logo=openai&logoColor=white)

> **"Capture the Beat of the Nation"** 🚀

A powerful AI-driven marketing assistant designed specifically for the **Sri Lankan market**. This tool scans real-time trends, categorizes them using advanced LLMs, and generates "piggyback" marketing strategies to help brands go viral.

---

## 🔥 Key Features

### 1. 🌍 Trend Watcher (Real-Time)
- Instantly fetches the top trending search topics in **Sri Lanka (LK)**.
- Scrapes Google Trends to keep you ahead of the curve.

### 2. 🧠 Virality Brain
- **AI Classification**: Automatically categorizes trends into sectors like *Humor, Politics, Cricket, Drama, Tech, and Lifestyle*.
- Uses **Llama 3 (via Groq)** or **GPT-3.5** to understand the cultural context.

### 3. 💡 Strategy Lab
- **Instant Campaign Generator**: Just input your product name and pick a trend.
- Generates a **viral strategy** and **social media captions** (TikTok/Twitter style) tailored to the trend.

---

## 🛠️ Installation & Setup

### Prerequisites
- Python 3.10 or higher
- An API Key for [Groq](https://console.groq.com/) (Recommended for speed) or OpenAI.

### 1. Clone the Repository
```bash
git clone https://github.com/thineeshamk/AI-Marketing-Content-Generator.git
cd AI-Marketing-Content-Generator
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Configure Secrets
Create a `.env` file in the root directory:
```env
# Option A: Groq (Fast & Free Tier available)
GROQ_API_KEY=gsk_...

# Option B: OpenAI
OPENAI_API_KEY=sk-...
```

---

## 🚀 How to Run

Launch the web application:
```bash
streamlit run src/app.py
```
The app will open in your browser at `http://localhost:8501`.

---

## 📸 Screenshots

| **Trend Center** | **Viral Strategy Lab** |
|:---:|:---:|
| *Detects live trends in Sri Lanka* | *Generates marketing plans instantly* |
| *(Add screenshots here)* | *(Add screenshots here)* |

---

## 🤝 Contributing
Contributions are welcome! Feel free to open issues or submit pull requests to improve the **Virality Brain** or add new trend sources.

---

<p align="center">
  Built with ❤️ for Sri Lankan Marketers
</p>