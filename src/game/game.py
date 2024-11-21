import os
from objects.level import Level
from engine.input import InputHandler

class Game:
    def __init__(self, width, height, nbEnnemies):
        self.level = Level(maxWidth=width, maxHeight=height, nbEnnemies=nbEnnemies)
        self.input_handler = InputHandler()

        self.message = ""

        self.running = True

    def run(self):
        while self.level.playerIsAlive:
            self.render()
            self.handle_events()

        print(self.message)

    def handle_events(self):
        res = False
        while not res:
            res = self.input_handler.get_position()

        self.message = self.level.movePlayer(res)

    def render(self):
        # Logique de rendu
        os.system('cls')
        print(self.level)
        print(self.message)

def main():
    level = Level(20, 20, 6)
    print(level)
    print(level.playerPos)
    level.movePlayer([0, -1])
    print(level.playerPos)
    print(level)

if __name__ == "__main__":
    main()