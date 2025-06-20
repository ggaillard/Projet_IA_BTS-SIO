# Application de tickets intelligente - Code complet

## Structure de l'application

```
systeme-tickets/
├── app.py                  # Application Flask principale
├── config.py               # Configuration API
├── requirements.txt        # Dépendances Python
├── tickets.json           # Base de données simple
├── templates/
│   ├── base.html          # Template de base
│   ├── index.html         # Liste des tickets
│   ├── new_ticket.html    # Création de ticket
│   └── ticket_detail.html # Détail d'un ticket
├── static/
│   ├── style.css          # Styles CSS
│   └── script.js          # JavaScript
└── .env                   # Variables d'environnement
```

## Fichier principal (app.py)

```python
from flask import Flask, request, render_template, redirect, url_for, jsonify, flash
import json
import os
from datetime import datetime
from dotenv import load_dotenv
import requests

# Chargement des variables d'environnement
load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'dev-key-change-in-production')

# Configuration API (Mistral ou autre)
API_KEY = os.getenv('API_KEY', 'your-api-key-here')
API_URL = os.getenv('API_URL', 'https://api.mistral.ai/v1/chat/completions')

def load_tickets():
    """Charge les tickets depuis le fichier JSON"""
    try:
        with open('tickets.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_tickets(tickets):
    """Sauvegarde les tickets dans le fichier JSON"""
    with open('tickets.json', 'w', encoding='utf-8') as f:
        json.dump(tickets, f, indent=4, ensure_ascii=False)

def classify_ticket_simple(description):
    """
    Classification simple par mots-clés (version de base)
    À améliorer avec une vraie API d'IA
    """
    description_lower = description.lower()
    
    # Catégories et mots-clés
    categories = {
        "Matériel": {
            "keywords": ["ordinateur", "pc", "écran", "souris", "clavier", "imprimante", 
                        "scanner", "batterie", "câble", "hardware", "matériel"],
            "priority_base": "Moyenne"
        },
        "Logiciel": {
            "keywords": ["logiciel", "application", "programme", "software", "bug", 
                        "windows", "office", "excel", "word", "installer", "désinstaller"],
            "priority_base": "Basse"
        },
        "Réseau": {
            "keywords": ["réseau", "wifi", "internet", "connexion", "ip", "dns", 
                        "serveur", "ethernet", "débit", "lenteur", "network"],
            "priority_base": "Haute"
        },
        "Accès": {
            "keywords": ["mot de passe", "password", "login", "compte", "accès", 
                        "droits", "permission", "authentification", "identifiant"],
            "priority_base": "Moyenne"
        },
        "Sécurité": {
            "keywords": ["virus", "malware", "sécurité", "antivirus", "spam", 
                        "phishing", "hacker", "piratage"],
            "priority_base": "Haute"
        }
    }
    
    # Mots-clés de priorité
    high_priority_keywords = ["urgent", "critique", "bloqué", "impossible", 
                             "panne", "down", "erreur critique"]
    low_priority_keywords = ["question", "demande", "information", "comment", 
                            "formation", "aide"]
    
    # Recherche de la catégorie
    best_category = "Autre"
    best_score = 0
    
    for category, data in categories.items():
        score = sum(1 for keyword in data["keywords"] if keyword in description_lower)
        if score > best_score:
            best_score = score
            best_category = category
    
    # Détermination de la priorité
    priority = categories.get(best_category, {}).get("priority_base", "Moyenne")
    
    # Ajustement selon les mots-clés de priorité
    if any(keyword in description_lower for keyword in high_priority_keywords):
        priority = "Haute"
    elif any(keyword in description_lower for keyword in low_priority_keywords):
        priority = "Basse"
    
    # Calcul de la confiance
    confidence = min(0.9, 0.5 + (best_score * 0.1)) if best_score > 0 else 0.3
    
    return {
        "category": best_category,
        "priority": priority,
        "confidence": confidence,
        "matched_keywords": best_score
    }

def classify_ticket_with_api(description):
    """
    Classification avancée avec API d'IA
    Version avec vraie API Mistral
    """
    if not API_KEY or API_KEY == 'your-api-key-here':
        # Fallback vers classification simple
        return classify_ticket_simple(description)
    
    try:
        # Prompt pour l'API
        prompt = f"""Tu es un système de classification de tickets IT pour une entreprise.

Classe ce ticket dans une de ces catégories EXACTEMENT :
- Matériel
- Logiciel  
- Réseau
- Accès
- Sécurité
- Autre

Détermine aussi la priorité : Haute, Moyenne ou Basse

Description du ticket : "{description}"

Réponds UNIQUEMENT au format JSON :
{{"category": "nom_catégorie", "priority": "niveau_priorité", "explanation": "courte_explication"}}"""

        headers = {
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        }
        
        data = {
            "model": "mistral-tiny",
            "messages": [{"role": "user", "content": prompt}],
            "max_tokens": 150,
            "temperature": 0.1
        }
        
        response = requests.post(API_URL, headers=headers, json=data, timeout=10)
        response.raise_for_status()
        
        result = response.json()
        content = result["choices"][0]["message"]["content"].strip()
        
        # Parsing du JSON retourné
        try:
            parsed = json.loads(content)
            return {
                "category": parsed.get("category", "Autre"),
                "priority": parsed.get("priority", "Moyenne"),
                "confidence": 0.85,
                "explanation": parsed.get("explanation", "")
            }
        except json.JSONDecodeError:
            # Si le parsing JSON échoue, fallback
            return classify_ticket_simple(description)
            
    except Exception as e:
        print(f"Erreur API : {e}")
        return classify_ticket_simple(description)

# Routes Flask
@app.route('/')
def index():
    """Page d'accueil avec liste des tickets"""
    tickets = load_tickets()
    
    # Statistiques pour le dashboard
    stats = {
        "total": len(tickets),
        "ouvert": len([t for t in tickets if t["status"] == "Ouvert"]),
        "en_cours": len([t for t in tickets if t["status"] == "En cours"]),
        "ferme": len([t for t in tickets if t["status"] == "Fermé"])
    }
    
    # Tri par date (plus récents en premier)
    tickets.sort(key=lambda x: x["created_at"], reverse=True)
    
    return render_template('index.html', tickets=tickets, stats=stats)

@app.route('/ticket/<ticket_id>')
def ticket_detail(ticket_id):
    """Affichage d'un ticket spécifique"""
    tickets = load_tickets()
    ticket = next((t for t in tickets if t["id"] == ticket_id), None)
    
    if not ticket:
        flash("Ticket non trouvé", "error")
        return redirect(url_for('index'))
    
    return render_template('ticket_detail.html', ticket=ticket)

@app.route('/new', methods=['GET', 'POST'])
def new_ticket():
    """Création d'un nouveau ticket"""
    if request.method == 'POST':
        title = request.form.get('title', '').strip()
        description = request.form.get('description', '').strip()
        user_name = request.form.get('user_name', '').strip()
        user_email = request.form.get('user_email', '').strip()
        use_api = request.form.get('use_api') == 'on'
        
        if not title or not description:
            flash("Le titre et la description sont obligatoires", "error")
            return render_template('new_ticket.html')
        
        # Classification du ticket
        if use_api:
            classification = classify_ticket_with_api(description)
        else:
            classification = classify_ticket_simple(description)
        
        # Génération ID unique
        ticket_id = datetime.now().strftime('%Y%m%d%H%M%S')
        
        # Création du ticket
        ticket = {
            'id': ticket_id,
            'title': title,
            'description': description,
            'user_name': user_name or 'Utilisateur',
            'user_email': user_email,
            'category': classification['category'],
            'priority': classification['priority'],
            'confidence': classification.get('confidence', 0.5),
            'explanation': classification.get('explanation', ''),
            'status': 'Ouvert',
            'assigned_to': assign_to_team(classification['category']),
            'created_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'updated_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'comments': []
        }
        
        # Sauvegarde
        tickets = load_tickets()
        tickets.append(ticket)
        save_tickets(tickets)
        
        flash(f"Ticket #{ticket_id} créé avec succès ! Catégorie: {classification['category']}, Priorité: {classification['priority']}", "success")
        return redirect(url_for('ticket_detail', ticket_id=ticket_id))
    
    return render_template('new_ticket.html')

@app.route('/api/classify', methods=['POST'])
def api_classify():
    """API pour classification en temps réel"""
    data = request.get_json()
    description = data.get('description', '')
    use_api = data.get('use_api', False)
    
    if not description.strip():
        return jsonify({"error": "Description manquante"}), 400
    
    try:
        if use_api:
            result = classify_ticket_with_api(description)
        else:
            result = classify_ticket_simple(description)
        
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def assign_to_team(category):
    """Assigne le ticket à l'équipe appropriée"""
    team_mapping = {
        "Matériel": "Support Niveau 1",
        "Logiciel": "Support Applications",
        "Réseau": "Équipe Infrastructure",
        "Accès": "Support Niveau 1",
        "Sécurité": "Équipe Sécurité",
        "Autre": "Support Général"
    }
    return team_mapping.get(category, "Support Général")

@app.route('/update_status/<ticket_id>', methods=['POST'])
def update_status(ticket_id):
    """Mise à jour du statut d'un ticket"""
    new_status = request.form.get('status')
    comment = request.form.get('comment', '').strip()
    
    tickets = load_tickets()
    ticket = next((t for t in tickets if t["id"] == ticket_id), None)
    
    if not ticket:
        flash("Ticket non trouvé", "error")
        return redirect(url_for('index'))
    
    # Mise à jour du statut
    ticket['status'] = new_status
    ticket['updated_at'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    # Ajout d'un commentaire si fourni
    if comment:
        ticket['comments'].append({
            'text': comment,
            'author': 'Technicien',
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        })
    
    save_tickets(tickets)
    flash(f"Statut mis à jour : {new_status}", "success")
    return redirect(url_for('ticket_detail', ticket_id=ticket_id))

if __name__ == '__main__':
    app.run(debug=True, port=5000)
```

