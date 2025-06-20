import os
from dotenv import load_dotenv

load_dotenv()

# Configuration des modèles
PROVIDER = os.getenv("PROVIDER", "mistral")
MODEL_NAME = os.getenv("MODEL_NAME", "mistral-small")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY")
MISTRAL_API_BASE = os.getenv("MISTRAL_API_BASE", "https://api.mistral.ai/v1")

# Configuration du repository
REPO_URL = os.getenv("REPO_URL", "")

# Configuration de l'embedding - utilise gratuit si pas d'OpenAI
USE_FREE_EMBEDDINGS = os.getenv("USE_FREE_EMBEDDINGS", "true").lower() == "true"
EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL", "sentence-transformers/all-MiniLM-L6-v2")

# Configuration de l'ingestion
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

def get_embeddings():
    """Retourne l'instance d'embeddings selon la configuration"""
    if USE_FREE_EMBEDDINGS or not OPENAI_API_KEY:
        # Utiliser des embeddings gratuits HuggingFace
        try:
            from langchain.embeddings import HuggingFaceEmbeddings
            return HuggingFaceEmbeddings(
                model_name=EMBEDDING_MODEL,
                model_kwargs={'device': 'cpu'},
                encode_kwargs={'normalize_embeddings': True}
            )
        except ImportError:
            raise ImportError("Pour utiliser les embeddings gratuits, installez: pip install sentence-transformers")
    else:
        # Utiliser OpenAI embeddings
        from langchain.embeddings import OpenAIEmbeddings
        return OpenAIEmbeddings(
            openai_api_key=OPENAI_API_KEY,
            model=EMBEDDING_MODEL
        )