"""
Utilitaires pour l'optimisation des modèles de deep learning
"""

import tensorflow as tf
import numpy as np
import os

def optimize_model_for_inference(model):
    """
    Optimise un modèle Keras pour l'inférence
    
    Args:
        model: Modèle Keras à optimiser
        
    Returns:
        Modèle optimisé
    """
    # On applique plusieurs optimisations courantes
    
    # 1. Fusionner les opérations BatchNorm avec les couches Conv précédentes
    tf.keras.backend.clear_session()
    model_config = model.get_config()
    weights = model.get_weights()
    
    # Création du modèle avec l'optimisation pour l'inférence
    optimized_model = tf.keras.models.Model.from_config(model_config)
    optimized_model.set_weights(weights)
    
    return optimized_model

def quantize_model(model, model_path, quantize_type='default'):
    """
    Quantifie un modèle Keras et le sauvegarde au format TFLite
    
    Args:
        model: Modèle Keras à quantifier
        model_path: Chemin où sauvegarder le modèle quantifié
        quantize_type: Type de quantification ('default', 'float16', 'int8')
        
    Returns:
        Chemin vers le modèle TFLite quantifié
    """
    # Création du convertisseur TFLite
    converter = tf.lite.TFLiteConverter.from_keras_model(model)
    
    # Configuration de la quantification
    if quantize_type == 'default':
        converter.optimizations = [tf.lite.Optimize.DEFAULT]
    elif quantize_type == 'float16':
        converter.optimizations = [tf.lite.Optimize.DEFAULT]
        converter.target_spec.supported_types = [tf.float16]
    elif quantize_type == 'int8':
        converter.optimizations = [tf.lite.Optimize.DEFAULT]
        converter.target_spec.supported_ops = [tf.lite.OpsSet.TFLITE_BUILTINS_INT8]
        converter.inference_input_type = tf.uint8
        converter.inference_output_type = tf.uint8
        
        # Pour la quantification int8 complète, il faudrait ajouter un dataset représentatif
        # et configurer le representative_dataset_gen
    
    # Conversion du modèle
    tflite_model = converter.convert()
    
    # Sauvegarde du modèle
    output_path = f"{model_path}.tflite"
    with open(output_path, 'wb') as f:
        f.write(tflite_model)
    
    print(f"Modèle quantifié sauvegardé à {output_path}")
    print(f"Taille originale: {os.path.getsize(model_path)} octets")
    print(f"Taille après quantification: {os.path.getsize(output_path)} octets")
    
    return output_path

def prune_model(model, sparsity=0.5):
    """
    Élague un modèle pour réduire sa taille (démo conceptuelle)
    
    Note: L'élagage réel nécessiterait TensorFlow Model Optimization Toolkit
    
    Args:
        model: Modèle Keras à élaguer
        sparsity: Niveau de parcimonie cible (% de poids à mettre à zéro)
        
    Returns:
        Une version conceptuellement "élaguée" du modèle
    """
    # Ceci est une démonstration conceptuelle
    # Dans un cas réel, nous utiliserions:
    # import tensorflow_model_optimization as tfmot
    # pruning_schedule = tfmot.sparsity.keras.PolynomialDecay(...)
    # pruned_model = tfmot.sparsity.keras.prune_low_magnitude(model, pruning_schedule)
    
    print(f"[DÉMO] Élagage du modèle avec une parcimonie cible de {sparsity*100}%")
    print("Note: Pour un vrai élagage, utilisez TensorFlow Model Optimization")
    
    return model