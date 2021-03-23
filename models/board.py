from models.colors import Color
import pygame


class Board:

    def __init__(self):
        self.SQ_SIZE = 50
        self.SQ_CNT = 12

        self.THICKNESS = 1
        self.WIDTH = self.HEIGHT = self.SQ_SIZE*self.SQ_CNT + self.THICKNESS*(self.SQ_CNT+1)  # 613

        self.win = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Snake")

    def draw_grid(self, update=True):
        """
        fill background with yellow and draw grid
        with black lines
        """

        self.win.fill(Color.YELLOW.value)
        for i in range(0, self.WIDTH, self.SQ_SIZE+self.THICKNESS):
            pygame.draw.line(self.win, Color.BLACK.value, (i, 0), (i, self.HEIGHT), self.THICKNESS)
            pygame.draw.line(self.win, Color.BLACK.value, (0, i), (self.WIDTH, i), self.THICKNESS)

        if update:
            pygame.display.update()

    def draw_square(self, color, x, y):
        """
        draw square with chosen color
        """

        pygame.draw.rect(
            self.win,
            color,
            (x*(self.SQ_SIZE+self.THICKNESS)+self.THICKNESS,
                y*(self.SQ_SIZE+self.THICKNESS)+self.THICKNESS,
                self.SQ_SIZE,
                self.SQ_SIZE))
        pygame.display.update()

    def draw_line_in_square(self, color, x1, y1, x2, y2):
        """
        draw line with given coordinates
        used to movement look smooth
        """

        pygame.draw.line(self.win, color, (x1, y1), (x2, y2), self.THICKNESS)
        pygame.display.update()

    def find_start_coord_for_line(self, x, y, d_x, d_y):
        """
        find coordinates for line to be drawn
        depending on square coordinates(0..11, 0..11)
        and snake movement direction
        """

        next_x, next_y = x+d_x, y+d_y

        if next_x == -1:
            x = self.SQ_CNT
        elif next_x == self.SQ_CNT:
            x = -1
        elif next_y == -1:
            y = self.SQ_CNT
        elif next_y == self.SQ_CNT:
            y = -1

        if d_x == 0 and d_y == -1:
            next_x1_c = x*(self.SQ_SIZE+self.THICKNESS)+self.THICKNESS
            next_y1_c = y*(self.SQ_SIZE+self.THICKNESS)-self.THICKNESS
            next_x2_c = next_x1_c+self.SQ_SIZE-1
            next_y2_c = next_y1_c
            return next_x1_c, next_y1_c, next_x2_c, next_y2_c

        elif d_x == 0 and d_y == 1:
            next_x1_c = x*(self.SQ_SIZE+self.THICKNESS)+self.THICKNESS
            next_y1_c = (y+1)*(self.SQ_SIZE+self.THICKNESS)+self.THICKNESS
            next_x2_c = next_x1_c+self.SQ_SIZE-1
            next_y2_c = next_y1_c
            return next_x1_c, next_y1_c, next_x2_c, next_y2_c

        elif d_x == -1 and d_y == 0:
            next_x1_c = x*(self.SQ_SIZE+self.THICKNESS)-self.THICKNESS
            next_y1_c = y*(self.SQ_SIZE+self.THICKNESS)+self.THICKNESS
            next_x2_c = next_x1_c
            next_y2_c = next_y1_c+self.SQ_SIZE-1
            return next_x1_c, next_y1_c, next_x2_c, next_y2_c

        elif d_x == 1 and d_y == 0:
            next_x1_c = (x+1)*(self.SQ_SIZE+self.THICKNESS)+self.THICKNESS
            next_y1_c = y*(self.SQ_SIZE+self.THICKNESS)+self.THICKNESS
            next_x2_c = next_x1_c
            next_y2_c = next_y1_c+self.SQ_SIZE-1
            return next_x1_c, next_y1_c, next_x2_c, next_y2_c
