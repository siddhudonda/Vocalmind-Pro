# config.py
import os

# LLM Configuration
LLM_API_KEY = os.getenv("OPENAI_API_KEY") or "your-api-key"
LLM_MODEL_NAME = "gpt-3.5-turbo"  # Change model here
