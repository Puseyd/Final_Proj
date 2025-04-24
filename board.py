import pygame
from cell import Cell
from sudoku_generator import generate_sudoku

class Board:
    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty
        self.selected_cell = None
        self.original = []
        self.board = []
        self.solution = []

        difficulty_map = {"easy": 30, "medium": 40, "hard": 50}
        removed = difficulty_map.get(difficulty, 30)
      
        self.board = generate_sudoku(9, removed)
        self.original = [[self.board[r][c] for c in range(9)] for r in range(9)]
        self.cells = [[Cell(width, height, screen, self.board[r][c], r, c)
                       for c in range(9)] for r in range(9)]

    def draw(self):
        for row in range(10):
            line_width = 4 if row % 3 == 0 else 1
            pygame.draw.line(self.screen, "BLACK", (0, row * self.height / 9), (self.width, row * self.height / 9), line_width)
        for col in range(10):
            line_width = 4 if col % 3 == 0 else 1
            pygame.draw.line(self.screen, "BLACK", (col * self.width / 9, 0), (col * self.width / 9, self.height), line_width)

        for row in self.cells:
            for cell in row:
                cell.draw()

    def select(self, row, col):
        if self.selected_cell:
            r, c = self.selected_cell
            self.cells[r][c].selected = False
        self.selected_cell = (row, col)
        self.cells[row][col].selected = True

    def click(self, x, y):
        if 0 <= x < self.width and 0 <= y < self.height:
            row = int(y // (self.height / 9))
            col = int(x // (self.width / 9))
            return row, col
        return None

    def clear(self):
        if self.selected_cell:
            row, col = self.selected_cell
            if self.original[row][col] == 0:
                self.cells[row][col].set_cell_value(0)
                self.cells[row][col].set_sketched_value(None)

    def sketch(self, value):
        if self.selected_cell:
            row, col = self.selected_cell
            if self.original[row][col] == 0:
                self.cells[row][col].set_sketched_value(value)

    def place_number(self, value):
        if self.selected_cell:
            row, col = self.selected_cell
            if self.original[row][col] == 0:
                self.cells[row][col].set_cell_value(value)
                self.cells[row][col].set_sketched_value(None)

    def reset_to_original(self):
        for r in range(9):
            for c in range(9):
                self.cells[r][c].set_cell_value(self.original[r][c])
                self.cells[r][c].set_sketched_value(None)

    def is_full(self):
        for row in self.cells:
            for cell in row:
                if cell.value == 0:
                    return False
        return True

    def update_board(self):
        for r in range(9):
            for c in range(9):
                self.board[r][c] = self.cells[r][c].value

    def find_empty(self):
        for r in range(9):
            for c in range(9):
                if self.cells[r][c].value == 0:
                    return (r, c)
        return None

    def check_board(self):
        for row in range(9):
            values = set()
            for col in range(9):
                val = self.cells[row][col].value
                if val in values or val == 0:
                    return False
                values.add(val)

        for col in range(9):
            values = set()
            for row in range(9):
                val = self.cells[row][col].value
                if val in values or val == 0:
                    return False
                values.add(val)

        for box_row in range(0, 9, 3):
            for box_col in range(0, 9, 3):
                values = set()
                for r in range(3):
                    for c in range(3):
                        val = self.cells[box_row + r][box_col + c].value
                        if val in values or val == 0:
                            return False
                        values.add(val)
        return True
