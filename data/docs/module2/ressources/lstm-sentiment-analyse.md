# Points clés à explorer - LSTM pour l'analyse de sentiment

## Introduction

Ce document approfondit les aspects essentiels des réseaux LSTM (Long Short-Term Memory) pour l'analyse de sentiment. Il est conçu pour accompagner le mini-projet RNN du Module 2 et vous aider à mieux comprendre le fonctionnement interne de ces réseaux.

## 1. Transformation du texte en entrées numériques

### Processus de tokenisation
Le texte brut doit être converti en valeurs numériques pour être traité par un réseau de neurones. Cette conversion se fait généralement en plusieurs étapes :

1. **Nettoyage du texte** : Suppression de la ponctuation, conversion en minuscules, élimination des mots vides (stopwords)
   ```python
   # Exemple de nettoyage
   import re
   import string
   
   def clean_text(text):
       text = text.lower()  # Conversion en minuscules
       text = re.sub(f'[{string.punctuation}]', ' ', text)  # Suppression de la ponctuation
       text = re.sub(r'\s+', ' ', text)  # Remplacement des espaces multiples
       return text.strip()
   ```

2. **Tokenisation** : Découpage du texte en mots individuels (tokens)
   ```python
   # Exemple simple de tokenisation
   def tokenize(text):
       return text.split()
   ```

3. **Création d'un vocabulaire** : Attribution d'un index unique à chaque mot unique
   ```python
   # Création d'un vocabulaire
   def build_vocab(texts):
       vocab = {}
       idx = 1  # Réserver 0 pour le padding
       for text in texts:
           for word in tokenize(clean_text(text)):
               if word not in vocab:
                   vocab[word] = idx
                   idx += 1
       return vocab
   ```

4. **Conversion en séquences numériques** : Remplacement de chaque mot par son index
   ```python
   # Conversion texte → séquence numérique
   def text_to_sequence(text, vocab):
       return [vocab.get(word, 0) for word in tokenize(clean_text(text))]
   ```

5. **Padding** : Uniformisation de la longueur des séquences
   ```python
   # Padding des séquences
   from tensorflow.keras.preprocessing.sequence import pad_sequences
   
   sequences = [text_to_sequence(text, vocab) for text in texts]
   padded_sequences = pad_sequences(sequences, maxlen=100, padding='post')
   ```

### Embeddings de mots
Une fois les mots convertis en indices, ils sont transformés en vecteurs denses via une couche d'embedding :

```python
# Création d'une couche d'embedding
from tensorflow.keras.layers import Embedding

embedding_dim = 100
vocab_size = len(vocab) + 1  # +1 pour l'index de padding (0)

embedding_layer = Embedding(
    input_dim=vocab_size,
    output_dim=embedding_dim,
    input_length=max_sequence_length,
    mask_zero=True  # Pour ignorer les tokens de padding
)
```

Ces embeddings représentent les mots dans un espace vectoriel où des mots sémantiquement proches ont des vecteurs similaires.

## 2. Gestion de l'information à long terme par les cellules LSTM

### Architecture d'une cellule LSTM
Une cellule LSTM utilise trois "portes" pour contrôler le flux d'information :

1. **Porte d'oubli (Forget Gate)** : Détermine quelles informations de l'état précédent doivent être conservées ou supprimées
   - Formule : $f_t = \sigma(W_f \cdot [h_{t-1}, x_t] + b_f)$
   - Où $\sigma$ est la fonction sigmoid qui produit des valeurs entre 0 et 1

2. **Porte d'entrée (Input Gate)** : Contrôle quelles nouvelles informations sont ajoutées à l'état de la cellule
   - Formule : $i_t = \sigma(W_i \cdot [h_{t-1}, x_t] + b_i)$
   - Nouvelles valeurs candidates : $\tilde{C}_t = \tanh(W_C \cdot [h_{t-1}, x_t] + b_C)$

3. **Porte de sortie (Output Gate)** : Détermine quelle partie de l'état de la cellule sera transmise à la sortie
   - Formule : $o_t = \sigma(W_o \cdot [h_{t-1}, x_t] + b_o)$

### Mécanisme de mémoire
La force des LSTM réside dans leur capacité à maintenir une mémoire à long terme grâce à l'état de la cellule ($C_t$) :

