import random
from random import shuffle


# Read letters with its frequency and value from file
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


# Make the letter pool
def letter_pool(letters_map):
    letters = []
    for letter in letters_map:
        for i in range(letters_map[letter]['f']):
            letters.append({str(letter): letters_map[letter]['v']})

    shuffle(letters)
    return letters


def player_letters(available_letters):
    letters = []
    for _ in range(7):
        random_i = random.randint(0, len(available_letters) - 1)
        letter = available_letters[random_i]
        letters.append(letter)
        available_letters.pop(random_i)
    return letters

