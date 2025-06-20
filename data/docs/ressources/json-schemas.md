# Schémas JSON pour le Chatbot Pédagogique

Ce document décrit les structures JSON utilisées pour organiser la base de connaissances du chatbot pédagogique sur le Deep Learning. Ces schémas permettent de standardiser les données et de faciliter leur utilisation par l'application.

## Base de connaissances principale

### Structure globale

La base de connaissances est organisée en concepts principaux, chacun contenant des sous-concepts. Voici la structure générale:

```json
{
  "concepts": [
    {
      "id": "string",
      "title": "string",
      "description": "string",
      "subconcepts": [
        {
          "id": "string",
          "title": "string",
          "definition": "string",
          "details": {
            "beginner": "string",
            "intermediate": "string",
            "advanced": "string"
          },
          "examples": ["string"],
          "related": ["string"]
        }
      ]
    }
  ]
}
```

### Description des champs

| Champ | Type | Description | Exemple |
|-------|------|-------------|---------|
| `concepts` | array | Liste des concepts principaux | |
| `id` | string | Identifiant unique du concept (format: snake_case) | "neural_network" |
| `title` | string | Titre lisible du concept | "Réseau de neurones" |
| `description` | string | Description générale du concept | "Modèle de calcul inspiré du cerveau..." |
| `subconcepts` | array | Liste des sous-concepts | |
| `definition` | string | Définition concise du sous-concept | "Un réseau de neurones est..." |
| `details` | object | Explications adaptées à différents niveaux | |
| `details.beginner` | string | Explication pour les débutants | "Imaginez une série de filtres..." |
| `details.intermediate` | string | Explication de niveau intermédiaire | "Techniquement, un CNN utilise..." |
| `details.advanced` | string | Explication avancée avec termes techniques | "L'opération de convolution peut..." |
| `examples` | array | Liste d'exemples concrets | ["ResNet", "LeNet-5"] |
| `related` | array | Liste d'IDs de concepts liés | ["convolution", "pooling"] |

## Exemple de concept

Voici un exemple complet d'un concept dans la base de connaissances:

```json
{
  "id": "cnn",
  "title": "Réseau de neurones convolutif (CNN)",
  "definition": "Type de réseau spécialisé dans le traitement des données en grille comme les images, utilisant des opérations de convolution pour détecter des motifs spatiaux.",
  "details": {
    "beginner": "Les CNN sont des réseaux spécialisés pour analyser les images. Ils utilisent des filtres qui 'glissent' sur l'image pour détecter des motifs comme les contours, les textures, puis des formes plus complexes.",
    "intermediate": "Ces réseaux exploitent trois idées clés: les connexions locales (chaque neurone voit seulement une petite région), le partage de paramètres (les mêmes filtres sont appliqués partout), et la mise en commun (pooling) pour réduire la dimensionnalité tout en préservant les caractéristiques importantes.",
    "advanced": "L'opération de convolution peut être vue comme un produit de tenseurs avec un noyau partagé, ce qui réduit considérablement le nombre de paramètres par rapport à un réseau entièrement connecté. Cette inductive bias de localité et d'invariance à la translation est particulièrement adaptée aux données visuelles."
  },
  "examples": [
    "LeNet-5 (1998): Premier CNN efficace, utilisé pour la reconnaissance de chiffres manuscrits",
    "ResNet (2015): Architecture introduisant les connexions résiduelles pour entraîner des réseaux très profonds",
    "EfficientNet (2019): Famille de CNN optimisés pour le rapport performance/nombre de paramètres"
  ],
  "related": ["convolution", "pooling", "image_recognition", "feature_map"]
}
```

## Schéma pour les questions et réponses

Pour le système de quiz et d'exercices, un schéma différent est utilisé:

```json
{
  "quizzes": [
    {
      "id": "string",
      "topic": "string",
      "difficulty": "beginner|intermediate|advanced",
      "questions": [
        {
          "id": "string",
          "text": "string",
          "type": "mcq|true_false|short_answer",
          "options": ["string"],
          "correct_answer": "string|number|array",
          "explanation": "string"
        }
      ]
    }
  ]
}
```

