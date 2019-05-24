from readchar import readchar

from game_board import GameBoard

if __name__ == '__main__':
    game_board = GameBoard(20, 10)
    print("WASD to move.")
    print("SPACE to shoot.")
    print("x to close.")
    print("Push any key to start!")
    while True:
        user_input = readchar().decode(encoding='utf-8')
        game_board.update(user_input)
        game_board.draw()
        if user_input == "x":
            exit(0)
