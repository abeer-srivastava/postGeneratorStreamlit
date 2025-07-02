from langchain_google_genai import ChatGoogleGenerativeAI
import os
import time
from dotenv import load_dotenv

load_dotenv()

llm = ChatGoogleGenerativeAI(
    google_api_key=os.getenv("GEMINI_API_KEY"),
    model="gemini-1.5-flash"
)

def safe_invoke(prompt, delay=2):
    """Invoke LLM with rate limiting"""
    time.sleep(delay)  # Add delay between requests
    return llm.invoke(prompt)

if __name__ == "__main__":
    response = llm.invoke("Two most important ingredients in samosa are ")
    print(response.content)