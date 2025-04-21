import pygame
from board import Board

def main():
    pygame.init()
    width, height = 600, 600
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Sudoku")
    running = True

    board = Board(width, height, screen, difficulty=30)  # 可以调整 30 为更难或更简单

    clock = pygame.time.Clock()

    while running:
        screen.fill("white")
        board.draw()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