1. **Mise à jour de l'état** : 
   - $C_t = f_t * C_{t-1} + i_t * \tilde{C}_t$
   - L'état précédent est partiellement oublié (multiplié par $f_t$)
   - Les nouvelles informations sont ajoutées (multipliées par $i_t$)

2. **Calcul de la sortie** :
   - $h_t = o_t * \tanh(C_t)$
   - La sortie est une version filtrée de l'état de la cellule

Ce mécanisme permet aux LSTM de :
- Mémoriser des informations importantes sur de longues séquences
- Oublier les informations non pertinentes
- Mettre à jour leur mémoire de manière sélective

## 3. Différence entre embeddings de mots positifs et négatifs

### Propriétés des embeddings

Après entraînement, les embeddings de mots similaires se rapprochent dans l'espace vectoriel. Pour l'analyse de sentiment, cela signifie que :

1. **Mots positifs** : Les embeddings de mots comme "excellent", "superbe", "fantastique" forment un cluster distinct
2. **Mots négatifs** : Les embeddings de mots comme "terrible", "horrible", "décevant" forment un autre cluster

### Visualisation des embeddings

Pour visualiser ces différences, on utilise souvent des techniques de réduction de dimensionnalité comme t-SNE ou PCA :

```python
# Visualisation des embeddings avec t-SNE
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt

# Récupérer la matrice d'embedding du modèle entraîné
embedding_matrix = model.layers[0].get_weights()[0]

# Sélectionner des mots spécifiques pour la visualisation
words_to_plot = ["good", "excellent", "amazing", "bad", "terrible", "awful"]
word_indices = [vocab[word] for word in words_to_plot if word in vocab]
word_vectors = embedding_matrix[word_indices]

# Réduction de dimension avec t-SNE
tsne = TSNE(n_components=2, random_state=42)
word_vectors_2d = tsne.fit_transform(word_vectors)

# Tracer les points
plt.figure(figsize=(10, 8))
for i, word in enumerate([words_to_plot[vocab.get(i, 0)] for i in word_indices]):
    x, y = word_vectors_2d[i]
    plt.scatter(x, y)
    plt.annotate(word, (x, y), fontsize=12)
plt.title("Visualisation des embeddings de mots")
plt.show()
```

### Caractéristiques observables

Dans une visualisation réussie, vous devriez observer :
- Des groupements clairs de mots positifs et négatifs
- Des distances plus courtes entre mots de même polarité
- Des vecteurs qui capturent plus que la simple polarité (ex: intensité, domaine, etc.)

## 4. Compréhension du contexte par le modèle LSTM

### Mécanisme de compréhension contextuelle

Les LSTM comprennent le contexte d'une phrase de plusieurs façons :

1. **Séquentialité** : Le modèle traite les mots dans l'ordre, permettant de capturer leur relation séquentielle
   ```
   "Ce film n'est pas mauvais" → Le LSTM peut comprendre que "pas mauvais" est positif
   ```

2. **Mémoire sélective** : Capacité à retenir les informations importantes et oublier les détails non pertinents
   ```
   "Malgré quelques défauts mineurs, le film était globalement excellent"
   → Le LSTM peut se concentrer sur "globalement excellent" plutôt que sur "défauts mineurs"
   ```

3. **Représentation bidirectionnelle** : Les LSTM bidirectionnels (Bi-LSTM) lisent la séquence dans les deux sens
   ```python
   # Implémentation d'un Bi-LSTM
   from tensorflow.keras.layers import Bidirectional, LSTM
   
   bidirectional_lstm = Bidirectional(LSTM(units=64, return_sequences=True))
   ```

### Exemple de traitement contextuel

Prenons l'exemple de la phrase "Ce n'est pas un bon film, c'est un chef-d'œuvre !" :

1. Le modèle lit séquentiellement chaque mot
2. À "pas un bon", il capture la négation
3. À "chef-d'œuvre", il comprend le contraste avec la première partie
4. L'état final de la cellule contient une représentation positive

## 5. Limitations de l'approche LSTM pour l'analyse de sentiment

### Défis inhérents

1. **Sarcasme et ironie** : Les LSTM peinent à détecter les nuances subtiles
   ```
   "Quelle performance incroyable ! Je n'ai jamais autant dormi au cinéma."
   ```

