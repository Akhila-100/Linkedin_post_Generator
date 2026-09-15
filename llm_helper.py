
from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Get Groq API key
groq_api_key = os.getenv("GROQ_API_KEY")

if not groq_api_key:
    raise ValueError(
        "GROQ_API_KEY is not set. "
        "Please add your Groq API key to the .env file."
    )

# Initialize Groq LLM
llm = ChatGroq(
    groq_api_key=groq_api_key,
    model_name="openai/gpt-oss-120b",
    temperature=0.7,
)

# Test the model when this file is executed directly
if __name__ == "__main__":
    response = llm.invoke(
        "What are the two most important ingredients in a samosa?"
    )

    print(response.content)

