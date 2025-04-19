import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 600, 600
LINE_WIDTH = 10
BOARD_ROWS, BOARD_COLS = 3, 3
SQUARE_SIZE = WIDTH // BOARD_COLS
CIRCLE_RADIUS = SQUARE_SIZE // 3
CIRCLE_WIDTH = 10
CROSS_WIDTH = 15
SPACE = 30

# Colors
BG_COLOR = (28, 170, 156)
LINE_COLOR = (23, 145, 135)
CIRCLE_COLOR = (239, 231, 200)
CROSS_COLOR = (66, 66, 66)
TEXT_COLOR = (255, 255, 255)

# Fonts
font = pygame.font.Font(None, 50)
input_font = pygame.font.Font(None, 40)

# Screen Setup
screen = pygame.display.set_mode((WIDTH, HEIGHT + 100))
pygame.display.set_caption("Tic-Tac-Toe")
screen.fill(BG_COLOR)

# Board
board = [[None] * BOARD_COLS for _ in range(BOARD_ROWS)]

# Player Names
player_names = ["", ""]
current_input = 0  # 0 -> Player 1, 1 -> Player 2
typing = True  # Name input mode

# Draw Grid Lines
def draw_lines():
    for i in range(1, BOARD_ROWS):
        pygame.draw.line(screen, LINE_COLOR, (0, i * SQUARE_SIZE), (WIDTH, i * SQUARE_SIZE), LINE_WIDTH)
        pygame.draw.line(screen, LINE_COLOR, (i * SQUARE_SIZE, 0), (i * SQUARE_SIZE, HEIGHT), LINE_WIDTH)

# Draw X and O
def draw_figures():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == "O":
                pygame.draw.circle(screen, CIRCLE_COLOR, 
                                   (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2), 
                                   CIRCLE_RADIUS, CIRCLE_WIDTH)
            elif board[row][col] == "X":
                startX = col * SQUARE_SIZE + SPACE
                startY = row * SQUARE_SIZE + SPACE
                endX = (col + 1) * SQUARE_SIZE - SPACE
                endY = (row + 1) * SQUARE_SIZE - SPACE
                pygame.draw.line(screen, CROSS_COLOR, (startX, startY), (endX, endY), CROSS_WIDTH)
                pygame.draw.line(screen, CROSS_COLOR, (startX, endY), (endX, startY), CROSS_WIDTH)

# Check Win Condition
def check_winner(player):
    for row in range(BOARD_ROWS):
        if all(cell == player for cell in board[row]):
            return True
    for col in range(BOARD_COLS):
        if all(board[row][col] == player for row in range(BOARD_ROWS)):
            return True
    if all(board[i][i] == player for i in range(BOARD_ROWS)) or all(board[i][BOARD_ROWS - 1 - i] == player for i in range(BOARD_ROWS)):
        return True
    return False

def display_winner(player):
    pygame.draw.rect(screen, BG_COLOR, (0, HEIGHT, WIDTH, 100))
    winner_name = player_names[0] if player == 'X' else player_names[1]
    text = font.render(f"{winner_name} Wins! Press 'R' to Restart", True, TEXT_COLOR)
    screen.blit(text, (WIDTH // 21, HEIGHT + 20))

# Show Turn Message
def display_turn():
    pygame.draw.rect(screen, BG_COLOR, (0, HEIGHT, WIDTH, 100))  # Clear message area
    turn_name = player_names[0] if player_turn == "X" else player_names[1]
    text = font.render(f"{turn_name}'s Turn", True, TEXT_COLOR)
    screen.blit(text, (WIDTH // 3, HEIGHT + 20))

# Restart Game
def restart():
    global board, player_turn, game_over, typing, current_input, player_names
    screen.fill(BG_COLOR)
    draw_lines()
    board = [[None] * BOARD_COLS for _ in range(BOARD_ROWS)]
    player_turn = "X"
    game_over = False
    player_names = ["", ""]
    typing = True
    current_input = 0

# Input Player Names
def input_names():
    screen.fill(BG_COLOR)
    text = font.render(f"Enter Player {current_input + 1} Name:", True, TEXT_COLOR)
    screen.blit(text, (WIDTH // 6, HEIGHT // 3))
    name_text = input_font.render(player_names[current_input], True, TEXT_COLOR)
    screen.blit(name_text, (WIDTH // 6, HEIGHT // 2))
    pygame.display.update()

# Game Loop
player_turn = "X"
game_over = False
draw_lines()

while True:
    if typing:
        input_names()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Handle Name Input
        if typing:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and player_names[current_input]:  # Enter pressed
                    current_input += 1
                    if current_input == 2:
                        typing = False  # Names entered, start game
                        screen.fill(BG_COLOR)
                        draw_lines()
                        display_turn()
                    else:
                        input_names()
                elif event.key == pygame.K_BACKSPACE:  # Delete last character
                    player_names[current_input] = player_names[current_input][:-1]
                elif len(player_names[current_input]) < 10:  # Limit name length
                    player_names[current_input] += event.unicode
            continue

        # Handle Clicks for Moves
        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mouseX, mouseY = event.pos
            if mouseY < HEIGHT:  # Ensure clicks are within board area
                clicked_row, clicked_col = mouseY // SQUARE_SIZE, mouseX // SQUARE_SIZE

                if board[clicked_row][clicked_col] is None:
                    board[clicked_row][clicked_col] = player_turn

                    if check_winner(player_turn):
                        display_winner(player_turn)
                        game_over = True
                    else:
                        player_turn = "O" if player_turn == "X" else "X"
                        display_turn()

        # Restart Game with 'R'
        if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
            restart()

    draw_figures()
    pygame.display.update()
