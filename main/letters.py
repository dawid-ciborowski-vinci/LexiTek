import random
from language import get_language

letters_map = {}


# Lire les lettres
def read_letters():
    with open(f'../data/{get_language()}/{get_language()}.let', 'r') as file:
        for line in file:
            letter, frequency, value = line.split()

            frequency = int(frequency)
            value = int(value)

            # f = frequency, v = value
            letters_map[letter] = {'f': frequency, 'v': value}


read_letters()


# Créer un pool de lettres
def letter_pool():
    pool = []
    for letter in letters_map.keys():
        for _ in range(letters_map[letter]['f']):
            pool.append(letter)
    return pool


# Obtenir la valeur d'une lettre
def get_value(letter):
    return letters_map[letter]['v']


# Afficher le pool de lettres d'un joueur
def player_letters(available_letters, number_of_letters):
    letters = []
    for _ in range(number_of_letters):
        random_i = random.randint(0, len(available_letters) - 1)
        letter = available_letters.pop(random_i)
        letters.append(letter)
    return letters


# Obtenir une lettre aléatoire
def pop_one(available_letters):
    letter = None
    if len(available_letters) != 0:
        random_i = random.randint(0, len(available_letters) - 1)
        letter = available_letters.pop(random_i)
    return letter
