import pygame

class Cell:
    def __init__(self, width, height, screen, value, row, col):
        self.cell_width = width / 9
        self.cell_height = height / 9
        self.font = pygame.font.SysFont("timesnewroman", int(min(self.cell_width, self.cell_height) * .7))
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen
        self.sketched = None
        self.selected = False
    def set_cell_value(self, value):
        self.value = value
    def set_sketched_value(self, value):
        self.sketched = value
    def draw(self):
        text_surface = self.font.render(str(self.value), True, (0,0,0))
        x_cord = self.col*self.cell_width + (self.cell_width / 2)
        y_cord = self.row*self.cell_height + (self.cell_height / 2)
        text_rect = text_surface.get_rect(center=((x_cord, y_cord)))
        self.screen.blit(text_surface, text_rect)
