# ✅ Checklist RGPD 20 points pour chatbots IA pédagogiques

Cette checklist vous permet d'auditer la conformité RGPD de votre chatbot pédagogique selon une approche méthodique et professionnelle.

## 📋 Instructions d'audit

Pour chaque point de contrôle :
- ✅ **Conforme** : Le système respecte entièrement cette exigence
- ❌ **Non-conforme** : Le système ne respecte pas cette exigence  
- ⚠️ **Partiellement conforme** : Le système respecte partiellement cette exigence
- 🔍 **À vérifier** : Informations insuffisantes pour conclure
- ➖ **Non applicable** : Cette exigence ne s'applique pas au contexte

---

## 📜 Section 1 : Base légale du traitement (3 points)

### ✅ Point 1 : Base légale identifiée et documentée

**Exigence RGPD** : Article 6 - Licéité du traitement

**À vérifier :**
- [ ] Une base légale spécifique est identifiée parmi les 6 bases de l'article 6
- [ ] La base légale est documentée et accessible
- [ ] La base légale est adaptée au contexte pédagogique

**Bases légales possibles pour un chatbot pédagogique :**
- **6.1.a)** Consentement de la personne concernée
- **6.1.b)** Exécution d'un contrat (contrat de scolarité)
- **6.1.e)** Mission d'intérêt public (mission éducative de l'établissement)

**Questions d'audit :**
1. Quelle base légale a été choisie pour le traitement ?
2. Cette base légale est-elle documentée dans un registre ?
3. Est-elle cohérente avec la finalité pédagogique ?

**État de conformité :** ⬜ Conforme ⬜ Non-conforme ⬜ Partiellement ⬜ À vérifier ⬜ N/A

---

### ✅ Point 2 : Information claire des utilisateurs sur la finalité

**Exigence RGPD** : Articles 13 et 14 - Information des personnes

**À vérifier :**
- [ ] Politique de confidentialité accessible et compréhensible
- [ ] Finalités du traitement clairement expliquées
- [ ] Information présente dès la première interaction

**Exemple d'information conforme :**
```
"Ce chatbot pédagogique collecte vos questions et analyse vos interactions 
pour personnaliser votre apprentissage du Deep Learning. Vos données sont 
traitées sur la base de notre mission éducative (article 6.1.e du RGPD)."
```

**Questions d'audit :**
1. L'utilisateur est-il informé avant la première utilisation ?
2. Les finalités sont-elles spécifiques et explicites ?
3. L'information est-elle rédigée en langage clair ?

**État de conformité :** ⬜ Conforme ⬜ Non-conforme ⬜ Partiellement ⬜ À vérifier ⬜ N/A

---

### ✅ Point 3 : Consentement explicite si nécessaire

**Exigence RGPD** : Article 7 - Conditions applicables au consentement

**À vérifier :**
- [ ] Consentement demandé si base légale 6.1.a
- [ ] Mécanisme de retrait du consentement disponible
- [ ] Consentement libre, spécifique, éclairé et univoque

**Cas où le consentement est requis :**
- Finalités non couvertes par la mission éducative
- Profilage des étudiants à des fins non pédagogiques
- Partage de données avec des tiers commerciaux

**Questions d'audit :**
1. Le consentement est-il nécessaire pour ce traitement ?
2. Si oui, est-il correctement recueilli ?
3. L'utilisateur peut-il retirer son consentement facilement ?

**État de conformité :** ⬜ Conforme ⬜ Non-conforme ⬜ Partiellement ⬜ À vérifier ⬜ N/A

---

## 👤 Section 2 : Droits des personnes concernées (4 points)

### ✅ Point 4 : Droit d'accès aux données implémenté

**Exigence RGPD** : Article 15 - Droit d'accès

**À vérifier :**
- [ ] Procédure pour exercer le droit d'accès documentée
- [ ] Délai de réponse de 1 mois respecté
- [ ] Fourniture d'une copie des données en format compréhensible

