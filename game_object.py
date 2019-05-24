class GameObject:
    def __init__(self, x: int, y: int, hp: int = 1, symbol: str = "■"):
        self.x = x
        self.y = y
        self.hp = hp
        self.symbol = symbol

    def update(self, board):
        raise NotImplementedError()

    def draw(self, board):
        if self.is_alive():
            board[self.y][self.x] = self.symbol

    def intersects(self, obj):
        return self.x == obj.x and self.y == obj.y

    def is_alive(self):
        return self.hp > 0

    def die(self):
        self.hp = 0

    def on_board(self, board):
        return 0 <= self.x < len(board.board[0]) and 0 <= self.y < len(board.board)
