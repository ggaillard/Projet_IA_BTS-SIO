# 🚨 Simulateur de pannes - Tests de résilience sécuritaire

Ce simulateur vous guide dans les tests de résistance du chatbot face à différents scénarios d'échec pour valider la robustesse sécuritaire.

## 🎯 Objectif des tests de panne

Les tests de résilience permettent de :
- **Vérifier** que le système ne révèle pas d'informations sensibles en cas d'erreur
- **Valider** les mécanismes de récupération automatique
- **Identifier** les vulnérabilités exposées uniquement lors de dysfonctionnements
- **Optimiser** la gestion d'erreurs pour maintenir la sécurité

## ⚠️ Instructions de sécurité

**Tests éthiques et contrôlés :**
- Effectuez ces tests UNIQUEMENT sur votre environnement de développement
- Ne jamais tester sur des systèmes de production sans autorisation
- Documentez tous les tests pour traçabilité
- Restaurez l'état normal après chaque test

## 🔧 Scénario 1 : API Mistral en maintenance

### Contexte de simulation
L'API Mistral AI devient temporairement indisponible (maintenance, quota épuisé, problème réseau).

### Méthodes de simulation

#### Option A : Clé API temporairement invalide
```python
# Dans votre configuration de test
MISTRAL_API_KEY_BACKUP = os.getenv("MISTRAL_API_KEY")
os.environ["MISTRAL_API_KEY"] = "sk-invalid-key-for-testing"

# Effectuer le test
response = test_chatbot_query("Explique les CNN")

# Restaurer la clé
os.environ["MISTRAL_API_KEY"] = MISTRAL_API_KEY_BACKUP
```

#### Option B : URL API modifiée
```python
# Modifier temporairement l'endpoint
MISTRAL_URL_BACKUP = "https://api.mistral.ai/v1/chat/completions"
MISTRAL_URL_TEST = "https://api-maintenance.mistral.ai/v1/chat/completions"

# Test avec URL invalide
```

#### Option C : Simulation de timeout
```python
# Configurer un timeout très court
import requests

session = requests.Session()
session.timeout = 0.001  # 1ms = garantit timeout

try:
    response = session.post(mistral_url, headers=headers, json=data)
except requests.Timeout:
    # Observer la gestion du timeout
    pass
```

### Éléments à observer et documenter

| Aspect | Questions à analyser | Résultat observé |
|--------|---------------------|------------------|
| **Message d'erreur** | Le message révèle-t-il des infos sensibles ? | |
| **Détails techniques** | URL, clé API, structure sont-ils exposés ? | |
| **Fallback** | Y a-t-il un mode dégradé fonctionnel ? | |
| **UX** | L'utilisateur comprend-il la situation ? | |
| **Logging** | L'incident est-il correctement tracé ? | |
| **Récupération** | Le système récupère-t-il automatiquement ? | |

### Messages d'erreur sécurisés vs non-sécurisés

**❌ Exemple NON sécurisé :**
```
Erreur: Impossible de contacter l'API Mistral à l'URL https://api.mistral.ai 
avec la clé sk-abc123... 
Code d'erreur 401: Invalid API key
Stack trace: /home/app/mistral_client.py line 45
```

**✅ Exemple sécurisé :**
```
Le service est temporairement indisponible. 
Veuillez réessayer dans quelques minutes.
Si le problème persiste, contactez l'assistance.
```

### Questions d'audit spécifiques

1. **Exposition d'informations :** Quelles données techniques sont visibles ?
2. **Gestion d'état :** Les conversations en cours sont-elles préservées ?
3. **Communication :** Le message utilisateur est-il approprié ?
4. **Monitoring :** L'incident génère-t-il les bonnes alertes ?

## 🌐 Scénario 2 : Connexion réseau coupée

### Contexte de simulation
La connexion réseau entre votre serveur et l'API Mistral est interrompue pendant une requête.

### Méthodes de simulation

#### Option A : Simulation par proxy
```python
# Configurer un proxy qui coupe la connexion
proxies = {
    'http': 'http://127.0.0.1:9999',  # Proxy inexistant
    'https': 'http://127.0.0.1:9999'
}

try:
    response = requests.post(url, proxies=proxies, timeout=5)
except requests.exceptions.ProxyError:
    # Observer la gestion d'erreur réseau
    pass
```

