from scripts.generer_niveau import generer_niveau
from scripts.traverse_niveau import traverse_niveau
from time import time

def main():
    nombre_test = 2000
    moyenne = 0

    start = time()
    for _ in range(nombre_test):
        won = False
        compteur = 0
        while not won:
            niveau = generer_niveau()
            compteur += 1
            won = traverse_niveau(niveau)
        moyenne += compteur
        # print(f"Jeu terminé ! {compteur} niveaux avant de réussir !")

    end = time()
    print(f"\n\n\nJeu terminé ! {moyenne / nombre_test} niveaux traversés en moyenne avant de réussir en {end - start} secondes !")
    


if __name__ == "__main__":
    main()
    