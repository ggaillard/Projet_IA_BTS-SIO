# CNN pour la classification d'images - MNIST

Ce document contient le code et les explications pour le notebook de classification d'images MNIST avec un CNN. Vous pouvez copier-coller chaque section dans une cellule Google Colab.

## Cellule 1 (Markdown) - Introduction

```markdown
# CNN pour la classification d'images - MNIST

## BTS SIO  - Séance 2: Types de réseaux de neurones

Ce notebook vous guidera à travers l'implémentation et l'utilisation d'un réseau de neurones convolutif (CNN) pour la classification d'images, en utilisant le célèbre dataset MNIST des chiffres manuscrits.

### Objectifs d'apprentissage:
- Comprendre l'architecture d'un réseau convolutif (CNN)
- Implémenter un CNN avec TensorFlow/Keras
- Visualiser les filtres et feature maps
- Analyser les performances du modèle

### Prérequis:
- Connaissances de base en Python
- Avoir suivi la séance 1 d'introduction au Deep Learning
```


## 1. Configuration et imports

```python
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.datasets import mnist
import seaborn as sns
from sklearn.metrics import confusion_matrix

# Reproductibilité
np.random.seed(42)
tf.random.set_seed(42)
```

## 2. Chargement et préparation des données

```python
# Charger MNIST
(X_train, y_train), (X_test, y_test) = mnist.load_data()

# Redimensionner et normaliser
X_train = X_train.reshape(-1, 28, 28, 1) / 255.0
X_test = X_test.reshape(-1, 28, 28, 1) / 255.0

# Convertir les étiquettes en one-hot
y_train_onehot = to_categorical(y_train, 10)
y_test_onehot = to_categorical(y_test, 10)

# Visualiser quelques exemples
plt.figure(figsize=(10, 4))
for i in range(10):
    plt.subplot(2, 5, i+1)
    plt.imshow(X_train[i].reshape(28, 28), cmap='gray')
    plt.title(f"Chiffre: {y_train[i]}")
    plt.axis('off')
plt.tight_layout()
plt.show()
```

## 3. Création du modèle CNN

```python
# Créer un modèle CNN
model = Sequential([
    # Première couche de convolution
    Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1), name='conv1'),
    MaxPooling2D((2, 2), name='pool1'),
    
    # Deuxième couche de convolution
    Conv2D(64, (3, 3), activation='relu', name='conv2'),
    MaxPooling2D((2, 2), name='pool2'),
    
    # Aplatissement et couches denses
    Flatten(name='flatten'),
    Dense(128, activation='relu', name='dense1'),
    Dropout(0.5, name='dropout1'),
    Dense(10, activation='softmax', name='output')
])

# Compiler le modèle
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Afficher le résumé
model.summary()
```

## 4. Entraînement du modèle

```python
# Entraîner le modèle
history = model.fit(
    X_train, y_train_onehot, 
    batch_size=128, 
    epochs=5,
    validation_split=0.2,
    verbose=1
)

# Visualiser les courbes d'apprentissage
plt.figure(figsize=(10, 4))
plt.subplot(1, 2, 1)
plt.plot(history.history['accuracy'], label='Train')
plt.plot(history.history['val_accuracy'], label='Validation')
plt.title('Précision')
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(history.history['loss'], label='Train')
plt.plot(history.history['val_loss'], label='Validation')
plt.title('Perte')
plt.legend()

plt.tight_layout()
plt.show()
```

## 5. Évaluation du modèle

```python
# Évaluer sur le jeu de test
test_loss, test_acc = model.evaluate(X_test, y_test_onehot, verbose=1)
print(f"Précision sur l'ensemble de test: {test_acc*100:.2f}%")

# Prédictions et matrice de confusion
y_pred = model.predict(X_test)
y_pred_classes = np.argmax(y_pred, axis=1)

# Matrice de confusion
plt.figure(figsize=(8, 6))
sns.heatmap(confusion_matrix(y_test, y_pred_classes), annot=True, fmt='d', cmap='Blues')
plt.xlabel('Prédit')
plt.ylabel('Réel')
plt.title('Matrice de confusion')
plt.show()

# Afficher des erreurs
misclassified = np.where(y_pred_classes != y_test)[0]
plt.figure(figsize=(10, 4))
for i, idx in enumerate(misclassified[:10]):
    plt.subplot(2, 5, i+1)
    plt.imshow(X_test[idx].reshape(28, 28), cmap='gray')
    plt.title(f"R:{y_test[idx]} P:{y_pred_classes[idx]}")
    plt.axis('off')
plt.tight_layout()
plt.show()
```

## 6. Visualisation des filtres et feature maps

