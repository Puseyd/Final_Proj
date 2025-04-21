import pygame
from board import Board

def main():
    pygame.init()
    screen = pygame.display.set_mode((600, 600))
    pygame.display.set_caption("Sudoku")
    board = Board(600, 600, screen, "easy")

    running = True
    while running:
        screen.fill("white")
        board.draw()
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()

if __name__ == "__main__":
    main()
