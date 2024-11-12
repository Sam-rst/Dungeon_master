from random import randint

def traverse_niveau(niveau: list[int]) -> int:
    vie = 1
    for salle in niveau:
        dice = randint(1, 6)
        if salle == 1 and (dice > 0 and dice < 4):
            vie -= 1
            if vie <= 0:
                return False
    return True
