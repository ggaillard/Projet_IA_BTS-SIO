# RNN/LSTM pour l'analyse de sentiment - Notebook complet

Ce notebook vous guide dans la création d'un modèle LSTM pour analyser le sentiment de textes (positif/négatif).

## Cellule 1 (Markdown) - Introduction

```markdown
# 🧠 RNN/LSTM pour l'analyse de sentiment

## Découverte des réseaux récurrents avec un cas concret

Dans ce notebook, vous allez :
- ✅ Comprendre comment les RNN traitent les séquences de texte
- ✅ Créer un modèle LSTM pour analyser le sentiment
- ✅ Visualiser les embeddings de mots
- ✅ Tester le modèle sur vos propres phrases

**Durée estimée** : 50 minutes

**Cas d'usage** : Analyser automatiquement les avis clients, commentaires, etc.
```

## Cellule 2 (Code) - Configuration et imports

```python
# Imports nécessaires
import tensorflow as tf
from tensorflow.keras.datasets import imdb
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense, Dropout
from tensorflow.keras.preprocessing import sequence
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.manifold import TSNE
import pandas as pd

# Configuration
print(f"TensorFlow version: {tf.__version__}")
print("GPU disponible:", "Oui" if tf.config.list_physical_devices('GPU') else "Non")

# Paramètres du modèle
MAX_FEATURES = 5000  # Nombre de mots dans le vocabulaire
MAX_LEN = 200       # Longueur maximale des séquences
EMBEDDING_SIZE = 128 # Taille des embeddings

print("\n✅ Configuration terminée !")
```

## Cellule 3 (Code) - Chargement et exploration des données

```python
# Chargement du dataset IMDB (avis de films)
print("📥 Chargement du dataset IMDB...")
(X_train, y_train), (X_test, y_test) = imdb.load_data(num_words=MAX_FEATURES)

print(f"📊 Données d'entraînement : {len(X_train)} avis")
print(f"📊 Données de test : {len(X_test)} avis")
print(f"📊 Vocabulaire : {MAX_FEATURES} mots les plus fréquents")

# Récupération du dictionnaire de mots
word_index = imdb.get_word_index()
reverse_word_index = {v: k for k, v in word_index.items()}
reverse_word_index[0] = '<PAD>'
reverse_word_index[1] = '<START>'
reverse_word_index[2] = '<UNKNOWN>'

def decode_review(encoded_review):
    """Convertit une séquence d'indices en texte lisible"""
    return ' '.join([reverse_word_index.get(i, '<UNKNOWN>') for i in encoded_review])

# Affichage de quelques exemples
print("\n📝 Exemples d'avis (avant preprocessing) :")
for i in range(3):
    sentiment = "😊 POSITIF" if y_train[i] == 1 else "😞 NÉGATIF"
    print(f"\n{sentiment} - Longueur: {len(X_train[i])} mots")
    decoded = decode_review(X_train[i])
    # Afficher seulement les premiers mots pour la lisibilité
    print(f"Texte: {decoded[:200]}...")

# Distribution des longueurs
lengths = [len(x) for x in X_train]
plt.figure(figsize=(12, 4))

plt.subplot(1, 2, 1)
plt.hist(lengths, bins=50, alpha=0.7)
plt.title('Distribution des longueurs d\'avis')
plt.xlabel('Nombre de mots')
plt.ylabel('Fréquence')
plt.axvline(MAX_LEN, color='red', linestyle='--', label=f'Limite fixée: {MAX_LEN}')
plt.legend()

plt.subplot(1, 2, 2)
plt.hist(y_train, bins=2, alpha=0.7, color=['red', 'green'])
plt.title('Distribution des sentiments')
plt.xlabel('Sentiment (0=Négatif, 1=Positif)')
plt.ylabel('Nombre d\'avis')
plt.xticks([0, 1], ['Négatif', 'Positif'])

plt.tight_layout()
plt.show()

print(f"\n📊 Statistiques des longueurs :")
print(f"   - Longueur moyenne : {np.mean(lengths):.1f} mots")
print(f"   - Longueur médiane : {np.median(lengths):.1f} mots")
print(f"   - Avis > {MAX_LEN} mots : {np.sum(np.array(lengths) > MAX_LEN)}")
```

