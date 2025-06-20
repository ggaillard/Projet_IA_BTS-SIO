# 🚨 CHATBOT DE DÉMONSTRATION POUR AUDIT DE SÉCURITÉ
# ⚠️  ATTENTION: Ce code contient des vulnérabilités INTENTIONNELLES
# 🎯 Objectif: Permettre aux étudiants de pratiquer l'audit de sécurité
# 🔒 Ne JAMAIS utiliser en production

from flask import Flask, render_template, request, jsonify, session
import requests
import json
import logging
import os
from datetime import datetime
import sqlite3

app = Flask(__name__)

# 🚨 VULNÉRABILITÉ 1: Clé API stockée en dur dans le code
MISTRAL_API_KEY = "sk-abc123def456ghi789jkl012mno345pqr678stu901vwx234yzab567cde890fgh"

# 🚨 VULNÉRABILITÉ 2: Secret key faible pour les sessions
app.secret_key = "secret123"

# 🚨 VULNÉRABILITÉ 3: Configuration de logging non sécurisée
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('chatbot.log'),
        logging.StreamHandler()
    ]
)

# 🚨 VULNÉRABILITÉ 4: Base de données sans protection
def init_db():
    """Initialise la base de données avec des données de test"""
    conn = sqlite3.connect('chatbot.db')
    cursor = conn.cursor()
    
    # Créer table des conversations
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS conversations (
            id INTEGER PRIMARY KEY,
            user_email TEXT,
            user_ip TEXT,
            message TEXT,
            response TEXT,
            timestamp TEXT,
            user_agent TEXT
        )
    ''')
    
    # 🚨 VULNÉRABILITÉ 5: Données personnelles en base sans chiffrement
    sample_data = [
        ('marie.dupont@universite.fr', '192.168.1.45', 'Jai des difficultés en math', 'Je comprends vos difficultés...', '2025-01-15 14:30:22', 'Mozilla/5.0...'),
        ('jean.martin@universite.fr', '192.168.1.46', 'Mes parents divorcent', 'Cest une situation difficile...', '2025-01-15 14:31:45', 'Chrome/120.0...'),
        ('admin@universite.fr', '192.168.1.1', 'Test système', 'Réponse de test', '2025-01-15 14:32:10', 'Admin-Bot/1.0')
    ]
    
    cursor.executemany('''
        INSERT OR IGNORE INTO conversations 
        (user_email, user_ip, message, response, timestamp, user_agent)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', sample_data)
    
    conn.commit()
    conn.close()

# Initialiser la DB au démarrage
init_db()

def call_mistral_api(message):
    """
    Appelle l'API Mistral AI - CONTIENT DES VULNÉRABILITÉS INTENTIONNELLES
    """
    # 🚨 VULNÉRABILITÉ 6: Pas de validation des entrées
    # Le message utilisateur est transmis directement sans filtrage
    
    url = "https://api.mistral.ai/v1/chat/completions"
    
    headers = {
        "Authorization": f"Bearer {MISTRAL_API_KEY}",
        "Content-Type": "application/json"
    }
    
    # 🚨 VULNÉRABILITÉ 7: Prompt système non sécurisé
    prompt_system = "Tu es un assistant pédagogique pour le Deep Learning."
    
    data = {
        "model": "mistral-tiny",
        "messages": [
            {"role": "system", "content": prompt_system},
            {"role": "user", "content": message}
        ],
        "max_tokens": 500,
        "temperature": 0.7
    }
    
    try:
        # 🚨 VULNÉRABILITÉ 8: Pas de timeout configuré
        response = requests.post(url, headers=headers, json=data)
        
        # 🚨 VULNÉRABILITÉ 9: Gestion d'erreur exposant des informations
        if response.status_code != 200:
            error_details = {
                "status_code": response.status_code,
                "api_key_used": MISTRAL_API_KEY,
                "url": url,
                "headers": headers,
                "error_message": response.text,
                "internal_config": {
                    "server": "chatbot-prod-01",
                    "database": "chatbot_users.db",
                    "api_endpoint": url
                }
            }
            # 🚨 VULNÉRABILITÉ 10: Logging d'informations sensibles
            logging.error(f"API Error: {error_details}")
            raise Exception(f"Erreur API Mistral: {error_details}")
        
        result = response.json()
        api_response = result['choices'][0]['message']['content']
        
        # 🚨 VULNÉRABILITÉ 11: Pas de validation de la réponse de l'API
        return api_response
        
    except requests.exceptions.RequestException as e:
        # 🚨 VULNÉRABILITÉ 12: Stack trace complet exposé
        error_info = {
            "error": str(e),
            "api_key": MISTRAL_API_KEY,
            "server_path": "/home/ubuntu/chatbot/app.py",
            "config_file": "/etc/chatbot/config.json",
            "database_path": "/var/data/chatbot_users.db"
        }
        logging.error(f"Request error: {error_info}")
        raise Exception(f"Erreur de connexion: {error_info}")

def save_conversation(user_email, user_ip, message, response, user_agent):
    """Sauvegarde la conversation en base"""
    conn = sqlite3.connect('chatbot.db')
    cursor = conn.cursor()
    
    # 🚨 VULNÉRABILITÉ 13: Injection SQL possible
    query = f"INSERT INTO conversations (user_email, user_ip, message, response, timestamp, user_agent) VALUES ('{user_email}', '{user_ip}', '{message}', '{response}', '{datetime.now()}', '{user_agent}')"
    
    try:
        cursor.execute(query)
        conn.commit()
        
        # 🚨 VULNÉRABILITÉ 14: Logging de données personnelles
        logging.info(f"Conversation saved for user {user_email} from IP {user_ip}: {message}")
        
    except Exception as e:
        logging.error(f"Database error for user {user_email}: {e}")
    finally:
        conn.close()

