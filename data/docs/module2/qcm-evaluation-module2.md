# 📝 QCM d'auto-évaluation - Module 2 : Architectures spécialisées

Ce QCM vous permettra d'évaluer votre compréhension des réseaux convolutifs (CNN) et récurrents (RNN) étudiés dans ce module.

## ✅ Instructions
- Cochez la ou les réponses correctes pour chaque question
- Certaines questions peuvent avoir plusieurs réponses correctes
- Pour les questions à choix multiples, 0,5 point est attribué par réponse correcte (maximum 1 point par question)
- À la fin du questionnaire, calculez votre score grâce au corrigé fourni
- Durée recommandée : 15 minutes

## 🔍 Partie A : Réseaux Convolutifs (CNN)

### 1. Dans un réseau convolutif, à quoi sert principalement l'opération de convolution ?
- [ ] À réduire la dimension des données
- [ ] À détecter des caractéristiques locales dans les données d'entrée
- [ ] À connecter tous les neurones entre eux
- [ ] À accélérer le temps d'entraînement

### 2. Qu'est-ce qu'un filtre (ou noyau) dans un CNN ?
- [ ] Une fonction qui supprime les pixels indésirables de l'image
- [ ] Une matrice de poids qui s'applique localement sur les données d'entrée
- [ ] Un seuil qui élimine les valeurs en dessous d'un certain niveau
- [ ] Une technique pour sélectionner les meilleures images d'entraînement

### 3. Quel est le rôle principal de l'opération de pooling dans un CNN ?
- [ ] Augmenter la taille des feature maps
- [ ] Réduire la dimensionnalité tout en préservant les informations importantes
- [ ] Ajouter de la non-linéarité au réseau
- [ ] Connecter les différentes couches de convolution

### 4. Quels sont les avantages des CNN pour le traitement d'images ? (plusieurs réponses possibles)
- [ ] Partage des paramètres entre différentes positions spatiales
- [ ] Invariance à la translation
- [ ] Réduction significative du nombre de paramètres par rapport aux réseaux entièrement connectés
- [ ] Capacité à traiter des images de n'importe quelle taille sans redimensionnement

### 5. Dans quelle couche d'un CNN typique se trouvent généralement le plus grand nombre de paramètres ?
- [ ] Couches de convolution
- [ ] Couches de pooling
- [ ] Couches entièrement connectées (fully connected)
- [ ] Couches de normalisation par lots (batch normalization)

### 6. Qu'est-ce qu'une feature map dans un CNN ?
- [ ] Une carte qui indique les régions d'intérêt dans l'image originale
- [ ] Le résultat de l'application d'un filtre de convolution sur une entrée
- [ ] Un graphique montrant la progression de l'entraînement
- [ ] La liste des caractéristiques extraites manuellement avant l'entraînement

### 7. Comment évoluent les caractéristiques détectées à mesure qu'on avance dans les couches d'un CNN ?
- [ ] Elles deviennent de plus en plus simples et élémentaires
- [ ] Elles restent de même nature mais deviennent plus précises
- [ ] Elles deviennent de plus en plus abstraites et complexes
- [ ] Elles concernent des régions de plus en plus petites de l'image

## 🧩 Partie B : Réseaux Récurrents (RNN)

### 8. Quelle est la principale caractéristique des réseaux de neurones récurrents (RNN) ?
- [ ] Ils utilisent des opérations de convolution pour traiter les données
- [ ] Ils contiennent des connexions formant des boucles permettant de mémoriser les informations
- [ ] Ils traitent chaque élément d'une séquence de manière complètement indépendante
- [ ] Ils sont spécialisés dans le traitement d'images

### 9. Pour quels types de données les RNN sont-ils particulièrement adaptés ?
- [ ] Images 2D
- [ ] Données tabulaires (comme des tableaux Excel)
- [ ] Données séquentielles (texte, séries temporelles, audio)
- [ ] Nuages de points 3D

### 10. Quel problème majeur affecte les RNN classiques lors du traitement de séquences longues ?
- [ ] Surconsommation de mémoire
- [ ] Temps de traitement exponentiel
- [ ] Problème de disparition ou d'explosion du gradient
- [ ] Incapacité à paralléliser les calculs

### 11. Quelle est la principale innovation des cellules LSTM par rapport aux RNN classiques ?
- [ ] Elles utilisent des opérations de convolution
- [ ] Elles possèdent des mécanismes de portes contrôlant le flux d'information
- [ ] Elles peuvent traiter plusieurs séquences en parallèle
- [ ] Elles ne nécessitent pas d'entraînement

