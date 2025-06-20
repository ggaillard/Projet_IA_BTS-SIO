# 📚 Chatbot IA avec Base Documentaire

Un chatbot intelligent utilisant RAG (Retrieval-Augmented Generation) pour analyser et répondre aux questions basées sur vos documents.

## ✨ Fonctionnalités

### 🔍 Analyse de Documents
- **Formats supportés** : TXT, MD, PDF, Python, JavaScript, HTML, CSS, JSON, XML
- **Sources multiples** : Repository Git, upload de fichiers, dossiers locaux
- **Indexation intelligente** : Découpage automatique et embeddings vectoriels

### 💬 Conversation Avancée
- **Historique contextuel** : Maintien du contexte sur plusieurs échanges
- **Sources tracées** : Références précises aux documents utilisés
- **Score de confiance** : Évaluation de la fiabilité des réponses

### 🛠️ Interface Complète
- **Interface Streamlit moderne** : Design responsive et intuitif
- **Recherche de documents** : Exploration directe de la base vectorielle
- **Export de conversations** : Sauvegarde en format Markdown
- **Statistiques détaillées** : Métriques de performance et d'usage

### 🔧 Configuration Flexible
- **Multi-providers** : Support OpenAI et Mistral AI
- **Paramètres ajustables** : Taille des chunks, seuils de similarité
- **Variables d'environnement** : Configuration sécurisée

## 🚀 Installation

### Prérequis
- Python 3.11+
- Git
- Clé API OpenAI ou Mistral AI

### Étapes d'installation

1. **Cloner le repository**
```bash
git clone https://github.com/votre-username/chatbot-ia.git
cd chatbot-ia
```

2. **Installer les dépendances**
```bash
pip install -r requirements.txt
```

3. **Configuration**
```bash
cp .env.example .env
# Éditer le fichier .env avec vos clés API
```

4. **Lancer l'application**
```bash
streamlit run app/main.py
```

## ⚙️ Configuration

### Variables d'environnement principales

| Variable | Description | Valeur par défaut |
|----------|-------------|-------------------|
| `PROVIDER` | Provider LLM (openai/mistral) | `openai` |
| `OPENAI_API_KEY` | Clé API OpenAI | Obligatoire si provider=openai |
| `MISTRAL_API_KEY` | Clé API Mistral | Obligatoire si provider=mistral |
| `MODEL_NAME` | Nom du modèle | `gpt-3.5-turbo` |
| `CHUNK_SIZE` | Taille des chunks | `1000` |
| `MAX_RESULTS` | Nombre max de résultats | `4` |

### Configuration avancée

```bash
# Embeddings
EMBEDDING_MODEL=text-embedding-ada-002

# Découpage de documents
CHUNK_SIZE=1000
CHUNK_OVERLAP=200

# Recherche vectorielle
MAX_RESULTS=4
SIMILARITY_THRESHOLD=0.7
```

## 📖 Utilisation

### 1. Indexation de documents

#### Via Repository Git
1. Dans la sidebar, onglet "Repository"
2. Entrer l'URL du repository Git
3. Cliquer sur "Cloner et indexer"

#### Via Upload de fichiers
1. Dans la sidebar, onglet "Upload"
2. Sélectionner les fichiers à analyser
3. Cliquer sur "Uploader et indexer"

### 2. Poser des questions

- Utiliser la zone de chat principale
- Activer l'historique contextuel si désiré
- Explorer les questions suggérées

### 3. Analyser les résultats

- **Sources** : Consulter les documents utilisés
- **Confiance** : Évaluer la fiabilité
- **Recherche** : Explorer la base documentaire

### 4. Export et sauvegarde

- Exporter les conversations en Markdown
- Consulter les statistiques de session
- Effacer l'historique si nécessaire

## 🏗️ Architecture

```
app/
├── __init__.py          # Package principal
├── config.py            # Configuration et validation
├── ingest.py            # Ingestion et indexation des documents
├── qa_chain.py          # Chaîne QA et logique de conversation
└── main.py              # Interface Streamlit

data/                    # Documents sources (auto-généré)
vectorstore/            # Base vectorielle FAISS (auto-généré)
.devcontainer/          # Configuration pour GitHub Codespaces
```

### Flux de données

1. **Ingestion** : Documents → Chunks → Embeddings → FAISS
2. **Requête** : Question → Recherche vectorielle → Contexte
3. **Génération** : LLM + Contexte → Réponse + Sources

## 🛡️ Sécurité et Bonnes Pratiques

### Gestion des clés API
- Utiliser des variables d'environnement
- Ne jamais commiter les fichiers `.env`
- Rotation régulière des clés

### Optimisation des coûts
- Ajuster `CHUNK_SIZE` selon le budget
- Limiter `MAX_RESULTS` pour réduire les tokens
- Utiliser des modèles moins coûteux pour les tests

### Performance
- Indexer uniquement les documents nécessaires
- Nettoyer régulièrement le vectorstore
- Monitorer les métriques de confiance

## 🔧 Développement

### Structure de développement
```bash
# Tests
pytest tests/

# Formatage du code
black app/

# Linting
flake8 app/
```

### Ajout de nouvelles fonctionnalités

1. **Nouveaux formats de documents** : Étendre `DocumentIngestor`
2. **Nouveaux providers LLM** : Modifier `AdvancedQAChain`
3. **Interface utilisateur** : Personnaliser `main.py`

### Variables de session Streamlit

| Variable | Usage |
|----------|-------|
| `st.session_state.qa_chain` | Instance principale QA |
| `st.session_state.messages` | Historique de chat |

## 📊 Métriques et Monitoring

### Métriques automatiques
- Nombre de documents indexés
- Confiance moyenne des réponses
- Nombre d'interactions par session

### Métriques personnalisées
- Temps de réponse
- Utilisation des tokens
- Satisfaction utilisateur

## 🤝 Contribution

1. Fork le repository
2. Créer une branche pour votre fonctionnalité
3. Ajouter des tests si nécessaire
4. Soumettre une Pull Request

## 📝 Licence

Ce projet est sous licence MIT. Voir le fichier `LICENSE` pour plus de détails.

## 🆘 Support

### FAQ

**Q: Comment ajouter support pour d'autres formats ?**
R: Étendre la classe `DocumentIngestor` avec de nouveaux loaders LangChain.

**Q: Peut-on utiliser d'autres bases vectorielles ?**
R: Oui, remplacer FAISS par Chroma, Pinecone, etc. dans `qa_chain.py`.

**Q: Comment optimiser la qualité des réponses ?**
R: Ajuster les prompts, la taille des chunks, et le seuil de similarité.

### Problèmes courants

- **Erreur de clé API** : Vérifier le fichier `.env`
- **Documents non trouvés** : Réindexer avec le bon format
- **Réponses de faible qualité** : Ajuster les paramètres de recherche

---

Développé pour G.G - Projet d'intelligence artificielle appliquée