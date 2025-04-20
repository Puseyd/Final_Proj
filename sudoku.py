import pygame
from board import *
from cell import *

def main():
    width = 600
    height = 600
    try:
        pygame.init()
        screen = pygame.display.set_mode((width, height))
        running = True
        board = Board(width,height, screen, 0)
        cell = Cell(width, height, screen, 0, 0, 0)
        cell1 = Cell(width, height, screen, 1, 1, 1)
        cell2 = Cell(width, height, screen, 4, 8, 8)

        while running:
            screen.fill("white")
            board.draw()
            cell.draw()
            cell1.draw()
            cell2.draw()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            pygame.display.flip()


    finally:
        pygame.quit()

if __name__ == "__main__":
    main()