### 12. Dans un réseau LSTM, à quoi sert la "porte d'oubli" (forget gate) ?
- [ ] À déterminer quelles informations de l'état précédent doivent être conservées ou supprimées
- [ ] À réinitialiser complètement le réseau quand la séquence est trop longue
- [ ] À sauter certaines étapes de calcul pour accélérer le traitement
- [ ] À ignorer les données d'entrée corrompues ou bruitées

### 13. Quelles applications typiques utilisent les RNN/LSTM ? (plusieurs réponses possibles)
- [ ] Reconnaissance de caractères manuscrits
- [ ] Traduction automatique
- [ ] Prédiction de séries temporelles
- [ ] Génération de texte
- [ ] Segmentation d'images

### 14. Qu'est-ce qui différencie principalement les GRU (Gated Recurrent Units) des LSTM ?
- [ ] Les GRU n'ont aucune forme de mémoire
- [ ] Les GRU ont une architecture plus simple avec moins de portes
- [ ] Les GRU sont spécifiquement conçus pour les données non séquentielles
- [ ] Les GRU ne peuvent pas être entraînés par rétropropagation

## 📊 Partie C : Comparaison et applications

### 15. Dans quel contexte choisiriez-vous un CNN plutôt qu'un RNN ?
- [ ] Pour l'analyse de sentiment dans des avis clients
- [ ] Pour la prédiction de cours boursiers
- [ ] Pour la détection de visages dans des photos
- [ ] Pour la traduction automatique de texte

### 16. Quelles sont les principales différences entre CNN et RNN ? (plusieurs réponses possibles)
- [ ] Les CNN traitent mieux les relations spatiales, les RNN les relations temporelles
- [ ] Les CNN ont généralement plus de paramètres que les RNN
- [ ] Les CNN sont plus faciles à paralléliser que les RNN
- [ ] Les CNN utilisent le concept d'état caché, contrairement aux RNN

### 17. Quelle architecture serait la plus adaptée pour l'analyse de logs système à des fins de sécurité ?
- [ ] Un CNN simple
- [ ] Un LSTM ou un GRU
- [ ] Un réseau densément connecté (MLP)
- [ ] Un réseau de neurones à convolution 1D

### 18. Quel modèle a-t-il tendance à être le plus efficace en termes de temps d'entraînement ?
- [ ] Les CNN sont généralement plus rapides à entraîner que les RNN
- [ ] Les RNN sont généralement plus rapides à entraîner que les CNN
- [ ] Les LSTM sont plus rapides à entraîner que les GRU
- [ ] Le temps d'entraînement est similaire pour toutes ces architectures

## Auto-évaluation

Une fois le QCM complété, vérifiez vos réponses avec le corrigé ci-dessous et calculez votre score.

### Corrigé avec explications

1. **b - À détecter des caractéristiques locales dans les données d'entrée**  
   *L'opération de convolution permet de détecter des motifs locaux dans l'image comme des bords, des textures ou des formes, grâce à des filtres qui balaient l'image.*

2. **b - Une matrice de poids qui s'applique localement sur les données d'entrée**  
   *Un filtre (ou noyau) est une petite matrice de poids qui est déplacée sur l'image pour détecter des motifs spécifiques par le calcul du produit de convolution.*

3. **b - Réduire la dimensionnalité tout en préservant les informations importantes**  
   *Le pooling réduit la taille des feature maps en conservant les informations les plus pertinentes, ce qui diminue le temps de calcul et rend le modèle plus robuste aux variations.*

4. **a, b, c - Partage des paramètres entre différentes positions spatiales, Invariance à la translation, Réduction significative du nombre de paramètres**  
   *Les CNN partagent les mêmes poids sur toute l'image (a), peuvent reconnaître des objets quelle que soit leur position (b) et utilisent beaucoup moins de paramètres que les réseaux entièrement connectés (c). Ils nécessitent cependant que les images soient redimensionnées à une taille fixe (d est incorrect).*

5. **c - Couches entièrement connectées (fully connected)**  
   *Dans un CNN typique, ce sont les couches entièrement connectées qui contiennent le plus grand nombre de paramètres, car chaque neurone est connecté à tous les neurones de la couche précédente.*

6. **b - Le résultat de l'application d'un filtre de convolution sur une entrée**  
   *Une feature map est la sortie obtenue après l'application d'un filtre de convolution sur les données d'entrée, représentant l'activation du filtre à chaque position.*

