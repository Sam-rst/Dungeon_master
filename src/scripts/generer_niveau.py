import numpy as np

def generer_niveau():
    """
    - Créé une liste vide
    - Remplis 20 fois cette liste avec un nombre aléatoire ``1`` ``(équivalent de → ennemi)`` ou ``0`` `(équivalent de salle vide)`
    - Retourne la liste
    """
    return np.random.randint(0, 2, 20)