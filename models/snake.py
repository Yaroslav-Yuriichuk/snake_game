import time
import pygame
from models.colors import Color


class Snake:

    def __init__(self, board):
        self.FPS = 100
        self.LINES_CNT = 5

        self.RUN = True

        self.snake = [(int(board.SQ_CNT/2), int(board.SQ_CNT/2))]
        self.d_x, self.d_y = 0, -1

    def move_snake(self, board, eat=False):
        """
        move snake by one square
        depending if it eats or no
        """

        clock = pygame.time.Clock()
        lines_drawn = 0

        if not eat:
            if len(self.snake) > 1:  # length > 1 and doesn't eat

                head_next_x, head_next_y = self.snake[0][0]+self.d_x, self.snake[0][1]+self.d_y
                last_next_x, last_next_y = self.snake[-2][0], self.snake[-2][1]

                # next head coordinates to insert in snake
                if head_next_x == -1:
                    head_next_x = board.SQ_CNT-1
                elif head_next_x == board.SQ_CNT:
                    head_next_x = 0
                elif head_next_y == -1:
                    head_next_y = board.SQ_CNT-1
                elif head_next_y == board.SQ_CNT:
                    head_next_y = 0

                # finding coord for last snake part if it's crossing the board(to find d_x, d_y properly for last part)
                if abs(last_next_y-self.snake[-1][1]) > 1:
                    if last_next_y == board.SQ_CNT-1:
                        last_next_y = -1
                    elif last_next_y == 0:
                        last_next_y = board.SQ_CNT
                elif abs(last_next_x-self.snake[-1][0]) > 1:
                    if last_next_x == board.SQ_CNT-1:
                        last_next_x = -1
                    elif last_next_x == 0:
                        last_next_x = board.SQ_CNT

                head_x1_c, head_y1_c, head_x2_c, head_y2_c = board.find_start_coord_for_line(
                    self.snake[0][0],
                    self.snake[0][1],
                    self.d_x,
                    self.d_y)
                last_x1_c, last_y1_c, last_x2_c, last_y2_c = board.find_start_coord_for_line(
                    2*self.snake[-1][0]-last_next_x,
                    2*self.snake[-1][1]-last_next_y,
                    last_next_x-self.snake[-1][0],
                    last_next_y-self.snake[-1][1])

                last_time = time.time()

                while lines_drawn < board.SQ_SIZE:

                    time_now = time.time()
                    dt = time_now - last_time
                    last_time = time_now
                    lines_to_draw = round(self.FPS*dt*self.LINES_CNT)

                    if lines_to_draw > board.SQ_SIZE - lines_drawn:
                        lines_to_draw = board.SQ_SIZE - lines_drawn

                    for i in range(lines_to_draw):
                        board.draw_line_in_square(Color.YELLOW.value, last_x1_c, last_y1_c, last_x2_c, last_y2_c)
                        board.draw_line_in_square(Color.RED.value, head_x1_c, head_y1_c, head_x2_c, head_y2_c)
                        head_x1_c += self.d_x
                        head_x2_c += self.d_x
                        head_y1_c += self.d_y
                        head_y2_c += self.d_y
                        last_x1_c += last_next_x-self.snake[-1][0]
                        last_x2_c += last_next_x-self.snake[-1][0]
                        last_y1_c += last_next_y-self.snake[-1][1]
                        last_y2_c += last_next_y-self.snake[-1][1]

                    lines_drawn += lines_to_draw

                    clock.tick(self.FPS)

                self.snake.insert(0, (head_next_x, head_next_y))
                self.snake.pop()

            else:  # length = 1 and doesn't eat

                head_next_x, head_next_y = self.snake[0][0]+self.d_x, self.snake[0][1]+self.d_y

                # next head coord to insert in snake
                if head_next_x == -1:
                    head_next_x = board.SQ_CNT-1
                elif head_next_x == board.SQ_CNT:
                    head_next_x = 0
                elif head_next_y == -1:
                    head_next_y = board.SQ_CNT-1
                elif head_next_y == board.SQ_CNT:
                    head_next_y = 0

                head_x1_c, head_y1_c, head_x2_c, head_y2_c = board.find_start_coord_for_line(
                    self.snake[0][0],
                    self.snake[0][1],
                    self.d_x,
                    self.d_y)
                last_x1_c, last_y1_c, last_x2_c, last_y2_c = board.find_start_coord_for_line(
                    self.snake[0][0]-self.d_x,
                    self.snake[0][1]-self.d_y,
                    self.d_x,
                    self.d_y)

                last_time = time.time()

                while lines_drawn < board.SQ_SIZE:

                    time_now = time.time()
                    dt = time_now - last_time
                    last_time = time_now
                    lines_to_draw = round(self.FPS*dt*self.LINES_CNT)

                    if lines_to_draw > board.SQ_SIZE - lines_drawn:
                        lines_to_draw = board.SQ_SIZE - lines_drawn

                    for i in range(lines_to_draw):
                        board.draw_line_in_square(Color.RED.value, head_x1_c, head_y1_c, head_x2_c, head_y2_c)
                        board.draw_line_in_square(Color.YELLOW.value, last_x1_c, last_y1_c, last_x2_c, last_y2_c)
                        head_x1_c += self.d_x
                        head_x2_c += self.d_x
                        head_y1_c += self.d_y
                        head_y2_c += self.d_y
                        last_x1_c += self.d_x
                        last_x2_c += self.d_x
                        last_y1_c += self.d_y
                        last_y2_c += self.d_y

                    lines_drawn += lines_to_draw
                    clock.tick(self.FPS)

                self.snake.insert(0, (head_next_x, head_next_y))
                self.snake.pop()

        else:  # eats

            head_next_x, head_next_y = self.snake[0][0]+self.d_x, self.snake[0][1]+self.d_y

            # next head coord to insert in snake
            if head_next_x == -1:
                head_next_x = board.SQ_CNT-1
            elif head_next_x == board.SQ_CNT:
                head_next_x = 0
            elif head_next_y == -1:
                head_next_y = board.SQ_CNT-1
            elif head_next_y == board.SQ_CNT:
                head_next_y = 0

            head_x1_c, head_y1_c, head_x2_c, head_y2_c = board.find_start_coord_for_line(
                self.snake[0][0],
                self.snake[0][1],
                self.d_x,
                self.d_y)

            last_time = time.time()

            while lines_drawn < board.SQ_SIZE:

                time_now = time.time()
                dt = time_now - last_time
                last_time = time_now
                lines_to_draw = round(self.FPS*dt*self.LINES_CNT)

                if lines_to_draw > board.SQ_SIZE - lines_drawn:
                    lines_to_draw = board.SQ_SIZE - lines_drawn

                for i in range(lines_to_draw):
                    board.draw_line_in_square(Color.RED.value, head_x1_c, head_y1_c, head_x2_c, head_y2_c)
                    head_x1_c += self.d_x
                    head_x2_c += self.d_x
                    head_y1_c += self.d_y
                    head_y2_c += self.d_y

                lines_drawn += lines_to_draw
                clock.tick(self.FPS)

            self.snake.insert(0, (head_next_x, head_next_y))

    def make_step(self, board, drop):
        """
        do one iteration:
        1. decide if eat drop
        2. bump into myself
        3. just move
        """

        next_x, next_y = self.snake[0][0]+self.d_x, self.snake[0][1]+self.d_y

        if next_x == -1:
            next_x = board.SQ_CNT-1
        elif next_x == board.SQ_CNT:
            next_x = 0
        elif next_y == -1:
            next_y = board.SQ_CNT-1
        elif next_y == board.SQ_CNT:
            next_y = 0

        # eat drop
        if next_x == drop.drop_x and next_y == drop.drop_y:
            self.move_snake(board, True)
            if drop.create_drop(self, board):
                drop.display_drop(board)
            else:
                self.RUN = False

        # bump into myseslf
        elif (next_x, next_y) in self.snake:
                    self.RUN = False

        # nothing of above
        else:
            self.move_snake(board)

    def display_snake(self, board):
        """
        draw snake
        """

        for (x, y) in self.snake:
            board.draw_square(Color.RED.value, x, y)
