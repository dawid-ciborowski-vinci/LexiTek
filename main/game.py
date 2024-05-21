from words import read_words, is_word_valid
from letters import player_letters, letter_pool, pop_one
from language import ui, set_language, get_language
from game_logic import place_word, display_board, display_player_pool, is_centered, is_adjacent_or_part

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
        players_number = input(f"{ui[get_language()]['player_number']} (max = {MAX_PLAYERS}):\t")
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
        name = input(f"{ui[get_language()]['player_name']}{i + 1} :\t")
        my_letters = player_letters(letters, LETTERS_PER_PLAYER)
        player = {'name': name, 'letters': my_letters, 'score': 0, 'pass': False}
        players[i] = player
    turn = 0

    # Init Number of Passes
    passes = 0

    # Game Loop
    running = True
    while running:
        player_number = turn % len(players)
        if players[player_number]['pass']:
            turn += 1
            continue
        player_letters_pool = players[player_number]['letters']

        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
        print(f"\t\t\t\t\t {ui[get_language()]['turn']}{player_number + 1} : {players[player_number]['name']}\n")
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

        while choice1 not in ['a', 'b', 'c']:
            print(ui[get_language()]['choose_action']['q'])
            print(ui[get_language()]['choose_action']['a'])
            print(ui[get_language()]['choose_action']['b'])
            print(ui[get_language()]['choose_action']['c'])
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

            word_placed = False
            while word_placed is False:
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

                if turn != 0 and not is_adjacent_or_part(board, word, direction, x, y):
                    print(ui[get_language()]['error_6'])
                    continue

                res = place_word(board, word, direction, x, y, player_letters_pool, letters)
                if res is True:
                    players[player_number]['score'] += score
                    word_placed = True
                else:
                    print(res)

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

        # PLAYER PASSES
        elif choice1 == 'c':
            players[player_number]['pass'] = True
            passes += 1
            if passes == players_number:
                running = False
        turn += 1

    # Game Over
    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    print(ui[get_language()]['game_over'])
    print(ui[get_language()]['scores'])

    max_score = -1
    winner = -1

    for i in range(players_number):
        print(f"► {players[i]['name']}\t:\t{players[i]['score']}")
        if players[i]['score'] > max_score:
            max_score = players[i]['score']
            winner = i

    print(f"\n{ui[get_language()]['winner']} {max_score} : {players[winner]['name']} !")
