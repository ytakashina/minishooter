from game_object import GameObject


class Enemy(GameObject):
    def __init__(self, x: int, y: int, hp: int):
        super().__init__(x, y, hp=hp, symbol="■")

    def update(self, board):
        if not self.on_board(board):
            self.die()
