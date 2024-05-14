import random
from random import shuffle

letters_map = {}


# Read letters with its frequency and value from file
def read_letters():
    with open(f'../data/letters_data.let', 'r') as file:
        for line in file:
            letter, frequency, value = line.split()

            frequency = int(frequency)
            value = int(value)

            # f = frequency, v = value
            letters_map[letter] = {'f': frequency, 'v': value}


# Make the letter pool
def letter_pool():
    pool = []
    for letter in letters_map.keys():
        for _ in range(letters_map[letter]['f']):
            pool.append(letter)
    return pool


def get_value(letter):
    return letters_map[letter]['v']


def player_letters(available_letters, number_of_letters):
    letters = []
    for _ in range(number_of_letters):
        random_i = random.randint(0, len(available_letters) - 1)
        letter = available_letters.pop(random_i)
        letters.append(letter)
    return letters


def pop_one(available_letters):
    letter = None
    if len(available_letters) != 0:
        random_i = random.randint(0, len(available_letters) - 1)
        letter = available_letters.pop(random_i)
    return letter
