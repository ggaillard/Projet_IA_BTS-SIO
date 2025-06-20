import os
from dotenv import load_dotenv

load_dotenv()

# Configuration des modèles
PROVIDER = os.getenv("PROVIDER", "openai")
MODEL_NAME = os.getenv("MODEL_NAME", "gpt-3.5-turbo")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY")
MISTRAL_API_BASE = os.getenv("MISTRAL_API_BASE", "https://api.mistral.ai/v1")

# Configuration du repository (ajouté)
REPO_URL = os.getenv("REPO_URL", "")

# Configuration du repository (optionnel)
REPO_URL = os.getenv("REPO_URL", "")

# Configuration de l'embedding
EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL", "text-embedding-ada-002")
CHUNK_SIZE = int(os.getenv("CHUNK_SIZE", "1000"))
CHUNK_OVERLAP = int(os.getenv("CHUNK_OVERLAP", "200"))

# Configuration de la recherche
MAX_RESULTS = int(os.getenv("MAX_RESULTS", "4"))
SIMILARITY_THRESHOLD = float(os.getenv("SIMILARITY_THRESHOLD", "0.7"))

def validate_config():
    """Valide la configuration et retourne les erreurs éventuelles"""
    errors = []
    
    if PROVIDER == "openai" and not OPENAI_API_KEY:
        errors.append("OPENAI_API_KEY manquante pour le provider OpenAI")
    elif PROVIDER == "mistral" and not MISTRAL_API_KEY:
        errors.append("MISTRAL_API_KEY manquante pour le provider Mistral")
    
    return errors

def get_model_config():
    """Retourne la configuration du modèle selon le provider"""
    if PROVIDER == "mistral":
        return {
            "api_key": MISTRAL_API_KEY,
            "base_url": MISTRAL_API_BASE,
            "model": MODEL_NAME or "mistral-small"
        }
    else:  # OpenAI par défaut
        return {
            "api_key": OPENAI_API_KEY,
            "model": MODEL_NAME or "gpt-3.5-turbo"
        }