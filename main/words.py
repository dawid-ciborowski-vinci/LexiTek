from language import get_language
from letters import get_value


# Read words from file
def read_words():
    words_map = {}
    with open(f'../data/{get_language()}/{get_language()}.dic', 'r') as file:
        for line in file:
            word = line.replace('\n', '')

            words_map[word.upper()] = len(word)

    return words_map


def is_word_valid(word, player_letters, dictionary, board, x, y, direction):
    # Check if the word is in the dictionary
    player_word = word.upper()
    if player_word not in dictionary:
        return 0

    score = 0

    # Check if the word can be formed with the player's letters and/or letters on the board
    for i, letter in enumerate(player_word):
        if letter not in player_letters:
            if direction == 'horizontal':
                if board[y][x + i] != letter and board[y][x + i] != '':
                    return 0
            elif direction == 'vertical':
                if board[y + i][x] != letter and board[y + i][x] != '':
                    return 0
        score += get_value(letter)

    return score