#### Option B : Firewall temporaire
```bash
# Linux/Mac - Bloquer temporairement l'accès
# ATTENTION: Nécessite des droits admin
sudo iptables -A OUTPUT -d api.mistral.ai -j DROP

# Test de votre application

# Restaurer
sudo iptables -D OUTPUT -d api.mistral.ai -j DROP
```

#### Option C : Simulation de déconnexion en cours de requête
```python
import threading
import time

def interrupt_connection():
    time.sleep(2)  # Attendre 2s puis couper
    # Simulation d'interruption réseau
    
# Lancer en parallèle avec votre requête
```

### Éléments à observer

| Aspect | Critères d'évaluation | Score |
|--------|----------------------|-------|
| **Détection timeout** | Temps avant détection de la panne | ⬜ <5s ⬜ 5-15s ⬜ >15s |
| **Gestion utilisateur** | Information claire de l'incident | ⬜ Claire ⬜ Acceptable ⬜ Confuse |
| **Retry automatique** | Tentatives de reconnexion | ⬜ Oui ⬜ Partiel ⬜ Non |
| **Préservation état** | Données utilisateur conservées | ⬜ Totale ⬜ Partielle ⬜ Perdue |
| **Récupération** | Retour automatique quand réseau OK | ⬜ Auto ⬜ Manuel ⬜ Aucune |

### Tests de robustesse réseau

**Test 1 : Coupure brève (5 secondes)**
- Observer : Le système attend-il et reprend-il ?
- Attendu : Retry automatique avec succès

**Test 2 : Coupure longue (2 minutes)**  
- Observer : Abandon avec message approprié ?
- Attendu : Timeout propre et message utilisateur

**Test 3 : Reconnexion avec nouvelle requête**
- Observer : Le système fonctionne-t-il normalement ?
- Attendu : Retour complet à la normale

## 🔐 Scénario 3 : Clé API compromise (révoquée)

### Contexte de simulation
La clé API Mistral a été compromise et révoquée côté fournisseur, générant des erreurs 401/403.

### Méthodes de simulation

#### Option A : Clé volontairement invalide
```python
# Sauvegarder la vraie clé
REAL_KEY = os.getenv("MISTRAL_API_KEY")

# Utiliser une clé syntaxiquement correcte mais invalide
os.environ["MISTRAL_API_KEY"] = "sk-" + "x" * 45  # Format correct, contenu invalide

# Effectuer les tests

# Restaurer
os.environ["MISTRAL_API_KEY"] = REAL_KEY
```

#### Option B : Clé avec permissions révoquées
```python
# Si vous avez accès à une clé expirée ou révoquée
REVOKED_KEY = "sk-ancienne-cle-revoquee..."
os.environ["MISTRAL_API_KEY"] = REVOKED_KEY
```

### Éléments critiques à évaluer

| Sécurité | Question | Conforme | Non-conforme |
|----------|----------|----------|--------------|
| **Exposition clé** | La clé compromise est-elle visible dans les logs ? | ⬜ | ⬜ |
| **Stack trace** | Les traces d'erreur révèlent-elles des chemins ? | ⬜ | ⬜ |
| **Arrêt sécurisé** | Le service s'arrête-t-il pour éviter d'autres dégâts ? | ⬜ | ⬜ |
| **Notification** | L'incident est-il notifié aux administrateurs ? | ⬜ | ⬜ |
| **Procédure** | Y a-t-il une procédure documentée de réponse ? | ⬜ | ⬜ |

### Scénario de compromission réaliste

**Étape 1 : Détection initiale**
```
12:34:56 - ERROR: API call failed with 401 Unauthorized
12:34:57 - ERROR: API call failed with 401 Unauthorized  
12:34:58 - ERROR: API call failed with 401 Unauthorized
```

**Étape 2 : Questions d'analyse**
1. Combien de tentatives avant arrêt automatique ?
2. Les erreurs 401 déclenchent-elles une alerte ?
3. Le système continue-t-il à exposer la clé compromise ?
4. Y a-t-il un mécanisme de clé de secours ?

**Étape 3 : Procédure de réponse attendue**
1. Arrêt immédiat des appels API
2. Notification équipe sécurité
3. Révocation côté Mistral (si pas déjà fait)
4. Génération nouvelle clé
5. Redéploiement sécurisé

## 💾 Scénario 4 : Surcharge serveur (CPU/Mémoire)

### Contexte de simulation
Le serveur hébergeant le chatbot atteint ses limites de ressources (CPU 100%, RAM saturée).

### Méthodes de simulation

