from game.game import Game

def main():
    game = Game(width=20, height=20, nbEnnemies=6)
    game.run()

if __name__ == "__main__":
    main()
