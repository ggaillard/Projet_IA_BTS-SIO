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