@app.route('/')
def index():
    """Page principale du chatbot"""
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    """Endpoint principal pour les conversations"""
    try:
        data = request.get_json()
        
        # 🚨 VULNÉRABILITÉ 15: Pas de validation des données POST
        user_message = data['message']  # Pas de vérification si 'message' existe
        user_email = data.get('email', 'anonymous@unknown.com')
        
        # 🚨 VULNÉRABILITÉ 16: Collecte excessive de données
        user_ip = request.remote_addr
        user_agent = request.headers.get('User-Agent')
        referer = request.headers.get('Referer')
        cookies = request.headers.get('Cookie')
        
        # Log de toutes les données collectées
        logging.info(f"Chat request from {user_email} ({user_ip}): {user_message}")
        logging.debug(f"User-Agent: {user_agent}, Referer: {referer}, Cookies: {cookies}")
        
        # Appel à l'API Mistral
        ai_response = call_mistral_api(user_message)
        
        # Sauvegarde en base
        save_conversation(user_email, user_ip, user_message, ai_response, user_agent)
        
        return jsonify({
            'response': ai_response,
            'timestamp': datetime.now().isoformat(),
            'debug_info': {  # 🚨 VULNÉRABILITÉ 17: Informations de debug exposées
                'user_ip': user_ip,
                'server': 'chatbot-prod-01',
                'api_key_last_4': MISTRAL_API_KEY[-4:],
                'database': 'chatbot.db'
            }
        })
        
    except KeyError as e:
        # 🚨 VULNÉRABILITÉ 18: Messages d'erreur bavards
        error_details = {
            "error": f"Missing required field: {e}",
            "received_data": request.get_json(),
            "server_config": {
                "api_key": MISTRAL_API_KEY,
                "database": "chatbot.db",
                "log_file": "chatbot.log"
            },
            "stack_trace": str(e)
        }
        logging.error(f"KeyError in chat endpoint: {error_details}")
        return jsonify({"error": error_details}), 400
        
    except Exception as e:
        # 🚨 VULNÉRABILITÉ 19: Stack trace complet dans la réponse
        error_response = {
            "error": str(e),
            "type": type(e).__name__,
            "server_info": {
                "api_key": MISTRAL_API_KEY,
                "config": "/etc/chatbot/secrets.json",
                "logs": "/var/log/chatbot/",
                "database": "/var/data/chatbot_users.db"
            }
        }
        return jsonify(error_response), 500

@app.route('/admin')
def admin():
    """Interface d'administration basique"""
    # 🚨 VULNÉRABILITÉ 20: Pas d'authentification pour l'admin
    conn = sqlite3.connect('chatbot.db')
    cursor = conn.cursor()
    
    # 🚨 VULNÉRABILITÉ 21: Exposition de toutes les données utilisateurs
    cursor.execute("SELECT * FROM conversations ORDER BY timestamp DESC LIMIT 50")
    conversations = cursor.fetchall()
    conn.close()
    
    # 🚨 VULNÉRABILITÉ 22: Données sensibles retournées sans masquage
    admin_data = {
        "conversations": conversations,
        "config": {
            "api_key": MISTRAL_API_KEY,
            "database_path": "chatbot.db",
            "log_level": "DEBUG"
        },
        "system_info": {
            "server": "chatbot-prod-01.internal.edu",
            "database": "chatbot_users.db",
            "api_endpoint": "https://api.mistral.ai/v1/chat/completions"
        }
    }
    
    return jsonify(admin_data)

@app.route('/health')
def health():
    """Endpoint de santé du service"""
    # 🚨 VULNÉRABILITÉ 23: Informations système exposées
    health_info = {
        "status": "OK",
        "timestamp": datetime.now().isoformat(),
        "api_key_status": "Active" if MISTRAL_API_KEY else "Missing",
        "api_key": MISTRAL_API_KEY,  # Clé complète exposée !
        "database": "chatbot.db",
        "config_file": "/etc/chatbot/config.json",
        "log_file": "chatbot.log",
        "server": "chatbot-prod-01.internal.edu:5000"
    }
    return jsonify(health_info)

@app.route('/logs')
def view_logs():
    """Affichage des logs - TRÈS DANGEREUX"""
    # 🚨 VULNÉRABILITÉ 24: Logs accessibles publiquement
    try:
        with open('chatbot.log', 'r') as f:
            logs = f.read()
        return f"<pre>{logs}</pre>"
    except FileNotFoundError:
        return "Logs not found"

# 🚨 VULNÉRABILITÉ 25: Gestion d'erreur globale exposant des informations
@app.errorhandler(500)
def internal_error(error):
    error_details = {
        "error": "Internal Server Error",
        "debug_info": {
            "api_key": MISTRAL_API_KEY,
            "database": "chatbot.db",
            "config": "/etc/chatbot/config.json",
            "exception": str(error)
        },
        "server": "chatbot-prod-01.internal.edu",
        "timestamp": datetime.now().isoformat()
    }
    return jsonify(error_details), 500

if __name__ == '__main__':
    # 🚨 VULNÉRABILITÉ 26: Configuration de développement en production
    app.run(
        debug=True,  # Debug activé = exposition d'informations
        host='0.0.0.0',  # Accessible depuis toutes les IP
        port=5000,
        threaded=True
    )