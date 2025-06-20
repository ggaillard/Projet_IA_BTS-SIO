# 🔒 GUIDE ENSEIGNANT - CHATBOT DE DÉMONSTRATION SÉCURITAIRE

> 📝 **Document confidentiel** - Réservé aux enseignants  
> 🎯 **Objectif** : Solutions et grille de correction pour l'audit de sécurité

## 🚨 INVENTAIRE COMPLET DES VULNÉRABILITÉS

### 📊 Récapitulatif par criticité

| Criticité | Nombre | Pourcentage |
|-----------|--------|-------------|
| 🔴 **Critique** | 8 | 31% |
| 🟠 **Élevée** | 10 | 38% |
| 🟡 **Moyenne** | 6 | 23% |
| 🟢 **Faible** | 2 | 8% |
| **Total** | **26** | **100%** |

---

## 🔴 VULNÉRABILITÉS CRITIQUES (Score CVSS 9.0-10.0)

### V01 - Clé API Mistral stockée en dur ⭐
**Fichier** : `app.py` ligne 10  
**Code** : `MISTRAL_API_KEY = "sk-abc123..."`  
**Impact** : Exposition complète de la clé API, accès frauduleux, facturation non autorisée  
**CVSS** : 9.8 (Critique)  
**Correction** : Variables d'environnement avec `os.getenv("MISTRAL_API_KEY")`

### V02 - Injection SQL directe ⭐
**Fichier** : `app.py` ligne 84  
**Code** : `query = f"INSERT INTO conversations... VALUES ('{user_email}'..."`  
**Impact** : Accès complet à la base de données, extraction/modification de données  
**CVSS** : 9.9 (Critique)  
**Correction** : Requêtes préparées avec paramètres liés

### V03 - Interface admin sans authentification ⭐
**Fichier** : `app.py` ligne 135  
**Route** : `/admin`  
**Impact** : Accès à toutes les conversations utilisateurs, informations système  
**CVSS** : 9.5 (Critique)  
**Correction** : Authentification multi-facteurs obligatoire

### V04 - Exposition de logs système ⭐
**Fichier** : `app.py` ligne 199  
**Route** : `/logs`  
**Impact** : Accès à tous les logs incluant données personnelles et secrets  
**CVSS** : 9.2 (Critique)  
**Correction** : Authentification + logs sanitisés

### V05 - Messages d'erreur exposant l'architecture ⭐
**Fichier** : `app.py` lignes 167-179  
**Impact** : Révélation de chemins système, clés API, configuration interne  
**CVSS** : 9.0 (Critique)  
**Correction** : Messages d'erreur génériques + logging sécurisé

### V06 - Stack traces complètes en production ⭐
**Fichier** : `app.py` lignes 180-195  
**Impact** : Exposition de l'architecture interne, facilite d'autres attaques  
**CVSS** : 9.1 (Critique)  
**Correction** : `debug=False` + gestionnaire d'erreurs personnalisé

### V07 - Données personnelles non chiffrées ⭐
**Fichier** : `app.py` fonction `init_db()`  
**Impact** : Violation RGPD, exposition de conversations privées  
**CVSS** : 9.3 (Critique)  
**Correction** : Chiffrement au repos + anonymisation

### V08 - Configuration debug en production ⭐
**Fichier** : `app.py` ligne 210  
**Code** : `app.run(debug=True, host='0.0.0.0')`  
**Impact** : Exposition du debugger, exécution de code arbitraire  
**CVSS** : 9.8 (Critique)  
**Correction** : `debug=False` + configuration par environnement

---

## 🟠 VULNÉRABILITÉS ÉLEVÉES (Score CVSS 7.0-8.9)

### V09 - Absence de validation des entrées
**Impact** : Injection de prompts, manipulation du comportement IA  
**CVSS** : 8.5 (Élevée)  
**Correction** : Validation stricte + filtrage des entrées

### V10 - Logging d'informations sensibles
**Impact** : Fuite de données personnelles dans les logs  
**CVSS** : 8.2 (Élevée)  
**Correction** : Masquage automatique des données sensibles

### V11 - Secret key Flask faible
**Impact** : Compromission des sessions, falsification de cookies  
**CVSS** : 8.0 (Élevée)  
**Correction** : Génération aléatoire sécurisée + rotation

### V12 - Absence de rate limiting
**Impact** : Attaques DDoS, épuisement des quotas API  
**CVSS** : 7.8 (Élevée)  
**Correction** : Limitation par IP + utilisateur

### V13 - Collecte excessive de données
**Impact** : Violation du principe de minimisation RGPD  
**CVSS** : 7.5 (Élevée)  
**Correction** : Collecte limitée aux données nécessaires

### V14 - Communications HTTP non chiffrées
**Impact** : Interception des données en transit  
**CVSS** : 8.1 (Élevée)  
**Correction** : HTTPS obligatoire avec certificats valides

### V15 - Absence de timeout API
**Impact** : Blocage du service, attaques de déni de service  
**CVSS** : 7.2 (Élevée)  
**Correction** : Timeouts configurés + retry avec backoff

### V16 - Informations de debug côté client
**Impact** : Exposition d'informations techniques dans le navigateur  
**CVSS** : 7.6 (Élevée)  
**Correction** : Suppression du mode debug côté client

### V17 - Raccourcis clavier admin cachés
**Impact** : Accès non autorisé via combinaisons de touches  
**CVSS** : 7.8 (Élevée)  
**Correction** : Suppression des raccourcis + authentification

### V18 - Variables de configuration exposées
**Impact** : Révélation de configuration interne via JavaScript  
**CVSS** : 8.3 (Élevée)  
**Correction** : Configuration côté serveur uniquement

---

## 🟡 VULNÉRABILITÉS MOYENNES (Score CVSS 4.0-6.9)

### V19 - Commentaires HTML avec informations sensibles
**Impact** : Fuite d'informations via le code source  
**CVSS** : 6.5 (Moyenne)  
**Correction** : Suppression des commentaires de production

### V20 - ID de session prévisibles
**Impact** : Hijacking de session possible  
**CVSS** : 6.2 (Moyenne)  
**Correction** : Génération cryptographiquement sécurisée

### V21 - Auto-remplissage d'email en debug
**Impact** : Facilite les tests non autorisés  
**CVSS** : 5.8 (Moyenne)  
**Correction** : Désactivation en production

### V22 - Informations système dans footer
**Impact** : Reconnaissance technique facilitée  
**CVSS** : 5.5 (Moyenne)  
**Correction** : Masquage des informations internes

### V23 - Endpoint health verbeux
**Impact** : Exposition d'informations de configuration  
**CVSS** : 6.8 (Moyenne)  
**Correction** : Health check minimaliste

### V24 - Gestion d'erreur globale exposante
**Impact** : Fuite d'informations lors d'erreurs inattendues  
**CVSS** : 6.0 (Moyenne)  
**Correction** : Gestionnaire générique sécurisé

---

## 🟢 VULNÉRABILITÉS FAIBLES (Score CVSS 1.0-3.9)

### V25 - Informations de version exposées
**Impact** : Reconnaissance technique mineure  
**CVSS** : 3.2 (Faible)  
**Correction** : Masquage des versions

### V26 - Liens directs vers sections admin
**Impact** : Découverte facilitée des endpoints sensibles  
**CVSS** : 2.8 (Faible)  
**Correction** : Suppression des liens directs

---

## 📊 GRILLE DE CORRECTION DÉTAILLÉE

### Barème de notation par vulnérabilité

| Vulnérabilité | Points identification | Points impact | Points correction | Total |
|---------------|---------------------|------------