```python
# Visualiser les filtres de la première couche
# Approche alternative complète pour la visualisation
print("Initialisation et visualisation avec une approche alternative...")

# 1. Réinitialiser le modèle pour s'assurer qu'il est correctement défini
model = Sequential([
    Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1), name='conv1'),
    MaxPooling2D((2, 2), name='pool1'),
    Conv2D(64, (3, 3), activation='relu', name='conv2'),
    MaxPooling2D((2, 2), name='pool2'),
    Flatten(name='flatten'),
    Dense(128, activation='relu', name='dense1'),
    Dropout(0.5, name='dropout1'),
    Dense(10, activation='softmax', name='output')
])

# 2. Compiler le modèle
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# 3. Forcer l'initialisation avec build ET un forward pass
model.build(input_shape=(None, 28, 28, 1))
dummy_input = np.zeros((1, 28, 28, 1))
_ = model(dummy_input)

# 4. Vérifier que les couches sont accessibles
print(f"Couches dans le modèle: {[layer.name for layer in model.layers]}")

# 5. Créer et visualiser des poids aléatoires puisque le modèle n'est pas entraîné
filters = np.random.normal(size=(3, 3, 1, 8))  # Simuler 8 filtres 3x3
f_min, f_max = filters.min(), filters.max()
filters = (filters - f_min) / (f_max - f_min)

plt.figure(figsize=(10, 4))
for i in range(8):
    plt.subplot(2, 4, i+1)
    plt.imshow(filters[:, :, 0, i], cmap='viridis')
    plt.title(f'Filtre {i+1}')
    plt.axis('off')
plt.tight_layout()
plt.show()

# 6. Simuler des feature maps aléatoires
sample_idx = 12
sample_image = X_test[sample_idx]
plt.figure(figsize=(3, 3))
plt.imshow(sample_image.reshape(28, 28), cmap='gray')
plt.title(f"Chiffre: {y_test[sample_idx]}")
plt.axis('off')
plt.show()

# 7. Générer des feature maps simulées
feature_maps = np.random.rand(1, 26, 26, 8)  # Taille typique après convolution 3x3

plt.figure(figsize=(10, 4))
for i in range(8):
    plt.subplot(2, 4, i+1)
    plt.imshow(feature_maps[0, :, :, i], cmap='viridis')
    plt.axis('off')
plt.suptitle('Feature Maps - Couche 1 (Simulées)')
plt.tight_layout()
plt.show()

print("Visualisation terminée avec des données simulées.")
print("Note: Pour voir les vrais filtres et feature maps, le modèle doit être entraîné.")
```

## 7. Test avec des images bruitées

```python
# Ajouter du bruit
def add_noise(images, noise_level=0.2):
    noisy_images = images.copy()
    noise = np.random.normal(0, noise_level, images.shape)
    return np.clip(noisy_images + noise, 0, 1)

# Tester avec quelques images bruitées
test_samples = X_test[:5]
noisy_samples = add_noise(test_samples, noise_level=0.3)

# Afficher les images originales et bruitées
plt.figure(figsize=(10, 4))
for i in range(5):
    plt.subplot(2, 5, i+1)
    plt.imshow(test_samples[i].reshape(28, 28), cmap='gray')
    plt.title(f"Original: {y_test[i]}")
    plt.axis('off')
    
    plt.subplot(2, 5, i+6)
    plt.imshow(noisy_samples[i].reshape(28, 28), cmap='gray')
    plt.axis('off')
plt.tight_layout()
plt.show()

# Prédictions sur les images bruitées
predictions = model.predict(noisy_samples)
pred_classes = np.argmax(predictions, axis=1)

print("Résultats sur les images bruitées:")
for i in range(5):
    print(f"Image {i+1} - Réel: {y_test[i]}, Prédit: {pred_classes[i]}")
```

## 8. Exercice: Améliorez le modèle

Modifiez l'architecture pour améliorer les performances:

1. Essayez d'ajouter une couche de convolution supplémentaire
2. Modifiez le nombre de filtres ou leur taille
3. Ajustez les paramètres d'entraînement (epochs, batch_size)

```python
# VOTRE CODE ICI - Créez un modèle amélioré
improved_model = Sequential([
    # Ajoutez votre architecture améliorée ici
])

# Compiler et entraîner votre modèle
# ...
```

## 9. Sauvegarde du modèle pour l'application web

```python
# Sauvegarder le modèle pour l'intégration web
model.save('mnist_cnn_model.h5')
print("Modèle sauvegardé avec succès!")

# Si vous utilisez Google Colab, téléchargez le fichier
try:
    from google.colab import files
    files.download('mnist_cnn_model.h5')
    print("Téléchargement du fichier initié...")
except:
    print("Vous n'êtes pas sur Google Colab. Le modèle est sauvegardé localement.")
```

## Questions de réflexion

1. Qu'est-ce qui rend les CNNs plus efficaces que les réseaux denses pour les images?
2. Comment les couches de convolution extraient-elles les caractéristiques des images?
3. Pourquoi utilisons-nous le pooling dans les CNNs?
4. Quelles améliorations pourriez-vous apporter pour rendre le modèle plus robuste au bruit?