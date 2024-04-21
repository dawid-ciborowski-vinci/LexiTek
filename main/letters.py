import random
from random import shuffle

letters_map = {}


# Read letters with its frequency and value from file
def read_letters(language):
    with open(f'../data/{language}/{language}.let', 'r') as file:
        for line in file:
            letter, frequency, value = line.split()

            frequency = int(frequency)
            value = int(value)

            # f = frequency, v = value
            letters_map[letter] = {'f': frequency, 'v': value}


# Make the letter pool
def letter_pool():
    return list(letters_map)


def get_value(letter):
    return letters_map[letter]['v']


def player_letters(available_letters, number_of_letters):
    letters = []
    for _ in range(number_of_letters):
        random_i = random.randint(0, len(available_letters) - 1)
        letter = available_letters.pop(random_i)
        letters.append(letter)
    return letters
