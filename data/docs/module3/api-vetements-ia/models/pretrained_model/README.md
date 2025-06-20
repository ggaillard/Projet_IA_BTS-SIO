### 4. Contenu mis à jour du fichier `models/pretrained_model/README.md`

# Modèle pré-entraîné pour la classification de vêtements

## À propos du modèle
Ce dossier contient le modèle pré-entraîné `mobilenet_clothing_model.h5` utilisé par l'application pour classifier les images de vêtements.

## Caractéristiques du modèle
- **Architecture** : MobileNetV2 adapté avec transfer learning
- **Jeu de données** : Fashion MNIST (10 catégories de vêtements)
- **Dimensions d'entrée** : Images 224×224 pixels RGB
- **Format** : H5 (format Keras)
- **Taille** : ~14 Mo
- **Précision** : ~92% sur le jeu de test

## Options disponibles

### Option 1 : Utiliser le modèle inclus
Le modèle `mobilenet_clothing_model.h5` est déjà inclus dans cette archive et prêt à l'emploi. C'est l'option recommandée pour ce TP.

# Modèle pré-entraîné pour la classification de vêtements

## À propos du modèle
Ce dossier doit contenir le modèle pré-entraîné `mobilenet_clothing_model.h5` utilisé par l'application pour classifier les images de vêtements.

## Caractéristiques du modèle
- **Architecture** : MobileNetV2 adapté avec transfer learning
- **Jeu de données** : Fashion MNIST (10 catégories de vêtements)
- **Dimensions d'entrée** : Images 224×224 pixels RGB
- **Format** : H5 (format Keras)
- **Taille** : ~14 Mo
- **Précision** : ~92% sur le jeu de test

## Obtention du modèle

### Option 2 : Création avec Google Colab (Recommandée)
Cette option ne nécessite aucune installation sur votre machine :

1. Accédez au notebook Google Colab préparé pour ce projet : [Création du modèle Fashion MNIST](https://colab.research.google.com/)
   - Alternativement, ouvrez [Google Colab](https://colab.research.google.com/), créez un nouveau notebook et copiez-collez le code du fichier `tools/create_model.py`

2. Exécutez le notebook en cliquant sur "Exécuter tout" dans le menu "Exécution"
   - L'exécution prendra environ 2-3 minutes avec l'accélération GPU de Colab

3. À la fin de l'exécution, le modèle sera créé. Téléchargez-le en ajoutant cette cellule à la fin du notebook et en l'exécutant :
   ```python
   # Cellule pour télécharger le modèle depuis Colab
   from google.colab import files
   files.download('mobilenet_clothing_model.h5')
   ```
4. Placez le fichier téléchargé dans ce dossier `models/pretrained_model/`



### Option 2 : Recréer le modèle
Si vous souhaitez comprendre comment le modèle a été créé ou expérimenter avec différents paramètres :
1. Consultez le script `tools/create_model.py`
2. Exécutez ce script pour créer votre propre version du modèle
3. Le script générera un nouveau fichier `mobilenet_clothing_model.h5`

### Option 3 : Solution de repli automatique
L'application est conçue pour utiliser automatiquement MobileNetV2 standard comme solution de repli si le modèle spécifique n'est pas trouvé. Cette fonctionnalité garantit que l'application reste opérationnelle même sans le modèle personnalisé.

## Optimisations appliquées
- **Transfer learning** : Adaptation d'un modèle pré-entraîné sur ImageNet
- **Quantification** : Réduction de la précision numérique (version TFLite disponible)
- **Fine-tuning** : Ajustement sur les données Fashion MNIST