### Description des champs du quiz

| Champ | Type | Description | Exemple |
|-------|------|-------------|---------|
| `quizzes` | array | Liste des quiz disponibles | |
| `id` | string | Identifiant unique du quiz | "cnn_basics" |
| `topic` | string | Sujet principal du quiz | "Réseaux convolutifs" |
| `difficulty` | enum | Niveau de difficulté | "intermediate" |
| `questions` | array | Liste des questions | |
| `text` | string | Énoncé de la question | "Quelle est la principale caractéristique..." |
| `type` | enum | Type de question | "mcq" (choix multiple) |
| `options` | array | Options pour les QCM | ["Pooling", "Convolution", "ReLU"] |
| `correct_answer` | mixed | Réponse(s) correcte(s) | 1 ou [0, 2] |
| `explanation` | string | Explication de la réponse | "La convolution est..." |

## Schéma pour l'historique des conversations

Pour gérer l'historique des conversations, le chatbot utilise le format suivant:

```json
{
  "conversations": [
    {
      "id": "string",
      "user_id": "string",
      "timestamp_start": "string (ISO date)",
      "timestamp_last_activity": "string (ISO date)",
      "messages": [
        {
          "role": "system|user|assistant",
          "content": "string",
          "timestamp": "string (ISO date)"
        }
      ],
      "context": {
        "user_level": "beginner|intermediate|advanced",
        "topics_covered": ["string"],
        "last_quiz_score": number,
        "session_metrics": {
          "questions_asked": number,
          "topics_explored": number,
          "quizzes_completed": number
        }
      }
    }
  ]
}
```

### Description des champs de conversation

| Champ | Type | Description | Exemple |
|-------|------|-------------|---------|
| `conversations` | array | Liste des conversations | |
| `id` | string | Identifiant unique de la conversation | "conv_123456" |
| `user_id` | string | Identifiant de l'utilisateur | "user_789" |
| `timestamp_start` | string | Date de début de conversation | "2023-06-15T14:23:45Z" |
| `messages` | array | Liste des messages échangés | |
| `role` | enum | Rôle de l'expéditeur du message | "user" |
| `content` | string | Contenu du message | "Qu'est-ce qu'un CNN?" |
| `context` | object | Informations contextuelles | |
| `user_level` | enum | Niveau estimé de l'utilisateur | "beginner" |
| `topics_covered` | array | Sujets abordés dans la conversation | ["cnn", "pooling"] |
| `session_metrics` | object | Métriques de la session | |

## Utilisation des schémas dans l'application

### Chargement de la base de connaissances

```python
import json

def load_knowledge_base(file_path="knowledge_base.json"):
    """
    Charge la base de connaissances depuis un fichier JSON.
    
    Args:
        file_path (str): Chemin vers le fichier JSON
        
    Returns:
        dict: Base de connaissances
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            knowledge_base = json.load(f)
        return knowledge_base
    except Exception as e:
        print(f"Erreur lors du chargement de la base de connaissances: {e}")
        return {"concepts": []}
```

### Recherche dans la base de connaissances

```python
def find_concept(knowledge_base, concept_id):
    """
    Trouve un concept ou sous-concept par son ID.
    
    Args:
        knowledge_base (dict): Base de connaissances
        concept_id (str): ID du concept à trouver
        
    Returns:
        dict: Concept trouvé ou None
    """
    # Recherche dans les concepts principaux
    for concept in knowledge_base.get("concepts", []):
        if concept["id"] == concept_id:
            return concept
        
        # Recherche dans les sous-concepts
        for subconcept in concept.get("subconcepts", []):
            if subconcept["id"] == concept_id:
                return subconcept
    
    return None
```

### Enrichissement du prompt avec la base de connaissances