## Templates HTML

### Template de base (templates/base.html)
```html
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}Système de Tickets{% endblock %}</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.7.2/font/bootstrap-icons.css" rel="stylesheet">
    <link href="{{ url_for('static', filename='style.css') }}" rel="stylesheet">
</head>
<body>
    <nav class="navbar navbar-expand-lg navbar-dark bg-primary">
        <div class="container">
            <a class="navbar-brand" href="{{ url_for('index') }}">
                <i class="bi bi-ticket-perforated"></i> Système de Tickets IT
            </a>
            <div class="navbar-nav ms-auto">
                <a class="nav-link" href="{{ url_for('index') }}">
                    <i class="bi bi-list-ul"></i> Tickets
                </a>
                <a class="nav-link" href="{{ url_for('new_ticket') }}">
                    <i class="bi bi-plus-circle"></i> Nouveau
                </a>
            </div>
        </div>
    </nav>

    <div class="container mt-4">
        {% with messages = get_flashed_messages(with_categories=true) %}
            {% if messages %}
                {% for category, message in messages %}
                    <div class="alert alert-{{ 'danger' if category == 'error' else 'success' }} alert-dismissible fade show">
                        {{ message }}
                        <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
                    </div>
                {% endfor %}
            {% endif %}
        {% endwith %}

        {% block content %}{% endblock %}
    </div>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js"></script>
    <script src="{{ url_for('static', filename='script.js') }}"></script>
</body>
</html>
```

