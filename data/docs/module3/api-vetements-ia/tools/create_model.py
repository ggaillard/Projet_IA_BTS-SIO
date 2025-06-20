# Installation/mise à jour des bibliothèques si nécessaire
!pip install -q tensorflow

import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten, Conv2D, MaxPooling2D
import numpy as np
import matplotlib.pyplot as plt
import time

print(f"TensorFlow version: {tf.__version__}")

# Vérification si GPU est disponible
if tf.config.list_physical_devices('GPU'):
    print("GPU détecté et activé ✅")
else:
    print("⚠️ Pas de GPU détecté, l'exécution sera plus lente")

## 1. Téléchargement et exploration du jeu de données
fashion_mnist = tf.keras.datasets.fashion_mnist
(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

# Noms des classes
class_names = ['T-shirt/top', 'Pantalon', 'Pull-over', 'Robe', 'Manteau',
               'Sandale', 'Chemise', 'Sneaker', 'Sac', 'Bottine']

print(f"Nombre d'exemples d'entraînement: {len(train_images)}")
print(f"Nombre d'exemples de test: {len(test_images)}")
print(f"Taille des images: {train_images[0].shape}")

# Visualisation de quelques exemples
plt.figure(figsize=(10, 10))
for i in range(9):
    plt.subplot(3, 3, i + 1)
    plt.imshow(train_images[i], cmap='gray')
    plt.title(class_names[train_labels[i]])
    plt.axis('off')
plt.tight_layout()
plt.show()

## 2. Préparation des données
# Redimensionnement pour le modèle (28x28x1)
train_images = train_images / 255.0  # Normalisation
test_images = test_images / 255.0

print(f"Forme des données d'entraînement: {train_images.shape}")
print(f"Forme des données de test: {test_images.shape}")

# Utilisation d'un sous-ensemble très petit pour l'entraînement
SUBSET_SIZE = 500  # Utiliser seulement 500 exemples pour l'entraînement rapide
train_subset = train_images[:SUBSET_SIZE]
labels_subset = train_labels[:SUBSET_SIZE]

## 3. Création du modèle (plus léger)
model = Sequential([
    Flatten(input_shape=(28, 28)),
    Dense(128, activation='relu'),
    Dense(10, activation='softmax')
])

# Résumé du modèle
print("Structure du modèle:")
model.summary()

## 4. Compilation et entraînement
model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

print("Début de l'entraînement...")
start_time = time.time()

# Entraînement sur 5 époques
history = model.fit(
    train_subset, labels_subset,
    epochs=5,
    batch_size=32,
    validation_split=0.2,
    verbose=1
)

print(f"Entraînement terminé en {time.time() - start_time:.2f} secondes")

## 5. Évaluation
test_loss, test_acc = model.evaluate(test_images, test_labels, verbose=0)
print(f"Précision sur les données de test: {test_acc*100:.2f}%")

# Visualisation des résultats d'entraînement
plt.figure(figsize=(12, 4))
plt.subplot(1, 2, 1)
plt.plot(history.history['accuracy'], label='Précision (entraînement)')
plt.plot(history.history['val_accuracy'], label='Précision (validation)')
plt.xlabel('Époque')
plt.ylabel('Précision')
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(history.history['loss'], label='Perte (entraînement)')
plt.plot(history.history['val_loss'], label='Perte (validation)')
plt.xlabel('Époque')
plt.ylabel('Perte')
plt.legend()
plt.tight_layout()
plt.show()

## 6. Exemples de prédictions
# Faisons quelques prédictions pour vérifier
predictions = model.predict(test_images[:9])

plt.figure(figsize=(12, 12))
for i in range(9):
    plt.subplot(3, 3, i+1)
    plt.imshow(test_images[i], cmap='gray')
    predicted_label = np.argmax(predictions[i])
    true_label = test_labels[i]

    if predicted_label == true_label:
        color = 'green'
    else:
        color = 'red'

    plt.title(f"Prédit: {class_names[predicted_label]}\nRéel: {class_names[true_label]}",
              color=color)
    plt.axis('off')
plt.tight_layout()
plt.show()

## 7. Sauvegarde du modèle
model.save('simple_clothing_model.h5')
print("Modèle sauvegardé avec succès sous le nom 'simple_clothing_model.h5'")

# Pour télécharger le modèle depuis Google Colab
from google.colab import files
files.download('simple_clothing_model.h5')

print("\n✅ Processus terminé avec succès!")
print("Vous pouvez maintenant utiliser ce modèle dans l'application de classification de vêtements.")
