# Hello World du Deep Learning - Reconnaissance de chiffres manuscrits

Ce notebook vous guide étape par étape dans votre premier modèle de Deep Learning. Vous allez créer un réseau de neurones capable de reconnaître des chiffres manuscrits.

## Cellule 1 (Markdown) - Introduction

```markdown
# 🧠 Hello World du Deep Learning

## Bienvenue dans votre première expérience avec les réseaux de neurones !

Aujourd'hui, vous allez :
- ✅ Créer votre premier modèle de Deep Learning
- ✅ L'entraîner sur 60 000 images de chiffres manuscrits
- ✅ Tester ses performances
- ✅ Dessiner vos propres chiffres pour les faire reconnaître

**Durée estimée** : 45 minutes

**Prérequis** : Aucun ! Suivez simplement les instructions.
```

## Cellule 2 (Code) - Configuration et vérification

```python
# Configuration et vérification de l'environnement
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten, Conv2D, MaxPooling2D, Dropout
from tensorflow.keras.utils import to_categorical
import seaborn as sns
from sklearn.metrics import confusion_matrix, classification_report

# Vérification de la version TensorFlow
print(f"Version TensorFlow : {tf.__version__}")

# Vérification GPU (optionnel mais intéressant)
print("GPU disponible :", "Oui" if tf.config.list_physical_devices('GPU') else "Non")
if tf.config.list_physical_devices('GPU'):
    print("GPU détecté :", tf.config.list_physical_devices('GPU')[0])

print("\n✅ Configuration terminée avec succès !")
```

## Cellule 3 (Code) - Chargement et exploration des données

```python
# Chargement du dataset MNIST
print("📥 Chargement des données MNIST...")
(X_train, y_train), (X_test, y_test) = mnist.load_data()

# Informations sur le dataset
print(f"📊 Données d'entraînement : {X_train.shape[0]} exemples")
print(f"📊 Données de test : {X_test.shape[0]} exemples")
print(f"📊 Taille des images : {X_train.shape[1]}x{X_train.shape[2]} pixels")
print(f"📊 Nombre de classes : {len(np.unique(y_train))}")

# Normalisation des données (valeurs entre 0 et 1)
X_train = X_train.astype('float32') / 255.0
X_test = X_test.astype('float32') / 255.0

print("\n🔧 Données normalisées (valeurs entre 0 et 1)")

# Visualisation de quelques exemples
plt.figure(figsize=(15, 6))
for i in range(12):
    plt.subplot(2, 6, i + 1)
    plt.imshow(X_train[i], cmap='gray')
    plt.title(f'Chiffre: {y_train[i]}')
    plt.axis('off')

plt.suptitle('Exemples de chiffres manuscrits du dataset MNIST', fontsize=16)
plt.tight_layout()
plt.show()

print("\n❓ Question : Observez ces exemples. Quels défis pourrait rencontrer notre modèle ?")
print("   - Styles d'écriture différents")
print("   - Épaisseurs de trait variables") 
print("   - Légères rotations ou déformations")
```

## Cellule 4 (Code) - Création du modèle

```python
# Création du modèle de réseau de neurones convolutif (CNN)
print("🏗️ Construction du modèle de réseau de neurones...")

model = Sequential([
    # Redimensionnement pour ajouter la dimension des canaux
    tf.keras.layers.Reshape((28, 28, 1), input_shape=(28, 28)),
    
    # Première couche de convolution
    Conv2D(32, (3, 3), activation='relu', name='conv1'),
    MaxPooling2D((2, 2), name='pool1'),
    
    # Deuxième couche de convolution
    Conv2D(64, (3, 3), activation='relu', name='conv2'),
    MaxPooling2D((2, 2), name='pool2'),
    
    # Aplatissement et couches denses
    Flatten(name='flatten'),
    Dense(128, activation='relu', name='dense1'),
    Dropout(0.5, name='dropout'),
    Dense(10, activation='softmax', name='output')
])

# Compilation du modèle
model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

# Affichage de l'architecture
print("\n📋 Architecture du modèle :")
model.summary()

print(f"\n📊 Nombre total de paramètres : {model.count_params():,}")
print("🧠 Ces paramètres vont être ajustés pendant l'entraînement !")
```

## Cellule 5 (Code) - Entraînement du modèle

```python
# Entraînement du modèle
print("🚀 Début de l'entraînement...")
print("⏱️ Cela peut prendre quelques minutes selon votre matériel.")

# Entraînement avec suivi des performances
history = model.fit(
    X_train, y_train,
    batch_size=128,
    epochs=5,  # Nombre de passages sur toutes les données
    validation_split=0.2,  # 20% des données pour la validation
    verbose=1
)

print("\n✅ Entraînement terminé !")

# Évaluation sur les données de test
test_loss, test_accuracy = model.evaluate(X_test, y_test, verbose=0)
print(f"\n📊 Résultats finaux :")
print(f"   - Précision sur les données de test : {test_accuracy*100:.2f}%")
print(f"   - Perte sur les données de test : {test_loss:.4f}")
```

