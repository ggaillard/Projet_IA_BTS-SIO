import numpy as np
import tensorflow as tf
from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from tensorflow.keras.utils import to_categorical

print("TensorFlow version:", tf.__version__)

# Pour la reproductibilité
np.random.seed(42)
tf.random.set_seed(42)

# Charger les données MNIST
print("Chargement des données MNIST...")
(X_train, y_train), (X_test, y_test) = mnist.load_data()

# Prétraitement des données
X_train = X_train.reshape(-1, 28, 28, 1) / 255.0
X_test = X_test.reshape(-1, 28, 28, 1) / 255.0

# Conversion des étiquettes en format one-hot
y_train_onehot = to_categorical(y_train, 10)
y_test_onehot = to_categorical(y_test, 10)

# Création du modèle CNN
model = Sequential([
    # Première couche de convolution
    Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1), name='conv1'),
    MaxPooling2D((2, 2), name='pool1'),
    
    # Deuxième couche de convolution
    Conv2D(64, (3, 3), activation='relu', name='conv2'),
    MaxPooling2D((2, 2), name='pool2'),
    
    # Aplatissement pour passer aux couches denses
    Flatten(name='flatten'),
    
    # Couches denses (fully connected)
    Dense(128, activation='relu', name='dense1'),
    Dropout(0.5, name='dropout1'),  # Évite le surapprentissage
    Dense(10, activation='softmax', name='output')  # 10 classes (chiffres 0-9)
])

# Compiler le modèle
model.compile(
    optimizer='adam',
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

# Afficher le résumé de l'architecture
model.summary()

# Entraînement du modèle
print("Entraînement du modèle...")
history = model.fit(
    X_train, 
    y_train_onehot, 
    batch_size=128, 
    epochs=5,  # Entraînement court pour l'exemple
    validation_split=0.2,
    verbose=1
)

# Évaluer le modèle
test_loss, test_acc = model.evaluate(X_test, y_test_onehot, verbose=1)
print(f"Précision sur l'ensemble de test: {test_acc*100:.2f}%")

# Sauvegarder le modèle
model.save('mnist_cnn_model.h5')
print("Modèle sauvegardé avec succès sous 'mnist_cnn_model.h5'")