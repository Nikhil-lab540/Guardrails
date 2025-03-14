from langchain_groq import ChatGroq
from nemoguardrails.llm.providers import register_llm_provider
import os

# Custom initialization function to ensure API key is properly set
def init_groq_with_api_key(api_key=None, **kwargs):
    # Use provided API key or get from environment
    if api_key:
        os.environ["GROQ_API_KEY"] = api_key
    return ChatGroq(**kwargs)

# Register the custom provider
register_llm_provider("groq", init_groq_with_api_key)