## Cellule 4 (Code) - Préparation des données

```python
# Padding des séquences (toutes à la même longueur)
print("🔧 Préparation des données...")
print(f"   - Troncature/padding à {MAX_LEN} mots")

X_train = sequence.pad_sequences(X_train, maxlen=MAX_LEN, padding='post')
X_test = sequence.pad_sequences(X_test, maxlen=MAX_LEN, padding='post')

print(f"   - Forme finale X_train : {X_train.shape}")
print(f"   - Forme finale X_test : {X_test.shape}")

# Visualisation de l'effet du padding
exemple_idx = 0
print(f"\n📝 Exemple de preprocessing :")
print(f"   - Avis original : {len([x for x in X_train[exemple_idx] if x != 0])} mots utiles")
print(f"   - Après padding : {X_train.shape[1]} positions")
print(f"   - Premières valeurs : {X_train[exemple_idx][:20]}")
print(f"   - (0 = padding, autres = indices de mots)")

# Conversion en format approprié pour TensorFlow
X_train = X_train.astype('int32')
X_test = X_test.astype('int32')
y_train = y_train.astype('int32') 
y_test = y_test.astype('int32')

print("\n✅ Données préparées pour l'entraînement !")
```

## Cellule 5 (Code) - Construction du modèle LSTM

```python
# Construction du modèle LSTM
print("🏗️ Construction du modèle LSTM...")

model = Sequential([
    # Couche d'embedding : convertit les indices en vecteurs denses
    Embedding(
        input_dim=MAX_FEATURES,    # Taille du vocabulaire
        output_dim=EMBEDDING_SIZE, # Dimension des embeddings
        input_length=MAX_LEN,      # Longueur des séquences
        name='embedding'
    ),
    
    # Couche LSTM : traite les séquences
    LSTM(
        units=64,           # Nombre d'unités LSTM
        dropout=0.2,        # Dropout sur les entrées
        recurrent_dropout=0.2,  # Dropout sur les connexions récurrentes
        name='lstm'
    ),
    
    # Couche de régularisation
    Dropout(0.5, name='dropout'),
    
    # Couche de sortie : classification binaire
    Dense(1, activation='sigmoid', name='output')
])

# Compilation du modèle
model.compile(
    optimizer='adam',
    loss='binary_crossentropy',
    metrics=['accuracy']
)

# Affichage de l'architecture
print("\n📋 Architecture du modèle :")
model.summary()

print(f"\n🔢 Détails des couches :")
print(f"   - Embedding : {MAX_FEATURES} mots → {EMBEDDING_SIZE} dimensions")
print(f"   - LSTM : 64 unités avec mémoire séquentielle")
print(f"   - Dense : 1 neurone pour classification binaire (0-1)")
print(f"   - Total paramètres : {model.count_params():,}")
```

## Cellule 6 (Code) - Entraînement du modèle

```python
# Entraînement du modèle
print("🚀 Début de l'entraînement...")
print("⏱️ Les LSTM sont plus lents que les CNN, patience !")

# Entraînement avec validation
history = model.fit(
    X_train, y_train,
    batch_size=128,
    epochs=3,  # Peu d'époques pour la démonstration
    validation_split=0.2,
    verbose=1
)

# Évaluation finale
test_loss, test_accuracy = model.evaluate(X_test, y_test, verbose=0)
print(f"\n📊 Résultats finaux :")
print(f"   - Précision sur test : {test_accuracy*100:.2f}%")
print(f"   - Perte sur test : {test_loss:.4f}")

# Visualisation des courbes d'apprentissage
plt.figure(figsize=(15, 5))

plt.subplot(1, 2, 1)
plt.plot(history.history['accuracy'], 'b-', label='Entraînement', linewidth=2)
plt.plot(history.history['val_accuracy'], 'r-', label='Validation', linewidth=2)
plt.title('Évolution de la précision')
plt.xlabel('Époque')
plt.ylabel('Précision')
plt.legend()
plt.grid(True, alpha=0.3)

plt.subplot(1, 2, 2)
plt.plot(history.history['loss'], 'b-', label='Entraînement', linewidth=2)
plt.plot(history.history['val_loss'], 'r-', label='Validation', linewidth=2)
plt.title('Évolution de la perte')
plt.xlabel('Époque')
plt.ylabel('Perte')
plt.legend()
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

print("\n✅ Entraînement terminé !")
```

