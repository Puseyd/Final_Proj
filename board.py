import pygame
from cell import Cell
from sudoku_generator import generate_sudoku

class Board:
    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty
        self.row_size = height / 9
        self.col_size = width / 9
        self.board = generate_sudoku(9, difficulty)
        self.cells = [[Cell(width, height, screen, self.board[r][c], r, c) for c in range(9)] for r in range(9)]

    def draw(self):
        for row in range(10):
            line_width = 4 if row % 3 == 0 else 1
            pygame.draw.line(self.screen, "BLACK", (0, row*self.row_size), (self.width, row*self.row_size), line_width)
        for column in range(10):
            line_width = 4 if column % 3 == 0 else 1
            pygame.draw.line(self.screen, "BLACK", (column*self.col_size, 0), (column*self.col_size, self.height), line_width)
        for row in self.cells:
            for cell in row:
                cell.draw()