#### Option A : Charge CPU artificielle
```python
import threading
import time

def cpu_stress():
    """Fonction pour saturer un cœur CPU"""
    end_time = time.time() + 30  # 30 secondes de stress
    while time.time() < end_time:
        pass  # Boucle vide = 100% CPU

# Lancer plusieurs threads pour saturer le CPU
threads = []
for i in range(4):  # 4 threads = saturation multi-core
    t = threading.Thread(target=cpu_stress)
    threads.append(t)
    t.start()

# Tester le chatbot pendant la surcharge
try:
    response = test_chatbot_query("Test sous charge")
finally:
    # Attendre la fin du stress test
    for t in threads:
        t.join()
```

#### Option B : Saturation mémoire
```python
import psutil

def memory_stress():
    """Allouer de la mémoire progressivement"""
    memory_hog = []
    total_ram = psutil.virtual_memory().total
    target_usage = int(total_ram * 0.8)  # 80% de la RAM
    
    chunk_size = 1024 * 1024 * 100  # 100 MB par chunk
    
    try:
        while psutil.virtual_memory().used < target_usage:
            chunk = bytearray(chunk_size)
            memory_hog.append(chunk)
            time.sleep(0.1)
    except MemoryError:
        print("Limite mémoire atteinte")
    
    # Maintenir la charge pendant le test
    time.sleep(30)
    
    # Libérer la mémoire
    del memory_hog
```

### Éléments à observer sous charge

| Aspect | Comportement normal | Sous charge | Dégradation |
|--------|-------------------|-------------|-------------|
| **Temps de réponse** | < 1s | ? | ? |
| **Taux de succès** | 100% | ? | ? |
| **Messages d'erreur** | Aucun | ? | ? |
| **Stabilité système** | Stable | ? | ? |
| **Récupération** | N/A | Automatique ? | Temps ? |

### Questions de résilience

1. **Dégradation gracieuse :** Le système ralentit-il progressivement ou s'arrête-t-il brutalement ?
2. **Priorisation :** Y a-t-il une priorisation des requêtes (admin > utilisateur) ?
3. **Protection :** Le système se protège-t-il contre l'épuisement total ?
4. **Monitoring :** Les seuils d'alerte sont-ils appropriés ?

## 🗄️ Scénario 5 : Base de données inaccessible

### Contexte de simulation
La base de données stockant les conversations et configurations devient inaccessible.

### Méthodes de simulation

#### Option A : Arrêt service base de données
```bash
# Si vous utilisez SQLite local
mv chatbot.db chatbot.db.backup

# Si vous utilisez PostgreSQL/MySQL
sudo systemctl stop postgresql
# ou
sudo systemctl stop mysql
```

#### Option B : Permissions révoquées
```python
# Modifier temporairement les paramètres de connexion
import sqlite3

# Créer une base temporaire corrompue
with open('temp_corrupted.db', 'w') as f:
    f.write("CORRUPTED DATA")

# Pointer vers cette base corrompue
DATABASE_PATH = 'temp_corrupted.db'
```

#### Option C : Saturation des connexions
```python
import sqlite3
import threading

def exhaust_connections():
    """Saturer les connexions disponibles"""
    connections = []
    try:
        for i in range(1000):  # Ouvrir de nombreuses connexions
            conn = sqlite3.connect('chatbot.db')
            connections.append(conn)
    except Exception as e:
        print(f"Saturation atteinte: {e}")
```

### Grille d'évaluation de la continuité

| Fonction | Sans BDD | Avec BDD | Mode dégradé |
|----------|----------|----------|--------------|
| **Conversations nouvelles** | ? | ✅ | ? |
| **Historique conversations** | ? | ✅ | ? |
| **Configuration utilisateur** | ? | ✅ | ? |
| **Logging des incidents** | ? | ✅ | ? |
| **Authentification** | ? | ✅ | ? |

### Mode de fonctionnement attendu

**Idéal - Mode dégradé fonctionnel :**
- Conversations temporaires en mémoire
- Pas d'historique mais service fonctionnel
- Notification transparente à l'utilisateur
- Sauvegarde différée quand BDD disponible

**Acceptable - Arrêt propre :**
- Détection rapide de l'indisponibilité
- Message d'erreur clair à l'utilisateur
- Tentatives de reconnexion automatiques
- Restauration complète quand BDD revient

**Inacceptable - Crash système :**
- Erreurs non gérées
- Exposition d'informations techniques
- Perte de données en cours
- Récupération manuelle nécessaire