**Implémentation technique suggérée :**
```python
@app.route('/api/data-access', methods=['POST'])
def handle_data_access_request():
    user_email = request.json['email']
    # Vérification d'identité
    # Extraction des données personnelles
    # Génération du rapport au format lisible
    return jsonify(user_data_report)
```

**Questions d'audit :**
1. Existe-t-il une procédure pour demander l'accès aux données ?
2. Les données sont-elles fournies dans un format compréhensible ?
3. Le délai de 1 mois est-il respecté ?

**État de conformité :** ⬜ Conforme ⬜ Non-conforme ⬜ Partiellement ⬜ À vérifier ⬜ N/A

---

### ✅ Point 5 : Droit de rectification possible

**Exigence RGPD** : Article 16 - Droit de rectification

**À vérifier :**
- [ ] Mécanisme de correction des données personnelles
- [ ] Procédure de notification aux tiers si rectification
- [ ] Interface utilisateur pour modifier ses informations

**Données rectifiables dans un chatbot :**
- Informations de profil étudiant
- Préférences d'apprentissage
- Historique des interactions si inexact

**Questions d'audit :**
1. L'utilisateur peut-il corriger ses données personnelles ?
2. La rectification est-elle propagée dans tous les systèmes ?
3. Les tiers concernés sont-ils notifiés si nécessaire ?

**État de conformité :** ⬜ Conforme ⬜ Non-conforme ⬜ Partiellement ⬜ À vérifier ⬜ N/A

---

### ✅ Point 6 : Droit à l'effacement (droit à l'oubli)

**Exigence RGPD** : Article 17 - Droit à l'effacement

**À vérifier :**
- [ ] Procédure d'effacement des données personnelles
- [ ] Suppression dans tous les systèmes (bases, sauvegardes, logs)
- [ ] Respect des exceptions légales (archives, recherche)

**Défis techniques pour un chatbot :**
```python
def delete_user_data(user_id):
    # Suppression des conversations
    # Anonymisation des logs
    # Suppression des modèles personnalisés
    # Notification aux systèmes tiers
    # Conservation d'archives anonymisées si légalement requis
```

**Questions d'audit :**
1. L'utilisateur peut-il demander l'effacement de ses données ?
2. L'effacement est-il complet (y compris sauvegardes) ?
3. Les exceptions légales sont-elles respectées ?

**État de conformité :** ⬜ Conforme ⬜ Non-conforme ⬜ Partiellement ⬜ À vérifier ⬜ N/A

---

### ✅ Point 7 : Droit à la portabilité des données

**Exigence RGPD** : Article 20 - Droit à la portabilité

**À vérifier :**
- [ ] Export des données dans un format structuré et lisible
- [ ] Transmission directe à un autre responsable si possible
- [ ] Limitation aux données fournies par la personne

**Format d'export suggéré :**
```json
{
    "user_profile": {
        "name": "Jean Dupont",
        "email": "jean.dupont@universite.fr"
    },
    "learning_data": {
        "conversations": [...],
        "progress": {...},
        "preferences": {...}
    },
    "export_date": "2025-01-15T10:30:00Z",
    "format_version": "1.0"
}
```

**Questions d'audit :**
1. Les données sont-elles exportables dans un format standard ?
2. L'export inclut-il toutes les données personnelles ?
3. La transmission directe à un tiers est-elle possible ?

**État de conformité :** ⬜ Conforme ⬜ Non-conforme ⬜ Partiellement ⬜ À vérifier ⬜ N/A

---

## 🔒 Section 3 : Sécurité technique (4 points)

### ✅ Point 8 : Chiffrement des données en transit

**Exigence RGPD** : Article 32 - Sécurité du traitement

**À vérifier :**
- [ ] HTTPS obligatoire pour toutes les communications
- [ ] Certificats SSL/TLS valides et à jour
- [ ] Algorithmes de chiffrement robustes (TLS 1.2 minimum)