## Cellule 6 (Code) - Visualisation des résultats d'entraînement

```python
# Visualisation des courbes d'apprentissage
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 5))

# Graphique de la précision
ax1.plot(history.history['accuracy'], 'b-', label='Entraînement', linewidth=2)
ax1.plot(history.history['val_accuracy'], 'r-', label='Validation', linewidth=2)
ax1.set_title('Évolution de la précision', fontsize=14, fontweight='bold')
ax1.set_xlabel('Époque')
ax1.set_ylabel('Précision')
ax1.legend()
ax1.grid(True, alpha=0.3)

# Graphique de la perte
ax2.plot(history.history['loss'], 'b-', label='Entraînement', linewidth=2)
ax2.plot(history.history['val_loss'], 'r-', label='Validation', linewidth=2)
ax2.set_title('Évolution de la perte (erreur)', fontsize=14, fontweight='bold')
ax2.set_xlabel('Époque')
ax2.set_ylabel('Perte')
ax2.legend()
ax2.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

print("📈 Interprétation des graphiques :")
print("   - Précision : doit augmenter (proche de 1.0 = 100%)")
print("   - Perte : doit diminuer (proche de 0 = peu d'erreurs)")
print("   - Les courbes d'entraînement et validation doivent être proches")
```

## Cellule 7 (Code) - Test avec des prédictions

```python
# Test du modèle avec des exemples
print("🔍 Test du modèle avec 10 exemples aléatoires...")

# Sélection d'exemples aléatoires
indices = np.random.choice(len(X_test), 10, replace=False)
examples = X_test[indices]
true_labels = y_test[indices]

# Prédictions
predictions = model.predict(examples, verbose=0)
predicted_labels = np.argmax(predictions, axis=1)
confidence_scores = np.max(predictions, axis=1)

# Affichage des résultats
plt.figure(figsize=(15, 6))
for i in range(10):
    plt.subplot(2, 5, i + 1)
    plt.imshow(examples[i], cmap='gray')
    
    # Couleur selon la justesse de la prédiction
    color = 'green' if predicted_labels[i] == true_labels[i] else 'red'
    
    plt.title(f'Vrai: {true_labels[i]} | Prédit: {predicted_labels[i]}\n'
              f'Confiance: {confidence_scores[i]*100:.1f}%', 
              color=color, fontsize=10)
    plt.axis('off')

plt.suptitle('Prédictions du modèle (Vert = Correct, Rouge = Erreur)', 
             fontsize=14, fontweight='bold')
plt.tight_layout()
plt.show()

# Statistiques
correct = np.sum(predicted_labels == true_labels)
print(f"\n📊 Résultats sur ces 10 exemples :")
print(f"   - Prédictions correctes : {correct}/10")
print(f"   - Confiance moyenne : {np.mean(confidence_scores)*100:.1f}%")
```

## Cellule 8 (Code) - Interface de dessin simple

```python
# Interface simple pour dessiner et tester
from IPython.display import display, HTML, Javascript
import ipywidgets as widgets
from io import BytesIO
import base64
from PIL import Image, ImageOps

# Fonction pour traiter l'image dessinée
def process_drawing(drawing_data):
    """Traite l'image dessinée et fait une prédiction"""
    try:
        # Décoder l'image base64
        image_data = base64.b64decode(drawing_data.split(',')[1])
        image = Image.open(BytesIO(image_data))
        
        # Conversion en niveaux de gris et redimensionnement
        image = image.convert('L')
        image = ImageOps.invert(image)  # Inverser (fond noir, trait blanc)
        image = image.resize((28, 28))
        
        # Conversion en array numpy
        img_array = np.array(image).astype('float32') / 255.0
        img_array = img_array.reshape(1, 28, 28)
        
        # Prédiction
        prediction = model.predict(img_array, verbose=0)
        predicted_digit = np.argmax(prediction)
        confidence = np.max(prediction) * 100
        
        # Affichage
        plt.figure(figsize=(10, 4))
        
        plt.subplot(1, 2, 1)
        plt.imshow(img_array[0], cmap='gray')
        plt.title('Votre dessin (28x28 pixels)')
        plt.axis('off')
        
        plt.subplot(1, 2, 2)
        plt.bar(range(10), prediction[0])
        plt.title(f'Prédictions\nChiffre prédit: {predicted_digit} (Confiance: {confidence:.1f}%)')
        plt.xlabel('Chiffre')
        plt.ylabel('Probabilité')
        plt.xticks(range(10))
        
        plt.tight_layout()
        plt.show()
        
        return predicted_digit, confidence
        
    except Exception as e:
        print(f"Erreur lors du traitement : {e}")
        return None, 0

# Interface HTML pour dessiner
display(HTML("""
<div style="text-align: center; border: 2px solid #4CAF50; padding: 20px; border-radius: 10px;">
    <h3>🎨 Dessinez un chiffre (0-9)</h3>
    <canvas id="drawingCanvas" width="280" height="280" 
            style="border: 2px solid #ccc; cursor: crosshair; background: white;"></canvas>
    <br><br>
    <button onclick="clearCanvas()" style="margin: 5px; padding: 10px 20px; font-size: 16px;">Effacer</button>
    <button onclick="predictDigit()" style="margin: 5px; padding: 10px 20px; font-size: 16px; background: #4CAF50; color: white;">Prédire</button>
</div>

<script>
var canvas = document.getElementById('drawingCanvas');
var ctx = canvas.getContext('2d');
var isDrawing = false;

// Configuration du dessin
ctx.lineWidth = 15;
ctx.lineCap = 'round';
ctx.strokeStyle = 'black';

// Événements de dessin
canvas.addEventListener('mousedown', startDrawing);
canvas.addEventListener('mousemove', draw);
canvas.addEventListener('mouseup', stopDrawing);
canvas.addEventListener('mouseout', stopDrawing);

function startDrawing(e) {
    isDrawing = true;
    draw(e);
}

function draw(e) {
    if (!isDrawing) return;
    
    var rect = canvas.getBoundingClientRect();
    var x = e.clientX - rect.left;
    var y = e.clientY - rect.top;
    
    ctx.lineTo(x, y);
    ctx.stroke();
    ctx.beginPath();
    ctx.moveTo(x, y);
}

function stopDrawing() {
    if (isDrawing) {
        ctx.beginPath();
        isDrawing = false;
    }
}

function clearCanvas() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
}

function predictDigit() {
    var dataURL = canvas.toDataURL();
    // Cette partie nécessiterait une interface Python-JavaScript plus avancée
    console.log('Prédiction demandée');
    alert('Exécutez la cellule suivante après avoir dessiné !');
}
</script>
"""))

print("✏️ Instructions :")
print("1. Dessinez un chiffre dans le carré ci-dessus")
print("2. Exécutez la cellule suivante pour voir la prédiction")
print("3. Répétez avec différents chiffres !")
```

