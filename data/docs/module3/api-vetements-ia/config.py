"""
Configuration de l'application
"""

import os

class Config:
    """Configuration de base pour l'application Flask"""
    # Flask
    DEBUG = os.environ.get('DEBUG', 'True') == 'True'
    PORT = int(os.environ.get('PORT', 5000))
    
    # Sécurité
    SECRET_KEY = os.environ.get('SECRET_KEY', 'clé_secrète_à_changer_en_production')
    
    # Upload
    MAX_CONTENT_LENGTH = 5 * 1024 * 1024  # 5 MB max
    UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), 'uploads')
    ALLOWED_EXTENSIONS = {'jpg', 'jpeg', 'png', 'gif'}
    
    # Modèle
    MODEL_PATH = os.environ.get(
        'MODEL_PATH', 
        os.path.join(os.path.dirname(__file__), 'models', 'pretrained_model', 'mobilenet_clothing_model.h5')
    )
    DEFAULT_MODEL = 'mobilenetv2'
    MODEL_INPUT_SIZE = (224, 224)
    
    # Performance
    CACHE_TIMEOUT = 3600  # 1 heure
    BATCH_SIZE = 4        # Traitement par lots
    
    # Métier
    CATEGORIES = {
        0: "T-shirt/top",
        1: "Pantalon",
        2: "Pull-over",
        3: "Robe",
        4: "Manteau",
        5: "Sandale",
        6: "Chemise",
        7: "Sneaker",
        8: "Sac",
        9: "Bottine"
    }