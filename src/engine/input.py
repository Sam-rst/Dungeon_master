
class InputHandler:
    def __init__(self):
        pass

    def get_position(self):
        """Retourne les déplacements du joueur basés sur les touches pressées."""
        key = input("Veuillez appuyer sur (z : ⬆️, q : ⬅️, s : ⬇️, d : ➡️) : ")
        match key:
            case "z":
                return [-1, 0]
            case "q":
                return [0, -1]
            case "s":
                return [1, 0]
            case "d":
                return [0, 1]
            case _:
                return False
