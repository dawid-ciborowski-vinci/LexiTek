from letters import read_letters, letter_pool
from words import read_words

letters = read_letters('french')
words = read_words('french')

print(letters)
print(letter_pool(letters))
