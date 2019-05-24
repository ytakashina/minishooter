from enemy import Enemy
from player import Player


def generate_board(w, h):
    return [["□" for i in range(w)] for j in range(h)]


class GameBoard:
    def __init__(self, w: int = 10, h: int = 10):
        self.w = w
        self.h = h
        self.board = generate_board(self.w, self.h)
        self.player = Player(5, 5, hp=5)
        self.objects = [self.player]
        for i in range(0, self.w, 2):
            enemy = Enemy(i, 1, hp=1)
            self.objects.append(enemy)

    def update(self, user_input):
        self.player.update(self, user_input)
        for obj in self.objects:
            obj.update(self)
        for obj1 in self.objects:
            if not obj1.is_alive():
                continue
            for obj2 in self.objects:
                if obj1 is not obj2 and obj2.is_alive() and obj1.intersects(obj2):
                    obj1.hp -= 1
                    obj2.hp -= 1

    def draw(self):
        self.board = generate_board(self.w, self.h)
        for obj in self.objects:
            obj.draw(self.board)
        print("\n".join(["".join(line) for line in self.board]))
        print("\n")
