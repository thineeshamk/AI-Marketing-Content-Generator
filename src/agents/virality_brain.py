import os
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

# Sectors definition
VIRALITY_SECTORS = [
    "Humor", "Politics", "Cricket", "Drama", "Tech", "Lifestyle", "News", "Entertainment"
]

def get_llm():
    """
    Returns the configured LLM instance. 
    Prioritizes Groq if available, then OpenAI.
    """
    groq_api_key = os.getenv("GROQ_API_KEY")
    openai_api_key = os.getenv("OPENAI_API_KEY")
    
    if groq_api_key:
        print("[*] Using Groq LLM (Llama3-8b-8192)")
        return ChatGroq(
            temperature=0, 
            model_name="llama3-8b-8192", 
            api_key=groq_api_key
        )
    elif openai_api_key:
        print("[*] Using OpenAI LLM")
        return ChatOpenAI(temperature=0, model="gpt-3.5-turbo")
    else:
        raise ValueError("No API Key found. Please set GROQ_API_KEY or OPENAI_API_KEY in .env")

def categorize_trend(trend_topic: str) -> str:
    """
    Categorizes a trend topic into one of the predefined Virality Sectors.
    """
    llm = get_llm()
    
    # Simple classification prompt
    template = """
    You are an expert Sri Lankan social media analyst.
    Categorize the following trend: "{trend}"
    Into EXACTLY ONE of these sectors: {sectors}.
    
    Return ONLY the category name. Nothing else.
    """
    
    prompt = ChatPromptTemplate.from_template(template)
    chain = prompt | llm | StrOutputParser()
    
    try:
        category = chain.invoke({
            "trend": trend_topic, 
            "sectors": ", ".join(VIRALITY_SECTORS)
        })
        return category.strip()
    except Exception as e:
        print(f"[!] Error categorizing trend '{trend_topic}': {e}")
        return "Uncategorized"

def generate_marketing_strategy(product: str, trend: str, category: str) -> str:
    """
    Generates a marketing strategy connecting the product to the trend.
    """
    llm = get_llm()
    
    template = """
    You are a viral marketing genius in Sri Lanka.
    
    Context:
    - User Product/Service: {product}
    - Current Viral Trend: {trend}
    - Trend Category: {category}
    
    Task:
    Create a short, punchy marketing strategy (3-4 bullet points) on how to 
    piggyback on this trend to promote the product. 
    Include a suggested social media caption (Twitter/TikTok style).
    
    Format:
    **Strategy:**
    - [Point 1]
    - [Point 2]
    
    **Caption:**
    "[Caption]"
    """
    
    prompt = ChatPromptTemplate.from_template(template)
    chain = prompt | llm | StrOutputParser()
    
    strategy = chain.invoke({
        "product": product,
        "trend": trend,
        "category": category
    })
    
    return strategy

if __name__ == "__main__":
    # Test
    print(categorize_trend("Cricket Match Today"))
