# Machine Learning Classique - Classification MNIST avec Random Forest

Ce document contient le code et les explications pour le notebook de classification d'images MNIST avec Random Forest (approche Machine Learning classique). Vous pouvez copier-coller chaque section dans une cellule Google Colab.

## Cellule 1 (Markdown) - Introduction

```markdown
# Classification avec Machine Learning classique

## Reconnaissance de chiffres manuscrits avec Random Forest

Dans ce notebook, nous allons implémenter une approche de Machine Learning classique pour la classification des chiffres manuscrits en utilisant le dataset MNIST. Nous utiliserons l'algorithme Random Forest, qui est basé sur un ensemble d'arbres de décision.

### Objectifs :
- Comprendre comment préparer des données d'images pour le ML classique
- Implémenter un classificateur Random Forest
- Évaluer ses performances et ses limites
- Comparer cette approche avec le Deep Learning
```

## Cellule 2 (Code) - Importation des bibliothèques

```python
# Importation des bibliothèques nécessaires
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import time
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import seaborn as sns
from sklearn.pipeline import Pipeline
from google.colab import output
output.enable_custom_widget_manager()
import ipywidgets as widgets
```

## Cellule 3 (Markdown) - Chargement des données

```markdown
## Chargement et exploration des données

Le dataset MNIST contient 70 000 images de chiffres manuscrits (0-9) en niveaux de gris. Chaque image est de taille 28x28 pixels, ce qui donne 784 pixels par image.
```

## Cellule 4 (Code) - Chargement des données MNIST

```python
print("Chargement du jeu de données MNIST...")
# Utilisation du jeu de données MNIST intégré à sklearn
from sklearn.datasets import fetch_openml
mnist = fetch_openml('mnist_784', version=1, as_frame=False)
X, y = mnist["data"], mnist["target"]
X = X / 255.0  # Normalisation des valeurs de pixels entre 0 et 1
y = y.astype(np.uint8)  # Conversion des labels en entiers

# Exploration des données
print(f"Dimensions du jeu de données: {X.shape}")
print(f"Nombre de classes: {len(np.unique(y))}")
```

## Cellule 5 (Code) - Visualisation des exemples

```python
# Affichage de quelques exemples
plt.figure(figsize=(10, 5))
for i in range(10):
    plt.subplot(2, 5, i + 1)
    plt.imshow(X[i].reshape(28, 28), cmap='gray')
    plt.title(f"Label: {y[i]}")
    plt.axis('off')
plt.tight_layout()
plt.suptitle("Exemples de chiffres manuscrits", y=1.05)
plt.show()
```

## Cellule 6 (Markdown) - Préparation des données

```markdown
## Préparation des données pour Machine Learning classique

Contrairement aux réseaux de neurones convolutifs (CNN), les algorithmes de ML classiques comme Random Forest ne sont pas conçus pour traiter directement des images. Nous devons donc :

1. Réduire la dimensionnalité des données (784 caractéristiques est trop élevé)
2. Extraire des caractéristiques pertinentes

Nous utiliserons l'Analyse en Composantes Principales (PCA) pour réduire la dimensionnalité tout en conservant l'essentiel de l'information.
```

## Cellule 7 (Code) - Préparation des données

```python
print("\n--- Préparation des données pour Random Forest ---")
print("Pour le Machine Learning classique, nous devons souvent extraire des caractéristiques manuellement.")

# Réduction de dimension avec PCA pour accélérer l'entraînement
print("Application d'une réduction de dimension (PCA)...")
n_components = 50  # Réduire de 784 à 50 caractéristiques

# Séparation en ensembles d'entraînement et de test
# Utilisation d'un échantillon réduit pour accélérer la démonstration
X_sample = X[:10000]
y_sample = y[:10000]

X_train, X_test, y_train, y_test = train_test_split(X_sample, y_sample, test_size=0.2, random_state=42)

print(f"Taille de l'ensemble d'entraînement: {X_train.shape}")
print(f"Taille de l'ensemble de test: {X_test.shape}")

# Création d'un pipeline d'extraction de caractéristiques
feature_pipeline = Pipeline([
    ('scaler', StandardScaler()),  # Normalisation des données
    ('pca', PCA(n_components=n_components))  # Réduction de dimension par PCA
])

# Application aux données
print("Extraction de caractéristiques...")
X_train_features = feature_pipeline.fit_transform(X_train)
X_test_features = feature_pipeline.transform(X_test)

print(f"Dimensions après extraction de caractéristiques: {X_train_features.shape}")
```

