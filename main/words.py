from language import get_language
from letters import get_value


# Lit les mots du dictionnaire
def read_words():
    words_map = {}
    with open(f'../data/{get_language()}/{get_language()}.dic', 'r') as file:
        for line in file:
            word = line.replace('\n', '')

            words_map[word.upper()] = len(word)

    return words_map


# Vérifie si le mot est valide
def is_word_valid(word, player_letters, dictionary, board, x, y, direction):
    # Vérifie si le mot est dans le dictionnaire
    player_word = word.upper()
    if player_word not in dictionary:
        return 0

    score = 0

    # Vérifie si le mot est dans les lettres du joueur
    for i, letter in enumerate(player_word):
        if letter not in player_letters:
            if direction == 'horizontal':
                if board[y][x + i] != letter:
                    return 0
            elif direction == 'vertical':
                if board[y + i][x] != letter:
                    return 0
        score += get_value(letter)

    return score