### Page d'accueil (templates/index.html)
```html
{% extends "base.html" %}

{% block title %}Tableau de bord - Tickets{% endblock %}

{% block content %}
<div class="row mb-4">
    <div class="col-md-12">
        <h1><i class="bi bi-speedometer2"></i> Tableau de bord des tickets</h1>
    </div>
</div>

<!-- Statistiques -->
<div class="row mb-4">
    <div class="col-md-3">
        <div class="card bg-primary text-white">
            <div class="card-body">
                <div class="d-flex justify-content-between">
                    <div>
                        <h4>{{ stats.total }}</h4>
                        <p>Total</p>
                    </div>
                    <i class="bi bi-ticket-perforated fs-1"></i>
                </div>
            </div>
        </div>
    </div>
    <div class="col-md-3">
        <div class="card bg-warning text-white">
            <div class="card-body">
                <div class="d-flex justify-content-between">
                    <div>
                        <h4>{{ stats.ouvert }}</h4>
                        <p>Ouverts</p>
                    </div>
                    <i class="bi bi-exclamation-circle fs-1"></i>
                </div>
            </div>
        </div>
    </div>
    <div class="col-md-3">
        <div class="card bg-info text-white">
            <div class="card-body">
                <div class="d-flex justify-content-between">
                    <div>
                        <h4>{{ stats.en_cours }}</h4>
                        <p>En cours</p>
                    </div>
                    <i class="bi bi-gear fs-1"></i>
                </div>
            </div>
        </div>
    </div>
    <div class="col-md-3">
        <div class="card bg-success text-white">
            <div class="card-body">
                <div class="d-flex justify-content-between">
                    <div>
                        <h4>{{ stats.ferme }}</h4>
                        <p>Fermés</p>
                    </div>
                    <i class="bi bi-check-circle fs-1"></i>
                </div>
            </div>
        </div>
    </div>
</div>

<!-- Liste des tickets -->
<div class="card">
    <div class="card-header d-flex justify-content-between align-items-center">
        <h5><i class="bi bi-list-ul"></i> Liste des tickets</h5>
        <a href="{{ url_for('new_ticket') }}" class="btn btn-primary">
            <i class="bi bi-plus-circle"></i> Nouveau ticket
        </a>
    </div>
    <div class="card-body">
        {% if tickets %}
            <div class="table-responsive">
                <table class="table table-hover">
                    <thead>
                        <tr>
                            <th>ID</th>
                            <th>Titre</th>
                            <th>Catégorie</th>
                            <th>Priorité</th>
                            <th>Statut</th>
                            <th>Assigné à</th>
                            <th>Créé le</th>
                            <th>Actions</th>
                        </tr>
                    </thead>
                    <tbody>
                        {% for ticket in tickets %}
                        <tr>
                            <td><code>#{{ ticket.id }}</code></td>
                            <td>
                                <strong>{{ ticket.title }}</strong>
                                <br><small class="text-muted">{{ ticket.user_name }}</small>
                            </td>
                            <td>
                                <span class="badge bg-secondary">{{ ticket.category }}</span>
                            </td>
                            <td>
                                {% set priority_class = {'Haute': 'danger', 'Moyenne': 'warning', 'Basse': 'success'} %}
                                <span class="badge bg-{{ priority_class.get(ticket.priority, 'secondary') }}">
                                    {{ ticket.priority }}
                                </span>
                            </td>
                            <td>
                                {% set status_class = {'Ouvert': 'warning', 'En cours': 'info', 'Fermé': 'success'} %}
                                <span class="badge bg-{{ status_class.get(ticket.status, 'secondary') }}">
                                    {{ ticket.status }}
                                </span>
                            </td>
                            <td><small>{{ ticket.assigned_to }}</small></td>
                            <td><small>{{ ticket.created_at }}</small></td>
                            <td>
                                <a href="{{ url_for('ticket_detail', ticket_id=ticket.id) }}" 
                                   class="btn btn-sm btn-outline-primary">
                                    <i class="bi bi-eye"></i>
                                </a>
                            </td>
                        </tr>
                        {% endfor %}
                    </tbody>
                </table>
            </div>
        {% else %}
            <div class="text-center py-5">
                <i class="bi bi-inbox fs-1 text-muted"></i>
                <p class="text-muted">Aucun ticket pour le moment</p>
                <a href="{{ url_for('new_ticket') }}" class="btn btn-primary">
                    Créer le premier ticket
                </a>
            </div>
        {% endif %}
    </div>
</div>
{% endblock %}
```

