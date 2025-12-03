#Sudoku inherits Board. Board inherits cell.
import pygame
from board import Board
pygame.init()

WIDTH = 540
HEIGHT = 650
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sudoku")

FONT = pygame.font.SysFont("Arial", 40)
SMALL_FONT = pygame.font.SysFont("Arial", 28)

# Simple button class for menus and in-game controls
class Button:
    def __init__(self, x, y, w, h, text):
        self.rect = pygame.Rect(x, y, w, h)
        self.text = text

    def draw(self):
        pygame.draw.rect(WIN, (0, 0, 0), self.rect, 2)
        label = SMALL_FONT.render(self.text, True, (0, 0, 0))
        WIN.blit(label, (self.rect.x + 10, self.rect.y + 10))

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)

# Start menu allowing the player to choose difficulty before the game begins
def start_menu():
    easy = Button(180, 200, 180, 50, "Easy")
    medium = Button(180, 280, 180, 50, "Medium")
    hard = Button(180, 360, 180, 50, "Hard")

    run = True
    while run:
        WIN.fill((255, 255, 255))
        title = FONT.render("Select Difficulty", True, (0, 0, 0))
        welcome = FONT.render("Welcome to Sudoku!", True, (0,0,0))
        WIN.blit(welcome, (125,50))
        WIN.blit(title, (155, 115))

        easy.draw()
        medium.draw()
        hard.draw()

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if easy.is_clicked(pos):
                    return "easy"
                if medium.is_clicked(pos):
                    return "medium"
                if hard.is_clicked(pos):
                    return "hard"

# Final screen shown when the player wins or loses, includes restart/exit buttons
def end_screen(message):
    restart = Button(200, 350, 150, 50, "Restart")
    exit_btn = Button(200, 420, 150, 50, "Exit")

    run = True
    while run:
        WIN.fill((255, 255, 255))
        msg = FONT.render(message, True, (0, 0, 0))
        WIN.blit(msg, (175, 200))


        restart.draw()
        exit_btn.draw()

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if restart.is_clicked(pos):
                    return "restart"
                if exit_btn.is_clicked(pos):
                    pygame.quit()
                    quit()

# Main gameplay loop: draws board, handles input, updates game state
def main():
    difficulty = start_menu()
    board = Board(540, 540, WIN, difficulty)

    reset_btn = Button(20, 560, 150, 50, "Reset")
    restart_btn = Button(195, 560, 150, 50, "Restart")
    exit_btn = Button(370, 560, 150, 50, "Exit")

    run = True
    while run:
        WIN.fill((255, 255, 255))
        board.draw()

        reset_btn.draw()
        restart_btn.draw()
        exit_btn.draw()

        pygame.display.update()

        if board.is_full():
            if board.check_board():
                result = end_screen("You Win!")
            else:
                result = end_screen("Game Over")

            if result == "restart":
                main()
                return

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()

                if reset_btn.is_clicked(pos):
                    board.reset_to_original()

                if restart_btn.is_clicked(pos):
                    main()
                    return

                if exit_btn.is_clicked(pos):
                    run = False

                clicked = board.click(pos[0], pos[1])
                if clicked:
                    board.select(clicked[0], clicked[1])

            if event.type == pygame.KEYDOWN:
                if board.selected:

                    if event.key == pygame.K_1:
                        board.sketch(1)
                    if event.key == pygame.K_2:
                        board.sketch(2)
                    if event.key == pygame.K_3:
                        board.sketch(3)
                    if event.key == pygame.K_4:
                        board.sketch(4)
                    if event.key == pygame.K_5:
                        board.sketch(5)
                    if event.key == pygame.K_6:
                        board.sketch(6)
                    if event.key == pygame.K_7:
                        board.sketch(7)
                    if event.key == pygame.K_8:
                        board.sketch(8)
                    if event.key == pygame.K_9:
                        board.sketch(9)

                    if event.key == pygame.K_RETURN:
                        row, col = board.selected
                        value = board.cells[row][col].sketched_value
                        board.place_number(value)


                    if event.key == pygame.K_BACKSPACE:
                        board.clear()

    pygame.quit()

if __name__ == "__main__":
    main()



