import pygame
#11/30/25
#Author(s): David Pusey, Akhilesh Devamadhavan
#This class represents a single cell in the Sudoku board. There are 81 Cells in a Board.

class Cell:
    #pygame is initialized once in the main method.
    def __init__(self, value, row, col, screen):
        self.value = value
        self.sketched_value = 0
        self.row = row
        self.col = col
        self.screen = screen
        self.selected = False

    def set_cell_value(self, value):
        self.value = value

    def set_sketched_value(self, value):
        self.sketched_value = value

    def draw(self):
        font = pygame.font.SysFont("comicsans", 40)  #Play around with sizes later. Half the size for the sketch image
        x = self.col * 60 #Transforms the chosen row and col into coordinates corresponding to the size of the board being 540 pixels.
        y = self.row * 60

        if self.value != 0:
            #Draw the cell along with the number in it.
            text = font.render(str(self.value), True, (0, 0, 0))
            self.screen.blit(text, (x + 20, y + 10))

        elif self.sketched_value != 0:
            #Draw the cell, number in gray, in top left corner of cell.
            sketch_font = pygame.font.SysFont("comicsans", 20)
            text = sketch_font.render(str(self.sketched_value), True, (128, 128, 128))
            self.screen.blit(text, (x + 5, y + 5))
        # No need to w empty cell if these conditionals fail, if not, the sudoku_generator handles the drawing of the cell.
        if self.selected: #Changes the border of the selected cell to red. Based on where teh the cursor is.

            pygame.draw.rect(self.screen, (255, 0, 0), (x, y, 60, 60), 3)
