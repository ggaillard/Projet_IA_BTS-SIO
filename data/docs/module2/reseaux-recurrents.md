# 🔍 Phase 2 : Mini-projet RNN pour le traitement du langage

![RNN Architecture](https://images.unsplash.com/photo-1498050108023-c5249f4df085?auto=format&fit=crop&q=80&w=1000&h=300)

## 🎯 Objectifs de la phase

Dans cette phase, vous allez :

- Comprendre les principes des réseaux récurrents (RNN) et de leurs variantes (LSTM, GRU)
- Implémenter un modèle LSTM pour l'analyse de sentiment
- Visualiser et interpréter le fonctionnement interne d'un RNN
- Analyser les performances du modèle sur des données textuelles

## 🧩 Partie 1: Principes des RNN (20 min)

### 📊 Architecture et fonctionnement des RNN

Les réseaux de neurones récurrents (RNN) sont conçus spécifiquement pour traiter des données séquentielles comme le texte, les séries temporelles ou les données audio. Contrairement aux réseaux classiques qui traitent chaque entrée indépendamment, les RNN maintiennent un "état interne" qui leur permet de se souvenir des informations précédentes.

### Problématique : Pourquoi les RNN ?

Imaginons que vous surveillez des logs de sécurité :
- Un réseau classique ne verrait que des entrées isolées, sans comprendre leur séquence
- Un RNN, lui, se souvient des événements précédents pour détecter des patterns suspects

### Le RNN expliqué avec l'analogie du carnet de notes

**Analogie du carnet de notes** :
1. Vous analysez un rapport d'incident et prenez des notes importantes
2. À chaque nouvelle section du rapport, vous :
   - Lisez le nouveau contenu (nouvelle entrée)
   - Consultez vos notes précédentes (état caché / mémoire)
   - Mettez à jour vos notes avec les informations les plus pertinentes
   - Utilisez la combinaison de la nouvelle section et de vos notes pour comprendre l'incident

**Dans un RNN** :
1. Le réseau traite les données séquentiellement (mot par mot, événement par événement)
2. À chaque étape, il combine :
   - L'entrée actuelle (ex : le mot actuel)
   - Son "état de mémoire" (ce qu'il a retenu des mots précédents)
3. Il produit :
   - Une sortie pour l'étape actuelle (ex: prédiction partielle)
   - Un nouvel état de mémoire pour l'étape suivante

**Avantages pour un développeur d'applications** :
- Traitement de séquences de longueur variable
- Capacité à "mémoriser" des informations importantes
- Applications diverses : analyse de texte, traduction, génération de contenu

## Les LSTM (Long Short-Term Memory) en langage simple

### Solution au problème de mémoire

Les RNN classiques ont du mal à retenir les informations sur de longues séquences - c'est le problème du "gradient qui s'évanouit". Les cellules LSTM ont été conçues pour résoudre ce problème.

**Analogie du rapport de sécurité avec système de marquage** :
- Vous avez maintenant un système pour marquer les informations importantes dans votre rapport
- Vous pouvez décider explicitement quelles informations :
  * Méritent d'être conservées pour l'analyse finale
  * Doivent être mises à jour avec de nouvelles données
  * Sont pertinentes pour l'incident en cours

### Les portes (gates) expliquées simplement

Au lieu d'une explication mathématique complexe, voici le fonctionnement en langage simple :

1. **Porte d'oubli** (Forget gate) : 
   
    - Comme un tri dans votre rapport : "Quelles informations passées ne sont plus utiles ?"
    - Exemple SIO : Si un nouvel utilisateur se connecte, vous pouvez "oublier" certains détails des sessions précédentes

2. **Porte d'entrée** (Input gate) :
   
    - Filtre les nouvelles informations : "Quelles nouvelles informations sont importantes ?"
    - Exemple SIO : Dans un log "Tentative d'accès admin échouée 5 fois", le nombre de tentatives est plus important que l'heure exacte

3. **Porte de sortie** (Output gate) :
   
    - Décide quelles informations partager : "Quelles parties de ma mémoire sont pertinentes maintenant ?"
    - Exemple SIO : Si vous analysez une faille de sécurité, vous vous concentrez sur les logs d'authentification, pas sur les mises à jour système

### Applications pour les étudiants BTS SIO

Voici des applications concrètes des RNN/LSTM dans votre domaine :

1. **Détection d'intrusion réseau** :
   
    - Les RNN/LSTM analysent les séquences de logs pour détecter des comportements anormaux
    - L'ordre chronologique des événements est crucial (d'où l'intérêt des RNN)

2. **Prédiction de pannes systèmes** :
   
    - Les LSTM peuvent analyser les historiques de performance serveur
    - Ils détectent les signes précurseurs de problèmes potentiels

3. **Chatbots d'assistance technique** :
   
    - Les RNN/LSTM permettent de comprendre le contexte d'une conversation de support
    - Ils maintiennent la cohérence dans les réponses du chatbot d'aide

4. **Analyse de logs de sécurité** :
   
    - Les LSTM peuvent identifier des patterns d'attaque complexes s'étendant sur de longues périodes
    - Ils peuvent corréler des événements apparemment sans lien

## 🔬 Partie 2: Implémentation d'un LSTM pour l'analyse de sentiment (40 min)

### Instructions

Pour cette partie pratique, vous allez explorer l'analyse de sentiment avec un modèle LSTM. Cette activité vous permettra de comprendre comment les réseaux récurrents traitent et "comprennent" le texte.

1. Ouvrez le notebook Jupyter [rnn-sequence.ipynb](ressources/rnn-sequence.ipynb) dans Google Colab
2. Suivez les instructions étape par étape pour implémenter un modèle LSTM pour l'analyse de sentiment
3. Exécutez chaque cellule et observez les résultats
4. Portez une attention particulière aux sections suivantes :
   
    - Prétraitement du texte (tokenisation)
    - Architecture du modèle LSTM
    - Visualisation des embeddings de mots
    - Analyse des performances et des erreurs

### Points clés à explorer

Pendant que vous travaillez sur ce notebook, réfléchissez aux questions suivantes qui feront l'objet d'une discussion en classe et d'une documentation à produire :

- **Comment le texte est-il transformé en entrées numériques pour le réseau ?**
  Observez le processus de tokenisation, la création du vocabulaire et la conversion en séquences d'indices.

- **Comment les cellules LSTM gèrent-elles l'information à long terme ?**
  Analysez l'architecture des cellules LSTM et leur capacité à mémoriser les informations pertinentes.

- **Quelle est la différence entre les embeddings de mots positifs et négatifs ?**
  Examinez la visualisation des embeddings et comment les mots de sentiments similaires se regroupent.

- **Comment le modèle LSTM peut-il comprendre le contexte d'une phrase ?**
  Réfléchissez à la manière dont l'ordre des mots et leurs relations sont capturés par le modèle.

- **Quelles sont les limitations de cette approche pour l'analyse de sentiment ?**
  Identifiez les cas où le modèle échoue et pourquoi (ironie, sarcasme, expressions idiomatiques).

- **Comment pourriez-vous améliorer ce modèle pour des tâches plus complexes ?**
  Proposez des modifications architecturales ou des techniques d'amélioration des données.

### 📋 Livrable attendu

À la fin de cette activité, vous devrez produire une documentation synthétique (1-2 pages) répondant aux questions ci-dessus. Ce document servira de référence pour votre compréhension des RNN/LSTM et pourra être intégré dans la base de connaissances de votre chatbot pédagogique.

Un document de référence complet sur ces concepts est disponible [ici](ressources/lstm-sentiment-analyse.md) pour vous aider à approfondir votre compréhension.

## 🔄 Partie 3: Application pratique et test avec Mistral AI (15 min)

### Mise en pratique avec l'API Mistral

Cette dernière partie vous permettra de comparer votre modèle LSTM avec les capacités d'un grand modèle de langage moderne.

1. Utilisez l'API Mistral AI pour réaliser des analyses de sentiment sur vos propres phrases test
2. Comparez les résultats obtenus avec ceux de votre modèle LSTM
3. Identifiez les différences en termes de nuances comprises et de précision

### Points de discussion

- Quelles sont les différences fondamentales entre un modèle LSTM et un LLM comme Mistral ?
- Dans quels cas le LSTM fonctionne-t-il mieux ? Dans quels cas Mistral est-il supérieur ?
- Comment les deux approches pourraient-elles être combinées dans un système réel ?

## 📋 Fiche d'observations à compléter

Durant toute cette phase sur les RNN, n'oubliez pas de compléter votre [fiche d'observations](ressources/Partie2-Phase2-fiche-observationsRNN.md) qui sera votre livrable principal pour cette partie du module.

## 📚 Conclusion et transition

Cette section sur les réseaux récurrents vous a permis de comprendre une autre architecture fondamentale du Deep Learning, particulièrement adaptée aux données séquentielles comme le texte ou les séries temporelles. 

Vous avez appris à:

- Reconnaître les situations où les RNN/LSTM sont particulièrement adaptés
- Comprendre les mécanismes de mémoire qui font la force de ces architectures
- Implémenter un modèle LSTM pour l'analyse de sentiment de texte
- Visualiser et interpréter les représentations internes du modèle

Ces connaissances constitueront une base essentielle pour le développement de votre projet de chatbot pédagogique dans les prochains modules.

[Retour au Module 2](index.md){ .md-button }
[Continuer vers l'auto-évaluation](qcm-evaluation-module2.md){ .md-button .md-button--primary }