**Configuration sécurisée :**
```nginx
server {
    listen 443 ssl http2;
    ssl_certificate /path/to/certificate.crt;
    ssl_certificate_key /path/to/private.key;
    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_ciphers ECDHE-RSA-AES256-GCM-SHA512:DHE-RSA-AES256-GCM-SHA512;
    # Redirection HTTP vers HTTPS
    return 301 https://$server_name$request_uri;
}
```

**Questions d'audit :**
1. Toutes les communications utilisent-elles HTTPS ?
2. Les certificats sont-ils valides et à jour ?
3. Les algorithmes de chiffrement sont-ils robustes ?

**État de conformité :** ⬜ Conforme ⬜ Non-conforme ⬜ Partiellement ⬜ À vérifier ⬜ N/A

---

### ✅ Point 9 : Chiffrement des données au repos

**Exigence RGPD** : Article 32 - Sécurité du traitement

**À vérifier :**
- [ ] Base de données chiffrée
- [ ] Fichiers de logs chiffrés
- [ ] Sauvegardes chiffrées
- [ ] Gestion sécurisée des clés de chiffrement

**Implémentation base de données :**
```python
# Configuration PostgreSQL avec chiffrement
DATABASE_CONFIG = {
    'encryption': 'AES-256',
    'key_management': 'external_hsm',
    'backup_encryption': True,
    'transparent_data_encryption': True
}
```

**Questions d'audit :**
1. Les données sensibles sont-elles chiffrées au repos ?
2. La gestion des clés est-elle sécurisée ?
3. Les sauvegardes sont-elles également chiffrées ?

**État de conformité :** ⬜ Conforme ⬜ Non-conforme ⬜ Partiellement ⬜ À vérifier ⬜ N/A

---

### ✅ Point 10 : Contrôle d'accès avec authentification forte

**Exigence RGPD** : Article 32 - Sécurité du traitement

**À vérifier :**
- [ ] Authentification multi-facteurs pour les administrateurs
- [ ] Gestion des rôles et permissions granulaires
- [ ] Politique de mots de passe robuste

**Politique d'accès recommandée :**
```yaml
access_policy:
  student_role:
    permissions: [read_own_data, chat_access]
  teacher_role:
    permissions: [read_student_progress, moderate_content]
  admin_role:
    permissions: [full_access]
    requires_2fa: true
    session_timeout: 30_minutes
```

**Questions d'audit :**
1. L'authentification multi-facteurs est-elle activée ?
2. Les permissions suivent-elles le principe du moindre privilège ?
3. Les mots de passe respectent-ils une politique robuste ?

**État de conformité :** ⬜ Conforme ⬜ Non-conforme ⬜ Partiellement ⬜ À vérifier ⬜ N/A

---

### ✅ Point 11 : Journalisation des accès aux données

**Exigence RGPD** : Article 32 - Sécurité du traitement

**À vérifier :**
- [ ] Logs de tous les accès aux données personnelles
- [ ] Traçabilité des modifications et suppressions
- [ ] Protection des logs contre la modification

**Structure de logs conforme :**
```json
{
    "timestamp": "2025-01-15T10:30:00Z",
    "user_id": "admin@universite.fr",
    "action": "data_access",
    "target": "student_conversations",
    "purpose": "technical_support",
    "ip_address": "192.168.1.100",
    "session_id": "sess_abc123",
    "legal_basis": "legitimate_interest"
}
```

**Questions d'audit :**
1. Tous les accès aux données sont-ils journalisés ?
2. Les logs incluent-ils les informations nécessaires ?
3. Les logs sont-ils protégés contre la modification ?

**État de conformité :** ⬜ Conforme ⬜ Non-conforme ⬜ Partiellement ⬜ À vérifier ⬜ N/A

---

## 📝 Section 4 : Gouvernance des données (4 points)

### ✅ Point 12 : Politique de rétention des données définie

**Exigence RGPD** : Article 5.1.e - Limitation de la conservation

