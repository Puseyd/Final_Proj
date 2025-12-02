import random
from math import sqrt
from copy import deepcopy


class SudokuGenerator:
    def __init__(self, size, removed_cells):
        self.size = size
        self.box_size = int(sqrt(size))
        self.removed_cells = removed_cells
        self.board = [[0 for _ in range(size)] for _ in range(size)]
        self.solution_board = None

    def get_board(self):
        return self.board

    def print_board(self):
        for row in self.board:
            print(' '.join(map(str, row)))
        print()

    def valid_in_row(self, row, num):
        for col in range(self.size):
            if self.board[row][col] == num:
                return False
        return True

    def valid_in_col(self, col, num):
        for row in range(self.size):
            if self.board[row][col] == num:
                return False
        return True

    def valid_in_box(self, row_start, col_start, num):
        for r in range(row_start, row_start + self.box_size):
            for c in range(col_start, col_start + self.box_size):
                if self.board[r][c] == num:
                    return False
        return True

    def is_valid(self, row, col, num):
        if not self.valid_in_row(row, num):
            return False
        if not self.valid_in_col(col, num):
            return False
        box_row_start = (row // self.box_size) * self.box_size
        box_col_start = (col // self.box_size) * self.box_size
        if not self.valid_in_box(box_row_start, box_col_start, num):
            return False
        return True

    def fill_box(self, row_start, col_start):
        numbers = list(range(1, self.size + 1))
        random.shuffle(numbers)
        k = 0
        for r in range(row_start, row_start + self.box_size):
            for c in range(col_start, col_start + self.box_size):
                self.board[r][c] = numbers[k]
                k += 1

    def fill_diagonal(self):
        for i in range(0, self.size, self.box_size):
            self.fill_box(i, i)

    def fill_remaining(self, row, col):
        # Move to next row
        if col == self.size:
            row += 1
            col = 0

        # BC: Board is filled
        if row == self.size:
            return True

        # Skips any diagonal boxes
        if row < self.box_size and col < self.box_size:
            col = self.box_size
        elif row < 2 * self.box_size:
            if col == (row // self.box_size) * self.box_size:
                col = col + self.box_size
        elif col == self.size - self.box_size:
            row += 1
            col = 0
            if row == self.size:
                return True

        # Skips the already filled cells
        if self.board[row][col] != 0:
            return self.fill_remaining(row, col + 1)

        # Try numbers 1 to size
        for num in range(1, self.size + 1):
            if self.is_valid(row, col, num):
                self.board[row][col] = num
                if self.fill_remaining(row, col + 1):
                    return True
                self.board[row][col] = 0  # Backtrack

        return False

    def fill_values(self):
        self.fill_diagonal()
        self.fill_remaining(0, self.box_size)
        self.solution_board = deepcopy(self.board)

    def remove_cells(self):
        count = self.removed_cells
        while count > 0:
            row = random.randint(0, self.size - 1)
            col = random.randint(0, self.size - 1)
            if self.board[row][col] != 0:
                self.board[row][col] = 0
                count -= 1


def generate_sudoku(size, removed_cells):
    generator = SudokuGenerator(size, removed_cells)
    generator.fill_values()
    generator.remove_cells()
    return generator.board, generator.solution_board