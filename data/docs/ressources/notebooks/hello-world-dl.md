# 🚀 Hello World du Deep Learning

## Reconnaissance de chiffres manuscrits avec TensorFlow et Keras

### Objectifs de ce notebook

- Charger et préparer un jeu de données de chiffres manuscrits
- Créer un réseau de neurones simple
- Entraîner le modèle
- Visualiser les résultats
- Tester le modèle avec vos propres dessins

```python
# Importation des bibliothèques nécessaires
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

# Vérification de la version de TensorFlow
print(f"TensorFlow version: {tf.__version__}")
print(f"Keras version: {keras.__version__}")

# Vérification du GPU (si disponible)
print("GPU disponible :", tf.test.is_gpu_available())
