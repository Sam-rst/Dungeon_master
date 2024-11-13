from random import randint
import numpy as np

class Player:
    def __init__(self):
        self.locatedAt = np.array([1, 1])

    def move(self, direction: str):
        newLocation = self.locatedAt
        if direction == "up" :
            newLocation[1] = newLocation[1]-1
        elif direction == "down" :
            newLocation[1] = newLocation[1]+1
        elif direction == "left" :
            newLocation[0] = newLocation[0]-1
        elif direction == "right" :
            newLocation[0] = newLocation[0]+1
        else:
            print("I didn't understood")
        self.locatedAt = newLocation
        return self.locatedAt

# thePlayer = Player()

# thePlayer.move("down")
# thePlayer.move("down")
# thePlayer.move("right")
# thePlayer.move("down")

# print(thePlayer.locatedAt)