## 📊 Scénario 6 : Quota API épuisé

### Contexte de simulation
Le quota journalier/mensuel de l'API Mistral AI est épuisé, générant des erreurs 429.

### Méthodes de simulation

#### Option A : Simulation 429 avec serveur de test
```python
from flask import Flask, jsonify

# Serveur de test simulant l'API Mistral
app = Flask(__name__)

@app.route('/v1/chat/completions', methods=['POST'])
def simulate_quota_exceeded():
    return jsonify({
        "error": {
            "message": "Rate limit exceeded. Try again later.",
            "type": "rate_limit_error",
            "code": "rate_limit_exceeded"
        }
    }), 429

# Pointer temporairement vers ce serveur de test
```

#### Option B : Compteur artificiel
```python
# Ajouter un compteur global de requêtes
request_count = 0
daily_limit = 100  # Limite artificielle basse

def make_api_call():
    global request_count
    request_count += 1
    
    if request_count > daily_limit:
        raise Exception("429: Rate limit exceeded")
    
    # Appel normal à l'API
```

### Stratégies de gestion à évaluer

| Stratégie | Description | Implémentée ? | Efficacité |
|-----------|-------------|---------------|------------|
| **Détection préventive** | Surveillance 80% du quota | ⬜ Oui ⬜ Non | /5 |
| **Rationing intelligent** | Priorisation des requêtes | ⬜ Oui ⬜ Non | /5 |
| **Communication transparente** | Information utilisateur claire | ⬜ Oui ⬜ Non | /5 |
| **Queue différée** | Report des requêtes non urgentes | ⬜ Oui ⬜ Non | /5 |
| **Fallback local** | Réponses basiques sans API | ⬜ Oui ⬜ Non | /5 |

### Questions d'optimisation économique

1. **Prévision :** Le système anticipe-t-il l'épuisement du quota ?
2. **Priorisation :** Quelles requêtes sont traitées en priorité ?
3. **Communication :** L'utilisateur comprend-il la situation ?
4. **Récupération :** Quand le service reprend-il automatiquement ?

### Simulation d'épuisement progressif

```python
# Simulation réaliste d'épuisement de quota
class QuotaManager:
    def __init__(self, daily_limit=1000):
        self.daily_limit = daily_limit
        self.used = 0
        self.last_reset = datetime.now().date()
    
    def check_quota(self):
        today = datetime.now().date()
        if today > self.last_reset:
            self.used = 0
            self.last_reset = today
        
        if self.used >= self.daily_limit:
            raise QuotaExceededError("Daily quota exhausted")
        
        if self.used > 0.8 * self.daily_limit:
            # Alerte 80%
            log_warning("Quota at 80%")
        
        return True
    
    def consume(self, tokens=1):
        self.used += tokens
```

## 📋 Grille d'évaluation consolidée

### Score global de résilience

| Scénario | Détection | Gestion | Récupération | UX | Sécurité | Total |
|----------|-----------|---------|--------------|----|---------:|-------|
| **API maintenance** | ___/20 | ___/20 | ___/20 | ___/20 | ___/20 | ___/100 |
| **Réseau coupé** | ___/20 | ___/20 | ___/20 | ___/20 | ___/20 | ___/100 |
| **Clé compromise** | ___/20 | ___/20 | ___/20 | ___/20 | ___/20 | ___/100 |
| **Surcharge serveur** | ___/20 | ___/20 | ___/20 | ___/20 | ___/20 | ___/100 |
| **Base inaccessible** | ___/20 | ___/20 | ___/20 | ___/20 | ___/20 | ___/100 |
| **Quota épuisé** | ___/20 | ___/20 | ___/20 | ___/20 | ___/20 | ___/100 |

**Score global : ___/600 (___% de résilience)**

### Interprétation des scores

#### Niveaux de résilience
- **90-100%** : 🟢 Excellent - Prêt pour production critique
- **80-89%** : 🟡 Bon - Acceptable pour production standard  
- **70-79%** : 🟠 Moyen - Améliorations nécessaires
- **<70%** : 🔴 Insuffisant - Refonte de la gestion d'erreurs requise

#### Critères de notation détaillés

**Détection (20 points) :**
- 18-20 : Détection automatique < 5 secondes
- 15-17 : Détection automatique < 30 secondes
- 10-14 : Détection manuelle ou tardive
- 0-9 : Pas de détection ou très tardive

