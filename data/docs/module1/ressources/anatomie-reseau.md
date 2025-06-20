# Anatomie d'un réseau de neurones

Ce document contient le code et les explications pour le notebook d'exploration interactive d'un réseau de neurones. Vous pouvez copier-coller chaque section dans une cellule Google Colab.

## Cellule 1 (Markdown) - Introduction

```markdown
# Anatomie d'un réseau de neurones

## Exploration interactive du fonctionnement interne d'un réseau de neurones

Dans ce notebook, nous allons explorer de manière interactive le fonctionnement interne d'un réseau de neurones. Vous pourrez manipuler directement les composants fondamentaux (neurones, poids, biais) et observer leur impact sur les prédictions.

### Objectifs :
- Comprendre le fonctionnement d'un neurone artificiel
- Visualiser l'effet des poids et du biais sur les décisions
- Explorer le flux d'information dans un réseau multicouche
- Observer l'évolution des poids pendant l'entraînement
```

## Cellule 2 (Code) - Configuration initiale

```python
# Partie 1: Configuration initiale
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from google.colab import output
output.enable_custom_widget_manager()
import ipywidgets as widgets
from IPython.display import display, clear_output
from matplotlib.colors import LinearSegmentedColormap

print("Configuration terminée!")
```

## Cellule 3 (Markdown) - Exploration d'un neurone unique

```markdown
## Exploration d'un neurone unique

Dans cette partie, nous allons observer le fonctionnement d'un neurone artificiel, l'unité fondamentale des réseaux de neurones.

Un neurone artificiel effectue deux opérations principales :
1. Une **somme pondérée** des entrées (z = w₁x₁ + w₂x₂ + ... + b)
2. L'application d'une **fonction d'activation** qui introduit la non-linéarité (a = f(z))

Utilisez les contrôles interactifs ci-dessous pour observer comment un neurone traite l'information.
```

## Cellule 4 (Code) - Fonctions du neurone

```python
# Fonction pour calculer la sortie d'un neurone
def neuron_output(x1, x2, w1, w2, b, activation="relu"):
    # Calcul de la somme pondérée
    z = x1 * w1 + x2 * w2 + b
    
    # Application de la fonction d'activation
    if activation == "relu":
        a = max(0, z)
    elif activation == "sigmoid":
        a = 1 / (1 + np.exp(-z))
    elif activation == "tanh":
        a = np.tanh(z)
    else:
        a = z  # Linéaire
    
    return z, a

# Fonction pour visualiser un neurone
def visualize_neuron(x1, x2, w1, w2, b, activation="relu"):
    # Calculer la sortie
    z, a = neuron_output(x1, x2, w1, w2, b, activation)
    
    # Créer la figure
    fig, axes = plt.subplots(1, 3, figsize=(18, 5))
    
    # 1. Représentation du neurone
    ax = axes[0]
    ax.set_xlim(-0.5, 2.5)
    ax.set_ylim(-0.5, 2.5)
    
    # Dessiner le neurone
    circle = plt.Circle((1, 1), 0.4, fill=True, color='lightblue', alpha=0.7)
    ax.add_artist(circle)
    
    # Dessiner les entrées
    ax.plot(0, 0.7, 'ro', markersize=10)
    ax.plot(0, 1.3, 'ro', markersize=10)
    
    # Dessiner la sortie
    ax.plot(2, 1, 'go', markersize=10)
    
    # Ajouter les connexions
    ax.arrow(0, 0.7, 0.6, 0.1, head_width=0.1, head_length=0.1, fc='black', ec='black', linewidth=2)
    ax.arrow(0, 1.3, 0.6, -0.1, head_width=0.1, head_length=0.1, fc='black', ec='black', linewidth=2)
    ax.arrow(1.4, 1, 0.6, 0, head_width=0.1, head_length=0.1, fc='black', ec='black', linewidth=2)
    
    # Ajouter les textes
    ax.text(-0.1, 0.7, f"x₁ = {x1:.2f}", fontsize=12, ha='right')
    ax.text(-0.1, 1.3, f"x₂ = {x2:.2f}", fontsize=12, ha='right')
    ax.text(1, 1, f"z = {z:.2f}\na = {a:.2f}", fontsize=12, ha='center')
    ax.text(0.5, 0.95, f"w₁ = {w1:.2f}", fontsize=10, rotation=15)
    ax.text(0.5, 1.15, f"w₂ = {w2:.2f}", fontsize=10, rotation=-15)
    ax.text(2.1, 1, f"Sortie = {a:.2f}", fontsize=12, ha='left')
    ax.text(1, 0.5, f"Biais = {b:.2f}", fontsize=10)
    
    ax.set_title("Neurone artificiel", fontsize=14)
    ax.set_axis_off()
    
    # 2. Représentation de la fonction d'activation
    ax = axes[1]
    x = np.linspace(-5, 5, 100)
    
    if activation == "relu":
        y = np.maximum(0, x)
        title = "Fonction d'activation: ReLU"
    elif activation == "sigmoid":
        y = 1 / (1 + np.exp(-x))
        title = "Fonction d'activation: Sigmoid"
    elif activation == "tanh":
        y = np.tanh(x)
        title = "Fonction d'activation: Tanh"
    else:
        y = x
        title = "Fonction d'activation: Linéaire"
    
    ax.plot(x, y, 'b-', linewidth=2)
    ax.axhline(y=0, color='k', linestyle='-', alpha=0.3)
    ax.axvline(x=0, color='k', linestyle='-', alpha=0.3)
    
    # Marquer le point correspondant à z
    ax.plot(z, a, 'ro', markersize=8)
    ax.plot([z, z], [0, a], 'r--', alpha=0.5)
    ax.plot([0, z], [a, a], 'r--', alpha=0.5)
    
    ax.set_xlim(-5, 5)
    ax.set_ylim(-1.5, 1.5)
    ax.set_xlabel("z (somme pondérée)")
    ax.set_ylabel("a (activation)")
    ax.set_title(title, fontsize=14)
    ax.grid(True, alpha=0.3)
    
    # 3. Visualisation de la frontière de décision
    ax = axes[2]
    
    # Créer des points pour former une grille
    grid_size = 20
    x1_values = np.linspace(0, 1, grid_size)
    x2_values = np.linspace(0, 1, grid_size)
    x1_grid, x2_grid = np.meshgrid(x1_values, x2_values)
    
    # Calculer la sortie pour chaque point de la grille
    z_grid = x1_grid * w1 + x2_grid * w2 + b
    
    if activation == "relu":
        a_grid = np.maximum(0, z_grid)
    elif activation == "sigmoid":
        a_grid = 1 / (1 + np.exp(-z_grid))
    elif activation == "tanh":
        a_grid = np.tanh(z_grid)
    else:
        a_grid = z_grid
    
    # Créer une carte de couleur
    cmap = plt.get_cmap('coolwarm')
    
    # Tracer la heatmap
    im = ax.imshow(a_grid, origin='lower', extent=[0, 1, 0, 1], 
                   cmap=cmap, vmin=0, vmax=1)
    plt.colorbar(im, ax=ax, label="Activation")
    
    # Ajouter le point actuel
    ax.plot(x1, x2, 'ko', markersize=8)
    
    # Tracer la frontière de décision (a = 0.5)
    if activation in ["sigmoid", "tanh"]:
        threshold = 0.5
        CS = ax.contour(x1_grid, x2_grid, a_grid, levels=[threshold], 
                         colors='k', linestyles='--')
        ax.clabel(CS, inline=True, fontsize=10, fmt={threshold: "a = 0.5"})
    
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_xlabel("x₁")
    ax.set_ylabel("x₂")
    ax.set_title("Carte d'activation", fontsize=14)
    
    plt.tight_layout()
    plt.show()
    
    return a
```

