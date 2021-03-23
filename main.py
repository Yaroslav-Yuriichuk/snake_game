from manager.game_manager import GameManager
from models.drop import Drop
from models.snake import Snake
from models.board import Board


def main():

    board = Board()
    snake = Snake(board)
    drop = Drop(board)

    game_manager = GameManager(board, snake, drop)
    game_manager.play()

if __name__ == "__main__":
    main()
