# 📝 QCM d'évaluation - Module 4 : Cybersécurité IA

Ce QCM vous permettra d'évaluer votre maîtrise des concepts de cybersécurité appliqués aux systèmes IA conversationnels étudiés dans ce module.

## ✅ Instructions
- Cochez la ou les réponses correctes pour chaque question
- Certaines questions peuvent avoir plusieurs réponses correctes
- Pour les questions à choix multiples, 0,5 point est attribué par réponse correcte (maximum 1 point par question)
- À la fin du questionnaire, calculez votre score grâce au corrigé fourni
- Durée recommandée : 15 minutes

## 🔍 Partie A : Analyse des risques IA (5 questions)

### 1. Parmi ces menaces, lesquelles sont spécifiques aux chatbots IA pédagogiques ? (plusieurs réponses possibles)
- [ ] Injection de prompts pour contourner les instructions système
- [ ] Attaques DDoS sur les serveurs web
- [ ] Extraction systématique de la base de connaissances propriétaire
- [ ] Empoisonnement des réponses par injection de fausses informations
- [ ] Failles SQL dans les bases de données

### 2. Dans la méthodologie CVSS adaptée IA, comment évalue-t-on la complexité d'une attaque par injection de prompts ?
- [ ] Faible - car elle ne nécessite que des compétences linguistiques
- [ ] Élevée - car elle nécessite une compréhension approfondie du modèle IA
- [ ] Variable selon le niveau de protection implémenté
- [ ] Ne peut pas être évaluée avec CVSS standard

### 3. Quelle base légale RGPD est la plus appropriée pour un chatbot pédagogique en établissement public ?
- [ ] Consentement de la personne concernée (art. 6.1.a)
- [ ] Exécution d'un contrat (art. 6.1.b)
- [ ] Mission d'intérêt public (art. 6.1.e)
- [ ] Intérêt légitime (art. 6.1.f)

### 4. Dans une matrice risque/impact, comment classer une vulnérabilité de "clé API stockée en dur" ?
- [ ] Probabilité faible / Impact faible
- [ ] Probabilité élevée / Impact élevé
- [ ] Probabilité faible / Impact élevé
- [ ] Probabilité élevée / Impact faible

### 5. Quel pourcentage du budget projet est généralement acceptable pour la cybersécurité d'un système IA en phase de consolidation ?
- [ ] 5-10% (minimal)
- [ ] 15-25% (standard)
- [ ] 30-40% (renforcé)
- [ ] >50% (critique)

## 🛡️ Partie B : Techniques d'attaque et protection (5 questions)

### 6. Parmi ces techniques, lesquelles sont efficaces contre l'injection de prompts ? (plusieurs réponses possibles)
- [ ] Filtrage par mots-clés suspects (ignore, système, admin)
- [ ] Limitation de longueur des entrées utilisateur
- [ ] Validation post-réponse pour détecter les fuites d'information
- [ ] Chiffrement des communications HTTPS
- [ ] Prompt système renforcé avec instructions de sécurité

### 7. Quel est l'ordre correct d'une stratégie de défense en profondeur pour un chatbot ?
- [ ] 1) Validation entrée → 2) Prompt système → 3) Filtrage réponse → 4) Monitoring
- [ ] 1) Chiffrement → 2) Authentification → 3) Validation → 4) Logging
- [ ] 1) Monitoring → 2) Prévention → 3) Détection → 4) Réponse
- [ ] 1) Firewall → 2) Antivirus → 3) IDS → 4) Backup

### 8. Dans le test "50 tentatives d'injection en 1 minute", quel taux de détection est considéré comme acceptable ?
- [ ] >70% (suffisant pour la plupart des cas)
- [ ] >85% (bon niveau de protection)
- [ ] >95% (excellent niveau requis pour production)
- [ ] 100% (seul niveau acceptable)

### 9. Quelle est la principale limite des techniques de filtrage par mots-clés ?
- [ ] Impact trop important sur les performances
- [ ] Coût de mise en œuvre trop élevé
- [ ] Génération de faux positifs bloquant des requêtes légitimes
- [ ] Inefficacité totale contre les attaques modernes

### 10. Pour détecter une tentative d'empoisonnement de données, quel indicateur est le plus fiable ?
- [ ] Volume anormalement élevé de requêtes
- [ ] Incohérence dans les réponses du chatbot par rapport aux sources fiables
- [ ] Utilisation de mots-clés suspects
- [ ] Adresse IP suspecte

