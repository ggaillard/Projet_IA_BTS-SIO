# Guide d'intégration FastAPI pour le chatbot pédagogique

Ce guide explique comment intégrer FastAPI dans votre projet de chatbot pédagogique sur le Deep Learning pour bénéficier de meilleures performances et de fonctionnalités plus avancées.

## Pourquoi passer à FastAPI ?

FastAPI offre plusieurs avantages pour notre projet :

1. **Performance** : FastAPI est l'un des frameworks Python les plus rapides, basé sur Starlette et Pydantic
2. **Documentation automatique** : Génération automatique de documentation interactive (OpenAPI/Swagger)
3. **Validation des données** : Validation automatique des requêtes et réponses avec Pydantic
4. **Support asynchrone natif** : Support de l'asynchrone pour les opérations à latence élevée (comme les appels API externes)
5. **Typage fort** : Utilisation du typage Python pour une meilleure détection d'erreurs

## Prérequis

- Python 3.7 ou supérieur
- Accès à un terminal pour installer les packages
- Compte et clé API Mistral AI

## Installation des dépendances

```bash
pip install fastapi uvicorn mistralai python-dotenv pydantic
```

**Note**: `uvicorn` est le serveur ASGI recommandé pour exécuter FastAPI.

## Structure du projet

Voici la structure de base recommandée pour votre projet :

```
chatbot-pedagogique/
├── .env                    # Variables d'environnement (clés API)
├── main.py                 # Point d'entrée principal avec FastAPI
├── models/
│   ├── __init__.py
│   ├── conversation.py     # Modèles Pydantic pour les requêtes/réponses
│   └── knowledge_base.py   # Modèles pour la base de connaissances
├── services/
│   ├── __init__.py
│   ├── mistral_service.py  # Interaction avec l'API Mistral
│   └── knowledge_service.py # Gestion de la base de connaissances
├── static/                 # Fichiers statiques (CSS, JS, images)
└── templates/              # Templates HTML (si utilisés)
```

## Configuration initiale

### 1. Fichier .env

Créez un fichier `.env` à la racine du projet avec votre clé API :

```
MISTRAL_API_KEY=votre_clé_api_ici
```

### 2. Modèles Pydantic (models/conversation.py)

Définissez les modèles de données pour les requêtes et réponses :

```python
from typing import List, Optional
from pydantic import BaseModel

class Message(BaseModel):
    role: str  # "user" ou "assistant"
    content: str

class ConversationRequest(BaseModel):
    messages: List[Message]
    user_level: Optional[str] = "beginner"
    temperature: Optional[float] = 0.7
    model: Optional[str] = "mistral-medium"

class ConversationResponse(BaseModel):
    response: str
    conversation_id: str
```

### 3. Service Mistral (services/mistral_service.py)

Créez un service pour interagir avec l'API Mistral :

```python
import os
from typing import List, Dict, Any
from mistralai.client import MistralClient
from mistralai.models.chat_completion import ChatMessage

class MistralService:
    def __init__(self):
        self.api_key = os.getenv("MISTRAL_API_KEY")
        self.client = MistralClient(api_key=self.api_key)
    
    def generate_response(self, messages: List[Dict[str, str]], 
                         model: str = "mistral-medium", 
                         temperature: float = 0.7) -> str:
        """
        Génère une réponse via l'API Mistral.
        
        Args:
            messages: Liste de messages au format {"role": "...", "content": "..."}
            model: Modèle Mistral à utiliser
            temperature: Température (créativité) de la génération
            
        Returns:
            str: Réponse générée
        """
        # Convertir les messages au format attendu par l'API Mistral
        mistral_messages = [
            ChatMessage(role=msg["role"], content=msg["content"])
            for msg in messages
        ]
        
        try:
            # Appel à l'API Mistral
            response = self.client.chat(
                model=model,
                messages=mistral_messages,
                temperature=temperature
            )
            
            return response.choices[0].message.content
        except Exception as e:
            # Gestion des erreurs
            print(f"Erreur lors de l'appel à l'API Mistral: {e}")
            return f"Désolé, une erreur s'est produite lors de la génération de la réponse: {str(e)}"
```

### 4. Application principale (main.py)

L'application FastAPI principale qui expose les endpoints :

```python
import os
import uuid
from fastapi import FastAPI, HTTPException, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse

from models.conversation import ConversationRequest, ConversationResponse
from services.mistral_service import MistralService

# Chargement des variables d'environnement
from dotenv import load_dotenv
load_dotenv()

# Initialisation de l'application FastAPI
app = FastAPI(
    title="Chatbot pédagogique API",
    description="API pour le chatbot pédagogique sur le Deep Learning",
    version="1.0.0"
)

# Configuration CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # En production, spécifiez les domaines autorisés
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialisation des services
mistral_service = MistralService()

# Stockage des conversations (dans un vrai projet, utilisez une base de données)
conversations = {}

# Routes
@app.post("/api/chat", response_model=ConversationResponse)
async def chat(request: ConversationRequest):
    """
    Endpoint pour interagir avec le chatbot
    """
    # Générer un ID de conversation s'il n'existe pas
    conversation_id = str(uuid.uuid4())
    
    try:
        # Obtenir la réponse de Mistral AI
        system_message = {
            "role": "system",
            "content": f"Tu es un assistant pédagogique spécialisé en Deep Learning pour des étudiants de niveau {request.user_level}."
        }
        
        # Préparer les messages avec le message système en premier
        all_messages = [system_message] + [msg.dict() for msg in request.messages]
        
        # Générer la réponse
        response = mistral_service.generate_response(
            messages=all_messages,
            model=request.model,
            temperature=request.temperature
        )
        
        # Sauvegarder la conversation
        if conversation_id not in conversations:
            conversations[conversation_id] = all_messages
        conversations[conversation_id].append({"role": "assistant", "content": response})
        
        return ConversationResponse(
            response=response,
            conversation_id=conversation_id
        )
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/health")
async def health_check():
    """
    Endpoint de vérification de la santé de l'API
    """
    return {"status": "healthy"}

# Servir les fichiers statiques (si nécessaire)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Point d'entrée
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
```