7. **c - Elles deviennent de plus en plus abstraites et complexes**  
   *Dans les premières couches, les CNN détectent des éléments simples comme des bords et des contours. Plus on avance dans le réseau, plus les caractéristiques détectées deviennent abstraites et complexes (formes, parties d'objets, objets entiers).*

8. **b - Ils contiennent des connexions formant des boucles permettant de mémoriser les informations**  
   *La particularité des RNN est leur structure avec des connexions cycliques, ce qui permet à l'information de persister d'une étape de traitement à l'autre.*

9. **c - Données séquentielles (texte, séries temporelles, audio)**  
   *Les RNN sont particulièrement adaptés aux données où l'ordre et le contexte sont importants, comme le texte, l'audio ou les séries temporelles.*

10. **c - Problème de disparition ou d'explosion du gradient**  
    *Lors de l'entraînement sur des séquences longues, les RNN souffrent du problème du gradient qui s'évanouit (ou explose), ce qui les empêche d'apprendre les dépendances à long terme.*

11. **b - Elles possèdent des mécanismes de portes contrôlant le flux d'information**  
    *Les LSTM introduisent un système de portes (forget, input, output) qui contrôle quelles informations sont conservées, mises à jour ou transmises, résolvant ainsi le problème du gradient qui s'évanouit.*

12. **a - À déterminer quelles informations de l'état précédent doivent être conservées ou supprimées**  
    *La porte d'oubli (forget gate) décide quelles informations de l'état précédent sont pertinentes et doivent être conservées, et lesquelles peuvent être écartées.*

13. **b, c, d - Traduction automatique, Prédiction de séries temporelles, Génération de texte**  
    *Les RNN/LSTM excellent dans les tâches séquentielles comme la traduction, la prédiction de séries temporelles et la génération de texte. La reconnaissance de caractères et la segmentation d'images sont plutôt des domaines de prédilection des CNN.*

14. **b - Les GRU ont une architecture plus simple avec moins de portes**  
    *Les GRU sont une version simplifiée des LSTM avec seulement deux portes au lieu de trois, ce qui les rend généralement plus rapides à entraîner mais potentiellement moins puissants sur certaines tâches.*

15. **c - Pour la détection de visages dans des photos**  
    *La détection d'objets dans des images est une tâche idéale pour un CNN. Les autres options concernent des données séquentielles, mieux traitées par les RNN.*

16. **a, c - Les CNN traitent mieux les relations spatiales, les RNN les relations temporelles; Les CNN sont plus faciles à paralléliser que les RNN**  
    *Les CNN sont spécialisés dans les motifs spatiaux, les RNN dans les séquences temporelles (a). Les CNN peuvent traiter une image entière en parallèle, tandis que les RNN sont intrinsèquement séquentiels (c). Les RNN n'ont généralement pas plus de paramètres que les CNN (b est incorrect). Ce sont les RNN qui utilisent un état caché, pas les CNN (d est incorrect).*

17. **b - Un LSTM ou un GRU**  
    *L'analyse de logs système implique des séquences d'événements où l'ordre et le contexte temporel sont cruciaux, ce qui correspond parfaitement aux capacités des LSTM/GRU.*

18. **a - Les CNN sont généralement plus rapides à entraîner que les RNN**  
    *Les CNN peuvent être hautement parallélisés, contrairement aux RNN qui sont séquentiels par nature, ce qui rend généralement l'entraînement des CNN plus rapide pour des volumes de données comparables.*

### Calcul de votre score
- Questions à choix unique (1-3, 5-12, 14-15, 17-18) : 1 point par réponse correcte
- Questions à choix multiples (4, 13, 16) : 0,5 point par réponse correcte et -0,25 par réponse incorrecte (minimum 0, maximum 1 point par question)

**Total des points possibles : 18**

### Interprétation
- **14-18 points** : Excellente maîtrise des architectures spécialisées de Deep Learning
- **10-13 points** : Bonne compréhension, quelques points à clarifier
- **6-9 points** : Compréhension de base, révision nécessaire de certains concepts
- **0-5 points** : Révision approfondie recommandée avant de poursuivre

## Pour approfondir
Si vous avez obtenu moins de 14 points, nous vous recommandons de revoir les concepts sur lesquels vous avez fait des erreurs. Consultez les ressources suivantes :

  - Les notebooks [CNN pour classification](ressources/cnn-classification.md) et [RNN pour analyse de sentiment](ressources/rnn-sequence.md)
  - Les sections explicatives sur les [réseaux convolutifs](reseaux-convolutifs.md) et les [réseaux récurrents](reseaux-recurrents.md)
  - La [synthèse des architectures spécialisées](ressources/synthese-module2.md)
  - Le [glossaire des termes du Deep Learning](../module1/ressources/glossaire-dl.md)

[Retour au Module 2](index.md){ .md-button }
[Continuer vers le Module 3](../module3/index.md){ .md-button .md-button--primary }