## Cellule 8 (Markdown) - Entraînement du modèle

```markdown
## Entraînement du modèle Random Forest

Nous allons maintenant entraîner un classificateur Random Forest sur nos données prétraitées. Random Forest est un algorithme d'ensemble qui combine les prédictions de plusieurs arbres de décision pour améliorer la précision et contrôler le sur-apprentissage.

Principaux hyperparamètres :
- **n_estimators** : Nombre d'arbres dans la forêt
- **max_depth** : Profondeur maximale de chaque arbre
- **min_samples_split** : Nombre minimum d'échantillons requis pour diviser un nœud
```

## Cellule 9 (Code) - Entraînement du modèle

```python
print("\n--- Entraînement du modèle Random Forest ---")

# Paramètres du modèle - vous pouvez les modifier
n_estimators = 100  # Nombre d'arbres
max_depth = 10      # Profondeur maximale des arbres
min_samples_split = 2  # Nombre minimum d'échantillons requis pour diviser un nœud

# Création du modèle
rf_model = RandomForestClassifier(
    n_estimators=n_estimators,
    max_depth=max_depth,
    min_samples_split=min_samples_split,
    random_state=42,
    n_jobs=-1  # Utiliser tous les cœurs disponibles
)

# Mesure du temps d'entraînement
start_time = time.time()
print("Entraînement du modèle en cours...")
rf_model.fit(X_train_features, y_train)
end_time = time.time()
training_time = end_time - start_time

print(f"Temps d'entraînement: {training_time:.2f} secondes")
```

## Cellule 10 (Markdown) - Évaluation du modèle

```markdown
## Évaluation du modèle

Évaluons maintenant les performances de notre modèle Random Forest sur l'ensemble de test. Nous utiliserons plusieurs métriques :
- Précision globale (accuracy)
- Matrice de confusion
- Rapport de classification détaillé (précision, rappel, F1-score pour chaque classe)
```

## Cellule 11 (Code) - Évaluation et métriques

```python
print("\n--- Évaluation du modèle Random Forest ---")

# Prédictions sur l'ensemble de test
y_pred = rf_model.predict(X_test_features)

# Calcul des métriques
accuracy = accuracy_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)
class_report = classification_report(y_test, y_pred)

print(f"Précision globale: {accuracy*100:.2f}%")
print("\nMatrice de confusion:")
plt.figure(figsize=(8, 6))
sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues')
plt.xlabel('Prédictions')
plt.ylabel('Valeurs réelles')
plt.title('Matrice de confusion')
plt.show()

print("\nRapport de classification:")
print(class_report)
```

## Cellule 12 (Markdown) - Analyse des erreurs

```markdown
## Analyse des erreurs

Examinons quelques exemples que notre modèle a mal classifiés pour mieux comprendre ses limites.
```

## Cellule 13 (Code) - Visualisation des erreurs

```python
print("\n--- Analyse des erreurs ---")

# Identifier les erreurs
error_indices = np.where(y_pred != y_test)[0]
n_errors = min(10, len(error_indices))  # Afficher max 10 erreurs

if n_errors > 0:
    plt.figure(figsize=(12, 4))
    for i, idx in enumerate(error_indices[:n_errors]):
        plt.subplot(2, 5, i + 1)
        # Récupérer l'image originale
        img = X_test[idx].reshape(28, 28)
        plt.imshow(img, cmap='gray')
        plt.title(f"Réel: {y_test[idx]}\nPrédit: {y_pred[idx]}")
        plt.axis('off')
    plt.tight_layout()
    plt.suptitle("Exemples d'erreurs de classification", y=1.05)
    plt.show()
else:
    print("Aucune erreur trouvée dans l'échantillon de test!")
```

