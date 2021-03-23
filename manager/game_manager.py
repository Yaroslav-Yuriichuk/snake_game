from models.colors import Color
import pygame
import time


class GameManager:

    def __init__(self, board, snake, drop):
        self.GAME_AGAIN = True
        self.RESTART = False
        self.GAME_CLOSED = False

        self.SCORE_FONT_SIZE = 151
        self.RESTART_FONT_SIZE = self.EXIT_FONT_SIZE = self.CONTINUE_FONT_SIZE = 69

        self.FONT_FPS = 100
        self.NUMBER_FONT_SIZE = 600
        self.NUMBER_FONT_DECR = 6

        self.board = board
        self.snake = snake
        self.drop = drop

        pygame.init()

    def play(self):
        """
        main method to start the game
        and run game until it's closed
        """

        while self.GAME_AGAIN and not self.GAME_CLOSED:
            self.start_round()

    def start_round(self):
        """
        method that starts another round
        """

        if not self.GAME_CLOSED:
            # intializing variables
            self.snake.snake = [(int(self.board.SQ_CNT/2), int(self.board.SQ_CNT/2))]
            self.snake.d_x, self.snake.d_y = 0, -1
            self.drop.drop_x, self.drop.drop_y = int(self.board.SQ_CNT/2), int(self.board.SQ_CNT/2)
            self.snake.RUN = True
            self.RESTART = False

            self.show_countdown()

            if not self.GAME_CLOSED:
                self.board.draw_grid()

                # draw initial snake
                self.snake.display_snake(self.board)

                # create first drop
                self.drop.create_drop(self.snake, self.board)
                self.drop.display_drop(self.board)

                self.run_game_loop()

                if not self.GAME_CLOSED:
                    self.show_score_and_wait_for_choise()

    def show_score_and_wait_for_choise(self):
        """
        show score and wait for choise:
        1. close game
        2. restart
        """

        if not self.RESTART:
            score_font = pygame.font.Font(None, self.SCORE_FONT_SIZE)
            restart_font = pygame.font.Font(None, self.RESTART_FONT_SIZE)
            exit_font = pygame.font.Font(None, self.EXIT_FONT_SIZE)

            score_text = score_font.render(f"Score: {len(self.snake.snake)}", True, Color.DARK_BLUE.value)
            restart_text = restart_font.render("Press R to restart", True, Color.DARK_BLUE.value)
            exit_text = exit_font.render("Press Esc to exit", True, Color.DARK_BLUE.value)

            score_place = score_text.get_rect(center=(
                int(self.board.WIDTH/2)+1,
                int(self.board.HEIGHT/2)+1-int(self.board.HEIGHT/8)))
            restart_place = restart_text.get_rect(center=(
                int(self.board.WIDTH/2)+1,
                int(self.board.HEIGHT/2)+1 +
                int(self.SCORE_FONT_SIZE/2) +
                int(self.RESTART_FONT_SIZE/2) -
                int(self.board.HEIGHT/8)))
            exit_place = exit_text.get_rect(center=(
                int(self.board.WIDTH/2)+1,
                int(self.board.HEIGHT/2)+1 +
                int(self.SCORE_FONT_SIZE/2) +
                int(3*self.EXIT_FONT_SIZE/2) -
                int(self.board.HEIGHT/8)))

            self.board.win.blit(score_text, score_place)
            self.board.win.blit(restart_text, restart_place)
            self.board.win.blit(exit_text, exit_place)
            pygame.display.update()

            exit_run = True
            while exit_run:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        exit_run = False
                        self.GAME_CLOSED = True
                    elif event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                        exit_run = False
                    elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                        self.GAME_AGAIN = False
                        exit_run = False
                        pygame.quit()

    def put_game_on_pause(self):
        """
        pause game and wait for choise:
        1. continue
        2. restart
        3. close game
        """

        pause_font = pygame.font.Font(None, self.SCORE_FONT_SIZE)
        restart_font = pygame.font.Font(None, self.RESTART_FONT_SIZE)
        continue_font = pygame.font.Font(None, self.CONTINUE_FONT_SIZE)
        exit_font = pygame.font.Font(None, self.EXIT_FONT_SIZE)

        pause_text = pause_font.render("Pause", True, Color.DARK_BLUE.value)
        restart_text = restart_font.render("Press R to restart", True, Color.DARK_BLUE.value)
        continue_text = continue_font.render("Press Enter to continue", True, Color.DARK_BLUE.value)
        exit_text = exit_font.render("Press Esc to exit", True, Color.DARK_BLUE.value)

        pause_place = pause_text.get_rect(center=(
            int(self.board.WIDTH/2)+1,
            int(self.board.HEIGHT/2)+1-int(self.board.HEIGHT/8)))
        restart_place = restart_text.get_rect(center=(
            int(self.board.WIDTH/2)+1,
            int(self.board.HEIGHT/2)+1 +
            int(self.SCORE_FONT_SIZE/2) +
            int(self.RESTART_FONT_SIZE/2) -
            int(self.board.HEIGHT/8)))
        continue_place = continue_text.get_rect(center=(
            int(self.board.WIDTH/2)+1,
            int(self.board.HEIGHT/2)+1 +
            int(self.SCORE_FONT_SIZE/2) +
            int(3*self.EXIT_FONT_SIZE/2) -
            int(self.board.HEIGHT/8)))
        exit_place = exit_text.get_rect(center=(
            int(self.board.WIDTH/2)+1,
            int(self.board.HEIGHT/2)+1 +
            int(self.SCORE_FONT_SIZE/2) +
            int(5*self.EXIT_FONT_SIZE/2) -
            int(self.board.HEIGHT/8)))

        self.board.win.blit(pause_text, pause_place)
        self.board.win.blit(restart_text, restart_place)
        self.board.win.blit(continue_text, continue_place)
        self.board.win.blit(exit_text, exit_place)
        pygame.display.update()

        pause_run = True
        while pause_run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pause_run = False
                    self.GAME_CLOSED = True
                    pygame.quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pause_run = False
                        pygame.quit()
                    elif event.key == pygame.K_RETURN:
                        pause_run = False
                        self.board.draw_grid()
                        self.snake.display_snake(self.board)
                        self.drop.display_drop(self.board)
                    elif event.key == pygame.K_r:
                        pause_run = False
                        self.snake.RUN = False
                        self.RESTART = True

    def show_countdown(self):
        """
        show coundown by drawing deminishing numbers 3, 2, 1
        """

        self.draw_number_smooth('3', self.NUMBER_FONT_SIZE)

        if not self.GAME_CLOSED:
            self.draw_number_smooth('2', self.NUMBER_FONT_SIZE)

        if not self.GAME_CLOSED:
            self.draw_number_smooth('1', self.NUMBER_FONT_SIZE)

    def draw_number_smooth(self, number, font_size):
        """
        draw deminishing number
        """

        clock = pygame.time.Clock()

        last_time = time.time()

        while font_size > 0:

            self.board.draw_grid(False)

            time_now = time.time()
            dt = time_now - last_time
            last_time = time_now
            font_decr = round(dt*self.FONT_FPS*self.NUMBER_FONT_DECR)

            number_font = pygame.font.Font(None, font_size)
            number_text = number_font.render(number, True, Color.DARK_BLUE.value)
            number_place = number_text.get_rect(center=(int(self.board.WIDTH/2)+1, int(self.board.HEIGHT/2)+1))
            self.board.win.blit(number_text, number_place)
            pygame.display.update()
            font_size -= font_decr

            clock.tick(self.FONT_FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.GAME_CLOSED = True
                    font_size = -1
                    pygame.quit()

    def run_game_loop(self):
        """
        control actions and snake movements
        while game is running
        """

        while self.snake.RUN:

            self.snake.make_step(self.board, self.drop)

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    self.GAME_CLOSED = True
                    self.snake.RUN = False
                    pygame.quit()

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.put_game_on_pause()
                    else:
                        if event.key == pygame.K_UP:
                            if not (self.snake.d_x == 0 and self.snake.d_y == 1):
                                self.snake.d_x, self.snake.d_y = 0, -1
                                break
                        elif event.key == pygame.K_DOWN:
                            if not (self.snake.d_x == 0 and self.snake.d_y == -1):
                                self.snake.d_x, self.snake.d_y = 0, 1
                                break
                        elif event.key == pygame.K_LEFT:
                            if not(self.snake.d_x == 1 and self.snake.d_y == 0):
                                self.snake.d_x, self.snake.d_y = -1, 0
                                break
                        elif event.key == pygame.K_RIGHT:
                            if not(self.snake.d_x == -1 and self.snake.d_y == 0):
                                self.snake.d_x, self.snake.d_y = 1, 0
                                break
