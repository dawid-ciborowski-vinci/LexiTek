# read letters with its frequency and value from file
from random import shuffle


def read_letters(language):
    letters_map = {}
    with open(f'../data/{language}/{language}.let', 'r') as file:
        for line in file:
            letter, frequency, value = line.split()

            frequency = int(frequency)
            value = int(value)

            # f = frequency, v = value
            letters_map[letter] = {'f': frequency, 'v': value}

    return letters_map


def letter_pool(letters_map):
    letters = []
    for letter in letters_map:
        for i in range(letters_map[letter]['f']):
            letters.append({str(letter): letters_map[letter]['v']})

    shuffle(letters)
    return letters
