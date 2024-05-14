from prettytable import PrettyTable

from LexiTek.main.language_map import ui
from LexiTek.main.letters import get_value, pop_one


BOARD_SIZE = 15


def place_word(board, word, direction, x, y, player_letters, letters, language):
    if not (0 <= x < BOARD_SIZE and 0 <= y < BOARD_SIZE):
        return ui[language]['error_1']

    if direction == 'horizontal' and x + len(word) > BOARD_SIZE:
        return ui[language]['error_2']
    elif direction == 'vertical' and y + len(word) > BOARD_SIZE:
        return ui[language]['error_3']

    if not is_word_placeable(board, word, direction, x, y):
        return ui[language]['error_4']

    if not is_word_compatible(board, word, direction, x, y):
        return ui[language]['error_5']

    if direction == 'horizontal':
        for i in range(len(word)):
            letter = word[i]
            board[y][x + i] = letter
            player_letters.remove(letter)
            letter = pop_one(letters)
            if letter is not None:
                player_letters.append(letter)
    elif direction == 'vertical':
        for i in range(len(word)):
            letter = word[i]
            board[y + i][x] = letter
            player_letters.remove(letter)
            letter = pop_one(letters)
            if letter is not None:
                player_letters.append(letter)

    return True


def is_word_placeable(board, word, direction, x, y):
    if direction == 'horizontal':
        if x + len(word) > BOARD_SIZE:
            return False
        for i in range(len(word)):
            if board[x + 1][y] != '':
                return False
    elif direction == 'vertical':
        if y + len(word) > BOARD_SIZE:
            return False
        for i in range(len(word)):
            if board[x][y + i] != '':
                return False
    return True


def is_word_compatible(board, word, direction, x, y):
    if direction == 'horizontal':
        for i in range(len(word)):
            if board[y][x + i] != '' and board[y][x + i] != word[i]:
                return False
    elif direction == 'vertical':
        for i in range(len(word)):
            if board[y + i][x] != '' and board[y + i][x] != word[i]:
                return False
    return True


def is_centered(word, direction, x, y):
    if direction == 'horizontal':
        if (x <= 7 < x + len(word)) and (y == 7):
            return True
    elif direction == 'vertical':
        if (y <= 7 < y + len(word)) and (x == 7):
            return True
    return False


def display_player_pool(pool):
    for letter in pool:
        print(f"{letter.capitalize()}", end="\t")
    print()
    for letter in pool:
        print(f"{get_value(letter)}", end="\t")
    print()


def display_board(board):
    table = PrettyTable()

    # Add column headers
    table.field_names = [" "] + [f"{i+1:<2}" for i in range(BOARD_SIZE)]

    # Add rows with delimiters
    for i, row in enumerate(board):
        row_content = []
        for j, cell in enumerate(row):
            if i == j == BOARD_SIZE // 2:  # Check if the cell is the center cell
                row_content.append(f"{cell if cell else '*':<2}")
            else:
                row_content.append(f"{cell if cell else ' ':<2}")
        table.add_row([f"{i+1:<2}"] + row_content)
        if i != BOARD_SIZE - 1:  # Don't add a delimiter after the last row
            table.add_row(["-"] * (BOARD_SIZE + 1))  # Add a delimiter row

    print(table)