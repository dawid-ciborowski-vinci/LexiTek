from prettytable import PrettyTable

from language import ui, get_language
from letters import get_value, pop_one

BOARD_SIZE = 15


def place_word(board, word, direction, x, y, player_letters, letters):
    if direction == 'horizontal':
        for i in range(len(word)):
            letter = word[i]
            if board[y][x + i] == '':  # Only remove the letter from the player's pool if it's not already on the board
                player_letters.remove(letter)
                letter_to_add = pop_one(letters)
                print(letter_to_add)
                if letter_to_add is not None:
                    player_letters.append(letter_to_add)
            board[y][x + i] = letter
    elif direction == 'vertical':
        for i in range(len(word)):
            letter = word[i]
            if board[y + i][x] == '':  # Only remove the letter from the player's pool if it's not already on the board
                player_letters.remove(letter)
                letter_to_add = pop_one(letters)
                print(letter_to_add)
                if letter_to_add is not None:
                    player_letters.append(letter_to_add)
            board[y + i][x] = letter

    return True


def is_word_placeable(board, word, direction, x, y):
    if direction == 'horizontal':
        if x + len(word) > BOARD_SIZE:
            return False
        for i in range(len(word)):
            if board[y][x + i] != '' and board[y][x + i] != word[i]:
                return False
    elif direction == 'vertical':
        if y + len(word) > BOARD_SIZE:
            return False
        for i in range(len(word)):
            if board[y + i][x] != '' and board[y + i][x] != word[i]:
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


def is_adjacent_or_part(board, word, direction, x, y):
    dx, dy = (1, 0) if direction == 'horizontal' else (0, 1)
    touches_or_crosses = False
    for i in range(len(word)):
        # Check the cell itself
        if board[y + dy * i][x + dx * i] != '':
            touches_or_crosses = True
        # Check the surrounding cells
        else:
            for j in range(-1, 2):
                for k in range(-1, 2):
                    if 0 <= y + dy * i + j < BOARD_SIZE and 0 <= x + dx * i + k < BOARD_SIZE:
                        if board[y + dy * i + j][x + dx * i + k] != '':
                            touches_or_crosses = True
                            break
                if touches_or_crosses:
                    break
        if touches_or_crosses:
            break
    return touches_or_crosses


def display_player_pool(pool):
    table = PrettyTable(header=False)
    letters = [letter.upper() for letter in pool]
    values = [get_value(letter) for letter in pool]
    table.add_row(letters)
    table.add_row(values)

    table.padding_width = 2

    print(table)

    """for letter in pool:
        print(f"{letter.capitalize()}", end="\t")
    print()
    for letter in pool:
        print(f"{get_value(letter)}", end="\t")
    print()"""


def display_board(board):
    table = PrettyTable()

    # Add column headers
    table.field_names = [" "] + [f"{i + 1:<2}" for i in range(BOARD_SIZE)]

    # Add rows with delimiters
    for i, row in enumerate(board):
        row_content = []
        for j, cell in enumerate(row):
            if i == j == BOARD_SIZE // 2:  # Check if the cell is the center cell
                row_content.append(f"{cell if cell else '*':<2}")
            else:
                row_content.append(f"{cell if cell else ' ':<2}")
        table.add_row([f"{i + 1:<2}"] + row_content)
        if i != BOARD_SIZE - 1:  # Don't add a delimiter after the last row
            table.add_row(["-"] * (BOARD_SIZE + 1))  # Add a delimiter row

    print(table)
