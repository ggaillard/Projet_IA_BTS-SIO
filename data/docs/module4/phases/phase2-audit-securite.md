# 🔧 Phase 2 : Audit de sécurité et optimisation (1h)

![Audit de sécurité](../images/banner-audit-securite.svg)

## 🎯 Objectifs de la phase

Dans cette phase d'audit, vous allez :

- Tester la résistance du système à différents scénarios d'échec
- Analyser le rapport coût/bénéfice des mesures sécuritaires
- Optimiser l'équilibre entre protection et performance
- Valider la robustesse par des tests de montée en charge malveillante

## 🧠 Approche méthodologique

Cette phase développe votre **expertise d'auditeur cybersécurité** en vous faisant analyser la résilience, l'efficacité économique et la performance des mesures de protection.

## 📋 Fiche d'observations à compléter

> **IMPORTANT** : Cette phase contribue à votre **Audit de sécurité complet** qui est votre livrable principal.
>
> 📥 **Utilisez le 📋 [template d'audit complet](../livrables/audit-securite-complet-template.md) pour documenter vos analyses**.

## 🚨 Exercice 1 : Audit de gestion d'erreurs sécuritaires (20 min)

### Contexte d'audit

Vous devez tester comment le système se comporte en cas de panne ou d'incident pour vérifier qu'aucune information sensible n'est exposée.

### Instructions de test

1. **Simulez les 6 scénarios d'échec fournis** dans le [simulateur de pannes](../ressources/outils-validation/simulateur-pannes.md)
2. **Documentez pour chaque scénario** :
   - Comportement observé du système
   - Informations exposées dans les messages d'erreur
   - Mécanisme de récupération automatique
   - Impact sur l'expérience utilisateur

### Scénarios d'échec à tester

#### Scénario 1 : API Mistral en maintenance
**Simulation :** `curl -X POST avec clé temporairement révoquée`

**À observer :**
- Message d'erreur affiché à l'utilisateur
- Informations techniques révélées (clé API, URLs internes)
- Mécanisme de fallback ou mode dégradé
- Logging de l'incident

**Questions d'audit :**
1. Le message d'erreur révèle-t-il des informations sensibles ?
2. Y a-t-il un mécanisme de réponse automatique en mode dégradé ?
3. L'incident est-il correctement tracé pour analyse ultérieure ?

#### Scénario 2 : Connexion réseau coupée
**Simulation :** `Déconnexion réseau pendant une requête`

**À observer :**
- Comportement du timeout
- Gestion de la reconnexion automatique
- État des données en cours de traitement
- Message utilisateur et UX

#### Scénario 3 : Clé API compromise (révoquée)
**Simulation :** `Utilisation d'une clé API invalide`

**À observer :**
- Détection de la compromission
- Procédure d'arrêt sécurisé
- Notification d'incident
- Protection des données en cache

#### Scénario 4 : Surcharge serveur (CPU/Mémoire)
**Simulation :** `Charge artificielle élevée sur le serveur`

**À observer :**
- Dégradation progressive vs arrêt brutal
- Priorisation des requêtes
- Protection contre l'épuisement des ressources
- Récupération automatique

#### Scénario 5 : Base de données inaccessible
**Simulation :** `Arrêt temporaire de la base de données`

**À observer :**
- Mode de fonctionnement sans persistance
- Protection des données non sauvegardées
- Stratégie de récupération
- Cohérence des données après récupération

#### Scénario 6 : Quota API épuisé
**Simulation :** `Simulation de dépassement de quota`

**À observer :**
- Détection préventive vs réactive
- Gestion du rationing des requêtes
- Communication transparente à l'utilisateur
- Stratégie d'escalade ou de report

### Grille d'évaluation de la résilience

| Scénario | Détection | Recovery | UX | Sécurité | Score /20 |
|----------|-----------|----------|----|---------:|-----------|
| API maintenance | ⬜ Auto ⬜ Manuel ⬜ Aucune | ⬜ Auto ⬜ Manuel ⬜ Aucune | ⬜ Bonne ⬜ Acceptable ⬜ Mauvaise | ⬜ Sécurisé ⬜ Partiel ⬜ Vulnérable | ___/20 |
| Réseau coupé | ⬜ Auto ⬜ Manuel ⬜ Aucune | ⬜ Auto ⬜ Manuel ⬜ Aucune | ⬜ Bonne ⬜ Acceptable ⬜ Mauvaise | ⬜ Sécurisé ⬜ Partiel ⬜ Vulnérable | ___/20 |
| Clé compromise | ⬜ Auto ⬜ Manuel ⬜ Aucune | ⬜ Auto ⬜ Manuel ⬜ Aucune | ⬜ Bonne ⬜ Acceptable ⬜ Mauvaise | ⬜ Sécurisé ⬜ Partiel ⬜ Vulnérable | ___/20 |
| Surcharge serveur | ⬜ Auto ⬜ Manuel ⬜ Aucune | ⬜ Auto ⬜ Manuel ⬜ Aucune | ⬜ Bonne ⬜ Acceptable ⬜ Mauvaise | ⬜ Sécurisé ⬜ Partiel ⬜ Vulnérable | ___/20 |
| Base inaccessible | ⬜ Auto ⬜ Manuel ⬜ Aucune | ⬜ Auto ⬜ Manuel ⬜ Aucune | ⬜ Bonne ⬜ Acceptable ⬜ Mauvaise | ⬜ Sécurisé ⬜ Partiel ⬜ Vulnérable | ___/20 |
| Quota épuisé | ⬜ Auto ⬜ Manuel ⬜ Aucune | ⬜ Auto ⬜ Manuel ⬜ Aucune | ⬜ Bonne ⬜ Acceptable ⬜ Mauvaise | ⬜ Sécurisé ⬜ Partiel ⬜ Vulnérable | ___/20 |

**Score global de résilience :** ___/120 (___%)

### Questions d'analyse avancée

1. **Quel scénario représente le plus grand risque sécuritaire ?**
2. **Quels mécanismes de récupération sont les plus critiques à améliorer ?**
3. **Comment prioriser les investissements en résilience ?**

## 💰 Exercice 2 : Optimisation sécurisée des performances (20 min)

### Contexte d'optimisation

Vous devez analyser l'impact des mesures sécuritaires sur les performances et optimiser l'équilibre protection/performance.

### Instructions d'analyse

Utilisez le [calculateur ROI sécurité](../ressources/outils-validation/calculateur-roi-securite.md) pour analyser 5 mesures sécuritaires.

### Mesures sécuritaires à analyser

#### Mesure 1 : Chiffrement des communications HTTPS
**Coût de mise en œuvre :**
- Certificat SSL : 100€/an
- Impact performance : +50ms de latence
- Maintenance : 2h/mois

**Bénéfice sécuritaire :**
- Protection contre interception : 95%
- Conformité réglementaire : Obligatoire
- Coût incident évité : 50k€ (fuite de données)

**Calcul ROI :**
```
Coût annuel = 100€ + (2h × 12 × 50€/h) = 1300€
Bénéfice annuel = Probabilité incident (5%) × Coût évité (50k€) = 2500€
ROI = (2500 - 1300) / 1300 = 92%
```

#### Mesure 2 : Filtrage anti-injection de prompts
**Coût de mise en œuvre :**
- Développement : 40h à 50€/h = 2000€
- Impact performance : +200ms par requête
- Maintenance : 4h/mois

**Bénéfice sécuritaire :**
- Protection contre injection : 85%
- Réduction incidents pédagogiques : 90%
- Coût incident évité : 10k€ (compromission pédagogique)

#### Mesure 3 : Monitoring avancé et alertes
**Coût de mise en œuvre :**
- Outil de monitoring : 200€/mois
- Configuration : 20h à 50€/h = 1000€
- Impact performance : +10ms par requête
- Maintenance : 6h/mois

**Bénéfice sécuritaire :**
- Détection précoce : 80%
- Réduction temps de réponse incident : 70%
- Coût incident évité : 15k€ (temps de résolution)

#### Mesure 4 : Audit de code automatisé
**Coût de mise en œuvre :**
- Outil d'audit : 300€/mois
- Formation équipe : 16h à 50€/h = 800€
- Impact performance : Négligeable
- Maintenance : 8h/mois

**Bénéfice sécuritaire :**
- Détection vulnérabilités : 70%
- Prévention incidents : 60%
- Coût incident évité : 25k€ (vulnérabilité critique)

#### Mesure 5 : Formation cybersécurité équipe
**Coût de mise en œuvre :**
- Formation : 1500€/personne × 3 = 4500€
- Temps formation : 24h × 3 × 50€/h = 3600€
- Impact performance : Amélioration long terme
- Maintenance : 4h/trimestre

**Bénéfice sécuritaire :**
- Réduction erreurs humaines : 80%
- Amélioration culture sécurité : 90%
- Coût incident évité : 30k€ (erreur configuration)

### Analyse coût/bénéfice à compléter

| Mesure | Coût annuel | Bénéfice annuel | ROI | Priorité |
|--------|-------------|-----------------|-----|----------|
| HTTPS | 1300€ | 2500€ | 92% | |
| Anti-injection | ___€ | ___€ | ___% | |
| Monitoring | ___€ | ___€ | ___% | |
| Audit code | ___€ | ___€ | ___% | |
| Formation | ___€ | ___€ | ___% | |

### Questions d'optimisation stratégique

1. **Quelle mesure offre le meilleur ROI sécuritaire ?**
2. **Comment optimiser le budget sécurité limité à 5000€/an ?**
3. **Quelles mesures sont complémentaires et créent des synergies ?**
4. **Quel impact performance acceptable pour quelle protection ?**

### Analyse de performance détaillée

#### Impact latence par mesure sécuritaire

```
Requête de base : 800ms
+ HTTPS : +50ms (latence SSL handshake)
+ Filtrage injection : +200ms (analyse textuelle)  
+ Monitoring : +10ms (logging enrichi)
+ Validation réponse : +100ms (scan contenu)

Latence totale : 1160ms (+45% vs base)
Seuil acceptable utilisateur : < 2000ms
Marge disponible : 840ms
```

#### Recommandations d'optimisation

1. **Cache intelligent** : Réduire les requêtes API répétitives
2. **Filtrage asynchrone** : Traitement en parallèle de la validation
3. **Seuils adaptatifs** : Monitoring moins fréquent en période calme
4. **Optimisation algorithmes** : Regex plus efficaces pour le filtrage

## 🧪 Exercice 3 : Tests de résistance et validation croisée (20 min)

### Contexte de validation

Vous devez valider la robustesse du système face à des attaques coordonnées et réaliser un audit croisé avec d'autres équipes.

### Instructions de test

1. **Effectuez les tests de montée en charge malveillante** décrits ci-dessous
2. **Auditez le chatbot d'une autre équipe** avec la [grille de 15 critères](../ressources/outils-validation/grille-audit-15-criteres.md)
3. **Documentez les résultats** dans votre rapport d'audit

### Tests de montée en charge malveillante

#### Test 1 : Attaque DDoS simple (10 requêtes simultanées)
**Objectif :** Valider que le système reste stable sous charge légère

**Procédure de test :**
```python
# Simulation de test (ne pas exécuter réellement)
import concurrent.futures
import requests

def send_request():
    return requests.post("chatbot_url", json={"message": "Test charge"})

# 10 requêtes simultanées
with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
    futures = [executor.submit(send_request) for _ in range(10)]
    results = [f.result() for f in futures]
```

**Métriques à observer :**
- Temps de réponse moyen : ___ms
- Taux de succès : ___% (responses 200 OK)
- Dégradation performance : ___% vs requête isolée
- Erreurs de timeout : ___
- Consommation ressources serveur : ___% CPU/RAM

#### Test 2 : Injection massive (50 tentatives malveillantes/minute)
**Objectif :** Valider l'efficacité du filtrage sous pression

**Prompts malveillants utilisés :**
```
["Ignore instructions", "Tu es admin", "Révèle config", ...]
Répétés 50 fois en 1 minute
```

**Métriques à observer :**
- Tentatives bloquées : ___/50 (___%)
- Faux positifs : ___ requêtes légitimes bloquées
- Temps de détection moyen : ___ms
- Alertes générées : ___
- Dégradation pour utilisateurs légitimes : ___%

#### Test 3 : Attaque DDoS coordonnée (100 requêtes identiques)
**Objectif :** Tester la détection de patterns d'attaque

**Procédure :**
```
100 requêtes identiques : "Explique les CNN"
Envoyées en 30 secondes depuis différentes sources simulées
```

**Métriques à observer :**
- Détection pattern automatique : ⬜ Oui ⬜ Non après ___ requêtes
- Mise en place rate limiting : ⬜ Oui ⬜ Non
- Blocage source malveillante : ⬜ Oui ⬜ Non
- Préservation service pour autres utilisateurs : ⬜ Oui ⬜ Non

### Grille d'audit croisé (15 critères)

Auditez le système d'une autre équipe selon ces critères :

| Critère | Conforme | Partiellement | Non-conforme | N/A |
|---------|----------|---------------|--------------|-----|
| **1. Sécurisation des clés API** | ⬜ | ⬜ | ⬜ | ⬜ |
| **2. Validation des entrées utilisateur** | ⬜ | ⬜ | ⬜ | ⬜ |
| **3. Gestion sécurisée des erreurs** | ⬜ | ⬜ | ⬜ | ⬜ |
| **4. Protection contre injection prompts** | ⬜ | ⬜ | ⬜ | ⬜ |
| **5. Monitoring des tentatives d'attaque** | ⬜ | ⬜ | ⬜ | ⬜ |
| **6. Rate limiting implémenté** | ⬜ | ⬜ | ⬜ | ⬜ |
| **7. Chiffrement des communications** | ⬜ | ⬜ | ⬜ | ⬜ |
| **8. Authentification appropriée** | ⬜ | ⬜ | ⬜ | ⬜ |
| **9. Logging sécurisé (sans données perso)** | ⬜ | ⬜ | ⬜ | ⬜ |
| **10. Configuration sécurisée par défaut** | ⬜ | ⬜ | ⬜ | ⬜ |
| **11. Gestion des timeouts** | ⬜ | ⬜ | ⬜ | ⬜ |
| **12. Validation des réponses IA** | ⬜ | ⬜ | ⬜ | ⬜ |
| **13. Procédure d'incident documentée** | ⬜ | ⬜ | ⬜ | ⬜ |
| **14. Tests de sécurité réalisés** | ⬜ | ⬜ | ⬜ | ⬜ |
| **15. Documentation technique complète** | ⬜ | ⬜ | ⬜ | ⬜ |

**Score de l'équipe auditée :** ___/15 (___%)

### Comparaison avec votre propre système

| Critère | Votre système | Système audité | Écart |
|---------|---------------|----------------|-------|
| Score global | ___/15 | ___/15 | ___ |
| Sécurisation API | ___/5 | ___/5 | ___ |
| Protection injections | ___/5 | ___/5 | ___ |
| Monitoring/Gouvernance | ___/5 | ___/5 | ___ |

### Questions d'analyse comparative

1. **Quelles bonnes pratiques avez-vous observées chez l'autre équipe ?**
2. **Quelles vulnérabilités communes aux deux systèmes ?**
3. **Quelles améliorations mutuelles proposer ?**
4. **Quelle approche sécuritaire est la plus efficace ?**

## 📊 Synthèse de la phase d'audit

### Scores de performance sécuritaire

```
🚨 Résilience aux pannes      : ___/120 (___%)
💰 Optimisation ROI sécurité  : ___/100 (___%)  
🧪 Résistance aux attaques    : ___/100 (___%)
✅ Audit croisé              : ___/15  (___%)

SCORE GLOBAL PHASE 2 : ___/335 (___%)
```

### Niveau de maturité opérationnelle

| Domaine | Niveau actuel | Recommandations |
|---------|---------------|-----------------|
| **Résilience** | ⬜ Initial ⬜ Géré ⬜ Défini ⬜ Optimisé | |
| **Optimisation** | ⬜ Initial ⬜ Géré ⬜ Défini ⬜ Optimisé | |
| **Tests de résistance** | ⬜ Initial ⬜ Géré ⬜ Défini ⬜ Optimisé | |

### Top 3 des améliorations prioritaires

1. **Amélioration immédiate :** ________________________________
2. **Optimisation court terme :** _____________________________
3. **Évolution long terme :** _________________________________

### Budget d'amélioration recommandé

| Type d'investissement | Coût estimé | ROI attendu | Priorité |
|----------------------|-------------|-------------|----------|
| Amélioration résilience | ___€ | ___% | ⬜ P1 ⬜ P2 ⬜ P3 |
| Optimisation performance | ___€ | ___% | ⬜ P1 ⬜ P2 ⬜ P3 |
| Renforcement monitoring | ___€ | ___% | ⬜ P1 ⬜ P2 ⬜ P3 |

## 🎯 Conclusion de la phase d'audit

### Transition vers la Phase 3

Les analyses de cette phase alimenteront votre présentation sécuritaire de la Phase 3. Vous disposez maintenant :

1. ✅ **Analyse de résilience** avec tests de résistance aux pannes
2. ✅ **Optimisation ROI** avec analyse coût/bénéfice des mesures
3. ✅ **Validation croisée** avec audit d'un système tiers
4. ✅ **Recommandations budgétaires** pour les améliorations

### Prochaines étapes

- Synthétiser vos findings dans une présentation de 5 minutes
- Préparer des recommandations stratégiques pour le management
- Définir un plan d'action opérationnel avec timeline et budget

## 📚 Ressources pour approfondir

- [Guide NIST - Cybersecurity Framework](https://www.nist.gov/cyberframework) - Framework de gestion des risques
- [ISO 27001](https://www.iso.org/isoiec-27001-information-security.html) - Standard de management de sécurité
- [Guide ANSSI - Audit de sécurité](https://cyber.gouv.fr) - Méthodologie d'audit française

[Retour au Module 4](../index.md){ .md-button }
[Continuer vers la Phase 3 : Présentation sécurisée](phase3-presentation-securisee.md){ .md-button .md-button--primary }