## Cellule 7 (Code) - Test et prédictions

```python
# Test du modèle sur quelques exemples
print("🔍 Test du modèle sur des exemples...")

# Sélection d'exemples
indices = np.random.choice(len(X_test), 8, replace=False)
test_examples = X_test[indices]
true_labels = y_test[indices]

# Prédictions
predictions = model.predict(test_examples, verbose=0)
predicted_probs = predictions.flatten()
predicted_labels = (predicted_probs > 0.5).astype(int)

# Affichage des résultats
print("\n📝 Exemples de prédictions :")
for i in range(8):
    true_sentiment = "😊 POSITIF" if true_labels[i] == 1 else "😞 NÉGATIF"
    pred_sentiment = "😊 POSITIF" if predicted_labels[i] == 1 else "😞 NÉGATIF"
    confidence = predicted_probs[i] if predicted_labels[i] == 1 else 1 - predicted_probs[i]
    correct = "✅" if true_labels[i] == predicted_labels[i] else "❌"
    
    print(f"\n{correct} Exemple {i+1}:")
    print(f"   Réel: {true_sentiment} | Prédit: {pred_sentiment} | Confiance: {confidence:.1%}")
    
    # Décoder quelques mots du texte
    decoded_text = decode_review(test_examples[i])
    # Afficher les premiers mots (sans les balises techniques)
    clean_text = decoded_text.replace('<START>', '').replace('<PAD>', '').strip()
    words = clean_text.split()[:15]  # Premiers 15 mots
    print(f"   Texte: {' '.join(words)}...")

# Matrice de confusion simple
from sklearn.metrics import confusion_matrix, classification_report

y_pred_all = (model.predict(X_test, verbose=0) > 0.5).astype(int).flatten()

print(f"\n📊 Performance globale sur l'ensemble de test :")
print(f"   - Précision : {test_accuracy:.1%}")
print(f"   - Exemples corrects : {np.sum(y_test == y_pred_all)}/{len(y_test)}")

# Matrice de confusion
cm = confusion_matrix(y_test, y_pred_all)
plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', 
            xticklabels=['Négatif', 'Positif'], 
            yticklabels=['Négatif', 'Positif'])
plt.title('Matrice de confusion')
plt.xlabel('Prédictions')
plt.ylabel('Réalité')
plt.show()

print(f"\nRapport de classification :")
print(classification_report(y_test, y_pred_all, target_names=['Négatif', 'Positif']))
```

## Cellule 8 (Code) - Visualisation des embeddings de mots