## Cellule 5 (Code) - Interface interactive pour un neurone

```python
# Créer des widgets interactifs pour le neurone
w1_slider = widgets.FloatSlider(value=1.0, min=-3.0, max=3.0, step=0.1, description='Poids w₁:')
w2_slider = widgets.FloatSlider(value=1.0, min=-3.0, max=3.0, step=0.1, description='Poids w₂:')
b_slider = widgets.FloatSlider(value=0.0, min=-3.0, max=3.0, step=0.1, description='Biais:')
x1_slider = widgets.FloatSlider(value=0.5, min=0.0, max=1.0, step=0.05, description='Entrée x₁:')
x2_slider = widgets.FloatSlider(value=0.5, min=0.0, max=1.0, step=0.05, description='Entrée x₂:')
activation_dropdown = widgets.Dropdown(
    options=['relu', 'sigmoid', 'tanh', 'linear'],
    value='relu',
    description='Activation:'
)

# Fonction pour mettre à jour la visualisation
def update_neuron_visualization(w1, w2, b, x1, x2, activation):
    clear_output(wait=True)
    output = visualize_neuron(x1, x2, w1, w2, b, activation)
    print(f"Sortie du neurone: {output:.4f}")
    
    # Expliquer le calcul
    z = x1 * w1 + x2 * w2 + b
    print(f"\nCalcul détaillé:")
    print(f"z = (x₁ × w₁) + (x₂ × w₂) + b")
    print(f"z = ({x1:.2f} × {w1:.2f}) + ({x2:.2f} × {w2:.2f}) + {b:.2f}")
    print(f"z = {x1*w1:.2f} + {x2*w2:.2f} + {b:.2f}")
    print(f"z = {z:.2f}")
    
    if activation == "relu":
        print(f"a = ReLU(z) = max(0, z) = max(0, {z:.2f}) = {max(0, z):.2f}")
    elif activation == "sigmoid":
        sig_z = 1 / (1 + np.exp(-z))
        print(f"a = Sigmoid(z) = 1 / (1 + e^(-z)) = 1 / (1 + e^(-{z:.2f})) = {sig_z:.2f}")
    elif activation == "tanh":
        tanh_z = np.tanh(z)
        print(f"a = tanh(z) = tanh({z:.2f}) = {tanh_z:.2f}")
    else:
        print(f"a = z = {z:.2f}")  # Linéaire

# Interface interactive pour le neurone
neuron_output = widgets.interactive_output(
    update_neuron_visualization,
    {'w1': w1_slider, 'w2': w2_slider, 'b': b_slider, 
     'x1': x1_slider, 'x2': x2_slider, 'activation': activation_dropdown}
)

# Afficher les widgets
print("Utilisez les contrôles ci-dessous pour modifier les propriétés du neurone:")
display(widgets.VBox([
    widgets.HBox([x1_slider, x2_slider]),
    widgets.HBox([w1_slider, w2_slider]),
    widgets.HBox([b_slider, activation_dropdown])
]))
display(neuron_output)
```

## Cellule 6 (Markdown) - De l'unique au réseau

```markdown
## De l'unique au réseau

Maintenant que nous avons exploré un neurone unique, passons à un réseau simple. Un réseau de neurones est composé de plusieurs neurones organisés en couches, où l'information se propage de l'entrée vers la sortie.

Le réseau ci-dessous contient :
- Une couche d'entrée (2 neurones)
- Une couche cachée (nombre ajustable de neurones)
- Une couche de sortie (1 neurone)

Observez comment l'information circule à travers le réseau et comment les différents poids affectent les activations.
```

## Cellule 7 (Code) - Fonctions du réseau

