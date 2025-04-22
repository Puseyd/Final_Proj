import pygame
import sys
from board import Board

pygame.init()

WIDTH, HEIGHT = 600, 650
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sudoku")

FONT = pygame.font.SysFont("timesnewroman", 32)
BIG_FONT = pygame.font.SysFont("timesnewroman", 48)

def draw_start_screen():
    screen.fill("white")
    title = BIG_FONT.render("Sudoku Game", True, "black")
    screen.blit(title, (WIDTH//2 - title.get_width()//2, 50))

    easy_btn = pygame.Rect(WIDTH//2 - 100, 150, 200, 50)
    med_btn = pygame.Rect(WIDTH//2 - 100, 225, 200, 50)
    hard_btn = pygame.Rect(WIDTH//2 - 100, 300, 200, 50)

    for btn, text in [(easy_btn, "Easy"), (med_btn, "Medium"), (hard_btn, "Hard")]:
        pygame.draw.rect(screen, "lightgray", btn)
        label = FONT.render(text, True, "black")
        screen.blit(label, (btn.centerx - label.get_width()//2, btn.centery - label.get_height()//2))

    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if easy_btn.collidepoint(x, y):
                    return "easy"
                elif med_btn.collidepoint(x, y):
                    return "medium"
                elif hard_btn.collidepoint(x, y):
                    return "hard"

def draw_end_screen(success):
    screen.fill("white")
    text = "You Win!" if success else "Incorrect Solution!"
    label = BIG_FONT.render(text, True, "green" if success else "red")
    screen.blit(label, (WIDTH//2 - label.get_width()//2, 150))

    restart_btn = pygame.Rect(WIDTH//2 - 100, 250, 200, 50)
    exit_btn = pygame.Rect(WIDTH//2 - 100, 325, 200, 50)

    for btn, text in [(restart_btn, "Restart"), (exit_btn, "Exit")]:
        pygame.draw.rect(screen, "lightgray", btn)
        label = FONT.render(text, True, "black")
        screen.blit(label, (btn.centerx - label.get_width()//2, btn.centery - label.get_height()//2))

    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if restart_btn.collidepoint(x, y):
                    return True
                elif exit_btn.collidepoint(x, y):
                    pygame.quit(); sys.exit()

def draw_buttons():
    reset = pygame.Rect(30, 605, 120, 40)
    restart = pygame.Rect(240, 605, 120, 40)
    exit_game = pygame.Rect(450, 605, 120, 40)
    for rect, text in [(reset, "Reset"), (restart, "Restart"), (exit_game, "Exit")]:
        pygame.draw.rect(screen, "lightgray", rect)
        label = FONT.render(text, True, "black")
        screen.blit(label, (rect.centerx - label.get_width()//2, rect.centery - label.get_height()//2))
    return reset, restart, exit_game

def game_loop(difficulty):
    board = Board(600, 600, screen, difficulty)
    running = True

    while running:
        screen.fill("white")
        board.draw()
        reset_btn, restart_btn, exit_btn = draw_buttons()
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if reset_btn.collidepoint(x, y):
                    board.reset_to_original()
                elif restart_btn.collidepoint(x, y):
                    return True
                elif exit_btn.collidepoint(x, y):
                    pygame.quit(); sys.exit()
                elif y < 600:
                    pos = board.click(x, y)
                    if pos:
                        row, col = pos
                        board.select(row, col)

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    row, col = board.selected_cell if board.selected_cell else (None, None)
                    if row is not None and board.cells[row][col].sketched:
                        board.place_number(board.cells[row][col].sketched)
                        if board.is_full():
                            if board.check_board():
                                if draw_end_screen(True):
                                    return True
                            else:
                                if draw_end_screen(False):
                                    return True
                elif event.key == pygame.K_BACKSPACE or event.key == pygame.K_DELETE:
                    board.clear()
                elif event.unicode.isdigit():
                    value = int(event.unicode)
                    if 1 <= value <= 9:
                        board.sketch(value)

def main():
    while True:
        difficulty = draw_start_screen()
        if not game_loop(difficulty):
            break

if __name__ == "__main__":
    main()