## 📊 Partie C : Métriques et monitoring (5 questions)

### 11. Un taux de faux positifs de 15% dans la détection d'attaques signifie que :
- [ ] 15% des attaques ne sont pas détectées
- [ ] 15% des alertes sont injustifiées (requêtes légitimes bloquées)
- [ ] 15% des utilisateurs sont impactés par des dysfonctionnements
- [ ] Le système est défaillant et doit être arrêté

### 12. Dans l'analyse de performance, une dégradation de +60% de latence sous attaque est :
- [ ] Excellente (impact négligeable)
- [ ] Acceptable (impact maîtrisé)
- [ ] Limite (optimisation nécessaire)
- [ ] Problématique (refonte requise)

### 13. Pour un chatbot pédagogique, quel KPI de sécurité est le plus critique à surveiller ?
- [ ] Nombre total de requêtes par jour
- [ ] Taux de détection des tentatives d'injection
- [ ] Temps de réponse moyen du système
- [ ] Nombre d'utilisateurs connectés simultanément

### 14. Un coût API passant de 150€/mois à 520€/mois sous attaque indique :
- [ ] Une faille de sécurité majeure nécessitant un arrêt immédiat
- [ ] Un besoin d'optimisation du filtrage en amont de l'API
- [ ] Un dimensionnement sous-évalué normal en production
- [ ] Une attaque DDoS réussie sur l'infrastructure

### 15. Pour surveiller la conformité RGPD d'un chatbot, quel indicateur est le plus pertinent ?
- [ ] Pourcentage de données chiffrées
- [ ] Temps de réponse aux demandes d'exercice des droits
- [ ] Nombre de cookies utilisés par l'application
- [ ] Fréquence des sauvegardes de données

## 🔧 Partie D : Vision stratégique et transfert (5 questions)

### 16. Pour un déploiement à 10,000 utilisateurs, quelle approche de scaling sécurisé est la plus appropriée ?
- [ ] Déploiement immédiat avec monitoring renforcé
- [ ] Approche progressive par phases avec validation à chaque étape
- [ ] Attendre d'avoir corrigé toutes les vulnérabilités identifiées
- [ ] Externaliser la sécurité à un prestataire spécialisé

### 17. Dans l'analyse coût/bénéfice, une mesure de sécurité avec un ROI de 92% signifie :
- [ ] Un investissement très rentable à prioriser
- [ ] Un coût acceptable pour une protection standard
- [ ] Une dépense excessive à éviter
- [ ] Un calcul erroné car le ROI sécurité ne peut pas être mesuré

### 18. Parmi ces compétences développées, lesquelles sont transférables à d'autres systèmes IA ? (plusieurs réponses possibles)
- [ ] Méthodologie d'audit structurée et reproductible
- [ ] Tests d'injection spécifiques aux chatbots textuels
- [ ] Analyse de risques spécifiques aux systèmes IA
- [ ] Configuration spécifique de l'API Mistral AI
- [ ] Framework de mesure de performance sécuritaire

### 19. Pour maintenir une expertise cybersécurité IA à jour, quelle approche est la plus efficace ?
- [ ] Formation annuelle intensive de 40 heures
- [ ] Veille continue + expérimentation régulière sur projets réels
- [ ] Certification tous les 3 ans
- [ ] Lecture de documentation technique mensuelle

### 20. Dans un contexte professionnel, comment valoriser l'expertise cybersécurité IA développée ?
- [ ] Spécialisation exclusive sur les technologies d'IA
- [ ] Combinaison avec des compétences sécurité traditionnelles
- [ ] Focus sur les aspects réglementaires uniquement
- [ ] Orientation vers le développement IA plutôt que la sécurité

## Auto-évaluation

Une fois le QCM complété, vérifiez vos réponses avec le corrigé ci-dessous et calculez votre score.

### Corrigé avec explications

#### Partie A : Analyse des risques IA

1. **a, c, d - Injection de prompts, Extraction base de connaissances, Empoisonnement des réponses**  
   *Les attaques DDoS et SQL sont généralistes. Les menaces spécifiques IA concernent la manipulation des modèles et l'exploitation de leurs particularités.*

2. **c - Variable selon le niveau de protection implémenté**  
   *La complexité d'une injection de prompts dépend fortement des mesures de protection en place : filtrage, validation, prompts système renforcés.*

3. **c - Mission d'intérêt public (art. 6.1.e)**  
   *Pour un établissement public d'enseignement, la mission éducative constitue une mission d'intérêt public, base légale la plus appropriée.*

