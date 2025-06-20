# Synthèse - Module 2

# Architectures spécialisées de réseaux de neurones
## Guide de référence synthétique

### 🔍 Architectures spécialisées

- **🏗️ Au-delà des réseaux de neurones simples**  
  Architectures conçues pour exploiter la structure spécifique des données (images, texte, séquences)

- **📚 Évolution des architectures**  
  Des perceptrons aux modèles complexes actuels, chaque architecture résout des problèmes spécifiques

- **🧩 Spécialisation par type de données**  
  CNN pour les images, RNN pour les séquences, Transformers pour le texte

- **🚀 Gains de performances considérables**  
  Les architectures spécialisées surpassent largement les modèles génériques pour leurs tâches ciblées

### 👁️ Réseaux de neurones convolutifs (CNN)

#### 🧠 Principes fondamentaux

- **🔍 Convolution**  
  Filtres (kernels) qui parcourent l'image pour détecter des motifs locaux

- **🏊 Pooling**  
  Réduction de dimension qui préserve les informations importantes tout en diminuant la taille des données

- **🔄 Hiérarchie des caractéristiques**  
  Extraction progressive de motifs de plus en plus abstraits (bords → formes → objets)

- **🔗 Couches fully connected**  
  Couches finales qui combinent les caractéristiques extraites pour la classification

#### 🏛️ Architecture typique d'un CNN

```
Input → Conv → ReLU → Pool → Conv → ReLU → Pool → Flatten → Dense → Output
```

- **Couches de convolution:** extraction de caractéristiques
- **Fonctions d'activation (ReLU):** introduction de non-linéarité
- **Couches de pooling:** réduction de dimension et invariance aux petites translations
- **Flatten:** transformation des matrices en vecteur
- **Couches denses:** classification finale

#### 💪 Forces du CNN

- **🔄 Partage des paramètres**  
  Les mêmes filtres sont appliqués sur toute l'image, réduisant le nombre de paramètres

- **📍 Invariance à la translation**  
  Capacité à reconnaître les objets quelle que soit leur position dans l'image

- **🧠 Extraction automatique des caractéristiques**  
  Pas besoin d'extraction manuelle des features comme en ML classique

- **🌐 Robustesse aux variations**  
  Bonne généralisation face aux variations de luminosité, angle, etc.

#### 📊 Applications principales

- **🖼️ Classification d'images**  
  Reconnaissance d'objets, de chiffres, de visages

- **🎯 Détection d'objets**  
  Localisation et identification d'objets multiples dans une image

- **🧩 Segmentation**  
  Séparation précise des différents éléments d'une image

- **👁️ Vision par ordinateur**  
  Voitures autonomes, robotique, réalité augmentée

### 📝 Réseaux récurrents (RNN)

#### 🧠 Principes fondamentaux

- **🔄 Boucles de récurrence**  
  Connections qui permettent de transmettre l'information d'une étape à la suivante

- **📚 État caché (hidden state)**  
  Mémoire interne qui conserve le contexte des éléments précédents

- **⏱️ Traitement séquentiel**  
  Analyse des données une étape à la fois, en tenant compte du contexte

- **🔗 Partage des paramètres dans le temps**  
  Les mêmes poids sont utilisés à chaque étape, permettant de traiter des séquences de longueur variable

#### 🔄 Problème du gradient qui s'évanouit

- **📉 Difficulté à capturer les dépendances à long terme**  
  L'information se dilue progressivement lors de la backpropagation

- **💡 Solutions: LSTM et GRU**  
  Architectures qui permettent de mieux conserver l'information sur de longues séquences

#### 🧩 Long Short-Term Memory (LSTM)

- **🚪 Système de portes (gates)**  
  • Porte d'oubli (forget gate): décide quelle information oublier  
  • Porte d'entrée (input gate): décide quelle information nouvelle stocker  
  • Porte de sortie (output gate): décide quelle information transmettre

