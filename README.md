# Jeu de Dames avec Intelligence Artificielle

## 🎯 Objectif du programme

Développer un **jeu de dames** en Python, accompagné d'une **IA capable de battre n'importe quel joueur humain**.

## ♟️ Règles du jeu implémenté

- Damier de **8 x 8 cases**.
- Chaque joueur commence avec **12 pions**.
- **Chaque joueur joue un coup par tour**, avec **un seul pion**.
- Les pions se déplacent **en diagonale**, **vers l'avant**, **sur les cases foncées**.
- Un pion peut capturer un adversaire en **sautant au-dessus**, si la **case suivante est vide**.
- **Captures multiples obligatoires** si elles sont possibles après une première capture.
- Lorsqu’un pion atteint la dernière rangée, il devient une **dame** :
  - Elle peut se déplacer et capturer **aussi en arrière**.
  - Les autres règles restent les mêmes.
- si un joueur ne plus jouer alors il perd la partie

## 🛠️ Technologies utilisées

- **Python**
- **IA avec l'algorithme Minimax**
- Utilisation ponctuelle de **l'IA générative** pour aider à la conception

## 🧠 Fonctionnement de l’IA

L’IA utilise **l’algorithme Minimax** pour choisir le meilleur coup selon les critères suivants :

- Maximiser la **différence de score** entre l'IA et l’adversaire
- Évaluation :
  - 1 point par **pion**
  - 1,5 point par **dame**

## 🧱 Architecture du projet

- ├── main.py # Point d'entrée du programme
- └── game/
- ├── init.py # Initialise le package
- ├── game.py # Logique du jeu
- └── utilities.py # Fonctions utilitaires


## 🎮 Ce que permet le programme

- Jouer à un **jeu de dames complet**, codé en Python
- Affronter une **IA imbattable**

## ⚠️ Problèmes rencontrés

- Tentative de développement initial via **Flask** pour créer une interface graphique, abandonnée par manque de temps
- **Conflits GitHub** (clashs, commits, création de répertoires inutiles)
- Difficulté à intégrer **l’apprentissage par renforcement**
  - Malgré cela, une **IA fonctionnelle** a été implantée

## 🚀 Améliorations futures

- Intégrer **l’apprentissage par renforcement** pour entraîner l’IA
- Rendre l’IA **plus rapide** et plus performante
- Ajouter d'autres variantes du **jeu de dames**, voire du **jeu d'échecs**
- 

---

Projet réalisé dans le cadre d'un travail collaboratif autour d'un centre d'intérêt commun : **les jeux de stratégie**.
