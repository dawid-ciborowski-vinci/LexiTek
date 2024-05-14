from words import read_words, is_word_valid
from letters import read_letters, player_letters, letter_pool, get_value, pop_one
from prettytable import PrettyTable

languages = ['french', 'english']

ui = {
    'french': {
        'player_number': "Nombre de joueurs:\t",
        'choice': "\nMon choix:\t",
        'choose_action': {'q': 'Que voulez-vous faire ?',
                          'a': 'a)\tPlacer un mot',
                          'b': 'b)\tÉchanger lettre(s)',
                          'c': 'c)\tPasser son tour'},
        'enter_word': "Mot à placer:\t",
        'enter_direction': {
            'q': "Position du mot:\t",
            'a': "a)\tHorizontale",
            'b': "b)\tVerticale",
        },
        'enter_x': "Colonne de la première lettre:\t",
        'enter_y': "Ligne de la première lettre:\t",
        'enter_letter': "Lettre:\t",
    },
    'english': {
        'player_number': "Number of players:\t",
        'choice': "\nMy choice:\t",
        'choose_action': {'q': 'What is your action ?',
                          'a': 'a)\tPlace a word',
                          'b': 'b)\tChange letter(s)',
                          'c': 'c)\tPass'},
        'enter_word': "Word to place:\t",
        'enter_direction': {
            'q': "Word Position:\t",
            'a': "a)\tHorizontal",
            'b': "b)\tVertical",
        },
        'enter_x': "Column of the first letter:\t",
        'enter_y': "Line of the first letter:\t",
        'enter_letter': "Letter:\t",
    }
}

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
    read_letters()
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
        print(f"\t\t\t\t\tTour du joueur n°{player_number + 1}\n")
        display_board(board)

        print("\nVoici vos lettres : \n")
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
                    print("La colonne doit être un nombre.")
                if not y.isnumeric():
                    print("La ligne doit être un nombre.")
                else:
                    x = int(x) - 1
                    y = int(y) - 1
                    if turn == 0 and not is_centered(word, direction, x, y):
                        print("Le mot doit passer par la case centrale (8, 8) lors du premier tour.")
                    else:
                        break

            res = place_word(board, word, direction, x, y, player_letters_pool, letters)
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


def place_word(board, word, direction, x, y, player_letters, letters):
    if not (0 <= x < BOARD_SIZE and 0 <= y < BOARD_SIZE):
        return "Erreur : Les coordonnées du mot sont en dehors des limites du plateau."

    if direction == 'horizontal' and x + len(word) > BOARD_SIZE:
        return "Erreur : Le mot dépasse les limites du plateau en direction horizontale."
    elif direction == 'vertical' and y + len(word) > BOARD_SIZE:
        return "Erreur : Le mot dépasse les limites du plateau en direction verticale."

    if not is_word_placeable(board, word, direction, x, y):
        return "Erreur : Le mot ne peut pas être placé à cet endroit."

    if not is_word_compatible(board, word, direction, x, y):
        return "Erreur : Le mot et sa position ne sont pas compatibles avec les lettres sur le plateau."

    if direction == 'horizontal':
        for i in range(len(word)):
            letter = word[i]
            board[y][x + i] = letter
            player_letters.remove(letter)
            letter = pop_one(letters)
            if letter is not None:
                player_letters.append(letter)
    elif direction == 'vertical':
        for i in range(len(word)):
            letter = word[i]
            board[y + i][x] = letter
            player_letters.remove(letter)
            letter = pop_one(letters)
            if letter is not None:
                player_letters.append(letter)

    return True


def is_word_placeable(board, word, direction, x, y):
    if direction == 'horizontal':
        if x + len(word) > BOARD_SIZE:
            return False
        for i in range(len(word)):
            if board[x + 1][y] != '':
                return False
    elif direction == 'vertical':
        if y + len(word) > BOARD_SIZE:
            return False
        for i in range(len(word)):
            if board[x][y + i] != '':
                return False
    return True


def is_word_compatible(board, word, direction, x, y):
    if direction == 'horizontal':
        for i in range(len(word)):
            if board[y][x + i] != '' and board[y][x + i] != word[i]:
                return False
    elif direction == 'vertical':
        for i in range(len(word)):
            if board[y + i][x] != '' and board[y + i][x] != word[i]:
                return False
    return True


def is_centered(word, direction, x, y):
    if direction == 'horizontal':
        if (x <= 7 < x + len(word)) and (y == 7):
            return True
    elif direction == 'vertical':
        if (y <= 7 < y + len(word)) and (x == 7):
            return True
    return False


def display_player_pool(pool):
    for letter in pool:
        print(f"{letter.capitalize()}", end="\t")
    print()
    for letter in pool:
        print(f"{get_value(letter)}", end="\t")
    print()


def display_board(board):
    table = PrettyTable()

    # Add column headers
    table.field_names = [" "] + [str(i+1) for i in range(BOARD_SIZE)]

    # Add rows with delimiters
    for i, row in enumerate(board):
        row_content = []
        for j, cell in enumerate(row):
            if i == j == BOARD_SIZE // 2:  # Check if the cell is the center cell
                row_content.append(cell if cell else "*")
            else:
                row_content.append(cell if cell else " ")
        table.add_row([str(i+1)] + row_content)
        if i != BOARD_SIZE - 1:  # Don't add a delimiter after the last row
            table.add_row(["-"] * (BOARD_SIZE + 1))  # Add a delimiter row

    print(table)
