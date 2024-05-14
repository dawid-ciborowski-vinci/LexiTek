# Read words from file
def read_words(language):
    words_map = {}
    with open(f'../data/{language}.dic', 'r') as file:
        for line in file:
            word = line.replace('\n', '')

            words_map[word.upper()] = len(word)

    return words_map


def is_word_valid(word, player_letters, dictionary):
    # Check if the word is in the dictionary
    player_word = word.upper()
    if player_word not in dictionary:
        return False

    # Check if the word can be formed with the player's letters
    for letter in player_word:
        if letter not in player_letters:
            return False
    return True