```python
# Fonction pour créer et visualiser un réseau simple
def create_simple_network(hidden_units=3, activation='relu'):
    # Créer un modèle séquentiel
    model = Sequential([
        Dense(hidden_units, activation=activation, input_shape=(2,)),
        Dense(1, activation='sigmoid')
    ])
    
    # Compiler le modèle (bien que nous ne l'entraînerons pas)
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    
    return model

# Fonction pour visualiser un réseau simple
def visualize_network(inputs, weights1=None, biases1=None, weights2=None, biases2=None, hidden_units=3, activation='relu'):
    # Créer le modèle si non fourni
    model = create_simple_network(hidden_units, activation)
    
    # Si des poids sont fournis, les appliquer
    if weights1 is not None and biases1 is not None and weights2 is not None and biases2 is not None:
        model.layers[0].set_weights([weights1, biases1])
        model.layers[1].set_weights([weights2, biases2])
    
    # Convertir les entrées pour prédiction
    x = np.array([inputs])
    
    # Obtenir les activations intermédiaires
    intermediate_layer_model = tf.keras.Model(inputs=model.input,
                                             outputs=model.layers[0].output)
    intermediate_activations = intermediate_layer_model.predict(x)[0]
    
    # Obtenir les activations de sortie
    output_activation = model.predict(x)[0][0]
    
    # Extraire les poids et biais
    weights1, biases1 = model.layers[0].get_weights()
    weights2, biases2 = model.layers[1].get_weights()
    
    # Créer la figure pour visualiser le réseau
    plt.figure(figsize=(12, 8))
    
    # Définir les positions des neurones
    input_layer_y = np.array([0.2, 0.8])
    hidden_layer_y = np.linspace(0.1, 0.9, hidden_units)
    output_layer_y = np.array([0.5])
    
    input_layer_x = 0.1
    hidden_layer_x = 0.5
    output_layer_x = 0.9
    
    # Dessiner les neurones d'entrée
    for i, y in enumerate(input_layer_y):
        plt.scatter(input_layer_x, y, s=200, c='blue', alpha=0.7)
        plt.text(input_layer_x, y, f"x{i+1}={inputs[i]:.2f}", fontsize=12, ha='center', va='center', color='white')
    
    # Dessiner les neurones cachés
    for i, y in enumerate(hidden_layer_y):
        # Calculer la somme pondérée
        z = np.dot(inputs, weights1[:, i]) + biases1[i]
        
        # Appliquer l'activation
        if activation == 'relu':
            a = max(0, z)
        elif activation == 'sigmoid':
            a = 1 / (1 + np.exp(-z))
        elif activation == 'tanh':
            a = np.tanh(z)
        else:
            a = z
        
        # Couleur basée sur l'activation
        color = plt.cm.viridis(a)
        
        plt.scatter(hidden_layer_x, y, s=200, c=[color], alpha=0.7)
        plt.text(hidden_layer_x, y, f"{a:.2f}", fontsize=12, ha='center', va='center', color='white')
    
    # Dessiner le neurone de sortie
    plt.scatter(output_layer_x, output_layer_y, s=200, c='red', alpha=0.7)
    plt.text(output_layer_x, output_layer_y, f"{output_activation:.2f}", fontsize=12, ha='center', va='center', color='white')
    
    # Dessiner les connexions entre couches d'entrée et cachée
    for i, y_in in enumerate(input_layer_y):
        for j, y_hid in enumerate(hidden_layer_y):
            # Couleur et épaisseur basées sur le poids
            weight = weights1[i, j]
            width = abs(weight) * 3
            color = 'red' if weight < 0 else 'green'
            alpha = min(abs(weight), 1.0)
            
            plt.plot([input_layer_x, hidden_layer_x], [y_in, y_hid], 
                    c=color, linewidth=width, alpha=alpha)
    
    # Dessiner les connexions entre couche cachée et sortie
    for i, y_hid in enumerate(hidden_layer_y):
        # Couleur et épaisseur basées sur le poids
        weight = weights2[i, 0]
        width = abs(weight) * 3
        color = 'red' if weight < 0 else 'green'
        alpha = min(abs(weight), 1.0)
        
        plt.plot([hidden_layer_x, output_layer_x], [y_hid, output_layer_y], 
                c=color, linewidth=width, alpha=alpha)
    
    # Étiquettes
    plt.text(input_layer_x, 0.03, "Couche d'entrée", fontsize=14, ha='center')
    plt.text(hidden_layer_x, 0.03, "Couche cachée", fontsize=14, ha='center')
    plt.text(output_layer_x, 0.03, "Couche de sortie", fontsize=14, ha='center')
    
    # Enlever les axes
    plt.axis('off')
    plt.title(f"Réseau de neurones - Activation cachée: {activation}", fontsize=16)
    plt.tight_layout()
    plt.show()
    
    # Afficher les calculs détaillés
    print("\nCalculs détaillés pour chaque neurone de la couche cachée:")
    for i in range(hidden_units):
        z = np.dot(inputs, weights1[:, i]) + biases1[i]
        print(f"\nNeurone caché {i+1}:")
        print(f"z = (x₁ × w₁,{i+1}) + (x₂ × w₂,{i+1}) + b{i+1}")
        print(f"z = ({inputs[0]:.2f} × {weights1[0, i]:.2f}) + ({inputs[1]:.2f} × {weights1[1, i]:.2f}) + {biases1[i]:.2f}")
        print(f"z = {inputs[0] * weights1[0, i]:.2f} + {inputs[1] * weights1[1, i]:.2f} + {biases1[i]:.2f} = {z:.2f}")
        
        if activation == 'relu':
            a = max(0, z)
            print(f"a = ReLU(z) = max(0, {z:.2f}) = {a:.2f}")
        elif activation == 'sigmoid':
            a = 1 / (1 + np.exp(-z))
            print(f"a = Sigmoid(z) = 1 / (1 + e^(-{z:.2f})) = {a:.2f}")
        elif activation == 'tanh':
            a = np.tanh(z)
            print(f"a = tanh(z) = tanh({z:.2f}) = {a:.2f}")
        else:
            a = z
            print(f"a = z = {z:.2f}")
    
    print("\nCalcul pour le neurone de sortie:")
    z_out = np.dot(intermediate_activations, weights2[:, 0]) + biases2[0]
    print(f"z = Σ(a_caché × w_sortie) + b_sortie = {z_out:.2f}")
    print(f"sortie = Sigmoid(z) = 1 / (1 + e^(-{z_out:.2f})) = {output_activation:.2f}")
    
    return model, weights1, biases1, weights2, biases2

# Fonction pour générer des poids aléatoires
def generate_random_weights(hidden_units=3):
    # Générer des poids aléatoires pour la première couche
    weights1 = np.random.normal(0, 1, (2, hidden_units))
    biases1 = np.random.normal(0, 1, hidden_units)
    
    # Générer des poids aléatoires pour la couche de sortie
    weights2 = np.random.normal(0, 1, (hidden_units, 1))
    biases2 = np.random.normal(0, 1, 1)
    
    return weights1, biases1, weights2, biases2
```

