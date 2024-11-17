import numpy as np

class Level:

    def __init__(self, maxWidth: int, maxHeight: int, nbEnnemies: int):
        self.maxWidth = maxWidth
        self.maxHeight = maxHeight
        self.nbEnnemies = nbEnnemies
        self.level = self.generate()

    def __str__(self):
        return f"{self.level}"

    def generate(self):
        """
        - Créé une liste vide
        - Remplis 20 fois cette liste avec un nombre aléatoire ``1`` ``(équivalent de → ennemi)`` ou ``0`` `(équivalent de salle vide)`
        - Retourne la liste
        """
        level = np.ones((self.maxWidth, self.maxHeight), dtype=int)
        level[1:-1, 1:-1] = 0 #Intérieur de la salle vide
        for _ in range(self.nbEnnemies):
            level[np.random.randint(1, self.maxWidth)-1:np.random.randint(1, self.maxHeight)-1, np.random.randint(1, self.maxWidth)-1:np.random.randint(1, self.maxHeight)-1] = 4 #Générer des monstres aléatoirement dans la salle
        level[2, 2] = 8

        return level

def main():
    level = Level(20, 20)
    print(level)

if __name__ == "__main__":
    main()