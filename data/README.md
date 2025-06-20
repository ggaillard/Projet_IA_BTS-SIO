# Atelier Deep Learning pour BTS SIO

Ce dépôt contient les ressources pédagogiques pour la formation en Deep Learning destinée aux étudiants de BTS SIO. La formation est structurée en 4 modules progressifs, aboutissant à la création d'un chatbot pédagogique utilisant l'API Mistral AI.

## Nouveautés

**Mise à jour - Avril 2025** : Ajout de QCM d'auto-évaluation pour chaque module avec :
- Questions à choix multiples pour vérifier la compréhension des concepts
- Exercices pratiques pour tester les compétences techniques
- Système de notation avec interprétation des résultats
- Recommandations personnalisées selon le score obtenu

## Structure du cours

Le cours est organisé en quatre modules progressifs :

1. **Fondamentaux du Deep Learning**
   - Introduction aux concepts de base des réseaux de neurones
   - Comparaison entre Machine Learning classique et Deep Learning
   - Mini-projet "Hello World" avec reconnaissance de chiffres manuscrits
   - **Nouveau** : QCM d'auto-évaluation sur les concepts fondamentaux

2. **Architectures spécialisées**
   - Réseaux convolutifs (CNN) pour la vision par ordinateur
   - Réseaux récurrents (RNN) pour le traitement des séquences
   - Mini-projets pratiques avec applications concrètes
   - **Nouveau** : QCM d'auto-évaluation sur les architectures CNN et RNN

3. **Développement d'applications pratiques**
   - Utilisation des frameworks TensorFlow/Keras
   - Optimisation des modèles pour le déploiement
   - Intégration de l'API Mistral AI
   - **Nouveau** : QCM d'auto-évaluation avec exercices pratiques d'intégration

4. **Projet intégrateur - Chatbot pédagogique**
   - Développement d'un chatbot expliquant le Deep Learning
   - Structuration d'une base de connaissances pédagogique
   - Optimisation des prompts pour l'API Mistral
   - **Nouveau** : QCM d'auto-évaluation sur le développement de chatbots

## Utilisation de ce dépôt

### Prérequis

- Python 3.7 ou supérieur
- Navigateur web récent pour Google Colab
- Compte Google (pour Google Colab)
- Compte Mistral AI (pour l'API, module 4)

### Installation

1. **Cloner le dépôt**
   ```bash
   git clone https://github.com/votre-repo/chatbot-deeplearning.git
   cd chatbot-deeplearning
   ```

2. **Installer les dépendances**
   ```bash
   pip install -r requirements.txt
   ```

3. **Générer la documentation**
   ```bash
   mkdocs build
   # ou pour un serveur de développement local
   mkdocs serve
   ```

## Documentation

La documentation complète est générée avec MkDocs et disponible :
- En ligne à [adresse-du-site]
- Localement après exécution de `mkdocs serve` à l'adresse http://localhost:8000

### Utilisation des QCM d'auto-évaluation

Les QCM d'auto-évaluation sont accessibles :
1. À la fin de chaque module dans la navigation
2. Via des liens directs à la fin des pages d'index de chaque module
3. Dans la carte de progression qui visualise le parcours d'apprentissage

Pour une expérience optimale :
- Complétez chaque module avant de faire le QCM correspondant
- Utilisez le [formulaire de feedback](docs/ressources/qcm-feedback.md) pour signaler tout problème
- Consultez le [suivi de progression](docs/suivi-progression.md) pour visualiser votre avancement

## Contribution

Les contributions à ce projet sont les bienvenues. Pour contribuer :

1. Forkez le dépôt
2. Créez une branche pour vos modifications
3. Soumettez une pull request

Veuillez suivre les normes de codage et documenter clairement vos modifications.

## Licence

Ce projet est distribué sous une double licence :

### Code source et scripts
Le code source, scripts et outils sont distribués sous la [Licence MIT](LICENSE). Cette licence permet une large utilisation, modification et distribution du code, y compris dans des projets commerciaux.

### Contenu pédagogique
Le contenu pédagogique (cours, documentation, QCM, illustrations) est distribué sous la [Licence Creative Commons Attribution - Pas d'Utilisation Commerciale - Partage dans les Mêmes Conditions 4.0 International (CC BY-NC-SA 4.0)](CONTENT_LICENSE.md). Cette licence permet le partage et l'adaptation du contenu à des fins non commerciales, à condition de créditer les auteurs originaux et de partager les modifications sous les mêmes conditions.







