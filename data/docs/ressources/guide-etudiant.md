# Guide d'utilisation des ressources - Formation Deep Learning

## Bienvenue dans votre formation Deep Learning !

Ce guide vous explique comment accéder et utiliser les différentes ressources du cours.

## 1. Accès aux notebooks Jupyter

### Qu'est-ce qu'un notebook Jupyter ?

Un notebook Jupyter est un document interactif qui vous permet d'exécuter du code Python directement dans votre navigateur, tout en incluant du texte explicatif, des images et des visualisations. C'est l'outil idéal pour apprendre le Deep Learning de façon pratique.

### Comment accéder aux notebooks du cours

Nous utilisons Google Colab, qui vous permet d'exécuter des notebooks Jupyter dans le cloud, sans aucune installation sur votre ordinateur. Vous avez simplement besoin d'un compte Google.

Pour accéder à chaque notebook :
1. Cliquez sur le badge "Open in Colab" ou le lien correspondant au notebook
2. Le notebook s'ouvrira dans Google Colab
3. Si demandé, connectez-vous avec votre compte Google

### Enregistrer votre travail

Important : Les notebooks s'ouvrent en mode lecture seule. Pour sauvegarder votre travail :
1. Allez dans le menu "Fichier" > "Enregistrer une copie dans Drive"
2. Une copie personnelle sera créée dans votre Google Drive
3. Travaillez désormais sur cette copie

### Liste des notebooks disponibles

| Notebook | Description | Lien direct |
|----------|-------------|-------------|
| Hello World du Deep Learning | Premier réseau de neurones sur MNIST | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/votre-depot/deeplearning-bts/blob/main/notebooks/hello-world-dl.ipynb) |
| Machine Learning classique | Classification avec Random Forest | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/votre-depot/deeplearning-bts/blob/main/notebooks/machine-learning-classique.ipynb) |
| Deep Learning | Classification avec réseau de neurones | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/votre-depot/deeplearning-bts/blob/main/notebooks/deep-learning.ipynb) |
| Anatomie d'un réseau | Exploration interactive d'un réseau | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/votre-depot/deeplearning-bts/blob/main/notebooks/anatomie-reseau.ipynb) |
| Template du mini-projet | Base pour le challenge d'amélioration | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/votre-depot/deeplearning-bts/blob/main/notebooks/model-template.ipynb) |

## 2. Utilisation des notebooks

### Exécuter les cellules

- Pour exécuter une cellule de code, cliquez sur le bouton ▶️ à gauche de la cellule ou appuyez sur `Ctrl+Entrée`
- Exécutez les cellules dans l'ordre, de haut en bas
- Attendez qu'une cellule ait terminé son exécution avant de passer à la suivante (le symbole ● devient ✓)

### Types de cellules

- **Cellules de code** : Contiennent du code Python exécutable
- **Cellules de texte** : Contiennent des explications et des instructions

### Conseils pratiques

- **Redémarrer le runtime** : Si vous rencontrez des erreurs, essayez de redémarrer le runtime (Menu "Runtime" > "Restart runtime")
- **RAM limitée** : Si vous recevez des erreurs de mémoire, fermez les autres onglets Colab
- **Déconnexion** : Google Colab peut se déconnecter après inactivité, sauvegardez régulièrement

## 3. Documents à compléter

### Téléchargement des fiches

Pour chaque séance, téléchargez les fiches d'observation et autres documents à compléter :
1. Cliquez sur les liens fournis dans la page de la séance
2. Choisissez entre la version PDF (pour impression) ou Word/ODT (pour édition électronique)

### Soumission des travaux

Pour soumettre vos travaux complétés :
1. Nommez vos fichiers avec votre nom et le numéro de séance (ex: "Dupont_Seance1_Fiche.docx")
2. Déposez-les sur la plateforme de cours en ligne ou envoyez-les par email selon les instructions de votre formateur
3. Pour les notebooks, partagez l'URL de votre copie dans Google Drive ou exportez-les au format .ipynb

## 4. Résolution des problèmes courants

| Problème | Solution |
|----------|----------|
| Le notebook ne se charge pas | Vérifiez votre connexion internet ou réessayez dans quelques minutes |
| Erreur "CUDA out of memory" | Allez dans "Runtime" > "Change runtime type" et sélectionnez "None" pour GPU |
| Modules manquants | Exécutez `!pip install nom-du-module` dans une cellule |
| Accès refusé | Assurez-vous d'être connecté à votre compte Google |

## 5. Ressources complémentaires

- [Documentation TensorFlow](https://www.tensorflow.org/tutorials)
- [Documentation Keras](https://keras.io/examples/)
- [Tutoriels Google Colab](https://colab.research.google.com/notebooks/welcome.ipynb)

