from random import randint
# from importations import level
import numpy as np

class Player:

    def __init__(self):
        self.keyboard = {
            "up": "z",
            "left": "q",
            "down": "s",
            "right": "d"
        }
        self.locatedAt = np.array([1, 1])
        # self.level = level()

    def move(self):
        nextTileCoords = self.getDirection()
        
        self.locatedAt = nextTileCoords
        return self.locatedAt

    def getDirection(self):
        direction = "none"
        newLocation = self.locatedAt
        actionInput = input("Action (Z, Q, S, D, ...):")
        if actionInput in self.keyboard.values() :
            direction = list(self.keyboard.keys())[list(self.keyboard.values()).index(actionInput)]
        else:
            print("I didn't understood")
        if direction == "up" :
            newLocation[1] = newLocation[1]-1
        elif direction == "down" :
            newLocation[1] = newLocation[1]+1
        elif direction == "left" :
            newLocation[0] = newLocation[0]-1
        elif direction == "right" :
            newLocation[0] = newLocation[0]+1
        return newLocation

thePlayer = Player()
while True:
    thePlayer.move()
    print(thePlayer.locatedAt)