4. **b - Probabilité élevée / Impact élevé**  
   *Clé API en dur : facilement découvrable (probabilité élevée) et permet compromission complète (impact élevé). Zone critique de la matrice.*

5. **c - 30-40% (renforcé)**  
   *En phase de consolidation d'un système IA sensible, un budget sécurité renforcé est justifié pour corriger les vulnérabilités initiales.*

#### Partie B : Techniques d'attaque et protection

6. **a, b, c, e - Filtrage mots-clés, Limitation longueur, Validation post-réponse, Prompt système renforcé**  
   *HTTPS protège la transmission mais pas contre l'injection. Les 4 autres techniques constituent une défense en profondeur efficace.*

7. **a - Validation entrée → Prompt système → Filtrage réponse → Monitoring**  
   *Ordre logique de traitement d'une requête : valider l'entrée, utiliser un prompt sécurisé, filtrer la sortie, monitorer l'ensemble.*

8. **c - >95% (excellent niveau requis pour production)**  
   *Avec seulement 5% d'attaques non détectées sur 50 tentatives, le système montre une robustesse acceptable pour la production.*

9. **c - Génération de faux positifs bloquant des requêtes légitimes**  
   *Le filtrage par mots-clés peut bloquer des questions légitimes contenant des termes suspects, dégradant l'expérience utilisateur.*

10. **b - Incohérence dans les réponses du chatbot par rapport aux sources fiables**  
    *L'empoisonnement se manifeste par des réponses incorrectes. La validation croisée avec des sources fiables est le meilleur indicateur.*

#### Partie C : Métriques et monitoring

11. **b - 15% des alertes sont injustifiées (requêtes légitimes bloquées)**  
    *Faux positif = alerte déclenchée à tort. 15% signifie que 15% des alertes concernent des requêtes légitimes.*

12. **c - Limite (optimisation nécessaire)**  
    *+60% de dégradation sous attaque est à la limite de l'acceptable. L'optimisation est nécessaire avant déploiement large.*

13. **b - Taux de détection des tentatives d'injection**  
    *Pour un chatbot pédagogique, la protection du contenu éducatif est critique. Le taux de détection est le KPI le plus important.*

14. **b - Un besoin d'optimisation du filtrage en amont de l'API**  
    *Coût ×3.5 indique que les attaques consomment des ressources API. Le filtrage pré-API permettrait d'économiser.*

15. **b - Temps de réponse aux demandes d'exercice des droits**  
    *La conformité RGPD se mesure par la capacité à respecter les droits des personnes, notamment le délai de 1 mois pour répondre aux demandes.*

#### Partie D : Vision stratégique et transfert

16. **b - Approche progressive par phases avec validation à chaque étape**  
    *Le scaling sécurisé nécessite une approche progressive permettant d'identifier et corriger les problèmes avant le déploiement complet.*

17. **a - Un investissement très rentable à prioriser**  
    *ROI de 92% signifie que l'investissement génère 1,92€ de bénéfice pour 1€ investi. C'est un excellent retour sur investissement.*

18. **a, c, e - Méthodologie d'audit, Analyse de risques IA, Framework de mesure**  
    *Ces compétences sont généralisables. Les tests d'injection chatbot et la config Mistral sont spécifiques à ce contexte.*

19. **b - Veille continue + expérimentation régulière sur projets réels**  
    *La cybersécurité IA évolue rapidement. La veille continue et la pratique régulière sont essentielles pour maintenir l'expertise.*

20. **b - Combinaison avec des compétences sécurité traditionnelles**  
    *L'expertise IA complète les compétences sécurité traditionnelles, créant un profil hybride très recherché sur le marché.*

### Calcul de votre score
- Questions à choix unique (2-5, 7-15, 16-17, 19-20) : 1 point par réponse correcte
- Questions à choix multiples (1, 6, 18) : 0,5 point par réponse correcte et -0,25 par réponse incorrecte (minimum 0, maximum 1 point par question)

**Total des points possibles : 20**

### Interprétation

#### Niveaux de maîtrise cybersécurité IA

- **17-20 points (85-100%)** : **🏆 Expert cybersécurité IA**
  - Maîtrise excellente des concepts et techniques
  - Capable d'auditer des systèmes IA en autonomie
  - Prêt pour des responsabilités sécuritaires avancées
  - *Profils cibles : Consultant cybersécurité IA, Responsable sécurité produit IA*

