# 📚 Chatbot IA avec Base Documentaire

[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)](https://streamlit.io)
[![LangChain](https://img.shields.io/badge/LangChain-0.1+-green.svg)](https://langchain.com)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

> **Projet BTS SIO SLAM** - Assistant intelligent utilisant RAG (Retrieval-Augmented Generation) pour analyser et répondre aux questions basées sur vos documents personnels.

## ✨ Fonctionnalités

🤖 **IA Conversationnelle** - Chat intelligent avec historique contextuel  
📄 **Multi-formats** - Support TXT, MD, PDF, code source  
🔍 **Recherche sémantique** - Indexation vectorielle avec FAISS  
🎯 **Sources traçables** - Références exactes aux documents utilisés  
⚙️ **Multi-providers** - Compatible OpenAI et Mistral AI  
🌐 **Interface moderne** - Dashboard Streamlit responsive  

## 🚀 Démarrage rapide

### Installation
```bash
# Cloner le projet
git clone https://github.com/votre-username/Projet_IA_BTS-SIO.git
cd Projet_IA_BTS-SIO

# Installer les dépendances
pip install -r requirements.txt

# Configuration
cp .env.example .env
# Éditer .env avec vos clés API
```

### Lancement
```bash
streamlit run app/main.py
```
📱 L'application s'ouvre sur `http://localhost:8501`

## ⚡ Utilisation

### 1️⃣ Indexer vos documents
- **Repository Git** : Cloner automatiquement un repo de documentation
- **Upload fichiers** : Glisser-déposer vos documents locaux

### 2️⃣ Converser avec l'IA
- Poser des questions sur vos documents
- Explorer les sources des réponses
- Maintenir un historique contextuel

### 3️⃣ Analyser les résultats
- Consulter les scores de confiance
- Rechercher dans la base documentaire
- Exporter les conversations

## 🛠️ Technologies

| Catégorie | Technologies |
|-----------|-------------|
| **Backend** | Python 3.11+, LangChain, FAISS |
| **Frontend** | Streamlit, HTML/CSS |
| **IA/ML** | OpenAI GPT, Mistral AI, Embeddings |
| **Documents** | PyMuPDF, python-docx, GitPython |
| **Déploiement** | GitHub Codespaces, Docker |

## 📊 Démonstration

### Interface principale
```
┌─────────────────────────────────────────────────────────────┐
│  📚 Chatbot IA - Base documentaire                         │
├─────────────────────────┬───────────────────────────────────┤
│  💬 Conversation        │  🔍 Outils d'analyse            │
│                         │                                   │
│  👤 Comment installer   │  📁 Gestion documents            │
│      les dépendances ?  │  ├── Repository Git              │
│                         │  ├── Upload fichiers             │
│  🤖 Pour installer les  │  └── Statistiques               │
│      dépendances, utili-│                                   │
│      sez la commande :  │  💡 Questions suggérées          │
│      pip install -r...  │  ├── Objectif du projet ?        │
│                         │  ├── Étapes d'utilisation ?      │
│  📋 Sources utilisées:  │  └── Fichiers importants ?       │
│  • requirements.txt    │                                   │
│  • README.md           │  📄 Export conversation          │
│                         │                                   │
│  Confiance: Élevée (0.9)│  📊 Session: 3 questions        │
└─────────────────────────┴───────────────────────────────────┘
```

## 🎯 Cas d'usage

### 🎓 Éducation
- Analyser des cours et supports pédagogiques
- Créer des assistants de révision personnalisés
- Explorer de la documentation technique

### 💼 Entreprise
- Centraliser les connaissances internes
- Assistant pour la documentation produit
- Support client automatisé

### 🔬 Recherche
- Analyser des publications scientifiques
- Synthétiser des rapports de recherche
- Explorer des bases de données documentaires

## 📈 Configuration avancée

### Variables d'environnement
```bash
# Provider IA (openai ou mistral)
PROVIDER=mistral
MISTRAL_API_KEY=votre_cle_ici

# Paramètres d'optimisation
CHUNK_SIZE=1000          # Taille des segments
MAX_RESULTS=4            # Nombre de résultats
SIMILARITY_THRESHOLD=0.7 # Seuil de pertinence
```

### Formats supportés
- **Texte** : `.txt`, `.md`
- **Code** : `.py`, `.js`, `.html`, `.css`, `.json`
- **Documents** : `.pdf` (version avancée)

## 🔧 Développement

### Structure du projet
```
app/
├── config.py      # Configuration et variables
├── ingest.py      # Ingestion des documents  
├── qa_chain.py    # Logique IA et conversation
└── main.py        # Interface Streamlit
```

### Tests et qualité
```bash
# Tests
pytest tests/

# Formatage
black app/

# Linting  
flake8 app/
```

## 🚀 Déploiement

### GitHub Codespaces (recommandé)
1. Fork ce repository
2. Créer un Codespace
3. Configuration automatique
4. Lancer l'application

### Docker
```bash
docker build -t chatbot-ia .
docker run -p 8501:8501 chatbot-ia
```

### Streamlit Cloud
1. Connecter votre repository
2. Configurer les variables d'environnement
3. Déploiement automatique

## 📚 Documentation

- **[DOCUMENTATION.md](DOCUMENTATION.md)** - Guide complet et technique
- **[Installation détaillée](DOCUMENTATION.md#installation)** - Toutes les options
- **[API Reference](DOCUMENTATION.md#api)** - Classes et méthodes
- **[Dépannage](DOCUMENTATION.md#dépannage)** - Solutions aux problèmes courants

## 🎓 Projet BTS SIO

### Compétences développées
- **Développement d'applications** - Architecture modulaire Python
- **Intelligence artificielle** - Intégration LLMs et RAG
- **Interface utilisateur** - Dashboard interactif Streamlit
- **Gestion de données** - Bases vectorielles et embeddings
- **Déploiement** - Cloud et conteneurisation

### Contexte pédagogique
Ce projet illustre l'application pratique des technologies d'IA modernes dans le développement d'solutions métier, en mettant l'accent sur l'architecture logicielle et l'expérience utilisateur.

## 🤝 Contribution

Les contributions sont les bienvenues ! Consultez [DOCUMENTATION.md](DOCUMENTATION.md#développement) pour les guidelines.

## 📄 Licence

Ce projet est sous licence MIT. Voir [LICENSE](LICENSE) pour plus de détails.

## 👨‍💻 Auteur

**[G.G]**  
---

⭐ **N'hésitez pas à mettre une étoile si ce projet vous aide !**