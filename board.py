import pygame
from cell import Cell
from sudoku_generator import generate_sudoku

class Board:
    def __init__(self, width, height, screen, difficulty):
        #intialize variables
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty

        #conditional to determine difficulty level
        if difficulty == "easy":
            removed = 30
        elif difficulty == "medium":
            removed = 40
        else:
            removed = 50

        temp = generate_sudoku(9, removed)

        self.board = temp[0]
        self.solution = temp[1]

        self.original = []

        for row in self.board:
            new_row = row[:]  # make a copy of the row
            self.original.append(new_row)

        self.cells = []

        for i in range(9):
            row = []

            for j in range(9):
                cell = Cell(self.board[i][j], i, j, screen)
                row.append(cell)

            self.cells.append(row)

    def draw(self):
        gap = self.width / 9

        for i in range(10):
            if i % 3 == 0:
                thickness = 4
            else:
                thickness = 1

            pygame.draw.line(self.screen, (0, 0, 0), (0, i * gap), (self.width, i * gap), thickness)
            pygame.draw.line(self.screen, (0, 0, 0), (i * gap, 0), (i * gap, self.height), thickness)

        for row in self.cells:
            for cell in row:
                cell.draw()

    def select(self, row, col):
        for r in self.cells:
            for cell in r:
                cell.selected = False
        self.cells[row][col].selected = True
        self.selected = (row, col)

    def click(self, x, y):

        if x < self.width and y < self.height:
            gap = self.width / 9
            row = int(y // gap)
            col = int(x // gap)
            return row, col
        return None

    def clear(self):
        if self.selected:
            row, col = self.selected
            if self.original[row][col] == 0:
                self.cells[row][col].set_cell_value(0)
                self.cells[row][col].set_sketched_value(0)

    def sketch(self, value):
        row, col = self.selected
        self.cells[row][col].set_sketched_value(value)

    def place_number(self, value):
        row, col = self.selected
        if self.original[row][col] == 0:
            self.cells[row][col].set_cell_value(value)
            self.cells[row][col].set_sketched_value(0)

    def reset_to_original(self):
        for i in range(9):
            for j in range(9):
                self.cells[i][j].set_cell_value(self.original[i][j])
                self.cells[i][j].set_sketched_value(0)

    def is_full(self):
        for row in self.cells:
            for cell in row:
                if cell.value == 0:
                    return False
        return True

    def check_board(self):
        for i in range(9):
            for j in range(9):
                if self.cells[i][j].value != self.solution[i][j]:
                    return False
        return True