- **14-16 points (70-84%)** : **🥈 Praticien confirmé**
  - Bonne compréhension des enjeux sécuritaires IA
  - Capable d'assister un audit avec supervision limitée
  - Quelques approfondissements à consolider
  - *Profils cibles : Auditeur sécurité junior, Spécialiste conformité IA*

- **11-13 points (55-69%)** : **🥉 Bases solides acquises**
  - Compréhension correcte des fondamentaux
  - Capable de participer à un audit sous supervision
  - Formation complémentaire recommandée
  - *Profils cibles : Assistant auditeur, Analyste sécurité débutant*

- **0-10 points (<55%)** : **📚 Révision approfondie nécessaire**
  - Concepts de base à revoir
  - Pratique supplémentaire indispensable
  - Formation complémentaire obligatoire avant responsabilités sécuritaires

### Analyse par domaine de compétence

#### 🔍 Analyse des risques IA (Questions 1-5)
**Votre score :** ___/5
- **4-5/5** : Excellente capacité d'analyse de risques IA
- **3/5** : Bonne compréhension, quelques nuances à maîtriser
- **2/5** : Bases correctes, approfondissement nécessaire
- **0-1/5** : Méthodologie d'analyse des risques à revoir

#### 🛡️ Techniques d'attaque et protection (Questions 6-10)
**Votre score :** ___/5
- **4-5/5** : Maîtrise opérationnelle des techniques de protection
- **3/5** : Compréhension correcte, expérience pratique à développer
- **2/5** : Connaissances théoriques, mise en pratique à renforcer
- **0-1/5** : Techniques de protection à étudier en profondeur

#### 📊 Métriques et monitoring (Questions 11-15)
**Votre score :** ___/5
- **4-5/5** : Capacité d'interprétation avancée des métriques sécurité
- **3/5** : Bonne lecture des indicateurs, analyse à affiner
- **2/5** : Compréhension basique, formation monitoring nécessaire
- **0-1/5** : Concepts de métriques sécurité à acquérir

#### 🔧 Vision stratégique et transfert (Questions 16-20)
**Votre score :** ___/5
- **4-5/5** : Vision stratégique mature, prêt pour responsabilités managériales
- **3/5** : Bonne compréhension business, leadership à développer
- **2/5** : Aspects stratégiques corrects, expérience à acquérir
- **0-1/5** : Vision business de la cybersécurité à construire

### Plan de développement personnalisé

#### Si score 17-20 : Voie d'expertise
**Objectifs immédiats :**
- Obtenir une certification cybersécurité (CISSP, CISA)
- Participer à des audits réels en stage ou mission
- Contribuer à la recherche en sécurité IA (publications, conferences)

**Opportunités professionnelles :**
- Stage en cabinet de conseil cybersécurité (focus IA)
- Poste junior chez un éditeur de solutions IA
- Participation à des programmes bug bounty IA

#### Si score 14-16 : Voie de consolidation
**Objectifs immédiats :**
- Approfondir les domaines <4/5 identifiés
- Participer à des projets pratiques supplémentaires
- Suivre des formations complémentaires ciblées

**Actions recommandées :**
- MOOC ANSSI Cybersécurité (gratuit)
- Participation à des CTF (Capture The Flag) sécurité
- Lecture d'études de cas d'incidents sécurité IA

#### Si score 11-13 : Voie de renforcement
**Objectifs immédiats :**
- Réviser les concepts fondamentaux identifiés
- Pratiquer sur des environnements d'entraînement
- Rechercher un mentorat cybersécurité

**Ressources recommandées :**
- Cours en ligne cybersécurité (Coursera, edX)
- Participation à des communautés OWASP locales
- Projets personnels d'audit sécurité

#### Si score <11 : Voie de reconstruction
**Objectifs immédiats :**
- Formation cybersécurité générale avant spécialisation IA
- Bases techniques à renforcer (réseaux, systèmes)
- Accompagnement pédagogique personnalisé

**Plan d'action :**
- Formation cybersécurité de base (40h minimum)
- Refaire le module 4 avec accompagnement renforcé
- Stage découverte en équipe cybersécurité

### Certification des acquis

#### Attestation de compétences développées

**Candidat :** _______________________  
**Score obtenu :** ___/20 (___%)  
**Niveau certifié :** ________________________________

**Compétences validées :**
- [ ] Analyse de risques spécifiques aux systèmes IA conversationnels
- [ ] Audit de sécurité avec méthodologies professionnelles  
- [ ] Tests de résistance et validation de robustesse
- [ ] Interprétation de métriques et KPIs de sécurité
- [ ] Vision stratégique et recommandations budgétaires

