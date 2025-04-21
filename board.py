import pygame
from cell import Cell
from sudoku_generator import generate_sudoku

class Board:
    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self.row_size = height / 9
        self.col_size = width / 9
        self.difficulty = difficulty

        difficulty_map = {"easy": 30, "medium": 40, "hard": 50}
        removed = difficulty_map.get(difficulty, 30)
        self.board = generate_sudoku(9, removed)
        self.cells = [[Cell(self.width, self.height, screen, self.board[r][c], r, c)
                       for c in range(9)] for r in range(9)]

    def draw(self):
        for row in range(9):
            width = 4 if row % 3 == 0 else 1
            pygame.draw.line(self.screen, "BLACK", (0, row*self.row_size), (self.width, row*self.row_size), width)
        for column in range(9):
            width = 4 if column % 3 == 0 else 1
            pygame.draw.line(self.screen, "BLACK", (column*self.col_size, 0), (column*self.col_size, self.height), width)

        for row in self.cells:
            for cell in row:
                cell.draw()
