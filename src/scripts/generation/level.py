import numpy as np

class Level:

    def __init__(self, maxWidth, maxHeight):
        self.maxWidth = maxWidth
        self.maxHeight = maxHeight
        self.level = self.generate()

    def __str__(self):
        return f"{self.level}"

    def generate(self):
        """
        - Créé une liste vide
        - Remplis 20 fois cette liste avec un nombre aléatoire ``1`` ``(équivalent de → ennemi)`` ou ``0`` `(équivalent de salle vide)`
        - Retourne la liste
        """
        row = np.random.randint(0, 2, self.maxWidth)
        level = np.array([row for _ in range(self.maxHeight)])
        return level

def main():
    level = Level(20, 20)
    level.generate()

if __name__ == "__main__":
    main()