```python
# Extraction et visualisation des embeddings
print("🎨 Visualisation des embeddings de mots...")

# Récupération de la couche d'embedding
embedding_layer = model.get_layer('embedding')
embeddings = embedding_layer.get_weights()[0]  # Matrice des embeddings

print(f"📊 Dimensions des embeddings : {embeddings.shape}")
print(f"   - {embeddings.shape[0]} mots dans le vocabulaire")
print(f"   - {embeddings.shape[1]} dimensions par mot")

# Sélection de mots intéressants pour la visualisation
interesting_words = [
    'good', 'great', 'excellent', 'amazing', 'wonderful', 'fantastic',  # Mots positifs
    'bad', 'terrible', 'awful', 'horrible', 'worst', 'hate',           # Mots négatifs
    'movie', 'film', 'story', 'actor', 'acting', 'director',          # Mots neutres/contexte
    'boring', 'interesting', 'funny', 'dramatic', 'beautiful'         # Mots descriptifs
]

# Récupération des indices et embeddings de ces mots
word_indices = []
word_labels = []
for word in interesting_words:
    if word in word_index and word_index[word] < MAX_FEATURES:
        idx = word_index[word]
        word_indices.append(idx)
        word_labels.append(word)

selected_embeddings = embeddings[word_indices]

print(f"\n🔍 Mots sélectionnés pour visualisation : {len(word_labels)}")

# Réduction de dimension avec t-SNE
print("🔄 Réduction de dimension en cours (t-SNE)...")
tsne = TSNE(n_components=2, random_state=42, perplexity=min(30, len(word_labels)-1))
embeddings_2d = tsne.fit_transform(selected_embeddings)

# Visualisation
plt.figure(figsize=(14, 10))

# Coloration par type de mot
colors = []
for word in word_labels:
    if word in ['good', 'great', 'excellent', 'amazing', 'wonderful', 'fantastic']:
        colors.append('green')
    elif word in ['bad', 'terrible', 'awful', 'horrible', 'worst', 'hate']:
        colors.append('red')
    elif word in ['movie', 'film', 'story', 'actor', 'acting', 'director']:
        colors.append('blue')
    else:
        colors.append('orange')

scatter = plt.scatter(embeddings_2d[:, 0], embeddings_2d[:, 1], 
                     c=colors, s=100, alpha=0.7)

# Ajout des labels
for i, word in enumerate(word_labels):
    plt.annotate(word, (embeddings_2d[i, 0], embeddings_2d[i, 1]), 
                xytext=(5, 5), textcoords='offset points', 
                fontsize=12, fontweight='bold')

plt.title('Visualisation des embeddings de mots\n' + 
          'Vert: Positif | Rouge: Négatif | Bleu: Contexte | Orange: Descriptif', 
          fontsize=14)
plt.xlabel('Dimension t-SNE 1')
plt.ylabel('Dimension t-SNE 2')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

print(f"\n💡 Observations attendues :")
print(f"   - Les mots positifs (verts) se regroupent ensemble")
print(f"   - Les mots négatifs (rouges) forment un autre cluster")
print(f"   - Les mots de contexte (bleus) sont plus dispersés")
print(f"   - Plus les mots sont proches, plus ils sont sémantiquement similaires")
```

## Cellule 9 (Code) - Test avec vos propres phrases

```python
# Fonction pour tester des phrases personnalisées
def predict_sentiment(text, model, word_index, max_features=MAX_FEATURES, max_len=MAX_LEN):
    """
    Prédit le sentiment d'un texte personnalisé
    """
    # Prétraitement du texte
    words = text.lower().split()
    
    # Conversion en indices
    sequence = []
    for word in words:
        if word in word_index and word_index[word] < max_features:
            sequence.append(word_index[word])
        else:
            sequence.append(2)  # <UNKNOWN>
    
    # Padding
    if len(sequence) < max_len:
        sequence = sequence + [0] * (max_len - len(sequence))
    else:
        sequence = sequence[:max_len]
    
    # Prédiction
    sequence = np.array([sequence])
    prediction = model.predict(sequence, verbose=0)[0][0]
    
    sentiment = "😊 POSITIF" if prediction > 0.5 else "😞 NÉGATIF"
    confidence = prediction if prediction > 0.5 else 1 - prediction
    
    return sentiment, confidence, prediction

# Test avec des phrases d'exemple
print("🧪 Test avec des phrases personnalisées :")

test_sentences = [
    "This movie is absolutely fantastic and amazing",
    "I hated this film it was terrible and boring",
    "The movie was okay nothing special",
    "Best movie I have ever seen in my life",
    "Worst acting and stupid story",
    "The cinematography was beautiful but the story was confusing",
    "Not bad but could be better",
    "This film changed my life incredible experience"
]

print("\n📱 Résultats des tests :")
for i, sentence in enumerate(test_sentences, 1):
    sentiment, confidence, raw_score = predict_sentiment(sentence, model, word_index)
    print(f"\n{i}. \"{sentence}\"")
    print(f"   → {sentiment} (confiance: {confidence:.1%}, score brut: {raw_score:.3f})")

# Test interactif (optionnel)
print(f"\n🎯 Testez vos propres phrases !")
print(f"💡 Tapez 'quit' pour terminer")

while True:
    try:
        user_input = input("\n✏️  Entrez une phrase en anglais : ")
        if user_input.lower() == 'quit':
            break
        
        sentiment, confidence, raw_score = predict_sentiment(user_input, model, word_index)
        print(f"📊 Résultat : {sentiment} (confiance: {confidence:.1%})")
        
        # Analyse des mots
        words = user_input.lower().split()
        print(f"🔍 Mots analysés : {len(words)} mots")
        unknown_words = [w for w in words if w not in word_index or word_index[w] >= MAX_FEATURES]
        if unknown_words:
            print(f"❓ Mots inconnus du modèle : {', '.join(unknown_words[:5])}")
    
    except KeyboardInterrupt:
        break
    except Exception as e:
        print(f"❌ Erreur : {e}")

print("\n✅ Tests terminés !")
```