## Cellule 14 (Markdown) - Importance des caractéristiques

```markdown
## Importance des caractéristiques

Un avantage des modèles comme Random Forest est leur interprétabilité. Nous pouvons examiner quelles caractéristiques (ici, quelles composantes principales) le modèle considère comme les plus importantes pour faire ses prédictions.
```

## Cellule 15 (Code) - Visualisation de l'importance des caractéristiques

```python
print("\n--- Importance des caractéristiques ---")
# Visualiser l'importance des composantes principales
feature_importance = rf_model.feature_importances_
sorted_idx = np.argsort(feature_importance)[::-1]

plt.figure(figsize=(10, 5))
plt.bar(range(20), feature_importance[sorted_idx[:20]])
plt.xticks(range(20), [f"Feat {i}" for i in sorted_idx[:20]], rotation=90)
plt.xlabel('Composantes principales')
plt.ylabel('Importance')
plt.title('Top 20 des composantes principales les plus importantes')
plt.tight_layout()
plt.show()

print("Les caractéristiques les plus importantes sont les composantes principales qui capturent le plus de variance dans les données.")
```

## Cellule 16 (Markdown) - Test de généralisation

```markdown
## Test de généralisation

Une question fondamentale en Machine Learning est : "Comment le modèle se comporte-t-il face à des données légèrement différentes de celles sur lesquelles il a été entraîné ?"

Testons la robustesse de notre modèle face à deux types de perturbations :
1. Ajout de bruit aléatoire
2. Rotation des images

Ces tests simulent des conditions plus réalistes où les données peuvent varier légèrement.
```

## Cellule 17 (Code) - Création de données modifiées

```python
print("\n--- Défi de généralisation ---")
print("Nous allons maintenant tester le modèle sur des chiffres légèrement modifiés pour évaluer sa capacité de généralisation.")

# Fonction pour ajouter du bruit aux images
def add_noise(images, noise_level=0.2):
    noisy_images = images.copy()
    noise = np.random.normal(0, noise_level, images.shape)
    noisy_images = noisy_images + noise
    # Assurer que les valeurs restent entre 0 et 1
    noisy_images = np.clip(noisy_images, 0, 1)
    return noisy_images

# Fonction pour appliquer une rotation aux images
def rotate_images(images, max_angle=15):
    from scipy.ndimage import rotate
    rotated_images = np.zeros_like(images)
    for i, img in enumerate(images):
        angle = np.random.uniform(-max_angle, max_angle)
        img_2d = img.reshape(28, 28)
        rotated = rotate(img_2d, angle, reshape=False)
        rotated_images[i] = rotated.flatten()
    return rotated_images

# Créer un jeu de données modifié
print("Création d'un jeu de données avec des chiffres modifiés...")

# Utiliser la partie restante des données pour ce test
X_new = X[10000:12000]
y_new = y[10000:12000]

# Appliquer des transformations
X_new_noisy = add_noise(X_new, noise_level=0.2)
X_new_rotated = rotate_images(X_new, max_angle=15)
```

## Cellule 18 (Code) - Visualisation des données modifiées

```python
# Visualiser quelques exemples
plt.figure(figsize=(12, 8))
for i in range(5):
    # Original
    plt.subplot(3, 5, i + 1)
    plt.imshow(X_new[i].reshape(28, 28), cmap='gray')
    plt.title(f"Original: {y_new[i]}")
    plt.axis('off')
    
    # Avec bruit
    plt.subplot(3, 5, i + 6)
    plt.imshow(X_new_noisy[i].reshape(28, 28), cmap='gray')
    plt.title("Avec bruit")
    plt.axis('off')
    
    # Avec rotation
    plt.subplot(3, 5, i + 11)
    plt.imshow(X_new_rotated[i].reshape(28, 28), cmap='gray')
    plt.title("Avec rotation")
    plt.axis('off')

plt.tight_layout()
plt.suptitle("Exemples de chiffres modifiés", y=1.02)
plt.show()
```

