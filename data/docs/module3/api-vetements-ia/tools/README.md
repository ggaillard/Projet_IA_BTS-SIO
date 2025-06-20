# Outils pour le modèle de classification de vêtements

Ce dossier contient des scripts utilitaires pour la création et la gestion du modèle de deep learning utilisé dans ce projet.

## Script `create_model.py`

### Objectif
Ce script permet de créer et d'entraîner un modèle de classification de vêtements basé sur MobileNetV2, en utilisant le jeu de données Fashion MNIST.

### Fonctionnement
1. Téléchargement automatique du jeu de données Fashion MNIST
2. Préparation des données (redimensionnement, conversion en RGB)
3. Chargement de MobileNetV2 pré-entraîné sur ImageNet
4. Adaptation du modèle pour la classification de vêtements (transfer learning)
5. Entraînement rapide du modèle
6. Évaluation et sauvegarde du modèle

### Exécution
```bash
# Depuis le dossier tools/
python create_model.py

```
### Prérequis

- TensorFlow 2.x
- Connexion internet : pour télécharger MobileNetV2 pré-entraîné
- RAM : minimum 4 Go
- Temps d'exécution estimé : 5-10 minutes (CPU), 2-3 minutes (GPU)

### Note importante

 - Ce script est fourni à des fins pédagogiques pour comprendre comment le modèle a été créé. 
 - Le modèle final est déjà inclus dans l'archive du projet dans le dossier `models/pretrained_model/`, donc vous n'avez pas besoin d'exécuter ce script pour utiliser l'application.