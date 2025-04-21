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
        self.cells = []
        self.initialize_cells()

    def initialize_cells(self):
        for row in range(9):
            self.cells.append([])
            for col in range(9):
                value = self.board[row][col]
                cell = Cell(self.width, self.height, self.screen, value, row, col)
                self.cells[row].append(cell)

    def draw(self):
        for row in self.cells:
            for cell in row:
                cell.draw()

        for row in range(10):
            width = 4 if row % 3 == 0 else 1
            pygame.draw.line(self.screen, "BLACK", (0, row * self.row_size), (self.width, row * self.row_size), width)

        for col in range(10):
            width = 4 if col % 3 == 0 else 1
            pygame.draw.line(self.screen, "BLACK", (col * self.col_size, 0), (col * self.col_size, self.height), width)