**Recommandations pour la suite :**
- **Formation complémentaire :** ________________________________
- **Expérience pratique :** ________________________________
- **Certification visée :** ________________________________

#### Portfolio de compétences cybersécurité IA

**Livrables produits pendant le module :**
✅ Rapport d'analyse des risques (5 menaces analysées)  
✅ Audit de sécurité complet (23 tests réalisés)  
✅ Analyse de métriques (5 KPIs interprétés)  
✅ Présentation sécuritaire (5 minutes, niveau professionnel)

**Méthodologies maîtrisées :**
✅ CVSS adapté IA pour classification vulnérabilités  
✅ Matrice risque/impact pour priorisation investissements  
✅ Framework ROI sécurité pour justification économique  
✅ Tests d'injection éthiques et contrôlés

**Outils utilisés :**
✅ Grilles d'audit structurées (15 critères)  
✅ Simulateurs de pannes et tests de résistance  
✅ Calculateurs de coût/bénéfice sécurité  
✅ Dashboards de métriques et KPIs

### Évolution vers l'expertise

#### Progression naturelle des compétences

**Mois 1-3 : Consolidation**
- Appliquer les méthodologies sur d'autres projets
- Développer l'expertise sur les outils professionnels
- Participer à des audits réels sous supervision

**Mois 4-6 : Spécialisation**
- Choisir un domaine de spécialisation (audit, conformité, conseil)
- Obtenir une première certification reconnue
- Contribuer à des projets open source sécurité IA

**Mois 7-12 : Expertise**
- Mener des audits en autonomie
- Former d'autres professionnels
- Publier des retours d'expérience

#### Opportunités de carrière

**Secteurs porteurs :**
- **Fintech** : Sécurisation des chatbots bancaires et financiers
- **Santé** : Conformité RGPD pour IA médicale
- **Éducation** : Audit de plateformes pédagogiques IA
- **E-commerce** : Sécurité des assistants virtuels clients

**Évolution salariale attendue :**
- **Junior (0-2 ans)** : 35-45k€
- **Confirmé (2-5 ans)** : 45-60k€  
- **Senior (5+ ans)** : 60-80k€
- **Expert/Consultant** : 80-120k€

**Prochaines étapes recommandées :**
1. **Identifier** votre domaine de prédilection (audit, conformité, conseil)
2. **Planifier** votre première certification cybersécurité
3. **Rechercher** des opportunités de stage/mission dans ce domaine
4. **Développer** un réseau professionnel cybersécurité IA

---

## 🎉 Félicitations !

Vous avez terminé le **Module 4 - Cybersécurité IA** et développé une expertise recherchée sur le marché !

**Votre expertise porte sur :**
🔒 Sécurisation complète d'un système IA conversationnel  
📊 Audit méthodique avec outils professionnels  
💰 Optimisation équilibre sécurité/performance/coût  
🎯 Vision stratégique pour déploiement industriel

**Cette compétence vous différencie** dans un marché où la cybersécurité IA devient critique pour tous les secteurs utilisant l'intelligence artificielle.

Bonne continuation dans votre parcours professionnel ! 🚀

---

## 📚 Ressources pour aller plus loin

### Formations spécialisées
- **[SANS FOR578 - Cyber Threat Intelligence](https://sans.org)** - Analyse de menaces avancée
- **[CISSP Certification](https://isc2.org)** - Certification cybersécurité reconnue mondialement  
- **[CISA Certification](https://isaca.org)** - Spécialisation audit de sécurité

### Veille technologique
- **[OWASP AI Security](https://owasp.org/www-project-ai-security-and-privacy-guide/)** - Guide sécurité IA mis à jour
- **[ANSSI Publications IA](https://cyber.gouv.fr)** - Recommandations officielles françaises
- **[NIST AI Risk Management](https://nist.gov/itl/ai-risk-management-framework)** - Framework US de gestion des risques IA

### Communautés professionnelles
- **[CLUSIF](https://clusif.fr)** - Club de la Sécurité de l'Information Français
- **[OWASP France](https://owasp.org/france/)** - Chapitre français OWASP
- **[AI Security Community](https://aisecurity.community)** - Communauté internationale sécurité IA

[Retour au Module 4](index.md){ .md-button }
[Voir la synthèse globale](ressources/synthese-module4.md){ .md-button .md-button--primary }