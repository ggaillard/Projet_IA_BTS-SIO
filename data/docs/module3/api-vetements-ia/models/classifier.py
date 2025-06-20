"""
Classe pour la classification d'images de vêtements avec un modèle pré-entraîné
"""

import tensorflow as tf
import numpy as np
import os
from tensorflow.keras.models import load_model
from utils.model_utils import optimize_model_for_inference

class ClothingClassifier:
    """Classificateur de vêtements basé sur MobileNetV2"""
    
    def __init__(self, model_path=None):
        """
        Initialise le classificateur
        
        Args:
            model_path: Chemin vers le modèle pré-entraîné (optionnel)
        """
        self.model = None
        self.model_path = model_path or os.path.join(
            os.path.dirname(__file__), 
            'pretrained_model', 
            'mobilenet_clothing_model.h5'
        )
        self.input_shape = (224, 224, 3)
        self.load_model()
    
    def load_model(self):
        """Charge le modèle pré-entraîné"""
        try:
            # Chargement du modèle
            print(f"Chargement du modèle depuis {self.model_path}...")
            self.model = load_model(self.model_path)
            
            # Optimisation du modèle pour l'inférence
            self.model = optimize_model_for_inference(self.model)
            
            # Préparation du modèle avec une prédiction sur des données factices
            dummy_input = np.zeros((1, *self.input_shape))
            _ = self.model.predict(dummy_input)
            
            print("Modèle chargé avec succès!")
            return True
            
        except Exception as e:
            print(f"Erreur lors du chargement du modèle: {e}")
            
            # Chargement d'un modèle par défaut si le modèle personnalisé échoue
            try:
                print("Tentative de chargement du modèle MobileNetV2 pré-entraîné...")
                base_model = tf.keras.applications.MobileNetV2(
                    input_shape=self.input_shape,
                    include_top=True,
                    weights='imagenet'
                )
                self.model = base_model
                print("Modèle MobileNetV2 chargé comme solution de repli.")
                return True
            except Exception as e2:
                print(f"Échec du chargement du modèle de repli: {e2}")
                return False
    
    def predict(self, image_array):
        """
        Prédiction sur une image prétraitée
        
        Args:
            image_array: Image prétraitée au format numpy array
            
        Returns:
            np.array: Prédictions pour chaque classe
        """
        if self.model is None:
            raise ValueError("Le modèle n'est pas chargé")
            
        # Vérification de la forme de l'entrée
        if len(image_array.shape) != 4:
            image_array = np.expand_dims(image_array, axis=0)
            
        # Prédiction
        predictions = self.model.predict(image_array)
        return predictions
    
    def is_loaded(self):
        """Vérifie si le modèle est chargé"""
        return self.model is not None