```python
def enrich_prompt_with_knowledge(user_message, knowledge_base, user_level="beginner"):
    """
    Enrichit le prompt utilisateur avec des informations pertinentes
    de la base de connaissances.
    
    Args:
        user_message (str): Message de l'utilisateur
        knowledge_base (dict): Base de connaissances
        user_level (str): Niveau de l'utilisateur
        
    Returns:
        str: Prompt enrichi
    """
    # Rechercher des mots-clés dans le message
    relevant_concepts = []
    
    for concept in knowledge_base.get("concepts", []):
        # Vérifier si le concept principal est mentionné
        if concept["title"].lower() in user_message.lower():
            relevant_concepts.append(concept)
        
        # Vérifier les sous-concepts
        for subconcept in concept.get("subconcepts", []):
            if subconcept["title"].lower() in user_message.lower():
                relevant_concepts.append(subconcept)
    
    # Construire le prompt enrichi
    if not relevant_concepts:
        return user_message
    
    enriched_prompt = f"Question de l'utilisateur: {user_message}\n\n"
    enriched_prompt += "Informations pertinentes de la base de connaissances:\n\n"
    
    for concept in relevant_concepts[:2]:  # Limiter à 2 concepts pour éviter un prompt trop long
        enriched_prompt += f"Concept: {concept['title']}\n"
        
        if "definition" in concept:
            enriched_prompt += f"Définition: {concept['definition']}\n"
        
        if "details" in concept and user_level in concept["details"]:
            enriched_prompt += f"Explication ({user_level}): {concept['details'][user_level]}\n"
        
        if "examples" in concept and concept["examples"]:
            examples = concept["examples"][:2]  # Limiter à 2 exemples
            enriched_prompt += f"Exemples: {', '.join(examples)}\n"
        
        enriched_prompt += "\n"
    
    enriched_prompt += f"Réponds à la question de l'utilisateur de manière conversationnelle en utilisant ces informations, adapté au niveau {user_level}."
    
    return enriched_prompt
```

## Validation des données

Pour assurer l'intégrité des données, un script de validation peut être utilisé:

```python
import jsonschema

# Définition du schéma pour validation
knowledge_base_schema = {
    "type": "object",
    "required": ["concepts"],
    "properties": {
        "concepts": {
            "type": "array",
            "items": {
                "type": "object",
                "required": ["id", "title", "subconcepts"],
                "properties": {
                    "id": {"type": "string"},
                    "title": {"type": "string"},
                    "description": {"type": "string"},
                    "subconcepts": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "required": ["id", "title", "definition"],
                            "properties": {
                                "id": {"type": "string"},
                                "title": {"type": "string"},
                                "definition": {"type": "string"},
                                "details": {
                                    "type": "object",
                                    "properties": {
                                        "beginner": {"type": "string"},
                                        "intermediate": {"type": "string"},
                                        "advanced": {"type": "string"}
                                    }
                                },
                                "examples": {
                                    "type": "array",
                                    "items": {"type": "string"}
                                },
                                "related": {
                                    "type": "array",
                                    "items": {"type": "string"}
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}

def validate_knowledge_base(knowledge_base, schema=knowledge_base_schema):
    """
    Valide la structure de la base de connaissances.
    
    Args:
        knowledge_base (dict): Base de connaissances à valider
        schema (dict): Schéma JSON de validation
        
    Returns:
        bool: True si valide, False sinon
    """
    try:
        jsonschema.validate(instance=knowledge_base, schema=schema)
        return True
    except jsonschema.exceptions.ValidationError as e:
        print(f"Erreur de validation: {e}")
        return False
```

## Bonnes pratiques pour l'extension de la base de connaissances

1. **Maintenir la cohérence** des IDs en utilisant le format snake_case
2. **Éviter les duplications** de concepts
3. **Créer des liens bidirectionnels** entre concepts liés
4. **Adapter les explications** aux différents niveaux
5. **Inclure des exemples concrets** pour chaque concept
6. **Valider le fichier JSON** après chaque modification
7. **Versionner la base de connaissances** pour suivre l'évolution
8. **Structurer hiérarchiquement** les concepts pour une navigation logique
9. **Limiter la profondeur** de la hiérarchie pour faciliter la navigation
10. **Documenter les changements** dans un journal des modifications

Ces schémas JSON constituent la structure fondamentale de la base de connaissances du chatbot pédagogique, assurant une organisation cohérente des informations et facilitant leur utilisation par l'application.