## Utilisation de l'API FastAPI

### Lancement de l'application

Pour démarrer l'application :

```bash
uvicorn main:app --reload
```

L'application sera accessible à l'adresse `http://localhost:8000`.

### Documentation automatique

FastAPI génère automatiquement une documentation interactive :

- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

### Appel de l'API depuis JavaScript

Voici comment appeler votre API depuis le frontend :

```javascript
async function sendMessage(message) {
    const conversation = [
        {
            role: "user",
            content: message
        }
    ];
    
    try {
        const response = await fetch('http://localhost:8000/api/chat', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                messages: conversation,
                user_level: "beginner", // ou "intermediate", "advanced"
                temperature: 0.7
            })
        });
        
        if (!response.ok) {
            throw new Error('Erreur réseau ou serveur');
        }
        
        const data = await response.json();
        return data.response;
    } catch (error) {
        console.error('Erreur:', error);
        return "Désolé, une erreur s'est produite lors de la communication avec le serveur.";
    }
}
```

## Fonctionnalités avancées

### 1. Traitement asynchrone

FastAPI supporte nativement l'asynchrone, utile pour les opérations à latence élevée :

```python
@app.post("/api/chat/async")
async def chat_async(request: ConversationRequest, background_tasks: BackgroundTasks):
    # Générer un ID pour cette requête
    request_id = str(uuid.uuid4())
    
    # Traiter la requête en arrière-plan
    background_tasks.add_task(process_chat_request, request, request_id)
    
    return {"status": "processing", "request_id": request_id}

async def process_chat_request(request: ConversationRequest, request_id: str):
    # Traitement asynchrone de la requête
    # ...
```

### 2. Dépendances et injection

FastAPI offre un système de dépendances puissant :

```python
async def get_mistral_service():
    return MistralService()

@app.post("/api/chat")
async def chat(
    request: ConversationRequest, 
    mistral_service: MistralService = Depends(get_mistral_service)
):
    # Utiliser le service injecté
    # ...
```

### 3. Rate limiting

Implémentation simple de rate limiting :

```python
from fastapi import Request, HTTPException
import time

# Dictionnaire pour stocker les compteurs de requêtes
request_counts = {}

@app.middleware("http")
async def rate_limit_middleware(request: Request, call_next):
    client_ip = request.client.host
    
    # Initialiser ou récupérer les données de l'IP
    if client_ip not in request_counts:
        request_counts[client_ip] = {"count": 0, "reset_time": time.time() + 60}
    
    # Vérifier si le compteur doit être réinitialisé
    if time.time() > request_counts[client_ip]["reset_time"]:
        request_counts[client_ip] = {"count": 0, "reset_time": time.time() + 60}
    
    # Vérifier la limite
    if request_counts[client_ip]["count"] >= 10:  # Limite de 10 requêtes par minute
        raise HTTPException(status_code=429, detail="Trop de requêtes")
    
    # Incrémenter le compteur
    request_counts[client_ip]["count"] += 1
    
    # Continuer avec la requête
    response = await call_next(request)
    return response
```

## Bonnes pratiques

1. **Utiliser des modèles Pydantic** pour valider les entrées/sorties
2. **Organiser le code** en modules réutilisables (services, modèles, etc.)
3. **Implémenter la gestion d'erreurs** pour toutes les opérations critiques
4. **Documenter les endpoints** avec des docstrings détaillées
5. **Utiliser des dépendances** pour l'injection et la réutilisation du code
6. **Implémenter des tests** avec pytest et le client de test FastAPI
7. **Utiliser des variables d'environnement** pour les configurations sensibles
8. **Mettre en cache les réponses fréquentes** pour optimiser les performances

## Comparaison avec Flask

| Fonctionnalité | FastAPI | Flask |
|----------------|---------|-------|
| Performance | Très rapide (basé sur Starlette) | Moins performant |
| Documentation | Automatique (OpenAPI/Swagger) | Manuelle ou extensions tierces |
| Validation | Automatique avec Pydantic | Manuelle ou Flask-WTF |
| Asynchrone | Support natif | Pas de support natif |
| Typage | Typage fort | Pas de typage par défaut |
| Extensions | Écosystème en croissance | Écosystème mature |
| Courbe d'apprentissage | Moyenne | Faible |

## Ressources supplémentaires

- [Documentation officielle FastAPI](https://fastapi.tiangolo.com/)
- [Pydantic](https://pydantic-docs.helpmanual.io/)
- [Uvicorn ASGI Server](https://www.uvicorn.org/)
- [Mistral AI API Docs](https://docs.mistral.ai/)

## Troubleshooting

| Problème | Solution |
|----------|----------|
| `ModuleNotFoundError` | Vérifiez que vous avez installé toutes les dépendances |
| Erreur CORS | Assurez-vous que le middleware CORS est correctement configuré |
| Erreur 422 Unprocessable Entity | Vérifiez la structure de votre requête selon les modèles Pydantic |
| Erreur API Mistral | Vérifiez votre clé API et la disponibilité du service |

Ce guide vous a fourni une base solide pour intégrer FastAPI dans votre projet de chatbot pédagogique. N'hésitez pas à explorer les fonctionnalités avancées de FastAPI pour améliorer encore votre application.