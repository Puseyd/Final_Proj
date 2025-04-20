import pygame

class Board:
    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty
        self.row_size = height // 9
        self.col_size = width // 9
    def draw(self):
        for row in range(9):
            if (row) % 3 == 0:
                pygame.draw.line(self.screen, "BLACK", (0, row*self.row_size), (self.width, row*self.row_size), 4)
            pygame.draw.line(self.screen, "BLACK", (0, row*self.row_size), (self.width, row*self.row_size))
        for column in range(9):
            if (column) % 3 == 0:
                pygame.draw.line(self.screen, "BLACK", (column*self.col_size, 0), (column*self.col_size, self.height), 4)
            pygame.draw.line(self.screen, "BLACK", (column*self.col_size, 0), (column*self.col_size, self.height))