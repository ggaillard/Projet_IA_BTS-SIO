# Intégration de l'API Mistral avec FastAPI - Premier test
# BTS SIO  - Séance 2: Types de réseaux et applications

```python
import requests
import json
import os
from dotenv import load_dotenv
from fastapi import FastAPI, Request, Form, HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, JSONResponse
import uvicorn
from pydantic import BaseModel


# Charger les variables d'environnement
load_dotenv()

# Configuration de l'API Mistral
MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY", "votre_clé_api")  # À remplacer par votre clé API
MISTRAL_API_URL = "https://api.mistral.ai/v1/chat/completions"

# Initialisation de l'application FastAPI
app = FastAPI(title="Explorateur de concepts Deep Learning", 
              description="Une API pour explorer les concepts du Deep Learning avec Mistral AI")

# Configuration des templates
templates = Jinja2Templates(directory="templates")

# 1. Fonction simple pour appeler l'API Mistral
def mistral_chat_completion(prompt, model="mistral-tiny", max_tokens=1000):
    """
    Appelle l'API Mistral pour générer une réponse à partir d'un prompt.
    
    Args:
        prompt (str): Le message à envoyer à l'API
        model (str): Le modèle à utiliser (mistral-tiny, mistral-small, mistral-medium, etc.)
        max_tokens (int): Nombre maximum de tokens pour la réponse
        
    Returns:
        dict: La réponse de l'API
    """
    headers = {
        "Authorization": f"Bearer {MISTRAL_API_KEY}",
        "Content-Type": "application/json"
    }
    
    data = {
        "model": model,
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "max_tokens": max_tokens
    }
    
    try:
        response = requests.post(MISTRAL_API_URL, headers=headers, data=json.dumps(data))
        response.raise_for_status()  # Lever une exception si la requête échoue
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Erreur lors de l'appel à l'API Mistral: {e}")
        return {"error": str(e)}

# 2. Test simple de l'API
def test_mistral_api():
    """
    Teste l'API Mistral avec un prompt simple.
    """
    prompt = "Explique-moi ce qu'est le Deep Learning en 3 phrases simples."
    
    print(f"Envoi du prompt à Mistral: '{prompt}'")
    response = mistral_chat_completion(prompt)
    
    if "error" in response:
        print(f"Erreur: {response['error']}")
        return
    
    # Extraire et afficher la réponse
    try:
        message_content = response["choices"][0]["message"]["content"]
        print("\nRéponse de Mistral:")
        print(message_content)
        
        # Informations supplémentaires sur la réponse
        if "usage" in response:
            usage = response["usage"]
            print("\nUtilisation de tokens:")
            print(f"- Prompt: {usage.get('prompt_tokens', 'N/A')} tokens")
            print(f"- Réponse: {usage.get('completion_tokens', 'N/A')} tokens")
            print(f"- Total: {usage.get('total_tokens', 'N/A')} tokens")
    except (KeyError, IndexError) as e:
        print(f"Erreur lors du traitement de la réponse: {e}")
        print("Réponse brute:", response)

# 3. Fonction avancée pour l'explication de concepts de Deep Learning
def explain_deep_learning_concept(concept, difficulty="débutant"):
    """
    Demande à l'API Mistral d'expliquer un concept de Deep Learning.
    
    Args:
        concept (str): Le concept à expliquer
        difficulty (str): Le niveau de difficulté (débutant, intermédiaire, avancé)
        
    Returns:
        str: L'explication générée
    """
    # Construire un prompt éducatif structuré
    prompt = f"""
    En tant que tuteur pédagogique spécialisé en Deep Learning, explique le concept de '{concept}' 
    à un étudiant de BTS SIO  (niveau {difficulty}).
    
    Ton explication doit inclure:
    1. Une définition simple et claire
    2. Un exemple concret d'application
    3. Comment ce concept est utilisé dans le développement d'applications
    
    Utilise un langage accessible mais techniquement précis.
    """
    
    response = mistral_chat_completion(prompt, model="mistral-small")
    
    if "error" in response:
        return f"Erreur: {response['error']}"
    
    try:
        return response["choices"][0]["message"]["content"]
    except (KeyError, IndexError):
        return "Erreur lors de la récupération de la réponse."

# 4. Modèles Pydantic pour les requêtes
class ConceptRequest(BaseModel):
    concept: str
    difficulty: str = "débutant"

# 5. Routes FastAPI
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/api/explain")
async def api_explain(request: ConceptRequest):
    if not request.concept:
        raise HTTPException(status_code=400, detail="Concept manquant")
    
    explanation = explain_deep_learning_concept(request.concept, request.difficulty)
    return {"explanation": explanation}

# 6. Template HTML simple pour l'interface
def create_template_directory():
    """Crée un répertoire templates et un fichier index.html"""
    import os
    os.makedirs('templates', exist_ok=True)
    
    with open('templates/index.html', 'w') as f:
        f.write("""
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Explorateur de concepts Deep Learning</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            background-color: #f5f8fa;
            color: #333;
        }
        h1 {
            color: #2c3e50;
            border-bottom: 2px solid #3498db;
            padding-bottom: 10px;
        }
        .container {
            background-color: white;
            border-radius: 8px;
            padding: 20px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }
        label {
            display: block;
            margin-top: 15px;
            font-weight: bold;
            color: #2c3e50;
        }
        input, select, button {
            width: 100%;
            padding: 10px;
            margin-top: 5px;
            border: 1px solid #ddd;
            border-radius: 4px;
            box-sizing: border-box;
        }
        button {
            background-color: #3498db;
            color: white;
            border: none;
            padding: 12px;
            margin-top: 20px;
            cursor: pointer;
            font-weight: bold;
            transition: background-color 0.3s;
        }
        button:hover {
            background-color: #2980b9;
        }
        #result {
            margin-top: 20px;
            padding: 20px;
            background-color: #f8f9fa;
            border-left: 4px solid #3498db;
            border-radius: 4px;
            white-space: pre-wrap;
        }
        .loading {
            text-align: center;
            margin-top: 20px;
            display: none;
        }
        .hint {
            font-size: 0.8em;
            color: #7f8c8d;
            margin-top: 5px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Explorateur de concepts Deep Learning</h1>
        <p>Utilisez cet outil pour explorer et comprendre les concepts clés du Deep Learning, expliqués par l'IA.</p>
        
        <form id="explainForm">
            <label for="concept">Concept à expliquer:</label>
            <input type="text" id="concept" required placeholder="Ex: réseaux de neurones convolutifs, LSTM, dropout...">
            <div class="hint">Essayez des concepts comme: convolution, pooling, fonction d'activation, rétropropagation...</div>
            
            <label for="difficulty">Niveau de difficulté:</label>
            <select id="difficulty">
                <option value="débutant">Débutant</option>
                <option value="intermédiaire">Intermédiaire</option>
                <option value="avancé">Avancé</option>
            </select>
            
            <button type="submit">Expliquer</button>
        </form>
        
        <div class="loading" id="loading">
            <p>Chargement de l'explication...</p>
        </div>
        
        <div id="result"></div>
    </div>
    
    <script>
        document.getElementById('explainForm').addEventListener('submit', async function(e) {
            e.preventDefault();
            
            const concept = document.getElementById('concept').value.trim();
            const difficulty = document.getElementById('difficulty').value;
            const resultDiv = document.getElementById('result');
            const loadingDiv = document.getElementById('loading');
            
            if (!concept) {
                resultDiv.innerHTML = "Veuillez entrer un concept à expliquer.";
                return;
            }
            
            // Afficher l'indicateur de chargement
            loadingDiv.style.display = 'block';
            resultDiv.innerHTML = "";
            
            try {
                const response = await fetch('/api/explain', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({ concept, difficulty })
                });
                
                const data = await response.json();
                
                if (data.error) {
                    resultDiv.innerHTML = `<p style="color: red">Erreur: ${data.error}</p>`;
                } else {
                    resultDiv.innerHTML = data.explanation.replace(/\\n/g, '<br>');
                }
            } catch (error) {
                resultDiv.innerHTML = `<p style="color: red">Erreur: ${error.message}</p>`;
            } finally {
                // Cacher l'indicateur de chargement
                loadingDiv.style.display = 'none';
            }
        });
    </script>
</body>
</html>
        """)
    
    print("Template index.html créé avec succès!")

# 7. Fonction principale pour exécuter l'application
def main():
    """Fonction principale"""
    print("=== EXPLORATION DE L'API MISTRAL POUR LE CHATBOT PÉDAGOGIQUE ===")
    
    # Tester si la clé API est configurée
    if MISTRAL_API_KEY == "votre_clé_api":
        print("\nERREUR: Vous devez configurer votre clé API Mistral!")
        print("1. Créez un fichier .env dans le même répertoire que ce script")
        print("2. Ajoutez la ligne: MISTRAL_API_KEY=votre_clé_api_réelle")
        print("3. Relancez le script")
        return
    
    # Test simple de l'API
    print("\n1. Test simple de l'API Mistral")
    test_mistral_api()
    
    # Création du répertoire et du fichier template
    print("\n2. Création du template pour l'application web")
    create_template_directory()
    print("   Template créé dans le répertoire 'templates/'")
    
    # Lancement de l'application FastAPI
    print("\n3. Démarrage de l'application web")
    print("   URL: http://localhost:8000")
    print("   Documentation de l'API: http://localhost:8000/docs")
    print("   Appuyez sur Ctrl+C pour quitter")
    uvicorn.run(app, host="0.0.0.0", port=8000)

if __name__ == "__main__":
    main()

```