- **📋 Cellule de mémoire**  
  Permet de conserver l'information importante sur de longues séquences

- **🧮 Flux d'information contrôlé**  
  Mécanismes sélectifs qui gèrent l'ajout et la suppression d'information

#### 📊 Applications principales

- **📝 Traitement du langage naturel**  
  Analyse de sentiment, traduction automatique, résumé de texte

- **⏱️ Séries temporelles**  
  Prédiction de valeurs futures, détection d'anomalies

- **🎵 Traitement audio**  
  Reconnaissance vocale, génération de musique

- **📊 Données séquentielles**  
  Toute donnée où l'ordre importe (génomique, logs, etc.)

### 📊 Comparaison des architectures

| Caractéristique | CNN | RNN/LSTM |
|-----------------|-----|----------|
| **Type de données idéal** | Images, données en grille | Séquences, texte, série temporelles |
| **Force principale** | Détection de patterns spatiaux | Capture des dépendances temporelles |
| **Structure de l'information** | Hiérarchie spatiale | Flux séquentiel avec mémoire |
| **Parallélisation** | Hautement parallélisable | Moins parallélisable (séquentiel) |
| **Taille de contexte** | Limitée par la taille des filtres | Théoriquement illimitée (LSTM) |
| **Paramètres** | Relativement peu nombreux (partage) | Plus nombreux pour LSTM/GRU |
| **Applications types** | Vision par ordinateur | NLP, prédiction de séries |

### 💡 Bonnes pratiques pour les architectures spécialisées

#### 🛠️ Conception du CNN

- **🔍 Commencer simple**  
  Débuter avec une architecture éprouvée (ex: LeNet, mini-VGG)

- **📊 Augmenter progressivement la profondeur**  
  Plus de filtres dans les couches profondes, moins dans les premières

- **📉 Réduire graduellement la dimension spatiale**  
  Diminuer la hauteur/largeur tout en augmentant le nombre de filtres

- **🧪 Dropout entre les couches denses**  
  Ajouter du dropout après la mise à plat pour éviter le surapprentissage

- **🔧 Batch normalization pour stabiliser**  
  Normaliser les activations pour accélérer l'entraînement

#### 🔄 Optimisation des RNN/LSTM

- **📚 Attention à la longueur des séquences**  
  Les séquences trop longues peuvent causer des problèmes de mémoire et d'entraînement

- **📊 Bidirectionnalité pour plus de contexte**  
  Les LSTM bidirectionnels analysent la séquence dans les deux sens

- **🧪 Empilement de couches LSTM**  
  Plusieurs couches pour capturer différents niveaux d'abstraction

- **⚖️ GRU vs LSTM**  
  GRU plus léger et plus rapide, LSTM potentiellement plus puissant pour les très longues séquences

### 🔄 Évolution vers les Transformers

- **⚠️ Limitations des RNN/LSTM**  
  Traitement séquentiel, difficultés avec les très longues séquences

- **🧠 Mécanisme d'attention**  
  Permet de se concentrer sur les parties pertinentes de la séquence

- **🚀 Architecture Transformer**  
  Traitement parallèle, meilleure capture des dépendances à long terme

- **📚 Modèles fondés sur les Transformers**  
  BERT, GPT, T5 qui révolutionnent le NLP et au-delà

### 🛠️ Conseils pratiques d'implémentation

- **📊 Gestion des données**  
  • CNN: redimensionnement, normalisation, augmentation de données  
  • RNN: padding, troncation, tokenisation, embeddings

- **🧪 Visualisation pour comprendre**  
  • CNN: visualiser filtres et feature maps  
  • RNN: analyser les états cachés et l'évolution des embeddings

- **⚙️ Hyperparamètres clés**  
  • CNN: taille et nombre de filtres, pas de convolution, type de pooling  
  • RNN: taille des états cachés, nombre de couches, dropout

- **📈 Transfer learning**  
  Réutiliser des modèles pré-entraînés (VGG, ResNet, etc.) pour gagner en temps et performance
