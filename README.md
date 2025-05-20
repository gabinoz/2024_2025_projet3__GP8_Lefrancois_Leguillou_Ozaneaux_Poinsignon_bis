Ce projet est une implémentation complète du jeu de dames en Python, avec une intelligence artificielle basée sur l'algorithme Minimax (avec élagage alpha-bêta) capable de battre n'importe quel joueur humain.

🕹️ Fonctionnalités
Plateau de dames 8x8 avec gestion complète des règles

Joueur humain contre IA

IA avec algorithme Minimax optimisé

Interface graphique (optionnel) ou version console

Système de promotion en dame, prises multiples, etc.

Niveau de difficulté ajustable (profondeur de l’arbre de recherche)

🧠 Algorithme IA : Minimax
Recherche récursive dans l'arbre des coups possibles

Évaluation des positions basée sur :

nombre de pions et dames

positionnement stratégique

mobilité

Élagage alpha-bêta pour améliorer les performances

Peut anticiper plusieurs coups à l’avance

📁 Structure du projet
bash
Copier
Modifier
checkers_ai/
│
├── main.py              # Lancement du jeu
├── board.py             # Gestion du plateau et des mouvements
├── game.py              # Logique de jeu
├── minimax.py           # Algorithme Minimax + alpha-bêta
├── ai.py                # Interface IA
├── gui.py               # Interface graphique (si utilisée)
└── README.md            # Ce fichier
🚀 Installation
Cloner le dépôt :

bash
Copier
Modifier
git clone https://github.com/tonpseudo/jeu-dames-python.git
cd jeu-dames-python
Installer les dépendances (si interface graphique) :

bash
Copier
Modifier
pip install pygame
▶️ Lancer le jeu
bash
Copier
Modifier
python main.py
🏁 Objectif
Ce projet a pour but de :

Mettre en pratique des concepts d’IA (Minimax, heuristiques, élagage)

Créer une IA imbattable au jeu de dames

Développer une logique de jeu complexe de bout en bout

📷 Captures d’écran (optionnel)
Ajoute ici des captures d’écran de ton interface ou de la console en action.

📚 Références
Algorithme Minimax : https://en.wikipedia.org/wiki/Minimax

Élagage Alpha-Bêta : https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning

Règles du jeu de dames : https://fr.wikipedia.org/wiki/Dames

🧑‍💻 Auteur
Ton Nom / Pseudo

Contact : ton@email.com
