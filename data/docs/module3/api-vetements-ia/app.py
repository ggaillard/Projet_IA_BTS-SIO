"""
Application principale pour l'API de recherche par image de vêtements
"""

from flask import Flask, request, jsonify, render_template, url_for
import os
import numpy as np
import time
from PIL import Image
import io
from config import Config
from models.classifier import ClothingClassifier
from utils.image_utils import preprocess_image

# Initialisation de l'application Flask
app = Flask(__name__)
app.config.from_object(Config)

# Dictionnaire des catégories de vêtements
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

# Initialisation du modèle (singleton pour éviter de le recharger à chaque requête)
classifier = ClothingClassifier()

@app.route('/')
def index():
    """Page d'accueil avec interface de test"""
    return render_template('index.html')

@app.route('/api/predict', methods=['POST'])
def predict():
    """
    API endpoint pour classifier une image de vêtement
    
    Accepte:
    - Fichier image via formulaire multipart
    - Image encodée en base64 via JSON
    
    Retourne:
    - JSON avec prédictions et scores
    """
    # Variables pour le timing
    start_time = time.time()
    
    # Vérification de la présence d'une image
    if 'image' in request.files:
        file = request.files['image']
        if file.filename == '':
            return jsonify({'error': 'Aucun fichier sélectionné'}), 400
            
        # Lecture de l'image
        image = Image.open(file.stream)
    
    elif request.json and 'image' in request.json:
        # Décodage de l'image base64
        try:
            image_data = request.json['image'].split(',')[1]
            image = Image.open(io.BytesIO(base64.b64decode(image_data)))
        except Exception as e:
            return jsonify({'error': f'Erreur de décodage: {str(e)}'}), 400
    
    else:
        return jsonify({'error': 'Aucune image fournie'}), 400
    
    # Prétraitement de l'image
    try:
        processed_image = preprocess_image(image)
    except Exception as e:
        return jsonify({'error': f'Erreur de prétraitement: {str(e)}'}), 400
    
    # Prédiction
    try:
        predictions = classifier.predict(processed_image)
        
        # Formatage des résultats
        results = []
        for i in np.argsort(predictions[0])[-3:][::-1]:  # Top 3 des prédictions
            results.append({
                'category': CATEGORIES[i],
                'category_id': int(i),
                'confidence': float(predictions[0][i])
            })
        
        # Temps d'exécution
        processing_time = time.time() - start_time
        
        return jsonify({
            'results': results,
            'processing_time_ms': round(processing_time * 1000, 2)
        })
        
    except Exception as e:
        return jsonify({'error': f'Erreur de prédiction: {str(e)}'}), 500

@app.route('/api/health', methods=['GET'])
def health_check():
    """Endpoint de vérification de l'état de l'API"""
    return jsonify({
        'status': 'healthy',
        'model_loaded': classifier.is_loaded(),
        'version': '1.0.0'
    })

if __name__ == '__main__':
    app.run(debug=app.config['DEBUG'], port=app.config['PORT'])