## Cellule 10 (Code) - Analyse des limites et erreurs

```python
# Analyse des erreurs du modèle
print("🔍 Analyse des erreurs et limites du modèle...")

# Trouver des exemples mal classifiés
y_pred_proba = model.predict(X_test, verbose=0).flatten()
y_pred = (y_pred_proba > 0.5).astype(int)

# Indices des erreurs
wrong_predictions = np.where(y_test != y_pred)[0]

print(f"📊 Statistiques d'erreurs :")
print(f"   - Erreurs totales : {len(wrong_predictions)}/{len(y_test)} ({len(wrong_predictions)/len(y_test):.1%})")

# Analyser les types d'erreurs
false_positives = np.where((y_test == 0) & (y_pred == 1))[0]  # Prédit positif alors que c'est négatif
false_negatives = np.where((y_test == 1) & (y_pred == 0))[0]  # Prédit négatif alors que c'est positif

print(f"   - Faux positifs : {len(false_positives)} (négatifs classés comme positifs)")
print(f"   - Faux négatifs : {len(false_negatives)} (positifs classés comme négatifs)")

# Examiner quelques erreurs intéressantes
print(f"\n🔍 Exemples d'erreurs intéressantes :")

# Faux positifs avec haute confiance
if len(false_positives) > 0:
    fp_confident = false_positives[np.argsort(y_pred_proba[false_positives])[-3:]]  # Top 3 plus confiants
    print(f"\n❌ Faux positifs (négatifs prédits comme positifs) :")
    for i, idx in enumerate(fp_confident):
        print(f"\n{i+1}. Confiance: {y_pred_proba[idx]:.1%}")
        decoded = decode_review(X_test[idx])
        clean_text = decoded.replace('<START>', '').replace('<PAD>', '').strip()
        words = clean_text.split()[:25]
        print(f"   Texte: {' '.join(words)}...")

# Faux négatifs avec haute confiance
if len(false_negatives) > 0:
    fn_confident = false_negatives[np.argsort(y_pred_proba[false_negatives])[:3]]  # Top 3 moins confiants
    print(f"\n❌ Faux négatifs (positifs prédits comme négatifs) :")
    for i, idx in enumerate(fn_confident):
        print(f"\n{i+1}. Confiance: {1-y_pred_proba[idx]:.1%}")
        decoded = decode_review(X_test[idx])
        clean_text = decoded.replace('<START>', '').replace('<PAD>', '').strip()
        words = clean_text.split()[:25]
        print(f"   Texte: {' '.join(words)}...")

# Test de cas difficiles
print(f"\n🧪 Test de cas difficiles :")

difficult_cases = [
    "This movie is not bad",  # Négation
    "I expected it to be terrible but it was actually okay",  # Contraste
    "The worst movie ever... just kidding it was great",  # Sarcasme
    "So bad it's good",  # Paradoxe
    "Could have been better",  # Nuance
]

for case in difficult_cases:
    sentiment, confidence, raw_score = predict_sentiment(case, model, word_index)
    print(f"\n📝 \"{case}\"")
    print(f"   → {sentiment} (confiance: {confidence:.1%})")
    print(f"   💭 Analyse: Cette phrase contient des nuances difficiles à interpréter")

print(f"\n💡 Limites observées du modèle LSTM :")
print(f"   ✅ Forces :")
print(f"      - Bonne compréhension du contexte général")
print(f"      - Capture des dépendances à long terme")
print(f"      - Robuste aux variations de formulation")
print(f"   ❌ Limites :")
print(f"      - Difficulté avec le sarcasme et l'ironie")
print(f"      - Problèmes avec les négations complexes")
print(f"      - Sensible aux expressions idiomatiques")
print(f"      - Nécessite beaucoup de données d'entraînement")
```

