# Dungeon Master

**Dungeon Master** est un jeu RPG d'exploration de donjon. Plongez dans un univers palpitant, affrontez des monstres et découvrez des trésors cachés !

Projet réalisé par Samuel RESSIOT et Maxime DUSSORT.

## Fonctionnalités
- ⚔️ Combattez des ennemis redoutables. (Pas tant que ça..)
- 🗺️ Explorez des donjons générés dynamiquement. (De superbes niveaux vous attendent)
- 💎 Collectionnez des objets et des trésors rares. (Huuum, pas si sûr..)
- 📖 Une aventure immersive avec une histoire captivante. (Oh.. bah alors là..)

## Prérequis
- **Python 3.8+** doit être installé sur votre système.
- Une connexion Internet est nécessaire pour cloner le projet.

---

## Installation

Clonez le projet et configurez l'environnement virtuel pour garantir une expérience isolée :  

```bash
# Clone du dépôt
git clone git@github.com:Sam-rst/Dungeon_master.git
cd Dungeon_master

# Création de l'environnement virtuel
python -m venv env

# Activation de l'environnement virtuel
# Sur Windows :
env\Scripts\activate

# Sur Linux/MacOS :
source env/bin/activate

# Installation des dépendances
pip install -r requirements.txt
```

---

## Lancement

Accédez au dossier contenant les fichiers sources, puis exécutez le jeu :  

```bash
cd src/
python main.py
```

---

## Structure du projet

Voici une vue d'ensemble de la structure du projet :

```
Dungeon_master/
├── src/
│   ├── main.py       # Point d'entrée du jeu
│   │
│   ├── engine/       # Moteur de  jeu
│   │   ├── input.py  # Gestion des entrées pour les déplacements
│   │   └── ...       # Autres logiques du jeu
│   ├── game/
│   │   ├── game.py   # Coeur central du projet
│   │   └── ...       # Autres objets du jeu
│   ├── objects/
│   │   ├── level.py  # Définition des niveaux
│   │   └── ...       # Autres objets du jeu
│   └── ...
│
├── requirements.txt  # Liste des dépendances Python
├── README.md         # Documentation du projet
└── env/              # Environnement virtuel (à créer)
```


## À venir
- 🔮 Nouveaux sorts magiques.
- 🧙‍♂️ Personnages jouables supplémentaires.
- 🏰 Extensions avec des donjons plus complexes.

Amusez-vous bien ! 🎮