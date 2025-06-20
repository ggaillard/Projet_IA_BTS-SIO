import os
from dotenv import load_dotenv
load_dotenv()

PROVIDER = os.getenv("PROVIDER", "openai")
MODEL_NAME = os.getenv("MODEL_NAME")
MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY")
MISTRAL_API_BASE = os.getenv("MISTRAL_API_BASE")