2. **Contexte culturel** : Les modèles manquent souvent de connaissances contextuelles
   ```
   "Ce film est tellement mauvais qu'il en devient culte."
   ```

3. **Expressions idiomatiques** : Difficulté à comprendre les expressions non littérales
   ```
   "Le réalisateur s'est vraiment cassé la tête pour ce scénario."
   ```

4. **Besoin de données d'entraînement importantes** : Les modèles performants nécessitent de grands corpus annotés

### Contraintes techniques

1. **Problème du gradient qui s'évanouit** : Même les LSTM peuvent avoir du mal avec des séquences très longues

2. **Temps d'entraînement** : L'entraînement est séquentiel et difficile à paralléliser

3. **Complexité computationnelle** : Les LSTM sont plus lourds que des approches plus simples (Bag-of-Words, TF-IDF)

## 6. Pistes d'amélioration pour l'analyse de sentiment

### Améliorations architecturales

1. **Bi-LSTM avec attention** : Ajout d'un mécanisme d'attention pour se concentrer sur les mots importants
   ```python
   # Exemple simplifié de mécanisme d'attention
   from tensorflow.keras.layers import Dense, Concatenate
   
   # Output de Bi-LSTM avec return_sequences=True
   lstm_output = ... # shape=(batch_size, sequence_length, lstm_units*2)
   
   # Couche d'attention
   attention = Dense(1, activation='tanh')(lstm_output)
   attention_weights = tf.nn.softmax(attention, axis=1)
   context_vector = tf.reduce_sum(lstm_output * attention_weights, axis=1)
   ```

2. **Embeddings contextuels** : Utiliser des embeddings pré-entraînés comme GloVe, Word2Vec ou BERT
   ```python
   # Chargement d'embeddings GloVe pré-entraînés
   import numpy as np
   
   embeddings_index = {}
   with open('glove.6B.100d.txt', encoding='utf-8') as f:
       for line in f:
           values = line.split()
           word = values[0]
           coefs = np.asarray(values[1:], dtype='float32')
           embeddings_index[word] = coefs
   ```

3. **Architectures hybrides** : Combiner CNN et LSTM pour extraire des motifs à différentes échelles
   ```python
   from tensorflow.keras.layers import Conv1D, MaxPooling1D
   
   # Exemple d'architecture hybride CNN-LSTM
   model = Sequential([
       Embedding(vocab_size, embedding_dim, input_length=max_sequence_length),
       Conv1D(filters=128, kernel_size=5, activation='relu'),
       MaxPooling1D(pool_size=2),
       LSTM(units=64),
       Dense(1, activation='sigmoid')
   ])
   ```

### Améliorations des données et du prétraitement

1. **Augmentation de données** : Création d'exemples supplémentaires par synonymisation, back-translation, etc.

2. **Traitement spécifique** : Gestion explicite des négations, des intensificateurs, etc.
   ```python
   # Exemple de détection de négation
   def mark_negations(text):
       negation_words = ['not', 'no', 'never', 'neither', 'nor', 'none']
       words = text.split()
       for i, word in enumerate(words):
           if word in negation_words and i < len(words) - 1:
               # Marquer le mot suivant une négation
               words[i+1] = 'NEG_' + words[i+1]
       return ' '.join(words)
   ```

3. **Fine-tuning sur un domaine spécifique** : Adaptation à un vocabulaire particulier (critique de films, avis produits, etc.)

## Conclusion

L'analyse de sentiment avec LSTM offre des capacités puissantes pour comprendre le sentiment exprimé dans un texte. Bien que cette approche présente certaines limitations, elle constitue une base solide qui peut être améliorée par diverses techniques. La compréhension approfondie de ces points clés vous permettra de développer des modèles plus performants et mieux adaptés à vos besoins spécifiques.

## Ressources complémentaires

- [Comprendre les LSTM](https://colah.github.io/posts/2015-08-Understanding-LSTMs/)
- [Tutoriel Keras sur les LSTM](https://keras.io/examples/nlp/bidirectional_lstm_imdb/)
- [Word2Vec: Efficient Estimation of Word Representations in Vector Space](https://arxiv.org/abs/1301.3781)
- [GloVe: Global Vectors for Word Representation](https://nlp.stanford.edu/projects/glove/)