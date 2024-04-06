# Read words from file
def read_words(language):
    words_map = {}
    with open(f'../data/{language}/{language}.dic', 'r') as file:
        for line in file:
            word = line.replace('\n', '')

            words_map[word] = len(word)

    return words_map


def validate_word(word, player_letters, dictionary):

    # Check if the word is in the dictionary
    if word not in dictionary:
        return False

    # Check if the word can be formed with the player's letters
    for letter in word:
        if letter not in player_letters:
            return False
        else:
            player_letters.remove(letter)

    return True
