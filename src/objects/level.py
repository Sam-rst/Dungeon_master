import numpy as np
import random

class Level:

    def __init__(self, maxWidth: int, maxHeight: int, nbEnnemies: int):
        self.maxWidth = maxWidth
        self.maxHeight = maxHeight
        self.nbEnnemies = nbEnnemies
        self.playerPos = [2, 2]
        self.playerIsAlive = True

        self.level = self.generate()

    def __str__(self):
        """Retourne une représentation en chaîne du niveau."""
        output = []
        for row in self.level:  # Utiliser self.level pour afficher le niveau généré
            row_output = []
            for cell in row:
                # Déterminer l'affichage basé sur la valeur de la cellule
                match cell:
                    case 1:
                        row_output.append('🧱')  # Mur
                    case 0:
                        row_output.append('  ')  # Cellule vide
                    case 5:
                        row_output.append('🧌 ')  # Troll
                    case 8:
                        row_output.append('🥷 ')  # Ninja
            output.append(''.join(row_output))  # Joindre les éléments de chaque ligne
        return '\n'.join(output)  # Retourner le niveau sous forme de chaîne avec des sauts de ligne

    def generate(self):
        """
        - Créé une liste vide
        - Remplis 20 fois cette liste avec un nombre aléatoire ``1`` ``(équivalent de → ennemi)`` ou ``0`` `(équivalent de salle vide)`
        - Retourne la liste
        """
        
        #1er étape : Générer un tableau rempli de 1 (murs) selon les dimensions du niveau
        level = np.ones((self.maxHeight, self.maxWidth), dtype=int)  # Créer un tableau 2D rempli de 1 (murs)

        #2e étape : Remplir l'intérieur du niveau par des 0 (cellule vide)
        level[1:-1, 1:-1] = 0

        #2e étape : Générer un labyrinthe "simple"
        for i in range(1, self.maxHeight - 1):
            for j in range(1, self.maxWidth - 1):
                if np.random.rand() < 0.3:  # 30% de chance de mettre un mur
                    level[i, j] = 1  # Remplacer par un mur

        #3e étape : Assurer le spawn du joueur dans le coin gauche de la carte
        level[1:4, 1:4] = 0

        #4e étape : Faire spawn le joueur
        level[self.playerPos[0], self.playerPos[1]] = 8
        
        #5e étape : Faire spawn les trolls
        for _ in range(self.nbEnnemies):
            troll_pos = [random.randint(1, self.maxWidth-1), random.randint(1, self.maxHeight-1)]
            level[troll_pos[0], troll_pos[1]] = 5

        return level

    def determinateNextCell(self, new_player_pos):
        return self.level[self.playerPos[0] + new_player_pos[0], self.playerPos[1] + new_player_pos[1]]
    
    def surviveAgainstTheTroll(self):
        # Une chance sur 6 de perdre contre un troll
        return random.randint(1, 6) != 1
    
    def changePlayerPosition(self, new_player_pos):
        # On efface dans la matrice la position du joueur temporairement
        self.level[self.playerPos[0], self.playerPos[1]] = 0
        
        # On change la position du joueur
        self.playerPos[0] += new_player_pos[0]
        self.playerPos[1] += new_player_pos[1]

        # On ajoute dans la matrice la nouvelle position du joueur
        self.level[self.playerPos[0], self.playerPos[1]] = 8

    def movePlayer(self, new_player_pos):
        match self.determinateNextCell(new_player_pos):
            case 0:
                self.changePlayerPosition(new_player_pos)
                return "Déplacement réussi !"
            case 1:
                return "Vous ne pouvez pas vous déplacer ici !"
            case 5:
                if self.surviveAgainstTheTroll():
                    self.changePlayerPosition(new_player_pos)
                    return "Attention, vous venez de tomber sur un monstre mais vous venez d'y survivre !"
                else:
                    self.changePlayerPosition(new_player_pos)
                    self.level[self.playerPos[0], self.playerPos[1]] = 8
                    self.playerIsAlive = False
                    return "Dommage, vous venez de perdre contre le troll !"
def main():
    level = Level(20, 20, 6)
    print(level)
    print(level.playerPos)
    level.movePlayer([0, -1])
    print(level.playerPos)
    print(level)

if __name__ == "__main__":
    main()