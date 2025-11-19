import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from .config import GROQ_API_KEY, LLM_PROVIDER

load_dotenv()


def get_llm():
    """Return a callable LLM function depending on selected provider."""

    # ===== Groq Setup =====
    if LLM_PROVIDER.lower() == "groq":
        if not GROQ_API_KEY:
            return "❌ GROQ_API_KEY missing in .env"

        try:
            # ✅ Use a currently supported Groq model
            llm = ChatGroq(
                api_key=GROQ_API_KEY,
                model="llama-3.1-8b-instant"  # Updated model
            )

            def call_groq(prompt: str):
                response = llm.invoke(prompt)
                # Return response content if present
                return response.content if hasattr(response, "content") else str(response)

            return call_groq

        except Exception as e:
            return f"⚠️ Groq API Error: {str(e)}"

    # ===== Fallback =====
    else:
        return "⚠️ Invalid LLM_PROVIDER in .env (use 'groq')"
