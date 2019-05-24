from game_object import GameObject
from bullet import Bullet

MOVES = {
    "d": (1, 0),
    "a": (-1, 0),
    "w": (0, -1),
    "s": (0, 1),
}


class Player(GameObject):
    def __init__(self, x: int, y: int, hp: int):
        super().__init__(x, y, hp=hp, symbol="▲")

    def update(self, board, user_input=""):
        move = MOVES.get(user_input)
        if move is not None:
            dx, dy = move
            self.x += dx
            self.y += dy
        if user_input == " ":
            bullet = self.shoot()
            board.objects.append(bullet)
        if not self.on_board(board):
            self.die()

    def die(self):
        print("You died!!")
        exit(0)

    def shoot(self):
        return Bullet(self.x, self.y - 1, 0, -1)