## Cellule 8 (Code) - Interface interactive pour le réseau

```python
# Créer des widgets interactifs pour le réseau
x1_net_slider = widgets.FloatSlider(value=0.5, min=0.0, max=1.0, step=0.05, description='Entrée x₁:')
x2_net_slider = widgets.FloatSlider(value=0.5, min=0.0, max=1.0, step=0.05, description='Entrée x₂:')
hidden_units_slider = widgets.IntSlider(value=3, min=1, max=5, description='Neurones cachés:')
activation_net_dropdown = widgets.Dropdown(
    options=['relu', 'sigmoid', 'tanh', 'linear'],
    value='relu',
    description='Activation:'
)
random_button = widgets.Button(description="Poids aléatoires")

# Variables pour stocker les poids courants
current_weights1, current_biases1, current_weights2, current_biases2 = generate_random_weights()

# Fonction pour visualiser le réseau
def update_network_visualization(x1, x2, hidden_units, activation):
    global current_weights1, current_biases1, current_weights2, current_biases2
    
    # Ajuster les dimensions des poids si nécessaire
    if current_weights1.shape[1] != hidden_units:
        current_weights1, current_biases1, current_weights2, current_biases2 = generate_random_weights(hidden_units)
    
    # Visualiser le réseau
    inputs = np.array([x1, x2])
    _, w1, b1, w2, b2 = visualize_network(
        inputs, current_weights1, current_biases1, current_weights2, current_biases2, 
        hidden_units, activation
    )
    
    # Mettre à jour les poids courants
    current_weights1, current_biases1 = w1, b1
    current_weights2, current_biases2 = w2, b2

# Fonction pour générer de nouveaux poids aléatoires
def regenerate_weights(b):
    global current_weights1, current_biases1, current_weights2, current_biases2
    current_weights1, current_biases1, current_weights2, current_biases2 = generate_random_weights(
        hidden_units_slider.value
    )
    # Mettre à jour la visualisation
    update_network_visualization(
        x1_net_slider.value, x2_net_slider.value,
        hidden_units_slider.value, activation_net_dropdown.value
    )

# Associer la fonction au bouton
random_button.on_click(regenerate_weights)

# Interface interactive pour le réseau
network_output = widgets.interactive_output(
    update_network_visualization,
    {'x1': x1_net_slider, 'x2': x2_net_slider, 
     'hidden_units': hidden_units_slider, 'activation': activation_net_dropdown}
)

# Afficher les widgets pour le réseau
print("\nExplorez le comportement d'un réseau simple:")
display(widgets.VBox([
    widgets.HBox([x1_net_slider, x2_net_slider]),
    widgets.HBox([hidden_units_slider, activation_net_dropdown]),
    random_button
]))
display(network_output)
```

## Cellule 9 (Markdown) - Visualisation de l'entraînement

```markdown
## Visualisation de l'entraînement

Dans cette dernière partie, nous allons observer l'évolution des poids pendant l'entraînement d'un réseau de neurones sur un problème classique : le problème XOR.

Le problème XOR (OU exclusif) consiste à prédire la sortie de la fonction logique XOR :
- (0,0) → 0
- (0,1) → 1
- (1,0) → 1
- (1,1) → 0

Ce problème n'est pas linéairement séparable, ce qui signifie qu'il ne peut pas être résolu par un seul neurone.
```

## Cellule 10 (Code) - Génération de données XOR

```python
# Générer des données XOR
def generate_xor_data(n_samples=100):
    X = np.random.rand(n_samples, 2)
    y = np.logical_xor(X[:, 0] > 0.5, X[:, 1] > 0.5).astype(np.float32)
    return X, y

# Afficher quelques exemples de données XOR
X_sample, y_sample = generate_xor_data(20)
plt.figure(figsize=(6, 6))
plt.scatter(X_sample[:, 0], X_sample[:, 1], c=y_sample, cmap='coolwarm', s=100)
plt.xlabel('x₁')
plt.ylabel('x₂')
plt.title('Problème XOR')
plt.grid(True, alpha=0.3)
plt.show()

print("Exemples de données XOR:")
for i in range(5):
    x1, x2 = X_sample[i]
    y = y_sample[i]
    print(f"x1={x1:.2f}, x2={x2:.2f} → y={y:.0f}")
```

## Cellule 11 (Code) - Création et entraînement du modèle XOR

