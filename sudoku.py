import pygame
from board import Board

def main():
    width = 600
    height = 600
    difficulty = 30

    try:
        pygame.init()
        screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Sudoku")
        running = True

        board = Board(width, height, screen, difficulty)

        while running:
            screen.fill("white")
            board.draw()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    row = int(y // (height / 9))
                    col = int(x // (width / 9))
                    for r in board.cells:
                        for c in r:
                            c.selected = False
                    board.cells[row][col].selected = True

            pygame.display.flip()

    finally:
        pygame.quit()

if __name__ == "__main__":
    main()
