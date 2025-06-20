# 🔍 Phase 0 : Analyse des risques sécuritaires (30 min)

![Analyse des risques](../images/banner-analyse-risques-chatbot.svg)

## 🎯 Objectifs de la phase

Dans cette phase d'analyse, vous allez :

- Cartographier les menaces spécifiques aux chatbots IA pédagogiques
- Classer les vulnérabilités selon leur criticité et leur impact
- Auditer la conformité RGPD d'un système conversationnel
- Établir une matrice risque/impact pour prioriser les actions sécuritaires

## 🧠 Approche méthodologique

Cette phase développe votre **expertise d'analyste cybersécurité IA** sans nécessiter de programmation. Vous analyserez, classerez et prioriserez les risques selon les standards professionnels de sécurité.

## 📋 Fiche d'observations à compléter

> **IMPORTANT** : Tout au long de cette phase, vous devrez compléter votre **Rapport d'analyse des risques** qui sera votre livrable principal.
>
> 📥 **Téléchargez et consultez le 📋 [template de rapport d'analyse](../livrables/rapport-analyse-risques-template.md) dès maintenant** pour structurer votre analyse.

## 🔍 Exercice 1 : Cartographie des menaces (10 min)

### Contexte d'analyse

Vous devez analyser la sécurité d'un chatbot pédagogique qui :
- Utilise l'API Mistral AI pour générer des réponses
- Stocke une base de connaissances sur le Deep Learning
- Interagit avec des étudiants via une interface web
- Traite des données d'apprentissage et d'interaction

### Instructions d'analyse

1. **Ouvrez et étudiez** les [5 scénarios d'attaque fournis](../ressources/kit-analyse-securitaire/scenarios-attaques.md)
2. **Analysez chaque scénario** selon ces critères :
   - Vecteur d'attaque utilisé
   - Assets ciblés (données, système, utilisateurs)
   - Impact potentiel (confidentialité, intégrité, disponibilité)
   - Facilité d'exploitation (niveau technique requis)

### Scénarios à analyser

| Scénario | Type d'attaque | À analyser |
|----------|----------------|------------|
| **Scénario 1** | Injection de prompts | Tentative de contournement des instructions système |
| **Scénario 2** | Fuite de données | Exposition de la base de connaissances interne |
| **Scénario 3** | Compromission API | Utilisation frauduleuse de la clé Mistral AI |
| **Scénario 4** | Empoisonnement de données | Corruption des réponses pédagogiques |
| **Scénario 5** | Déni de service | Surcharge du système par requêtes malveillantes |

### Questions d'analyse à documenter

Pour chaque scénario, répondez dans votre rapport :

1. **Vecteur d'attaque** : Comment l'attaque est-elle menée techniquement ?
2. **Assets impactés** : Quels éléments du système sont ciblés ?
3. **Impact métier** : Quelles conséquences pour l'établissement et les étudiants ?
4. **Probabilité** : Cette attaque est-elle probable dans votre contexte ?
5. **Détection** : Comment identifier cette attaque en cours ?

## ✅ Exercice 2 : Classification des vulnérabilités (10 min)

### Méthodologie de classification

Utilisez la [grille de classification CVSS adaptée IA](../ressources/guides-securitaires/guide-cartographie-menaces.md) pour évaluer 15 vulnérabilités identifiées.

### Instructions de classification

1. **Consultez la liste** des [15 vulnérabilités courantes](../ressources/outils-validation/liste-15-vulnerabilites.md)
2. **Classez chaque vulnérabilité** selon :
   - **Criticité** : Critique / Élevée / Moyenne / Faible
   - **Facilité d'exploitation** : Facile / Moyenne / Difficile
   - **Impact** : Élevé / Moyen / Faible

### Vulnérabilités à classer

| ID | Vulnérabilité | Votre classification |
|----|---------------|---------------------|
| V01 | Clé API Mistral stockée en dur dans le code | |
| V02 | Absence de validation des entrées utilisateur | |
| V03 | Logs contenant des données personnelles | |
| V04 | Interface admin sans authentification forte | |
| V05 | Base de connaissances modifiable sans contrôle | |
| V06 | Absence de rate limiting sur les requêtes | |
| V07 | Messages d'erreur exposant des informations système | |
| V08 | Sauvegarde des conversations sans chiffrement | |
| V09 | Absence de monitoring des tentatives d'injection | |
| V10 | Configuration serveur avec privilèges excessifs | |
| V11 | Absence de validation de l'intégrité des réponses | |
| V12 | Cookies de session sans flags de sécurité | |
| V13 | Communication HTTP non chiffrée | |
| V14 | Absence de procédure de révocation d'accès | |
| V15 | Stockage de métadonnées sans anonymisation | |

### Questions d'analyse pour classification

1. **Quel est votre top 5 des vulnérabilités les plus critiques ?**
2. **Quelles vulnérabilités sont spécifiques aux systèmes IA ?**
3. **Lesquelles peuvent être exploitées sans compétences techniques ?**
4. **Quels sont les liens entre ces vulnérabilités (chaîne d'exploitation) ?**

## 📋 Exercice 3 : Audit de conformité RGPD (10 min)

### Contexte réglementaire

Le chatbot pédagogique traite des données personnelles d'étudiants. Vous devez auditer sa conformité RGPD selon une approche systématique.

### Instructions d'audit

Utilisez la [checklist RGPD 20 points](../ressources/outils-validation/checklist-rgpd-20-points.md) pour auditer le système.

### Checklist de conformité à valider

| Point de contrôle | Conforme | Non-conforme | N/A |
|-------------------|----------|--------------|-----|
| **Base légale** | | | |
| 1. Base légale identifiée pour le traitement | | | |
| 2. Information des utilisateurs sur la finalité | | | |
| 3. Consentement explicite si nécessaire | | | |
| **Droits des personnes** | | | |
| 4. Droit d'accès aux données implémenté | | | |
| 5. Droit de rectification possible | | | |
| 6. Droit à l'effacement (droit à l'oubli) | | | |
| 7. Droit à la portabilité des données | | | |
| **Sécurité technique** | | | |
| 8. Chiffrement des données en transit | | | |
| 9. Chiffrement des données au repos | | | |
| 10. Contrôle d'accès avec authentification forte | | | |
| 11. Journalisation des accès aux données | | | |
| **Gouvernance** | | | |
| 12. Politique de rétention des données définie | | | |
| 13. Procédure de notification de violation | | | |
| 14. Analyse d'impact (AIPD) réalisée si nécessaire | | | |
| 15. DPO consulté ou désigné | | | |
| **Tiers et transferts** | | | |
| 16. Contrat avec Mistral AI conforme RGPD | | | |
| 17. Transferts hors UE sécurisés (adequacy decision) | | | |
| 18. Sous-traitants RGPD-compliant | | | |
| **Documentation** | | | |
| 19. Registre des traitements tenu à jour | | | |
| 20. Politique de confidentialité accessible | | | |

### Questions d'audit RGPD

1. **Quel est votre score de conformité global ?** (X/20)
2. **Quels sont les 3 points de non-conformité les plus critiques ?**
3. **Quelles données personnelles sont traitées par le chatbot ?**
4. **Comment garantir la minimisation des données collectées ?**
5. **Quelles mesures techniques renforcent la privacy by design ?**

## 📊 Livrable : Matrice risque/impact et synthèse

### Matrice risque/impact à compléter

Positionnez chaque menace analysée selon :
- **Axe horizontal** : Probabilité (Faible / Moyenne / Élevée)
- **Axe vertical** : Impact (Faible / Moyen / Élevé)

```
        Impact
    Élevé  |  ?  |  ?  |  ?  |
    Moyen  |  ?  |  ?  |  ?  |
    Faible |  ?  |  ?  |  ?  |
           +-----+-----+-----+
           Faible Moyen Élevé
                Probabilité
```

### Questions de synthèse stratégique

1. **Quelles menaces nécessitent une action immédiate ?** (quadrant élevé/élevé)
2. **Quels risques surveiller régulièrement ?** (quadrant moyen)
3. **Comment prioriser vos investissements sécuritaires ?**
4. **Quel budget sécurité recommandez-vous ?** (% du budget projet)
5. **Quelles compétences sécuritaires développer dans l'équipe ?**

## 🎯 Conclusion de la phase d'analyse

### Livrables attendus

À l'issue de cette phase, vous devez avoir complété :

1. ✅ **Cartographie des 5 menaces principales** avec analyse détaillée
2. ✅ **Classification des 15 vulnérabilités** par criticité
3. ✅ **Audit RGPD** avec score de conformité
4. ✅ **Matrice risque/impact** avec recommandations stratégiques

### Transition vers la Phase 1

Les risques identifiés dans cette phase guideront les tests de sécurité et validations de la Phase 1. Votre analyse servira de référentiel pour prioriser les mesures de protection à implémenter.

## 📚 Ressources pour approfondir

- [Guide ANSSI - Sécurité des systèmes d'IA](https://cyber.gouv.fr) - Référentiel français officiel
- [OWASP Top 10 for LLM Applications](https://owasp.org/www-project-top-10-for-large-language-model-applications/) - Vulnérabilités courantes des LLM
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework) - Framework de gestion des risques IA

[Retour au Module 4](../index.md){ .md-button }
[Continuer vers la Phase 1 : Développement sécurisé](phase1-developpement-securise.md){ .md-button .md-button--primary }