```python
# Créer un modèle pour résoudre XOR
learning_rate = 0.1
hidden_units = 4
epochs = 20

# Générer des données
X_train, y_train = generate_xor_data(200)

# Créer un modèle
model = Sequential([
    Dense(hidden_units, activation='relu', input_shape=(2,)),
    Dense(1, activation='sigmoid')
])

# Compiler avec un optimiseur personnalisé
optimizer = tf.keras.optimizers.SGD(learning_rate=learning_rate)
model.compile(optimizer=optimizer, loss='binary_crossentropy', metrics=['accuracy'])

# Entraîner le modèle
history = model.fit(
    X_train, y_train,
    epochs=epochs,
    batch_size=32,
    verbose=1
)

# Afficher les résultats d'entraînement
plt.figure(figsize=(12, 5))

# Graphique de précision
plt.subplot(1, 2, 1)
plt.plot(history.history['accuracy'], '-o')
plt.title('Précision pendant l\'entraînement')
plt.xlabel('Époque')
plt.ylabel('Précision')
plt.grid(True, alpha=0.3)

# Graphique de perte
plt.subplot(1, 2, 2)
plt.plot(history.history['loss'], '-o')
plt.title('Perte pendant l\'entraînement')
plt.xlabel('Époque')
plt.ylabel('Perte')
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()
```

Je vais compléter le fichier anatomie-reseau.md à partir de la cellule 12, en continuant le document là où il a été interrompu.

## Cellule 12 (Code) - Visualisation de la frontière de décision

```python
# Visualiser la frontière de décision finale
h = 0.01
x_min, x_max = 0, 1
y_min, y_max = 0, 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
grid_points = np.c_[xx.ravel(), yy.ravel()]

# Convertir les points en format approprié pour le modèle
grid_pred = model.predict(grid_points)
grid_pred = grid_pred.reshape(xx.shape)

# Tracer la frontière de décision
plt.figure(figsize=(8, 6))
plt.contourf(xx, yy, grid_pred, alpha=0.8, cmap=plt.cm.RdBu)

# Tracer les données d'entraînement
plt.scatter(X_train[:, 0], X_train[:, 1], c=y_train, cmap=plt.cm.RdBu, edgecolors='k')
plt.xlabel('x1')
plt.ylabel('x2')
plt.title('Frontière de décision pour le problème XOR')
plt.colorbar()
plt.show()

# Évaluer les performances finales
train_loss, train_acc = model.evaluate(X_train, y_train, verbose=0)
print(f"Précision finale sur l'ensemble d'entraînement: {train_acc*100:.2f}%")
```

## Cellule 13 (Markdown) - Exploration interactive avancée

```markdown
## Exploration interactive avancée

Maintenant que nous avons exploré les bases des réseaux de neurones, exploitons davantage l'interactivité pour comprendre comment ils apprennent et se comportent.

Utilisez les widgets interactifs ci-dessous pour explorer différentes architectures et configurations du réseau sur le problème XOR. Observez comment les changements affectent la frontière de décision et les performances.
```

## Cellule 14 (Code) - Interface interactive avancée

```python
# Créer des widgets interactifs pour l'exploration avancée
num_hidden_slider = widgets.IntSlider(value=4, min=2, max=10, step=1, description='Neurones cachés:')
learning_rate_slider = widgets.FloatLogSlider(value=0.1, base=10, min=-3, max=0, step=0.1, description='Learning rate:')
epochs_slider = widgets.IntSlider(value=100, min=10, max=500, step=10, description='Époques:')
activation_dropdown = widgets.Dropdown(
    options=['relu', 'tanh', 'sigmoid'],
    value='relu',
    description='Activation:'
)

# Fonction pour créer et entraîner le modèle avec les paramètres spécifiés
def create_and_train_model(hidden_units, learning_rate, epochs, activation):
    # Créer un modèle
    model = Sequential([
        Dense(hidden_units, activation=activation, input_shape=(2,)),
        Dense(1, activation='sigmoid')
    ])
    
    # Compiler le modèle
    optimizer = tf.keras.optimizers.SGD(learning_rate=learning_rate)
    model.compile(optimizer=optimizer, loss='binary_crossentropy', metrics=['accuracy'])
    
    # Créer des données
    X, y = generate_xor_data(200)
    
    # Afficher les données
    plt.figure(figsize=(12, 5))
    plt.subplot(1, 2, 1)
    plt.scatter(X[:, 0], X[:, 1], c=y, cmap='coolwarm')
    plt.title('Données XOR')
    plt.xlabel('x1')
    plt.ylabel('x2')
    
    # Entraîner le modèle
    history = model.fit(
        X, y,
        epochs=epochs,
        batch_size=32,
        verbose=0
    )
    
    # Afficher l'historique d'entraînement
    plt.subplot(1, 2, 2)
    plt.plot(history.history['loss'])
    plt.title('Perte pendant l\'entraînement')
    plt.xlabel('Époque')
    plt.ylabel('Perte')
    plt.tight_layout()
    plt.show()
    
    # Visualiser la frontière de décision
    h = 0.01
    x_min, x_max = 0, 1
    y_min, y_max = 0, 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
    grid_points = np.c_[xx.ravel(), yy.ravel()]
    
    # Obtenir les prédictions
    grid_pred = model.predict(grid_points, verbose=0)
    grid_pred = grid_pred.reshape(xx.shape)
    
    # Tracer la frontière de décision
    plt.figure(figsize=(8, 6))
    plt.contourf(xx, yy, grid_pred, alpha=0.8, cmap=plt.cm.RdBu)
    
    # Tracer les données
    plt.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.RdBu, edgecolors='k')
    plt.xlabel('x1')
    plt.ylabel('x2')
    plt.title(f'Frontière de décision (Neurones: {hidden_units}, LR: {learning_rate:.4f}, Activation: {activation})')
    plt.colorbar()
    plt.show()
    
    # Évaluer le modèle
    loss, acc = model.evaluate(X, y, verbose=0)
    print(f"Architecture: {hidden_units} neurones cachés, learning rate: {learning_rate:.4f}, activation: {activation}")
    print(f"Précision: {acc*100:.2f}%")
    print(f"Perte: {loss:.4f}")
    
    # Afficher les poids du réseau pour comprendre ce qu'il a appris
    weights1, biases1 = model.layers[0].get_weights()
    weights2, biases2 = model.layers[1].get_weights()
    
    print("\nPoids de la couche cachée:")
    for i in range(hidden_units):
        print(f"Neurone {i+1}: {weights1[:, i]} (biais: {biases1[i]:.4f})")
    
    print("\nPoids de la couche de sortie:")
    print(f"{weights2.flatten()} (biais: {biases2[0]:.4f})")

# Interface interactive
interactive_output = widgets.interactive_output(
    create_and_train_model,
    {'hidden_units': num_hidden_slider, 
     'learning_rate': learning_rate_slider, 
     'epochs': epochs_slider, 
     'activation': activation_dropdown}
)

# Afficher les widgets
print("Explorez différentes architectures et configurations:")
display(widgets.VBox([
    widgets.HBox([num_hidden_slider, activation_dropdown]),
    widgets.HBox([learning_rate_slider, epochs_slider])
]))
display(interactive_output)
```