## Cellule 11 (Code) - Comparaison avec Mistral AI (optionnel)

```python
# Comparaison avec une approche moderne (API Mistral)
print("🆚 Comparaison avec l'API Mistral AI...")

# Note: Cette section nécessite une clé API Mistral
# Remplacez 'your_api_key' par votre vraie clé API

def analyze_with_mistral(text, api_key=None):
    """
    Analyse de sentiment avec l'API Mistral (simulation)
    """
    if api_key is None:
        # Simulation pour la démonstration
        print("⚠️  Clé API manquante - Simulation activée")
        
        # Logique simplifiée pour la simulation
        positive_words = ['good', 'great', 'excellent', 'amazing', 'wonderful', 'fantastic', 'best', 'love']
        negative_words = ['bad', 'terrible', 'awful', 'horrible', 'worst', 'hate', 'boring']
        
        text_lower = text.lower()
        pos_count = sum(1 for word in positive_words if word in text_lower)
        neg_count = sum(1 for word in negative_words if word in text_lower)
        
        if pos_count > neg_count:
            return "😊 POSITIF", 0.85
        elif neg_count > pos_count:
            return "😞 NÉGATIF", 0.85
        else:
            return "😐 NEUTRE", 0.60
    else:
        # Code réel pour l'API Mistral (à implémenter)
        print("🔄 Appel à l'API Mistral...")
        # Implémentation réelle ici
        pass

# Tests comparatifs
comparison_sentences = [
    "This movie is absolutely fantastic",
    "I hated this boring film",
    "The movie was not bad at all",
    "This film is so bad it's good"
]

print(f"\n📊 Comparaison des approches :")
print(f"{'Phrase':<40} {'LSTM':<15} {'Mistral':<15} {'Accord'}")
print(f"{'='*40} {'='*15} {'='*15} {'='*6}")

for sentence in comparison_sentences:
    # Prédiction LSTM
    lstm_sentiment, lstm_conf, _ = predict_sentiment(sentence, model, word_index)
    
    # Prédiction Mistral (simulée)
    mistral_sentiment, mistral_conf = analyze_with_mistral(sentence)
    
    # Accord entre les deux
    accord = "✅" if lstm_sentiment.split()[1] == mistral_sentiment.split()[1] else "❌"
    
    print(f"{sentence[:38]:<40} {lstm_sentiment:<15} {mistral_sentiment:<15} {accord}")

print(f"\n💭 Réflexions sur les différences :")
print(f"   - LSTM : Basé sur des patterns appris des données d'entraînement")
print(f"   - Mistral : Modèle plus large avec compréhension contextuelle avancée")
print(f"   - Accord général mais différences sur les cas complexes")
```

## Cellule 12 (Markdown) - Questions de réflexion et exercices

