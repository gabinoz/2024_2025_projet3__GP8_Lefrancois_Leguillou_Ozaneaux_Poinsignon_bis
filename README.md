Ce projet est une implémentation complète du jeu de dames en Python, avec une intelligence artificielle basée sur l'algorithme Minimax (avec élagage alpha-bêta) capable de battre n'importe quel joueur humain.

🕹️ Fonctionnalités
Plateau de dames 8x8 avec gestion complète des règles

Joueur humain contre IA

IA avec algorithme Minimax optimisé

Interface graphique basique

Système de promotion en dame, prises multiples, etc.

Niveau de difficulté ajustable (profondeur de l’arbre de recherche il faut modifier le "depth=..." dans le game.py ligne 263)

🧠 Algorithme IA : Minimax
Recherche récursive dans l'arbre des coups possibles

Évaluation des positions basée sur :

nombre de pions et dames

positionnement stratégique

mobilité

Élagage alpha-bêta pour améliorer les performances

Peut anticiper plusieurs coups à l’avance

📁 Structure du projet

checkers_ai/
│
├── main.py              # Lancement du jeu
├── board.py             # Gestion du plateau et des mouvements
├── game.py              # Logique de jeu
    ├── minimax.py           # Algorithme Minimax intégré au game.py└── README.md            # Ce fichier

🚀 Installation
Cloner le dépôt :

git clone https://github.com/gabinoz/2024_2025_projet3__GP8_Lefrancois_Leguillou_Ozaneaux_Poinsignon_bis

pip install pygame


▶️ Lancer le jeu

python main.py
executer le main.py



🏁 Objectif
Ce projet a pour but de :

Mettre en pratique des concepts d’IA (Minimax, heuristiques, élagage)

Créer une IA imbattable au jeu de dames

Développer une logique de jeu complexe de bout en bout


📚 Références
Algorithme Minimax : https://en.wikipedia.org/wiki/Minimax

Élagage Alpha-Bêta : https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning

Règles du jeu de dames : https://fr.wikipedia.org/wiki/Dames

🧑‍💻 Auteur
GP8 - Albert Leguillou - Gabin Ozaneaux - Maxence Lefrançois - Raphaël Poinsignon  


