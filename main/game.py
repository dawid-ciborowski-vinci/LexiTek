from words import read_words, is_word_valid
from letters import player_letters, letter_pool, pop_one
from language import ui, set_language, get_language
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
        for i, lang in enumerate(languages):
            print(f"{i + 1}.\t{lang.capitalize()}")
        language_choice = input("\nChoose your language:\t")
    set_language(languages[int(language_choice) - 1])

    # Players number
    players_number = '0'
    while players_number == '0' or not players_number.isnumeric() or int(players_number) > MAX_PLAYERS:
        players_number = input(ui[get_language()]['player_number'])
    players_number = int(players_number)

    # Init Letters
    letters = letter_pool()

    # Init Dictionary
    dictionary = read_words()

    # Init Board
    board = [['' for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]

    # Init Players and turn
    players = {}
    for i in range(players_number):
        my_letters = player_letters(letters, LETTERS_PER_PLAYER)
        player = {'letters': my_letters, 'score': 0}
        players[i] = player
    turn = 0

    # Game loop
    running = True
    while running:
        player_number = turn % len(players)
        player_letters_pool = players[player_number]['letters']

        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
        print(f"\t\t\t\t\t {ui[get_language()]['turn']}{player_number + 1}\n")
        display_board(board)

        print(f"\n{ui[get_language()]['your_letters']} \n")
        display_player_pool(player_letters_pool)

        print()

        # STEP 1: PLAYER MAKE ACTION
        choice1 = ''
        word = ""
        x, y = '', ''
        direction = ""
        changed_all_letters = False

        while choice1 not in ['a', 'b']:
            print(ui[get_language()]['choose_action']['q'])
            print(ui[get_language()]['choose_action']['a'])
            print(ui[get_language()]['choose_action']['b'])
            if changed_all_letters:
                print(ui[get_language()]['choose_action']['c'])
            choice1 = input(ui[get_language()]['choice'])

        # PLAYER PLACES A WORD
        if choice1 == 'a':
            score = 0
            while direction not in ['a', 'b']:
                print(ui[get_language()]['enter_direction']['q'])
                print(ui[get_language()]['enter_direction']['a'])
                print(ui[get_language()]['enter_direction']['b'])
                direction = input(ui[get_language()]['choice'])

            if direction == 'a':
                direction = 'horizontal'
            elif direction == 'b':
                direction = 'vertical'

            if turn == 0:  # If it's the first turn
                while score == 0:
                    word = input(ui[get_language()]['enter_word']).upper()
                    score = is_word_valid(word, player_letters_pool, dictionary, board, 8, 8, direction)

                while True:
                    x = input(ui[get_language()]['enter_x'])
                    y = input(ui[get_language()]['enter_y'])
                    if not x.isnumeric():
                        print(f"{ui[get_language()]['column_must_number']}")
                    if not y.isnumeric():
                        print(f"{ui[get_language()]['line_must_number']}")
                    else:
                        x = int(x) - 1
                        y = int(y) - 1
                        if not is_centered(word, direction, x, y):
                            print(f"{ui[get_language()]['centered']}")
                        else:
                            break
            else:  # If it's not the first turn
                while True:
                    x = input(ui[get_language()]['enter_x'])
                    y = input(ui[get_language()]['enter_y'])
                    if not x.isnumeric():
                        print(f"{ui[get_language()]['column_must_number']}")
                    if not y.isnumeric():
                        print(f"{ui[get_language()]['line_must_number']}")
                    else:
                        x = int(x) - 1
                        y = int(y) - 1
                        break

                while score == 0:
                    word = input(ui[get_language()]['enter_word']).upper()
                    score = is_word_valid(word, player_letters_pool, dictionary, board, x, y, direction)

            res = place_word(board, word, direction, x, y, player_letters_pool, letters)
            if res is True:
                players[player_number]['score'] += score
            print(res)
            print(f"Score: {players[player_number]['score']}")

        # PLAYER CHANGES A LETTER
        elif choice1 == 'b':
            letter_choice = ''
            while letter_choice not in player_letters_pool:
                letter_choice = input(ui[get_language()]['enter_letter']).upper()
            removed_letter = player_letters_pool.remove(letter_choice)
            letter_to_add = pop_one(letters)
            if letter_to_add is not None:
                letters.append(removed_letter)
                player_letters_pool.append(letter_to_add)

        turn += 1
