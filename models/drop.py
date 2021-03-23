import random
import pygame
from models.colors import Color


class Drop:

    def __init__(self, board):
        self.drop_x, self.drop_y = int(board.SQ_CNT/2), int(board.SQ_CNT/2)

    def create_drop(self, snake, board):
        """
        find out if drop can be created
        and create if yes
        """

        if len(snake.snake) == board.SQ_CNT ** 2:
            return False
        else:
            while (self.drop_x, self.drop_y) in snake.snake:
                self.drop_x, self.drop_y = random.randint(0, board.SQ_CNT-1), random.randint(0, board.SQ_CNT-1)

            return True

    def display_drop(self, board):
        """
        draw drop
        """

        board.draw_square(Color.GREEN.value, self.drop_x, self.drop_y)
