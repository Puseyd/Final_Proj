import pygame

class Board:
    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty
        self.row_size = height / 9
        self.col_size = width / 9

    def draw(self):
        for row in range(9):
            width = 4 if row % 3 == 0 else 1
            pygame.draw.line(self.screen, "BLACK", (0, row * self.row_size), (self.width, row * self.row_size), width)
        for col in range(9):
            width = 4 if col % 3 == 0 else 1
            pygame.draw.line(self.screen, "BLACK", (col * self.col_size, 0), (col * self.col_size, self.height), width)
