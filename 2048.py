import pygame
import sys
import numpy as np
import random

# Inicjalizacja pygame.
pygame.init()

# Stałe dla gry.
SCREEN_SIZE = 500
BOARD_SIZE = 4
TILE_SIZE = SCREEN_SIZE // BOARD_SIZE
BACKGROUND_COLOR = (187, 173, 160)
TILE_COLORS = {2: (238, 228, 218), 4: (237, 224, 200), 8: (242, 177, 121),
               16: (245, 149, 99), 32: (246, 124, 95), 64: (246, 94, 59),
               128: (237, 207, 114), 256: (237, 204, 97), 512: (237, 200, 80),
               1024: (237, 197, 63), 2048: (237, 194, 46)}
programIcon = pygame.image.load('dist/images/icon.png')
font = pygame.font.Font('dist/fonts/Roboto-Regular.ttf', 26)
fontSmall = pygame.font.Font('dist/fonts/Roboto-Regular.ttf', 18)
score = 0

# Inicjalizacja planszy.
board = np.zeros((BOARD_SIZE, BOARD_SIZE), dtype=int)

# Konfiguracja ekranu.
screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
pygame.display.set_icon(programIcon)
pygame.display.set_caption('2048')

# Funkcja odpowiedzialna za dodawanie nowej płytki na planszy.


def add_new_tile():
    empty_positions = [(r, c) for r in range(BOARD_SIZE)
                       for c in range(BOARD_SIZE) if board[r][c] == 0]
    if not empty_positions:
        return
    row, col = random.choice(empty_positions)
    board[row][col] = 2 if random.random() < 0.9 else 4


# Funkcja sprawdza, czy istnieją płytki, które mogą zostać połączone.


def can_combine_tiles():
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            tile = board[row][col]
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                r, c = row + dr, col + dc
                if 0 <= r < BOARD_SIZE and 0 <= c < BOARD_SIZE and board[r][c] == tile:
                    return True
    return False

# Funkcja określa czy gra została zakończona.


def is_game_over():
    return np.all(board != 0) and not can_combine_tiles()

# Funkcja sprawdz czy grał wygrał, tj. osiągnął kafelek 2048.


def has_won():
    return 2048 in board

# Aktualizowanie wyniku.


def update_score(value):
    global score
    score += value


# Funckja łączy płytki.


def combine_tiles(row):
    new_row = [i for i in row if i != 0]
    combined = []
    skip = False
    for i in range(len(new_row)):
        if skip:
            skip = False
            continue
        if i + 1 < len(new_row) and new_row[i] == new_row[i + 1]:
            combined.append(2 * new_row[i])
            update_score(2 * new_row[i])
            skip = True
        else:
            combined.append(new_row[i])
    combined += [0] * (BOARD_SIZE - len(combined))
    return combined

# Funkcja obłsuguje logikę przesuwania płytek w zadanym kierunku.


def move_tiles(direction):
    global board
    moved = False
    for i in range(BOARD_SIZE):
        if direction in ['LEFT', 'RIGHT']:
            row = board[i, :]
            if direction == 'RIGHT':
                row = row[::-1]
            combined_row = combine_tiles(row)
            if direction == 'RIGHT':
                combined_row = combined_row[::-1]
            if not all(board[i, :] == combined_row):
                moved = True
            board[i, :] = combined_row
        else:
            col = board[:, i]
            if direction == 'DOWN':
                col = col[::-1]
            combined_col = combine_tiles(col)
            if direction == 'DOWN':
                combined_col = combined_col[::-1]
            if not all(board[:, i] == combined_col):
                moved = True
            board[:, i] = combined_col
    if moved:
        add_new_tile()

# Funkcja obsługuje interakcje klawiszy klikanych przez użytkownika.


def handle_input(event):
    if event.key == pygame.K_LEFT:
        move_tiles('LEFT')
    elif event.key == pygame.K_RIGHT:
        move_tiles('RIGHT')
    elif event.key == pygame.K_UP:
        move_tiles('UP')
    elif event.key == pygame.K_DOWN:
        move_tiles('DOWN')

# Funkcja rysuje interfejs użytkownika, w tym planszę gry i wynik, gdy gracz wygrał rysuję odpowiednią wiadomość i możliwość resetowania gry, tak samo w przypadku przegranej.


def draw_ui():
    screen.fill(BACKGROUND_COLOR)
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            value = board[row][col]
            tile_color = TILE_COLORS.get(value, BACKGROUND_COLOR)
            pygame.draw.rect(screen, tile_color, (col * TILE_SIZE,
                             row * TILE_SIZE, TILE_SIZE, TILE_SIZE))
            if value:
                text_surface = font.render(f'{value}', True, (0, 0, 0))
                text_rect = text_surface.get_rect(
                    center=((col + 0.5) * TILE_SIZE, (row + 0.5) * TILE_SIZE))
                screen.blit(text_surface, text_rect)
    score_text = fontSmall.render(f'Wynik: {score}', True, (0, 0, 0))
    screen.blit(score_text, (10, SCREEN_SIZE - 30))

    message = ""
    sub_message = "Wciśnij enter, aby kontynuować."

    if has_won():
        message = f'Wygrałeś! Twój wynik: {score}'
    elif is_game_over():
        message = f'Przegrałeś! Twój wynik: {score}'

    if message:
        main_text = font.render(message, True, (0, 0, 0))
        sub_text = font.render(sub_message, True, (0, 0, 0))

        main_text_rect = main_text.get_rect(
            center=(SCREEN_SIZE // 2, SCREEN_SIZE // 2 - 20))
        sub_text_rect = sub_text.get_rect(
            center=(SCREEN_SIZE // 2, SCREEN_SIZE // 2 + 20))

        overlay_surface = pygame.Surface(
            (SCREEN_SIZE, SCREEN_SIZE), pygame.SRCALPHA)
        overlay_surface.fill((255, 255, 255, 180))

        overlay_surface.blit(main_text, main_text_rect)
        overlay_surface.blit(sub_text, sub_text_rect)

        screen.blit(overlay_surface, (0, 0))

    pygame.display.update()

# Funkcja resetowania gry.


def reset_game():
    global board, score
    score = 0
    board = np.zeros((BOARD_SIZE, BOARD_SIZE), dtype=int)
    add_new_tile()


# Funkcja pokazująca ekran startowy.

def show_start_screen():
    start = False
    while not start:
        screen.fill(BACKGROUND_COLOR)
        start_text = font.render(
            'Wciśnij spacje, aby wystartować', True, (0, 0, 0))
        text_rect = start_text.get_rect(
            center=(SCREEN_SIZE // 2, SCREEN_SIZE // 2))
        screen.blit(start_text, text_rect)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    start = True


# Funkcja main z główną petla gry.


def main():
    show_start_screen()  # Pokazuje ekran startowy
    running = True
    add_new_tile()  # Start gry z jednym kafelkiem.
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if not is_game_over():
                    handle_input(event)  # Interacja użytkownika
                elif event.key == pygame.K_RETURN:
                    reset_game()  # Resetowanie gry
        draw_ui()  # Rysowanie interfejsu

    # Zakończenie programu.

    pygame.quit()
    sys.exit()


# Start gry.


if __name__ == "__main__":
    main()
