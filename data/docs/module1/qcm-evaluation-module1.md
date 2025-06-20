# 📝 QCM d'auto-évaluation - Module 1 : Fondamentaux du Deep Learning

Ce QCM vous permettra d'évaluer votre compréhension des concepts fondamentaux du Deep Learning vus durant cette première séance.

## ✅ Instructions
- Cochez la ou les réponses correctes pour chaque question
- Certaines questions peuvent avoir plusieurs réponses correctes
- Pour les questions à choix multiples, 0,5 point est attribué par réponse correcte (maximum 1 point par question)
- À la fin du questionnaire, calculez votre score grâce au corrigé fourni
- Durée recommandée : 20 minutes

## 🔍 Partie 1 : Introduction pratique

### 1. Dans le "Hello World" du Deep Learning avec MNIST, que représentent les données d'entrée ?
- [ ] Des échantillons de texte manuscrit
- [ ] Des images de chiffres manuscrits de 0 à 9
- [ ] Des enregistrements audio de chiffres prononcés
- [ ] Des coordonnées de points représentant des chiffres

### 2. Lors de la normalisation des données d'image MNIST, pourquoi divise-t-on les valeurs des pixels par 255 ?
- [ ] Pour compresser les images et économiser de la mémoire
- [ ] Pour ramener toutes les valeurs entre 0 et 1
- [ ] Pour augmenter la vitesse de traitement
- [ ] Pour convertir les images en noir et blanc

### 3. Parmi ces applications, laquelle n'est PAS un exemple typique de Deep Learning présenté dans l'introduction pratique ?
- [ ] GitHub Copilot pour la complétion de code
- [ ] Reconnaissance d'objets en temps réel 
- [ ] Génération de texte contextuel
- [ ] Analyse statistique de données tabulaires

### 4. Lors de l'expérimentation avec le modèle MNIST, quel paramètre a le plus d'influence sur le temps d'entraînement ?
- [ ] Le nombre d'époques
- [ ] La taille du batch
- [ ] Le type de fonction d'activation
- [ ] Le nombre de classes de sortie

### 5. Quels sont les avantages observés du Deep Learning dans votre première expérience pratique ? (plusieurs réponses possibles)
- [ ] Capacité à traiter directement des images brutes
- [ ] Pas besoin de prétraitement des données
- [ ] Apprentissage automatique des caractéristiques importantes
- [ ] Reconnaissance robuste malgré des variations dans les entrées
- [ ] Facilité d'implémentation et d'entraînement

## 🧩 Partie 2 : Concepts fondamentaux

### 6. Quelle est la principale différence entre le Machine Learning classique et le Deep Learning concernant les caractéristiques (features) ?
- [ ] Le Machine Learning classique fonctionne avec moins de données
- [ ] Le Deep Learning extrait automatiquement les caractéristiques pertinentes
- [ ] Le Machine Learning classique ne nécessite pas de phase d'entraînement
- [ ] Le Deep Learning demande moins de puissance de calcul

### 7. Quels sont les composants fondamentaux d'un réseau de neurones ? (plusieurs réponses possibles)
- [ ] Neurones
- [ ] Poids et connexions
- [ ] Fonctions d'activation
- [ ] Instructions conditionnelles
- [ ] Biais

### 8. Dans un réseau de neurones, qu'est-ce qu'une "couche cachée" ?
- [ ] Une couche qui n'est pas visible dans le code
- [ ] Une couche située entre la couche d'entrée et la couche de sortie
- [ ] Une couche qui ne s'active que dans certaines conditions
- [ ] Une couche utilisée uniquement pendant la phase de test

### 9. En observant le schéma d'un neurone artificiel, quelles opérations mathématiques sont appliquées dans l'ordre correct ?
- [ ] Multiplication → Addition → Fonction d'activation
- [ ] Addition → Multiplication → Fonction d'activation
- [ ] Fonction d'activation → Multiplication → Addition
- [ ] Multiplication → Fonction d'activation → Addition

### 10. Lors de la comparaison entre Machine Learning classique et Deep Learning sur des données bruitées, qu'avez-vous observé ?
- [ ] Les deux approches ont des performances similaires
- [ ] Le Machine Learning classique est plus robuste au bruit
- [ ] Le Deep Learning maintient généralement de meilleures performances
- [ ] Les deux approches échouent complètement avec des données bruitées

## 🛠️ Partie 3 : Mini-projet individuel

### 11. Dans le mini-projet, quelle modification a généralement le plus d'impact positif sur les performances du modèle CNN ?
- [ ] Ajouter une couche de convolution supplémentaire
- [ ] Augmenter simplement le nombre de neurones dans les couches existantes
- [ ] Changer l'optimiseur d'Adam à SGD
- [ ] Réduire le nombre d'époques d'entraînement

### 12. Quel est l'effet principal de l'ajout d'une couche de Dropout dans un modèle de Deep Learning ?
- [ ] Accélération de l'entraînement
- [ ] Réduction du surapprentissage (overfitting)
- [ ] Amélioration des performances sur les données complexes
- [ ] Simplification de l'architecture du réseau

### 13. Analysez ce graphique d'entraînement. Quelle affirmation est correcte ?

```
Précision
^
|
|      ****     *******
|    **               ******
|   *                        ******
|  *
| *
|*
+---------------------------------> Époques
  — Entraînement   .... Validation
```

- [ ] Le modèle n'apprend pas correctement
- [ ] Le modèle souffre de surapprentissage
- [ ] Le modèle souffre de sous-apprentissage
- [ ] Le modèle généralise parfaitement