```markdown
## 🤔 Questions de réflexion

Après avoir terminé ce notebook, réfléchissez aux questions suivantes :

### 1. Architecture et fonctionnement
- Comment le texte est-il transformé en données numériques utilisables par le LSTM ?
- Pourquoi utilise-t-on des embeddings plutôt que du one-hot encoding ?
- Quel est le rôle de chaque porte dans une cellule LSTM ?

### 2. Preprocessing et données
- Pourquoi est-il nécessaire de faire du padding sur les séquences ?
- Quel impact a la longueur maximale choisie (MAX_LEN) sur les performances ?
- Comment pourrait-on améliorer le preprocessing pour de meilleurs résultats ?

### 3. Performance et limitations
- Dans quels cas le modèle LSTM échoue-t-il le plus souvent ?
- Comment pourrait-on améliorer la détection du sarcasme et de l'ironie ?
- Quels sont les avantages/inconvénients par rapport aux approches plus récentes ?

### 4. Applications pratiques
- Dans quels contextes professionnels cette technologie serait-elle utile ?
- Comment adapter ce modèle pour analyser des avis en français ?
- Quelles considérations éthiques faut-il prendre en compte ?

## 🏋️ Exercices d'approfondissement

### Exercice 1 : Modification de l'architecture
Modifiez le modèle pour inclure :
- Une couche LSTM bidirectionnelle
- Plus de couches LSTM empilées
- Une couche d'attention

### Exercice 2 : Amélioration des données
- Testez avec différentes valeurs de MAX_LEN
- Essayez d'autres techniques de preprocessing
- Implémentez de l'augmentation de données pour le texte

### Exercice 3 : Évaluation avancée
- Calculez des métriques plus détaillées (F1-score, précision, rappel par classe)
- Analysez les erreurs de manière plus systématique
- Créez des visualisations des performances

### Exercice 4 : Application pratique
- Adaptez le modèle pour un autre dataset (par exemple, des avis produits)
- Implémentez une interface web simple pour tester le modèle
- Comparez avec d'autres approches (règles, ML classique)
```

## Cellule 13 (Markdown) - Conclusion et liens vers le projet chatbot

```markdown
## 🎯 Conclusion : Vers le chatbot pédagogique

### Ce que vous avez appris

✅ **Concepts techniques maîtrisés :**
- Fonctionnement des réseaux récurrents et des cellules LSTM
- Preprocessing de données textuelles pour l'IA
- Création d'embeddings de mots et leur visualisation
- Évaluation et analyse des performances d'un modèle NLP

✅ **Compétences pratiques développées :**
- Implémentation complète d'un modèle LSTM avec TensorFlow/Keras
- Debugging et optimisation d'un modèle de Deep Learning
- Analyse critique des limites et biais d'un modèle
- Comparaison d'approches différentes pour le même problème

### Liens avec le projet final

🚀 **Applications pour votre chatbot pédagogique :**

1. **Compréhension du contexte :** Les principes des RNN/LSTM vous aideront à comprendre comment les LLM comme Mistral traitent les conversations séquentielles.

2. **Gestion de l'historique :** Votre chatbot devra maintenir le contexte d'une conversation, similaire à la mémoire des LSTM.

3. **Qualité des réponses :** L'analyse de sentiment peut vous aider à évaluer si les réponses de votre chatbot sont appropriées.

4. **Embeddings et sémantique :** La visualisation des embeddings vous donne une intuition sur comment les modèles comprennent les relations entre concepts.

### Prochaines étapes

📚 **Pour aller plus loin :**
- Module 3 : Applications professionnelles et intégration d'APIs
- Module 4 : Développement de votre chatbot pédagogique
- Exploration des modèles Transformer et des LLM modernes

💡 **Réflexion personnelle :**
Prenez quelques minutes pour noter :
- Les concepts qui vous ont le plus marqué
- Les applications que vous imaginez dans votre contexte professionnel
- Les questions qui restent ouvertes pour vous

🔗 **Ressources complémentaires :**
- [Understanding LSTM Networks - Colah's Blog](http://colah.github.io/posts/2015-08-Understanding-LSTMs/)
- [Documentation TensorFlow sur les RNN](https://www.tensorflow.org/guide/keras/rnn)
- [Tutoriel complet sur le NLP avec TensorFlow](https://www.tensorflow.org/text)

---

**Bravo ! Vous avez terminé votre exploration des réseaux récurrents ! 🎉**

*Passez maintenant au QCM d'évaluation du Module 2 pour valider vos acquis.*
```