**Gestion (20 points) :**
- 18-20 : Mode dégradé fonctionnel maintenu
- 15-17 : Arrêt propre avec message approprié
- 10-14 : Gestion partielle avec quelques dysfonctionnements
- 0-9 : Crash ou comportement imprévisible

**Récupération (20 points) :**
- 18-20 : Récupération automatique complète
- 15-17 : Récupération automatique partielle
- 10-14 : Récupération manuelle simple
- 0-9 : Récupération complexe ou impossible

**UX (20 points) :**
- 18-20 : Messages clairs, utilisateur informé et guidé
- 15-17 : Messages compréhensibles, impact minimal
- 10-14 : Messages acceptables, impact modéré
- 0-9 : Messages confus, impact majeur sur l'expérience

**Sécurité (20 points) :**
- 18-20 : Aucune information sensible exposée
- 15-17 : Exposition mineure d'informations techniques
- 10-14 : Exposition modérée mais non critique
- 0-9 : Exposition significative d'informations sensibles

## 🔧 Recommandations d'amélioration

### Améliorations par niveau de priorité

#### Priorité 1 - Corrections critiques (Score < 50)
- **Sécurisation des messages d'erreur** : Éliminer toute exposition d'informations sensibles
- **Gestion des exceptions** : Implémenter des try/catch appropriés
- **Logging sécurisé** : Séparer logs techniques et logs utilisateur

#### Priorité 2 - Optimisations importantes (Score 50-70)
- **Mode dégradé** : Développer des fallbacks fonctionnels
- **Monitoring proactif** : Alertes avant panne complète
- **Documentation** : Procédures de réponse aux incidents

#### Priorité 3 - Améliorations souhaitables (Score > 70)
- **Récupération intelligente** : Retry avec backoff exponentiel
- **Prédiction de pannes** : Machine learning pour anticiper
- **Automatisation** : Scripts de récupération automatique

### Template d'amélioration

Pour chaque scénario avec score < 80 :

**Problème identifié :**
- Description précise du dysfonctionnement
- Score actuel et score cible

**Solution proposée :**
- Modification technique nécessaire
- Coût estimé (temps de développement)
- Impact attendu sur le score

**Plan d'implémentation :**
- Étapes de mise en œuvre
- Tests de validation
- Métriques de succès

## 🎯 Intégration dans l'audit global

### Utilisation des résultats

Ces tests de résilience s'intègrent dans votre audit de sécurité global :

1. **Phase 2 - Exercice 1** : Scores de résilience aux pannes
2. **Rapport d'audit** : Section "Robustesse opérationnelle" 
3. **Recommandations** : Priorisation des améliorations
4. **Budget** : Estimation des coûts de mise à niveau

### Métriques à reporter

| Métrique | Valeur | Interprétation |
|----------|--------|----------------|
| **Score global résilience** | ___% | Niveau de robustesse général |
| **Scénario le plus critique** | _________ | Priorité d'amélioration #1 |
| **Exposition sécuritaire** | ___/6 scénarios | Nombre de fuites d'informations |
| **Récupération automatique** | ___/6 scénarios | Capacité de self-healing |

### Documentation des tests

Pour chaque test effectué, documentez :

```
Scénario : _________________
Date/Heure : _______________
Durée du test : ____________
Méthode de simulation : ____
Résultats observés : _______
Score attribué : ___/100
Actions correctives : ______
Responsable : ______________
```

Cette documentation sera précieuse pour :
- Traçabilité des tests de sécurité
- Amélioration continue du système
- Audit de conformité externe
- Formation des équipes

## 📚 Ressources complémentaires

### Outils de simulation avancés

- **Chaos Monkey** : Outil Netflix pour tests de résilience
- **Gremlin** : Plateforme de chaos engineering
- **Pumba** : Tests de résilience pour containers Docker

### Méthodologies de référence

- **FMEA** (Failure Mode and Effects Analysis) : Analyse systématique des modes de défaillance
- **Chaos Engineering** : Discipline pour tester la résilience en production
- **Game Days** : Simulations d'incident en équipe

### Standards et certifications

- **ISO 22301** : Continuité d'activité et gestion de crise
- **NIST Cybersecurity Framework** : Fonction "Recover"
- **ITIL v4** : Gestion des incidents et problèmes

Ces simulations de pannes constituent un élément essentiel de votre stratégie de cybersécurité IA, permettant de valider que votre système reste sécurisé même en cas de dysfonctionnement.