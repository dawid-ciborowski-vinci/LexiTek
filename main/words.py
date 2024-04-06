# Read words from file
def read_words(language):
    words_map = {}
    with open(f'../data/{language}/{language}.dic', 'r') as file:
        for line in file:
            word = line.replace('\n', '')

            words_map[word] = len(word)

    return words_map