### Création de ticket (templates/new_ticket.html)
```html
{% extends "base.html" %}

{% block title %}Nouveau ticket{% endblock %}

{% block content %}
<div class="row">
    <div class="col-md-8 mx-auto">
        <div class="card">
            <div class="card-header">
                <h5><i class="bi bi-plus-circle"></i> Créer un nouveau ticket</h5>
            </div>
            <div class="card-body">
                <form method="POST">
                    <div class="mb-3">
                        <label for="title" class="form-label">Titre du problème *</label>
                        <input type="text" class="form-control" id="title" name="title" 
                               placeholder="Résumé bref du problème" maxlength="100" required>
                    </div>
                    
                    <div class="mb-3">
                        <label for="description" class="form-label">Description détaillée *</label>
                        <textarea class="form-control" id="description" name="description" 
                                  rows="5" placeholder="Décrivez le problème en détail..." 
                                  required></textarea>
                        <div class="form-text">
                            Plus vous donnez de détails, meilleure sera la classification automatique.
                        </div>
                    </div>
                    
                    <div class="row">
                        <div class="col-md-6">
                            <div class="mb-3">
                                <label for="user_name" class="form-label">Votre nom</label>
                                <input type="text" class="form-control" id="user_name" name="user_name" 
                                       placeholder="Nom et prénom">
                            </div>
                        </div>
                        <div class="col-md-6">
                            <div class="mb-3">
                                <label for="user_email" class="form-label">Email de contact</label>
                                <input type="email" class="form-control" id="user_email" name="user_email" 
                                       placeholder="email@entreprise.com">
                            </div>
                        </div>
                    </div>
                    
                    <div class="mb-3">
                        <div class="form-check">
                            <input class="form-check-input" type="checkbox" id="use_api" name="use_api" checked>
                            <label class="form-check-label" for="use_api">
                                Utiliser l'IA pour la classification avancée
                            </label>
                            <div class="form-text">
                                Si décoché, utilise la classification par mots-clés simple.
                            </div>
                        </div>
                    </div>
                    
                    <!-- Zone de prévisualisation -->
                    <div id="preview-zone" class="mb-3" style="display: none;">
                        <div class="alert alert-info">
                            <h6>Aperçu de la classification :</h6>
                            <div id="preview-content"></div>
                        </div>
                    </div>
                    
                    <div class="d-flex justify-content-between">
                        <a href="{{ url_for('index') }}" class="btn btn-secondary">
                            <i class="bi bi-arrow-left"></i> Retour
                        </a>
                        <div>
                            <button type="button" class="btn btn-outline-primary" id="preview-btn">
                                <i class="bi bi-eye"></i> Aperçu
                            </button>
                            <button type="submit" class="btn btn-primary">
                                <i class="bi bi-check-circle"></i> Créer le ticket
                            </button>
                        </div>
                    </div>
                </form>
            </div>
        </div>
    </div>
</div>

<script>
// Prévisualisation de la classification
document.getElementById('preview-btn').addEventListener('click', function() {
    const description = document.getElementById('description').value;
    const useApi = document.getElementById('use_api').checked;
    
    if (!description.trim()) {
        alert('Veuillez saisir une description');
        return;
    }
    
    fetch('/api/classify', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({description: description, use_api: useApi})
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            alert('Erreur: ' + data.error);
        } else {
            const priorityColor = {
                'Haute': 'danger',
                'Moyenne': 'warning',
                'Basse': 'success'
            };
            
            document.getElementById('preview-content').innerHTML = `
                <p><strong>Catégorie:</strong> <span class="badge bg-secondary">${data.category}</span></p>
                <p><strong>Priorité:</strong> <span class="badge bg-${priorityColor[data.priority] || 'secondary'}">${data.priority}</span></p>
                <p><strong>Confiance:</strong> ${Math.round(data.confidence * 100)}%</p>
                ${data.explanation ? `<p><strong>Explication:</strong> ${data.explanation}</p>` : ''}
            `;
            document.getElementById('preview-zone').style.display = 'block';
        }
    })
    .catch(error => {
        console.error('Erreur:', error);
        alert('Erreur de communication avec le serveur');
    });
});
</script>
{% endblock %}
```

## Fichiers de configuration

### Requirements.txt
```
Flask==2.3.3
python-dotenv==1.0.0
requests==2.31.0
```

### .env (exemple)
```
SECRET_KEY=your-secret-key-here
API_KEY=your-mistral-api-key-here
API_URL=https://api.mistral.ai/v1/chat/completions
```

### CSS personnalisé (static/style.css)
```css
.priority-haute {
    border-left: 4px solid #dc3545;
}

.priority-moyenne {
    border-left: 4px solid #ffc107;
}

.priority-basse {
    border-left: 4px solid #28a745;
}

.ticket-card {
    transition: transform 0.2s;
}

.ticket-card:hover {
    transform: translateY(-2px);
    box-shadow: 0 4px 8px rgba(0,0,0,0.1);
}

.status-badge {
    font-size: 0.8em;
}

#preview-zone {
    border-radius: 8px;
}
```

Cette application complète permet aux étudiants d'avoir une base fonctionnelle pour tester la classification automatique avec ou sans API, tout en comprenant les concepts d'intégration d'IA dans une application métier.