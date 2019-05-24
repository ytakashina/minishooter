from game_object import GameObject


class Bullet(GameObject):
    def __init__(self, x: int, y: int, vx: int, vy: int):
        self.vx = vx
        self.vy = vy
        super().__init__(x, y, hp=1, symbol="●")

    def update(self, board):
        self.x += self.vx
        self.y += self.vy
        if not self.on_board(board):
            self.die()