## Cellule 15 (Markdown) - Interpréter les résultats

```markdown
## Interpréter les résultats

Maintenant que vous avez exploré différentes configurations de réseaux de neurones, prenons un moment pour analyser et comprendre les résultats :

### Observations clés

1. **Nombre de neurones cachés** :
   - Trop peu de neurones (2-3) limitent la capacité du réseau à apprendre la fonction XOR
   - Un nombre approprié (4-6) permet généralement une bonne séparation
   - Trop de neurones peuvent parfois mener à du surapprentissage (la frontière devient trop complexe)

2. **Taux d'apprentissage (Learning Rate)** :
   - Trop faible (< 0.01) : apprentissage très lent, peut ne pas converger dans le nombre d'époques donné
   - Approprié (0.01 - 0.1) : bonne convergence avec une frontière stable
   - Trop élevé (> 0.5) : instabilité, oscillations, voire divergence

3. **Fonction d'activation** :
   - ReLU : rapide, peut parfois créer des frontières plus angulaires
   - Tanh : frontières plus lisses, parfois meilleure pour ce problème spécifique
   - Sigmoid : peut être plus lente à converger pour des problèmes comme XOR

4. **Nombre d'époques** :
   - Insuffisant : modèle sous-entraîné, frontière imprécise
   - Suffisant : bonne frontière de décision
   - Excessif : risque de surapprentissage, mais moins problématique pour ce cas simple

### Comment le réseau apprend-il le XOR ?

Le problème XOR est intéressant car il n'est pas linéairement séparable. En d'autres termes, on ne peut pas tracer une seule ligne droite pour séparer les classes.

Un réseau avec une couche cachée résout ce problème en :
1. Créant des "lignes de séparation" avec chaque neurone de la couche cachée
2. Combinant ces lignes pour former des régions complexes
3. Ajustant les poids pour positionner ces lignes de manière optimale

C'est une parfaite illustration de pourquoi nous avons besoin de réseaux multicouches pour résoudre des problèmes non linéaires.
```

## Cellule 16 (Code) - Visualisation des neurones cachés

```python
# Fonction pour visualiser la contribution de chaque neurone caché
def visualize_hidden_neurons(hidden_units=4, activation='relu'):
    # Créer un modèle
    model = Sequential([
        Dense(hidden_units, activation=activation, input_shape=(2,)),
        Dense(1, activation='sigmoid')
    ])
    
    # Compiler le modèle
    optimizer = tf.keras.optimizers.SGD(learning_rate=0.1)
    model.compile(optimizer=optimizer, loss='binary_crossentropy', metrics=['accuracy'])
    
    # Créer des données
    X, y = generate_xor_data(200)
    
    # Entraîner le modèle
    model.fit(X, y, epochs=100, batch_size=32, verbose=0)
    
    # Obtenir les poids
    weights1, biases1 = model.layers[0].get_weights()
    weights2, biases2 = model.layers[1].get_weights()
    
    # Créer une grille de points pour visualisation
    h = 0.01
    x_min, x_max = 0, 1
    y_min, y_max = 0, 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
    grid_points = np.c_[xx.ravel(), yy.ravel()]
    
    # Créer un modèle intermédiaire pour obtenir les activations de la couche cachée
    intermediate_model = tf.keras.Model(inputs=model.input, outputs=model.layers[0].output)
    hidden_activations = intermediate_model.predict(grid_points, verbose=0)
    
    # Visualiser la contribution de chaque neurone caché
    fig, axes = plt.subplots(2, hidden_units, figsize=(4*hidden_units, 8))
    
    # Pour chaque neurone caché
    for i in range(hidden_units):
        # Activation du neurone
        neuron_activation = hidden_activations[:, i].reshape(xx.shape)
        
        # La ligne de décision du neurone (où l'activation est proche de 0)
        if activation == 'tanh':
            decision_boundary = np.zeros_like(neuron_activation)
        elif activation == 'relu':
            decision_boundary = np.zeros_like(neuron_activation)
        else:  # sigmoid
            decision_boundary = np.ones_like(neuron_activation) * 0.5
        
        # Visualiser l'activation du neurone
        im = axes[0, i].contourf(xx, yy, neuron_activation, cmap='viridis')
        axes[0, i].set_title(f'Neurone {i+1}\nw=[{weights1[0, i]:.2f}, {weights1[1, i]:.2f}]\nb={biases1[i]:.2f}')
        axes[0, i].set_xlabel('x1')
        axes[0, i].set_ylabel('x2')
        plt.colorbar(im, ax=axes[0, i])
        
        # Visualiser la ligne de décision
        axes[1, i].contour(xx, yy, neuron_activation, levels=[0] if activation in ['tanh', 'relu'] else [0.5], 
                           colors='r', linewidths=2)
        axes[1, i].scatter(X[:, 0], X[:, 1], c=y, cmap='coolwarm', edgecolors='k')
        axes[1, i].set_title(f'Ligne de décision\nContribution finale: {"+" if weights2[i, 0] > 0 else "-"}{abs(weights2[i, 0]):.2f}')
        axes[1, i].set_xlabel('x1')
        axes[1, i].set_ylabel('x2')
    
    plt.tight_layout()
    plt.show()
    
    # Afficher la frontière de décision finale
    hidden_output = np.dot(hidden_activations, weights2) + biases2
    final_pred = 1 / (1 + np.exp(-hidden_output))  # sigmoid
    final_pred = final_pred.reshape(xx.shape)
    
    plt.figure(figsize=(8, 6))
    plt.contourf(xx, yy, final_pred, alpha=0.8, cmap=plt.cm.RdBu)
    plt.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.RdBu, edgecolors='k')
    plt.xlabel('x1')
    plt.ylabel('x2')
    plt.title('Frontière de décision finale (combinaison des neurones cachés)')
    plt.colorbar()
    plt.show()
    
    # Expliquer comment les neurones se combinent
    print("Comment les neurones cachés se combinent pour résoudre le problème XOR:")
    print("-" * 80)
    print("1. Chaque neurone caché crée une 'ligne de décision' dans l'espace d'entrée")
    print("2. Le signe du poids de sortie détermine si le neurone contribue positivement ou négativement")
    print("3. La combinaison de ces lignes forme la frontière de décision complexe finale")
    print("-" * 80)
    print("\nPoids de la couche de sortie:")
    for i in range(hidden_units):
        print(f"Neurone {i+1} → Sortie: {'positif' if weights2[i, 0] > 0 else 'négatif'} ({weights2[i, 0]:.4f})")
    print(f"Biais de sortie: {biases2[0]:.4f}")

# Créer des widgets pour l'exploration
hidden_units_viz = widgets.IntSlider(value=4, min=2, max=8, step=1, description='Neurones:')
activation_viz = widgets.Dropdown(
    options=['relu', 'tanh', 'sigmoid'],
    value='relu',
    description='Activation:'
)

# Interface interactive
viz_output = widgets.interactive_output(
    visualize_hidden_neurons,
    {'hidden_units': hidden_units_viz, 'activation': activation_viz}
)

# Afficher les widgets
print("Explorez comment chaque neurone caché contribue à la solution:")
display(widgets.HBox([hidden_units_viz, activation_viz]))
display(viz_output)
```

