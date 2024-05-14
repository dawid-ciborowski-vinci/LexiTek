from words import read_words, is_word_valid
from letters import player_letters, letter_pool, pop_one
from language_map import ui
from game_logic import place_word, display_board, display_player_pool, is_centered

languages = ['french', 'english', 'italian']

BOARD_SIZE = 15
MAX_PLAYERS = 4
LETTERS_PER_PLAYER = 7

dictionary = {}


# Function to run the LexiTek game
def game():
    # Language
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("\t\t\t\t\t\t\tLexiTek")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

    language_choice = -1
    while not str(language_choice).isnumeric() or int(language_choice) - 1 not in range(len(languages)):
        for i, language in enumerate(languages):
            print(f"{i + 1}.\t{language.capitalize()}")
        language_choice = input("\nChoose your language:\t")
    language = languages[int(language_choice) - 1]

    # Players number
    players_number = '0'
    while players_number == '0' or not players_number.isnumeric() or int(players_number) > MAX_PLAYERS:
        players_number = input(ui[language]['player_number'])
    players_number = int(players_number)

    # Init Letters
    letters = letter_pool()

    # Init Dictionary
    dictionary = read_words(language)

    # Init Board
    board = [['' for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]

    # Init Players and turn
    players = {}
    for i in range(players_number):
        my_letters = player_letters(letters, LETTERS_PER_PLAYER)
        players[i] = my_letters
    turn = 0

    # Game loop
    running = True
    while running:
        player_number = turn % len(players)
        player_letters_pool = players[player_number]

        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
        print(f"\t\t\t\t\t {ui[language]['turn']}{player_number + 1}\n")
        display_board(board)

        print(f"\n{ui[language]['your_letters']} \n")
        display_player_pool(player_letters_pool)

        print()

        # STEP 1: PLAYER MAKE ACTION
        choice1 = ''
        word = ""
        x, y = '', ''
        direction = ""
        changed_all_letters = False

        while choice1 not in ['a', 'b']:
            print(ui[language]['choose_action']['q'])
            print(ui[language]['choose_action']['a'])
            print(ui[language]['choose_action']['b'])
            if changed_all_letters:
                print(ui[language]['choose_action']['c'])
            choice1 = input(ui[language]['choice'])

        # PLAYER PLACES A WORD
        if choice1 == 'a':
            while not is_word_valid(word, player_letters_pool, dictionary):
                word = input(ui[language]['enter_word']).upper()

            while direction not in ['a', 'b']:
                print(ui[language]['enter_direction']['q'])
                print(ui[language]['enter_direction']['a'])
                print(ui[language]['enter_direction']['b'])
                direction = input(ui[language]['choice'])

            if direction == 'a':
                direction = 'horizontal'
            elif direction == 'b':
                direction = 'vertical'

            while True:
                x = input(ui[language]['enter_x'])
                y = input(ui[language]['enter_y'])
                if not x.isnumeric():
                    print(f"{ui[language]['column_must_number']}")
                if not y.isnumeric():
                    print(f"{ui[language]['line_must_number']}")
                else:
                    x = int(x) - 1
                    y = int(y) - 1
                    if turn == 0 and not is_centered(word, direction, x, y):
                        print(f"{ui[language]['centered']}")
                    else:
                        break

            res = place_word(board, word, direction, x, y, player_letters_pool, letters, language)
            print(res)

        # PLAYER CHANGES A LETTER
        elif choice1 == 'b':
            letter_choice = ''
            while letter_choice not in player_letters_pool:
                letter_choice = input(ui[language]['enter_letter']).upper()
            removed_letter = player_letters_pool.remove(letter_choice)
            letter_to_add = pop_one(letters)
            if letter_to_add is not None:
                letters.append(removed_letter)
                player_letters_pool.append(letter_to_add)

        turn += 1
