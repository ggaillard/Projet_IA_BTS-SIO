"""
Utilitaires pour le prétraitement des images
"""

import numpy as np
from PIL import Image, ImageOps
import io
import base64

def preprocess_image(image, target_size=(224, 224)):
    """
    Prétraite une image pour l'inférence
    
    Args:
        image: Image PIL ou chemin vers une image
        target_size: Taille cible pour le redimensionnement
        
    Returns:
        np.array: Image prétraitée
    """
    # Convertir en PIL Image si ce n'est pas déjà le cas
    if not isinstance(image, Image.Image):
        if isinstance(image, str):
            image = Image.open(image)
        elif isinstance(image, bytes) or isinstance(image, io.BytesIO):
            image = Image.open(io.BytesIO(image))
        else:
            raise ValueError("Format d'image non pris en charge")
    
    # Assurer que l'image est en RGB
    if image.mode != 'RGB':
        image = image.convert('RGB')
    
    # Redimensionner
    image = image.resize(target_size, Image.LANCZOS)
    
    # Convertir en tableau numpy
    img_array = np.array(image) / 255.0  # Normalisation
    
    return np.expand_dims(img_array, axis=0)

def decode_base64_image(base64_string):
    """
    Décode une image encodée en base64
    
    Args:
        base64_string: Image encodée en base64
        
    Returns:
        PIL.Image: Image décodée
    """
    if ',' in base64_string:
        base64_string = base64_string.split(',')[1]
        
    image_data = base64.b64decode(base64_string)
    return Image.open(io.BytesIO(image_data))

def center_crop_image(image):
    """
    Recadre une image au centre pour obtenir un carré
    
    Args:
        image: Image PIL
        
    Returns:
        PIL.Image: Image recadrée
    """
    width, height = image.size
    
    # Déterminer la dimension la plus petite
    min_dim = min(width, height)
    
    # Calculer les coordonnées de découpe
    left = (width - min_dim) // 2
    top = (height - min_dim) // 2
    right = left + min_dim
    bottom = top + min_dim
    
    # Découper l'image
    return image.crop((left, top, right, bottom))