## Cellule 17 (Markdown) - Conclusion

```markdown
## Conclusion : L'anatomie d'un réseau de neurones

### Ce que nous avons exploré

Dans ce notebook, nous avons disséqué le fonctionnement interne d'un réseau de neurones en explorant :

1. **Le neurone individuel**
   - Comment les entrées sont pondérées et combinées
   - L'effet du biais sur le seuil d'activation
   - L'impact des différentes fonctions d'activation

2. **La structure d'un réseau**
   - Comment les neurones s'organisent en couches
   - Comment l'information se propage à travers le réseau
   - Comment les couches interagissent pour créer des représentations complexes

3. **Le processus d'apprentissage**
   - Comment un réseau s'entraîne par descente de gradient
   - Comment les poids s'ajustent pour minimiser l'erreur
   - Comment le réseau apprend progressivement à résoudre des problèmes complexes

4. **La résolution de problèmes non linéaires**
   - Comment un problème comme XOR nécessite plusieurs neurones
   - Comment chaque neurone caché contribue à la solution finale
   - Comment les frontières de décision complexes émergent de la combinaison de neurones simples

### Applications pratiques

Ces connaissances fondamentales vous permettront de :

- **Concevoir** des architectures appropriées pour différents problèmes
- **Diagnostiquer** les problèmes dans vos modèles (sous-apprentissage, sur-apprentissage)
- **Optimiser** les performances de vos réseaux
- **Expliquer** le fonctionnement interne des modèles de Deep Learning

### Prochaines étapes

Dans les modules suivants, nous approfondirons ces concepts en explorant :

- Les réseaux de neurones convolutifs (CNN) pour la vision par ordinateur
- Les réseaux récurrents (RNN) pour le traitement de séquences
- Les techniques avancées d'entraînement et d'optimisation
- L'application pratique de ces connaissances dans des projets réels

Maintenant que vous avez une compréhension solide de l'anatomie d'un réseau de neurones, vous êtes prêt à aborder des architectures plus complexes et spécialisées !
```

## Cellule 18 (Code) - Schéma conceptuel à compléter