### 14. Lors du test du modèle sur des données bruitées, quelle modification tend à améliorer le plus la robustesse ?
- [ ] Augmentation du nombre d'époques
- [ ] Ajout de couches de Dropout
- [ ] Réduction du nombre de neurones
- [ ] Changement de la fonction d'activation

### 15. Quelle relation décrit le mieux le lien entre les trois phases du Module 1 ?
- [ ] Chaque phase est indépendante et peut être étudiée séparément
- [ ] La Phase 1 fournit l'expérience pratique, la Phase 2 explique les concepts, et la Phase 3 applique ces connaissances
- [ ] Les phases doivent obligatoirement être suivies dans l'ordre pour comprendre le Deep Learning
- [ ] Les phases représentent trois approches alternatives pour apprendre le Deep Learning

## Auto-évaluation

Une fois le QCM complété, vérifiez vos réponses avec le corrigé ci-dessous et calculez votre score.

### Corrigé avec explications

1. **b - Des images de chiffres manuscrits de 0 à 9**  
   *Le dataset MNIST contient 70 000 images en niveaux de gris de chiffres manuscrits, format standard pour débuter en Deep Learning.*

2. **b - Pour ramener toutes les valeurs entre 0 et 1**  
   *La normalisation des valeurs de pixels (qui sont initialement entre 0 et 255) permet de stabiliser l'entraînement et d'accélérer la convergence du modèle.*

3. **d - Analyse statistique de données tabulaires**  
   *C'est typiquement un cas où le Machine Learning classique est plus approprié que le Deep Learning. Les autres options sont des applications typiques de Deep Learning présentées dans l'introduction.*

4. **a - Le nombre d'époques**  
   *Une époque représente un passage complet sur toutes les données d'entraînement. Augmenter le nombre d'époques multiplie proportionnellement le temps d'entraînement.*

5. **a, c, d - Capacité à traiter directement des images brutes, Apprentissage automatique des caractéristiques importantes, Reconnaissance robuste malgré des variations dans les entrées**  
   *Le Deep Learning requiert généralement un prétraitement (normalisation), donc b est incorrect. Il n'est pas nécessairement plus facile à implémenter que le ML classique, donc e est incorrect.*

6. **b - Le Deep Learning extrait automatiquement les caractéristiques pertinentes**  
   *C'est la différence fondamentale : le ML classique nécessite une extraction manuelle des caractéristiques alors que le DL les apprend automatiquement à partir des données brutes.*

7. **a, b, c, e - Neurones, Poids et connexions, Fonctions d'activation, Biais**  
   *Les instructions conditionnelles ne font pas partie de la structure standard d'un réseau de neurones.*

8. **b - Une couche située entre la couche d'entrée et la couche de sortie**  
   *Les couches cachées sont responsables de l'extraction progressive des caractéristiques et sont situées entre l'entrée et la sortie du réseau.*

9. **a - Multiplication → Addition → Fonction d'activation**  
   *Dans un neurone artificiel, on multiplie d'abord les entrées par les poids, puis on additionne ces produits avec le biais, et enfin on applique la fonction d'activation.*

10. **c - Le Deep Learning maintient généralement de meilleures performances**  
    *Grâce à sa capacité à extraire des caractéristiques hiérarchiques complexes, le Deep Learning est souvent plus robuste aux variations et au bruit dans les données.*

11. **a - Ajouter une couche de convolution supplémentaire**  
    *Cette modification permet au réseau d'extraire des caractéristiques plus complexes et plus abstraites, améliorant généralement les performances sur MNIST.*

12. **b - Réduction du surapprentissage (overfitting)**  
    *Le Dropout désactive aléatoirement des neurones pendant l'entraînement, ce qui empêche le réseau de trop s'adapter aux données d'entraînement et améliore la généralisation.*

13. **b - Le modèle souffre de surapprentissage**  
    *Le graphique montre que la précision sur les données d'entraînement continue d'augmenter alors que celle sur les données de validation commence à diminuer, signe classique de surapprentissage.*

14. **b - Ajout de couches de Dropout**  
    *Le Dropout améliore la robustesse du modèle en le forçant à ne pas dépendre excessivement de certains neurones, ce qui le rend plus performant sur des données bruitées ou légèrement différentes.*

15. **b - La Phase 1 fournit l'expérience pratique, la Phase 2 explique les concepts, et la Phase 3 applique ces connaissances**  
    *Cette structure suit l'approche pédagogique du module : pratique d'abord, conceptualisation ensuite, et application finale dans un projet.*

### Calcul de votre score
- Questions à choix unique (1-4, 6, 8-15) : 1 point par réponse correcte
- Questions à choix multiples (5, 7) : 0,5 point par réponse correcte et -0,25 par réponse incorrecte (minimum 0, maximum 1 point par question)

**Total des points possibles : 15**

### Interprétation
- **12-15 points** : Excellente maîtrise des concepts fondamentaux du Deep Learning
- **9-11 points** : Bonne compréhension, quelques points à clarifier
- **6-8 points** : Compréhension de base, révision nécessaire de certains concepts
- **0-5 points** : Révision approfondie recommandée avant de poursuivre

## Pour approfondir
Si vous avez obtenu moins de 12 points, nous vous recommandons de revoir les concepts sur lesquels vous avez fait des erreurs. Consultez les ressources suivantes :

  - Le notebook ["Hello World du Deep Learning"](../module1/ressources/hello-world-dl.md) (Phase 1)
  - La section ["Concepts fondamentaux"](../module1/concepts-fondamentaux.md) du cours (Phase 2)
  - La ["fiche d'observations du mini-projet d'amélioration"](../module1/ressources/Partie1-Phase3-fiche-observations.md) (Phase 3)
  - Le [glossaire des termes du Deep Learning](../module1/ressources/glossaire-dl.md)