**À vérifier :**
- [ ] Durées de conservation définies par type de données
- [ ] Justification des durées par rapport aux finalités
- [ ] Suppression automatique à l'échéance

**Politique de rétention suggérée :**
```
Type de données         | Durée | Justification
Conversations actives   | 1 an  | Suivi pédagogique
Données de progression  | 3 ans | Diplôme et validation
Logs de sécurité       | 6 mois| Détection d'incidents
Données anonymisées    | 5 ans | Recherche pédagogique
```

**Questions d'audit :**
1. Une politique de rétention est-elle définie ?
2. Les durées sont-elles justifiées et proportionnées ?
3. La suppression automatique est-elle implémentée ?

**État de conformité :** ⬜ Conforme ⬜ Non-conforme ⬜ Partiellement ⬜ À vérifier ⬜ N/A

---

### ✅ Point 13 : Procédure de notification de violation

**Exigence RGPD** : Articles 33 et 34 - Notification des violations

**À vérifier :**
- [ ] Procédure de détection des violations documentée
- [ ] Notification CNIL dans les 72h si risque élevé
- [ ] Notification des personnes si risque élevé pour leurs droits

**Plan de réponse aux incidents :**
```
1. Détection (automatique + manuelle)
2. Évaluation du risque (< 4h)
3. Containment et investigation (< 8h)
4. Notification CNIL si requis (< 72h)
5. Notification des personnes si requis (< 72h)
6. Rapport post-incident et amélioration
```

**Questions d'audit :**
1. Une procédure de gestion des violations existe-t-elle ?
2. Les délais de notification sont-ils respectables ?
3. Les équipes sont-elles formées à cette procédure ?

**État de conformité :** ⬜ Conforme ⬜ Non-conforme ⬜ Partiellement ⬜ À vérifier ⬜ N/A

---

### ✅ Point 14 : Analyse d'impact (AIPD) réalisée si nécessaire

**Exigence RGPD** : Article 35 - Analyse d'impact relative à la protection des données

**À vérifier :**
- [ ] AIPD réalisée si traitement à haut risque
- [ ] Consultation du DPO dans le processus
- [ ] Mesures de mitigation identifiées et implémentées

**Critères nécessitant une AIPD :**
- Évaluation systématique des étudiants
- Surveillance systématique des comportements
- Traitement de données sensibles à grande échelle
- Prise de décision automatisée avec effet légal

**Questions d'audit :**
1. Une AIPD a-t-elle été réalisée si nécessaire ?
2. Les risques ont-ils été correctement identifiés ?
3. Des mesures de mitigation ont-elles été prises ?

**État de conformité :** ⬜ Conforme ⬜ Non-conforme ⬜ Partiellement ⬜ À vérifier ⬜ N/A

---

### ✅ Point 15 : DPO consulté ou désigné

**Exigence RGPD** : Articles 37-39 - Délégué à la protection des données

**À vérifier :**
- [ ] DPO désigné si obligation légale (organisme public)
- [ ] DPO consulté sur les questions de protection des données
- [ ] Coordonnées du DPO accessibles aux personnes concernées

**Missions du DPO pour un chatbot :**
- Conseil sur la conformité RGPD
- Surveillance des traitements
- Point de contact avec les autorités
- Formation des équipes
- Audit des mesures de protection

**Questions d'audit :**
1. Un DPO est-il désigné si obligatoire ?
2. Le DPO est-il consulté sur ce traitement ?
3. Ses coordonnées sont-elles accessibles ?

**État de conformité :** ⬜ Conforme ⬜ Non-conforme ⬜ Partiellement ⬜ À vérifier ⬜ N/A

---

## 🌍 Section 5 : Tiers et transferts (3 points)

### ✅ Point 16 : Contrat avec Mistral AI conforme RGPD

**Exigence RGPD** : Article 28 - Sous-traitant