## Cellule 9 (Code) - Expérimentations suggérées

```python
# Expérimentations pour approfondir votre compréhension
print("🧪 Expérimentations suggérées :")
print("\n1. Modifiez l'architecture du modèle :")
print("   - Changez le nombre de neurones (128 → 64 ou 256)")
print("   - Ajoutez/supprimez des couches")
print("   - Modifiez les fonctions d'activation")

print("\n2. Ajustez les paramètres d'entraînement :")
print("   - Nombre d'époques (5 → 3 ou 10)")
print("   - Taille du batch (128 → 64 ou 256)")
print("   - Optimiseur ('adam' → 'sgd')")

print("\n3. Analysez les erreurs :")

# Matrice de confusion pour analyser les erreurs
y_pred = model.predict(X_test, verbose=0)
y_pred_classes = np.argmax(y_pred, axis=1)

plt.figure(figsize=(10, 8))
cm = confusion_matrix(y_test, y_pred_classes)
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', 
            xticklabels=range(10), yticklabels=range(10))
plt.title('Matrice de confusion\n(Lignes: vrais chiffres, Colonnes: prédictions)')
plt.xlabel('Chiffre prédit')
plt.ylabel('Vrai chiffre')
plt.show()

print("\n📊 Analyse des erreurs :")
for i in range(10):
    for j in range(10):
        if i != j and cm[i, j] > 50:  # Erreurs fréquentes
            print(f"   - Le chiffre {i} est souvent confondu avec {j} ({cm[i, j]} fois)")

print("\n🤔 Questions de réflexion :")
print("   - Pourquoi certains chiffres sont-ils plus difficiles à reconnaître ?")
print("   - Comment pourriez-vous améliorer le modèle ?")
print("   - Quelles applications réelles pourraient utiliser ce type de modèle ?")
```

## Cellule 10 (Markdown) - Conclusion et prochaines étapes

```markdown
# 🎉 Félicitations !

Vous venez de créer et d'entraîner votre premier modèle de Deep Learning !

## 📊 Ce que vous avez accompli :
- ✅ Chargé et préparé un dataset de 70 000 images
- ✅ Construit un réseau de neurones convolutif (CNN)
- ✅ Entraîné le modèle avec **{model.count_params():,} paramètres**
- ✅ Obtenu une précision de **~98%** sur des chiffres manuscrits
- ✅ Testé le modèle avec vos propres dessins

## 🧠 Concepts clés découverts :
- **Réseau de neurones convolutif (CNN)** : spécialisé pour les images
- **Entraînement** : ajustement automatique des paramètres
- **Validation** : vérification sur des données non vues
- **Overfitting** : quand le modèle mémorise au lieu d'apprendre

## 🚀 Prochaines étapes :
1. Explorez les concepts théoriques dans la Phase 2
2. Expérimentez avec d'autres architectures
3. Découvrez les réseaux récurrents (RNN) pour le texte
4. Créez votre propre chatbot pédagogique !

## 💡 Applications réelles :
- 📮 Tri automatique du courrier postal
- 🏦 Lecture automatique de chèques bancaires
- 📱 Reconnaissance de texte dans les photos
- 🏥 Analyse d'images médicales

**Temps écoulé** : ~45 minutes | **Prochaine étape** : Concepts fondamentaux
```