## Cellule 19 (Code) - Évaluation sur données modifiées

```python
# Évaluer le modèle sur les données modifiées
print("\nÉvaluation sur les données avec bruit:")
X_new_noisy_features = feature_pipeline.transform(X_new_noisy)
y_new_noisy_pred = rf_model.predict(X_new_noisy_features)
accuracy_noisy = accuracy_score(y_new, y_new_noisy_pred)
print(f"Précision sur données bruitées: {accuracy_noisy*100:.2f}%")

print("\nÉvaluation sur les données avec rotation:")
X_new_rotated_features = feature_pipeline.transform(X_new_rotated)
y_new_rotated_pred = rf_model.predict(X_new_rotated_features)
accuracy_rotated = accuracy_score(y_new, y_new_rotated_pred)
print(f"Précision sur données pivotées: {accuracy_rotated*100:.2f}%")

print("\nComparaison avec la précision originale:")
print(f"Précision sur données originales: {accuracy*100:.2f}%")
print(f"Précision sur données bruitées: {accuracy_noisy*100:.2f}%")
print(f"Précision sur données pivotées: {accuracy_rotated*100:.2f}%")
```

## Cellule 20 (Markdown) - Conclusions

```markdown
## Conclusions sur le Machine Learning classique

Après avoir implémenté et testé notre modèle Random Forest pour la classification des chiffres manuscrits, nous pouvons tirer plusieurs conclusions :

### Points forts du Random Forest:
- Entraînement relativement rapide
- Bonnes performances sur les données originales
- Interprétabilité (importance des caractéristiques)

### Limites:
- Nécessite une extraction manuelle de caractéristiques (PCA dans notre cas)
- Sensibilité aux transformations des données (bruit, rotation)
- Difficulté à capturer des motifs complexes sans feature engineering approprié

### Questions pour la réflexion:
1. Pourquoi avons-nous besoin de réduire la dimensionnalité pour le Random Forest?
2. Comment pourrait-on améliorer la robustesse aux transformations?
3. Quelles autres caractéristiques pourraient être extraites manuellement pour améliorer les performances?
```

## Cellule 21 (Markdown) - Widget interactif

```markdown
## Tester le modèle vous-même

Utilisez le widget ci-dessous pour tester le modèle sur différents exemples. Vous pourrez voir l'image et la prédiction correspondante.
```

## Cellule 22 (Code) - Widget interactif

```python
print("\n--- Testez le modèle vous-même ---")

def test_model(digit_idx):
    if digit_idx < len(X_test):
        # Afficher l'image
        img = X_test[digit_idx].reshape(28, 28)
        plt.figure(figsize=(6, 6))
        plt.imshow(img, cmap='gray')
        plt.title(f"Chiffre à classifier")
        plt.axis('off')
        plt.show()
        
        # Faire la prédiction
        features = feature_pipeline.transform([X_test[digit_idx]])
        prediction = rf_model.predict(features)[0]
        real_label = y_test[digit_idx]
        
        print(f"Prédiction du modèle Random Forest: {prediction}")
        print(f"Étiquette réelle: {real_label}")
        print(f"Prédiction {'correcte' if prediction == real_label else 'incorrecte'}")
    else:
        print("Index hors limites!")

# Créer un slider pour sélectionner un chiffre à tester
digit_selector = widgets.IntSlider(
    value=0,
    min=0,
    max=len(X_test)-1,
    step=1,
    description='Index:',
    continuous_update=False
)

# Bouton pour exécuter le test
test_button = widgets.Button(description="Tester")
output = widgets.Output()

def on_button_clicked(b):
    with output:
        output.clear_output()
        test_model(digit_selector.value)

test_button.on_click(on_button_clicked)

# Afficher les widgets
display(widgets.HBox([digit_selector, test_button]))
display(output)

print("Utilisez le slider pour sélectionner un index et cliquez sur 'Tester' pour classifier le chiffre correspondant.")
```