**À vérifier :**
- [ ] Contrat de sous-traitance signé avec Mistral AI
- [ ] Clauses RGPD obligatoires présentes
- [ ] Audit de conformité du sous-traitant

**Clauses contractuelles essentielles :**
```
- Traitement uniquement sur instruction documentée
- Obligation de confidentialité du personnel
- Mesures de sécurité appropriées
- Assistance pour répondre aux demandes des personnes
- Notification des violations de données
- Suppression ou restitution des données en fin de contrat
```

**Questions d'audit :**
1. Un contrat de sous-traitance existe-t-il avec Mistral AI ?
2. Les clauses RGPD obligatoires sont-elles présentes ?
3. La conformité du sous-traitant a-t-elle été auditée ?

**État de conformité :** ⬜ Conforme ⬜ Non-conforme ⬜ Partiellement ⬜ À vérifier ⬜ N/A

---

### ✅ Point 17 : Transferts hors UE sécurisés

**Exigence RGPD** : Chapitre V - Transferts vers des pays tiers

**À vérifier :**
- [ ] Identification des transferts vers des pays tiers
- [ ] Base légale pour les transferts (décision d'adéquation, clauses types)
- [ ] Information des personnes sur les transferts

**Statut des transferts vers les USA (Mistral AI) :**
- Mistral AI (France) : Pas de transfert hors UE si hébergement européen
- Si utilisation de services cloud US : Vérifier Data Privacy Framework
- Clauses contractuelles types si nécessaire

**Questions d'audit :**
1. Les données sont-elles transférées hors de l'UE ?
2. Une base légale de transfert est-elle en place ?
3. Les personnes sont-elles informées de ces transferts ?

**État de conformité :** ⬜ Conforme ⬜ Non-conforme ⬜ Partiellement ⬜ À vérifier ⬜ N/A

---

### ✅ Point 18 : Sous-traitants RGPD-compliant

**Exigence RGPD** : Article 28 - Responsabilité des sous-traitants

**À vérifier :**
- [ ] Inventaire de tous les sous-traitants
- [ ] Vérification de leur conformité RGPD
- [ ] Chaîne de sous-traitance documentée

**Sous-traitants typiques d'un chatbot :**
```
- Mistral AI (traitement du langage)
- Hébergeur cloud (AWS, Azure, OVH)
- Service d'authentification (OAuth providers)
- Outils d'analytics (monitoring, logs)
- Services de sauvegarde
```

**Questions d'audit :**
1. Tous les sous-traitants sont-ils identifiés ?
2. Leur conformité RGPD a-t-elle été vérifiée ?
3. La chaîne de sous-traitance est-elle maîtrisée ?

**État de conformité :** ⬜ Conforme ⬜ Non-conforme ⬜ Partiellement ⬜ À vérifier ⬜ N/A

---

## 📋 Section 6 : Documentation (2 points)

### ✅ Point 19 : Registre des traitements tenu à jour

**Exigence RGPD** : Article 30 - Registre des activités de traitement

**À vérifier :**
- [ ] Registre des traitements documenté
- [ ] Informations obligatoires présentes
- [ ] Mise à jour régulière du registre

**Fiche de traitement "Chatbot pédagogique" :**
```
Nom du traitement : Chatbot pédagogique Deep Learning
Finalité : Assistance pédagogique personnalisée
Base légale : Mission d'intérêt public (art. 6.1.e)
Catégories de personnes : Étudiants BTS SIO
Catégories de données : Identité, conversations, progression
Destinataires : Enseignants, administration pédagogique
Transferts : Mistral AI (sous-traitant UE)
Durée de conservation : 1 an (conversations), 3 ans (progression)
Mesures de sécurité : Chiffrement, authentification, logs
```

**Questions d'audit :**
1. Le traitement est-il inscrit au registre ?
2. Toutes les informations obligatoires sont-elles présentes ?
3. Le registre est-il tenu à jour ?

**État de conformité :** ⬜ Conforme ⬜ Non-conforme ⬜ Partiellement ⬜ À vérifier ⬜ N/A

---

### ✅ Point 20 : Politique de confidentialité accessible

**Exigence RGPD** : Articles 13 et 14 - Information des personnes

**À vérifier :**
- [ ] Politique de confidentialité facilement accessible
- [ ] Toutes les informations obligatoires présentes
- [ ] Langage clair et compréhensible

**Contenu obligatoire de la politique :**
```
1. Identité du responsable de traitement
2. Coordonnées du DPO
3. Finalités et base légale du traitement
4. Destinataires des données
5. Transferts vers des pays tiers
6. Durée de conservation
7. Droits des personnes et modalités d'exercice
8. Droit d'introduire une réclamation
9. Caractère obligatoire ou facultatif du traitement
10. Existence d'une prise de décision automatisée
```

**Questions d'audit :**
1. La politique de confidentialité est-elle accessible ?
2. Contient-elle toutes les informations obligatoires ?
3. Est-elle rédigée en langage clair ?

**État de conformité :** ⬜ Conforme ⬜ Non-conforme ⬜ Partiellement ⬜ À vérifier ⬜ N/A

---

## 📊 Synthèse de l'audit RGPD

### Calcul du score de conformité

```
Nombre de points conformes : ___/20
Nombre de points non-conformes : ___/20
Nombre de points partiellement conformes : ___/20
Nombre de points à vérifier : ___/20
Nombre de points non applicables : ___/20

Score de conformité = (Conformes + 0.5×Partiels) / (Total - N/A) × 100
Score obtenu : ____%
```

### Interprétation du score

| Score | Niveau de conformité | Actions requises |
|-------|---------------------|------------------|
| **90-100%** | 🟢 **Excellente conformité** | Maintenir et auditer régulièrement |
| **75-89%** | 🟡 **Bonne conformité** | Corriger les points non-conformes |
| **60-74%** | 🟠 **Conformité partielle** | Plan d'action urgent nécessaire |
| **< 60%** | 🔴 **Non-conformité critique** | Arrêt recommandé jusqu'à mise en conformité |

### Top 5 des points de non-conformité critiques

| Rang | Point | Impact | Priorité |
|------|-------|--------|----------|
| 1 | | | |
| 2 | | | |
| 3 | | | |
| 4 | | | |
| 5 | | | |

### Plan d'action recommandé

**Actions immédiates (< 1 mois) :**
1. ________________________________________________________________
2. ________________________________________________________________
3. ________________________________________________________________

**Actions à moyen terme (1-3 mois) :**
1. ________________________________________________________________
2. ________________________________________________________________
3. ________________________________________________________________

**Actions à long terme (3-6 mois) :**
1. ________________________________________________________________
2. ________________________________________________________________
3. ________________________________________________________________

### Budget estimé pour la mise en conformité

| Type d'action | Coût estimé | Délai |
|---------------|-------------|-------|
| Mesures techniques | ___€ | ___ mois |
| Formation du personnel | ___€ | ___ mois |
| Conseil juridique | ___€ | ___ mois |
| Outils de conformité | ___€ | ___ mois |
| **Total** | **___€** | **___ mois** |

---

## 🎯 Conclusion de l'audit RGPD

Cette checklist vous a permis d'évaluer méthodiquement la conformité RGPD de votre chatbot pédagogique. 

**Points clés à retenir :**

1. **La conformité RGPD n'est pas optionnelle** pour un système traitant des données d'étudiants
2. **La sécurité technique** doit être complétée par des mesures organisationnelles
3. **La documentation** est essentielle pour démontrer la conformité
4. **La formation des équipes** est cruciale pour maintenir la conformité

**Prochaines étapes :**
- Intégrer cette analyse dans votre rapport d'analyse des risques
- Prioriser les actions correctives selon l'impact et l'urgence
- Planifier un audit de suivi dans 6 mois

Cette évaluation RGPD contribue à sécuriser votre système et à protéger les droits des étudiants utilisateurs.