```python
# Fonction pour générer un schéma conceptuel à compléter
def create_conceptual_diagram():
    # Créer la figure
    plt.figure(figsize=(12, 10))
    
    # Définir les positions des composants
    input_layer_x = 0.1
    hidden_layer1_x = 0.3
    hidden_layer2_x = 0.5
    output_layer_x = 0.7
    prediction_x = 0.9
    
    input_layer_y = [0.2, 0.5, 0.8]
    hidden_layer1_y = [0.2, 0.5, 0.8]
    hidden_layer2_y = [0.3, 0.7]
    output_layer_y = [0.5]
    
    # Dessiner les couches
    plt.text(0.02, 0.5, "1. Couche d'entrée", fontsize=12, ha='left', va='center')
    for y in input_layer_y:
        circle = plt.Circle((input_layer_x, y), 0.05, fill=True, color='lightblue', alpha=0.7)
        plt.gca().add_patch(circle)
    
    plt.text(hidden_layer1_x-0.08, 0.08, "2. Première couche cachée", fontsize=12, ha='center', va='center')
    for y in hidden_layer1_y:
        circle = plt.Circle((hidden_layer1_x, y), 0.05, fill=True, color='lightgreen', alpha=0.7)
        plt.gca().add_patch(circle)
    
    plt.text(hidden_layer2_x-0.08, 0.08, "3. Deuxième couche cachée", fontsize=12, ha='center', va='center')
    for y in hidden_layer2_y:
        circle = plt.Circle((hidden_layer2_x, y), 0.05, fill=True, color='lightsalmon', alpha=0.7)
        plt.gca().add_patch(circle)
    
    plt.text(output_layer_x-0.02, 0.08, "4. Couche de sortie", fontsize=12, ha='center', va='center')
    for y in output_layer_y:
        circle = plt.Circle((output_layer_x, y), 0.05, fill=True, color='plum', alpha=0.7)
        plt.gca().add_patch(circle)
    
    # Dessiner le processus d'apprentissage
    plt.text(prediction_x-0.02, 0.08, "5. Prédiction", fontsize=12, ha='center', va='center')
    rect = plt.Rectangle((prediction_x-0.06, 0.45), 0.12, 0.1, fill=True, color='lightgrey', alpha=0.7)
    plt.gca().add_patch(rect)
    plt.text(prediction_x, 0.5, "ŷ", fontsize=14, ha='center', va='center')
    
    # Erreur et données réelles
    plt.text(prediction_x-0.02, 0.35, "6. Calcul de l'erreur", fontsize=12, ha='center', va='center')
    rect = plt.Rectangle((prediction_x-0.06, 0.25), 0.12, 0.1, fill=True, color='lightcoral', alpha=0.7)
    plt.gca().add_patch(rect)
    plt.text(prediction_x, 0.3, "Loss", fontsize=14, ha='center', va='center')
    
    plt.text(prediction_x-0.02, 0.15, "7. Données réelles", fontsize=12, ha='center', va='center')
    rect = plt.Rectangle((prediction_x-0.06, 0.15), 0.12, 0.1, fill=True, color='lightblue', alpha=0.7)
    plt.gca().add_patch(rect)
    plt.text(prediction_x, 0.2, "y", fontsize=14, ha='center', va='center')
    
    # Connexions entre les couches
    for y1 in input_layer_y:
        for y2 in hidden_layer1_y:
            plt.plot([input_layer_x, hidden_layer1_x], [y1, y2], 'k-', alpha=0.3)
    
    for y1 in hidden_layer1_y:
        for y2 in hidden_layer2_y:
            plt.plot([hidden_layer1_x, hidden_layer2_x], [y1, y2], 'k-', alpha=0.3)
    
    for y1 in hidden_layer2_y:
        for y2 in output_layer_y:
            plt.plot([hidden_layer2_x, output_layer_x], [y1, y2], 'k-', alpha=0.3)
    
    # Connexion sortie -> prédiction
    plt.plot([output_layer_x, prediction_x], [output_layer_y[0], 0.5], 'k-', alpha=0.3)
    
    # Flux d'erreur
    plt.plot([prediction_x, prediction_x], [0.45, 0.35], 'r--', alpha=0.7)
    plt.arrow(prediction_x, 0.2, 0, 0.05, head_width=0.01, head_length=0.01, fc='blue', ec='blue')
    
    # Rétropropagation
    plt.arrow(prediction_x-0.1, 0.3, -0.1, 0, head_width=0.01, head_length=0.01, fc='red', ec='red', linestyle='dashed')
    plt.text(prediction_x-0.15, 0.33, "Rétropropagation", fontsize=10, ha='center', va='center', color='red')
    
    # Propagation avant
    plt.arrow(hidden_layer2_x+0.1, 0.5, 0.1, 0, head_width=0.01, head_length=0.01, fc='green', ec='green')
    plt.text(hidden_layer2_x+0.15, 0.53, "Propagation avant", fontsize=10, ha='center', va='center', color='green')
    
    # Finalisation du schéma
    plt.xlim(0, 1)
    plt.ylim(0, 1)
    plt.title("Schéma conceptuel d'un réseau de neurones", fontsize=16)
    plt.axis('off')
    plt.tight_layout()
    plt.show()
    
    print("Complétez le schéma conceptuel en identifiant les éléments numérotés:")
    print("1. ________________________________")
    print("2. ________________________________")
    print("3. ________________________________")
    print("4. ________________________________")
    print("5. ________________________________")
    print("6. ________________________________")
    print("7. ________________________________")

# Afficher le schéma conceptuel
create_conceptual_diagram()
```

## Cellule 19 (Markdown) - Exercice final

```markdown
## Exercice final : Synthèse des connaissances

Pour consolider votre compréhension des réseaux de neurones, complétez les informations suivantes :

### Structure d'un réseau de neurones pour la reconnaissance de chiffres manuscrits (MNIST)

| Couche | Nombre de neurones | Fonction d'activation recommandée |
|--------|-------------------|----------------------------------|
| Couche d'entrée | _______ | _______ |
| Première couche cachée | _______ | _______ |
| Deuxième couche cachée (facultative) | _______ | _______ |
| Couche de sortie | _______ | _______ |

### Processus d'apprentissage

Décrivez brièvement les étapes du processus d'apprentissage d'un réseau de neurones :

1. _________________________________________________________________

2. _________________________________________________________________

3. _________________________________________________________________

4. _________________________________________________________________

### Réflexion personnelle

Comment expliqueriez-vous maintenant le fonctionnement d'un réseau de neurones à un camarade qui n'a jamais étudié ce sujet ?

_________________________________________________________________

_________________________________________________________________

_________________________________________________________________

### Auto-évaluation

Sur une échelle de 1 à 5, évaluez votre niveau de compréhension actuel des éléments suivants :

- Structure d'un neurone : ___/5
- Fonctions d'activation : ___/5
- Architecture d'un réseau : ___/5
- Processus d'apprentissage : ___/5
```

Ce contenu complète le document sur l'anatomie d'un réseau de neurones, en ajoutant les cellules 12 à 19 qui manquaient dans la version originale.