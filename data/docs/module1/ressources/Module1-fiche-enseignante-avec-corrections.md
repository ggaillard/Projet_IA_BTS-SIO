# 📋 Fiche Enseignante - Module 1 : Fondamentaux du Deep Learning

## Présentation générale du module

**Durée totale** : 4 heures  
**Public cible** : Étudiants BTS SIO (débutants en Deep Learning)  
**Prérequis** : Bases en programmation Python, compte Google pour Colab

**Approche pédagogique** : Apprentissage par la pratique d'abord, conceptualisation ensuite

## Objectifs d'apprentissage

À l'issue de ce module, les étudiants seront capables de :
1. Manipuler un réseau de neurones simple via TensorFlow/Keras
2. Distinguer les différences entre Machine Learning classique et Deep Learning
3. Comprendre les concepts fondamentaux (couches, fonction d'activation, propagation)
4. Modifier et analyser un modèle de Deep Learning simple

## Organisation du module

### Phase 1 : Introduction pratique (1h)

#### Objectifs spécifiques
- Créer un premier contact positif avec le Deep Learning
- Manipuler un réseau de neurones sans barrière théorique préalable
- Observer concrètement le fonctionnement et les performances d'un modèle

#### Déroulement et conseils d'animation

| Durée | Activité | Conseils pour l'enseignant |
|-------|----------|----------------------------|
| 15 min | **Démonstrations** applications DL<br>• GitHub Copilot<br>• Reconnaissance d'objets<br>• Génération de texte | • Choisir des exemples spectaculaires et accessibles<br>• Associer les étudiants via questions<br>• Établir des liens avec des applications réelles |
| 30 min | **Manipulation guidée** notebook "Hello World"<br>• Exécution pas à pas<br>• Observation des performances<br>• Premières expérimentations | • S'assurer que tous les étudiants ont accès à Colab<br>• Circuler pour aider aux problèmes techniques<br>• Encourager l'observation et le questionnement |
| 15 min | **Remplissage** fiche d'observations<br>• Analyse des résultats<br>• Documentation des observations | • Insister sur l'importance de la documentation<br>• Encourager la précision des observations<br>• Prévoir un temps de mise en commun |

#### Éléments de correction pour la Fiche d'observations - Phase 1

| Question | Éléments de réponse attendus |
|----------|------------------------------|
| Version de TensorFlow détectée | TensorFlow 2.x (la version exacte dépend de Colab) |
| GPU disponible ? | Oui (généralement dans Colab) |
| Importance du GPU pour le Deep Learning | Accélération considérable de l'entraînement grâce au calcul parallèle des GPU, permettant de traiter des modèles plus grands et plus complexes |
| Nombre d'exemples d'entraînement | 60 000 images |
| Nombre d'exemples de test | 10 000 images |
| Dimension des images | 28×28 pixels (784 pixels au total) |
| Pourquoi normalise-t-on les valeurs? | Pour ramener toutes les valeurs entre 0 et 1, ce qui facilite la convergence du modèle et évite les problèmes numériques |
| Difficultés potentielles | Variabilité des styles d'écriture, similarité entre certains chiffres (ex: 1 et 7, 3 et 8), qualité variable du tracé, positionnement non centré |
| Nombre de couches du modèle | 4-5 couches (entrée, convolutions, pooling, dense, sortie) |
| Nombre total de paramètres | Entre 500 000 et 1 500 000 selon l'architecture exacte |
| Rôle des couches de convolution | Extraction de caractéristiques locales (bords, contours, motifs) indépendamment de leur position |
| Rôle des couches de pooling | Réduction de dimension, invariance aux petites translations, abstraction des caractéristiques |
| Pourquoi utiliser 'softmax'? | Pour obtenir une distribution de probabilités sur les 10 classes (somme = 1) |
| Nombre d'époques | 5-10 généralement |
| Précision sur données d'entraînement | ~99% |
| Précision sur données de validation | ~98% |
| Précision sur l'ensemble de test | ~97-98% |
| Signes de surapprentissage | Écart entre précision d'entraînement et de validation qui se creuse au fil des époques |
| La courbe de précision est-elle croissante? | Oui, avec une augmentation rapide au début puis une stabilisation |
| La courbe de perte est-elle décroissante? | Oui, avec une diminution rapide au début puis une stabilisation |
| Écart entre courbes d'entraînement et validation | Faible à modéré, ce qui indique une bonne généralisation |
| Entraînement suffisant? | Oui, si les courbes se stabilisent. Plus d'époques n'apporterait que peu d'amélioration |

### Phase 2 : Concepts fondamentaux (1h30)

#### Objectifs spécifiques
- Comprendre les différences entre ML classique et Deep Learning
- Explorer l'anatomie d'un réseau de neurones
- Saisir les concepts de forward/backward propagation

#### Déroulement et conseils d'animation

| Durée | Activité | Conseils pour l'enseignant |
|-------|----------|----------------------------|
| 30 min | **Comparaison** ML/DL<br>• Exploration des deux approches<br>• Test sur données normales/bruitées | • Insister sur les différences fondamentales (features engineered vs learned)<br>• Laisser les étudiants découvrir par eux-mêmes les forces/faiblesses |
| 45 min | **Exploration interactive**<br>• Neurone unique<br>• Réseau simple<br>• Visualisation de l'entraînement | • Utiliser des analogies concrètes (ex: neurone comme détecteur de motifs)<br>• Favoriser la manipulation et l'expérimentation<br>• Poser des questions guidées pour la réflexion |
| 15 min | **Schéma conceptuel**<br>• Complétion collaborative<br>• Discussion des concepts | • Synthétiser les observations<br>• Formaliser progressivement les concepts<br>• Vérifier la compréhension par des questions |

#### Éléments de correction pour la Fiche d'observations - Phase 2

**Comparaison Machine Learning vs Deep Learning**

| Aspect observé | Machine Learning (Random Forest) | Deep Learning (CNN) |
|----------------|----------------------------------|---------------------|
| Préparation des données | Nécessite un prétraitement important et une extraction manuelle de caractéristiques | Travaille directement sur les données brutes (pixels) |
| Extraction de caractéristiques | Manuelle, nécessite expertise du domaine | Automatique, apprend les caractéristiques pertinentes |
| Temps d'entraînement | Relativement rapide (quelques secondes à minutes) | Plus long (minutes à heures), nécessite souvent un GPU |
| Précision globale | Bonne (~95-96%) | Excellente (~98-99%) |
| Précision sur données bruitées | Faible à moyenne, sensible au bruit | Bonne, plus robuste aux variations |
| Précision sur données avec rotation | Très faible, ne gère pas les rotations | Modérée à bonne selon l'entraînement |
| Facilité d'implémentation | Plus simple, moins de paramètres à régler | Plus complexe, plus d'hyperparamètres |
| Interprétabilité | Plus interprétable (règles de décision explicites) | Moins interprétable ("boîte noire") |
| Capacité de généralisation | Limitée aux caractéristiques explicites | Meilleure sur des motifs complexes et variations |

**Schéma conceptuel du réseau de neurones**

1. Couche d'entrée (Input Layer)
2. Première couche cachée (Hidden Layer 1)
3. Deuxième couche cachée (Hidden Layer 2)
4. Couche de sortie (Output Layer)
5. Prédiction (Prediction)
6. Calcul de l'erreur (Loss Calculation)
7. Données réelles (Ground Truth)

**Structure du réseau**

1. Type de réseau représenté: Réseau de neurones multicouche (MLP) ou perceptron multicouche

2. Nombre de neurones pour MNIST:
   - Couche d'entrée: 784 (28×28 pixels)
   - Première couche cachée: 128-512 (variable selon architecture)
   - Deuxième couche cachée: 64-256 (variable selon architecture)
   - Couche de sortie: 10 (un neurone par chiffre 0-9)

3. Fonctions d'activation appropriées:
   - Couches cachées: ReLU (Rectified Linear Unit)
   - Couche de sortie: Softmax (pour obtenir des probabilités)

**Processus d'apprentissage**

1. Forward propagation: Les données d'entrée sont propagées à travers le réseau pour produire une prédiction
2. Calcul de l'erreur: Comparaison entre la prédiction et la valeur réelle (ground truth)
3. Backward propagation: L'erreur est propagée en arrière pour calculer les gradients
4. Mise à jour des poids: Les paramètres du réseau sont ajustés pour minimiser l'erreur

### Phase 3 : Mini-projet individuel (1h)

#### Objectifs spécifiques
- Appliquer les connaissances acquises
- Développer une démarche d'amélioration méthodique
- Analyser l'impact des modifications

#### Déroulement et conseils d'animation

| Durée | Activité | Conseils pour l'enseignant |
|-------|----------|----------------------------|
| 15 min | **Préparation** modèle de base<br>• Configuration notebook<br>• Analyse du modèle initial | • Fournir le code de base prêt à l'emploi<br>• Expliquer clairement la structure du projet<br>• Rappeler les points d'observation importants |
| 30 min | **Expérimentation** modifications<br>• Implémentation des changements<br>• Tests et comparaisons | • Suggérer des modifications adaptées au niveau<br>• Encourager la démarche scientifique (hypothèse→test→analyse)<br>• Circuler pour guider sans trop diriger |
| 15 min | **Analyse** des résultats<br>• Documentation des observations<br>• Réflexion sur les améliorations | • Rappeler l'importance de l'analyse critique<br>• Encourager la comparaison entre étudiants<br>• Valoriser les démarches originales |

#### Éléments de correction pour la Fiche d'observations - Phase 3

**Modèle de base**

| Élément | Réponse attendue |
|---------|------------------|
| Architecture | CNN simple avec 1-2 couches de convolution, 1-2 couches de pooling, 1 couche dense et 1 couche de sortie |
| Nombre de paramètres | ~500 000 pour le modèle de base proposé |
| Fonction d'activation | ReLU pour les couches intermédiaires, Softmax pour la sortie |
| Optimiseur | Adam |
| Précision du modèle de base | ~97-98% sur l'ensemble de test |

**Modifications et leurs impacts**

| Modification | Impact attendu |
|--------------|----------------|
| Ajout d'une couche de convolution | Augmentation de la capacité à détecter des motifs plus complexes. Amélioration potentielle de ~0.5-1% de précision. |
| Augmentation du nombre de neurones | Augmentation de la capacité du modèle mais risque de surapprentissage. Amélioration variable selon le niveau de régularisation. |
| Ajout de Dropout | Réduction du surapprentissage, possiblement plus robuste. Peut réduire légèrement la performance sur les données d'entraînement mais améliorer sur les données de test. |
| Changement d'optimiseur | SGD plus lent à converger qu'Adam mais parfois plus stable. Performance finale similaire mais nécessite plus d'époques. |
| Augmentation du nombre d'époques | Amélioration des performances jusqu'à un plateau. Au-delà, risque de surapprentissage. |

**Test sur données bruitées**

| Version | Performances attendues |
|---------|------------------------|
| Modèle de base | ~70-80% sur données bruitées |
| Modèle avec plus de filtres | ~75-85% sur données bruitées |
| Modèle avec Dropout | ~80-90% sur données bruitées (généralement plus robuste) |

**Évaluation des analyses**

Une bonne analyse devrait inclure:
- Identification correcte des modifications ayant le plus d'impact positif
- Compréhension de l'effet du Dropout sur la robustesse
- Observation pertinente des types d'erreurs (ex: confusion entre 3/8, 4/9, etc.)
- Réflexion sur les compromis entre complexité du modèle et performances

## Évaluation et suivi

### Livrables à récupérer
- Fiche d'observations Phase 1 : "Hello World du Deep Learning"
- Fiche d'observations Phase 2 : "Concepts fondamentaux"
- Fiche d'observations Phase 3 : "Mini-projet d'amélioration"

### Critères d'évaluation

| Critère | Indicateurs de réussite |
|---------|------------------------|
| **Manipulation technique** | • Notebook fonctionnel<br>• Modifications correctement implémentées |
| **Compréhension des concepts** | • Explication correcte des éléments du réseau<br>• Schéma conceptuel bien complété |
| **Analyse critique** | • Observations pertinentes sur les performances<br>• Identification correcte des forces/faiblesses |
| **Documentation** | • Fiches d'observations complètes et précises<br>• Justification des choix techniques |

### Barème suggéré (sur 20 points)

| Livrable | Points | Éléments évalués |
|----------|--------|------------------|
| Fiche Phase 1 | 6 pts | • Complétude (3 pts)<br>• Pertinence des observations (3 pts) |
| Fiche Phase 2 | 8 pts | • Tableau comparatif ML/DL (3 pts)<br>• Schéma conceptuel correct (3 pts)<br>• Processus d'apprentissage (2 pts) |
| Fiche Phase 3 | 6 pts | • Modifications implémentées (2 pts)<br>• Analyse des résultats (2 pts)<br>• Pertinence des conclusions (2 pts) |

## Ressources et matériel

### Pour l'enseignant
- Présentations des concepts clés (neurones, couches, fonctions d'activation)
- Solutions complètes des notebooks
- Exemples d'améliorations possibles avec impact attendu
- Glossaire des erreurs courantes et leurs solutions

### Pour les étudiants
- Notebooks pré-configurés
- Fiches d'observations à compléter
- Guide d'utilisation de Google Colab
- Glossaire des termes techniques

## Adaptations possibles

### Pour les étudiants avancés
- Proposer des architectures plus complexes à explorer
- Suggérer des défis supplémentaires (ex: atteindre une précision cible)
- Encourager l'exploration de datasets alternatifs

### Pour les étudiants en difficulté
- Fournir des modèles pré-configurés avec modifications à choisir
- Proposer un travail en binôme
- Simplifier les fiches d'observations avec plus de guidage

## Points de vigilance et conseils

### Difficultés techniques courantes
- Problèmes d'accès à Google Colab → Préparer un environnement de secours
- Temps d'exécution trop long → Réduire taille du dataset ou nombre d'époques
- Erreurs dans le code → Prévoir des checkpoints de code fonctionnel

### Difficultés conceptuelles courantes
- Confusion entre les types de couches → Utiliser des analogies visuelles
- Difficulté à comprendre la backpropagation → Simplifier avec des exemples concrets
- Interprétation des métriques → Fournir des références de comparaison

### Gestion du temps
- Prévoir une marge pour les problèmes techniques
- Adapter le nombre de modifications à tester selon l'avancement
- Préparer des activités "tampons" pour les plus rapides

## Prolongements possibles

- QCM d'auto-évaluation pour vérifier les acquis
- Exercices complémentaires pour renforcer la compréhension
- Suggestions de projets personnels pour prolonger l'apprentissage

---

## Annexe : Concepts clés à aborder

### Vocabulaire essentiel
- Neurone artificiel
- Poids et biais
- Couches (entrée, cachée, sortie)
- Fonction d'activation
- Forward propagation
- Backpropagation
- Gradient descent
- Epoch (époque)
- Batch
- Loss function

### Différences ML vs DL à souligner
- Extraction manuelle vs automatique des caractéristiques
- Processus d'entraînement
- Besoins en données et en calcul
- Domaines d'application privilégiés

### Architectures à présenter
- Perceptron multicouche (MLP)
- Réseau convolutif (CNN) - introduction
- Réseau récurrent (RNN) - mention

## Annexe : FAQ anticipées

**Q: Pourquoi utiliser le Deep Learning plutôt que le Machine Learning classique ?**  
R: Le Deep Learning excelle pour les données complexes (images, texte, son) où l'extraction manuelle de caractéristiques est difficile. Il peut apprendre des représentations hiérarchiques des données.

**Q: Comment choisir le nombre de couches et de neurones ?**  
R: C'est souvent empirique. Plus le problème est complexe, plus le réseau doit être profond. On commence généralement avec des architectures standard puis on ajuste.

**Q: Pourquoi normaliser les données d'entrée ?**  
R: Pour homogénéiser les échelles et faciliter la convergence de l'entraînement. Des valeurs trop disparates peuvent causer des instabilités numériques.

**Q: Comment éviter le surapprentissage (overfitting) ?**  
R: Techniques de régularisation comme le dropout, l'augmentation de données, l'arrêt précoce (early stopping).

**Q: Quel matériel est nécessaire pour faire du Deep Learning ?**  
R: Pour l'apprentissage, un GPU est souvent nécessaire. Pour ce TP, Google Colab fournit gratuitement l'accès à des GPUs.