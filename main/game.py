from words import read_words, is_word_valid
from letters import read_letters, player_letters, letter_pool, get_value

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
    }
}

BOARD_SIZE = 15
MAX_PLAYERS = 4
LETTERS_PER_PLAYER = 7

dictionary = {}


def place_word(board, word, direction, x, y, player_letters):
    if not (0 <= x < BOARD_SIZE and 0 <= y < BOARD_SIZE):
        return False

    if not is_word_placeable(board, word, direction, x, y):
        return False

    if direction == 'horizontal':
        for i in range(len(word)):
            letter = word[i]
            board[y][x + i] = letter
            player_letters.remove(letter)
    elif direction == 'vertical':
        for i in range(len(word)):
            letter = word[i]
            board[y + 1][x] = letter
            player_letters.remove(letter)

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


def is_centered(word, direction, x, y):
    if direction == 'horizontal':
        if (x <= 7 < x + len(word)) and (y == 7 or (y < 7 and y + 1 < 7) or (y > 7 and y - 1 >= 7)):
            return True
    elif direction == 'vertical':
        if (y <= 7 < y + len(word)) and (x == 7 or (x < 7 and x + 1 < 7) or (x > 7 and x - 1 >= 7)):
            return True
    return False


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
    read_letters(language)
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

            while True:
                x = input(ui[language]['enter_x'])
                y = input(ui[language]['enter_y'])
                if not x.isnumeric():
                    print("La colonne doit être un nombre.")
                if not y.isnumeric():
                    print("La ligne doit être un nombre.")
                else:
                    x = int(x)
                    y = int(y)
                    if turn == 1 and not is_centered(word, direction, x, y):
                        print("Le mot doit passer par la case centrale (7, 7) lors du premier tour.")
                    else:
                        break

            if direction == 'a':
                direction = 'horizontal'
            elif direction == 'b':
                direction = 'vertical'

            res = place_word(board, word, direction, x, y, player_letters_pool)
            print(res)

        # PLAYER CHANGES A LETTER
        #elif choice1 == 'b':
        turn += 1


def display_player_pool(pool):
    for letter in pool:
        print(f"{letter.capitalize()}", end="\t")
    print()
    for letter in pool:
        print(f"{get_value(letter)}", end="\t")
    print()


def display_board(board):
    print('\t', end='')
    for i in range(len(board[0])):
        print(f'{i}\t', end='')
    print()
    for i, row in enumerate(board):
        print(f'{i}\t', end='')
        for cell in row:
            print(cell if cell else '.', end='\t')
        print()


"""    
        choix = ''
        while not choix in ['a', 'b']:
            choix = 'a'
            if len(defausse) != 0:
                carte_defausse = defausse[len(defausse) - 1]
                print(f"\nDéfausse:\t{cartes.donner_valeur(carte_defausse[0])} | {carte_defausse[1]}\n")
                print("a) Piocher")
                print("b) Tirer de la défausse")
                choix = input("\nVotre choix:\t")

        print()

        carte_tiree = None
        if choix == 'a':
            print("Vous tirez dans la pioche.")
            carte_tiree = cartes.tirer_carte(pioche)
            if carte_tiree is None:
                choix = 'b'

        if choix == 'b':
            print("Vous tirez dans la défausse.")
            carte_tiree = cartes.tirer_carte(defausse)

        if carte_tiree is not None:
            print(f"Vous tirez la carte:\t{cartes.donner_valeur(carte_tiree[0])} | {carte_tiree[1]}")
            distribution[player].append(carte_tiree)

        # ETAPE 2: DEPOSER COMBINAISON OU PAS
        choix = ''
        cartes_non_valide = True

        while cartes_non_valide or not choix in ['a', 'b', 'c']:
            print()
            cartes.afficher_cartes(distribution[player])
            print("\na) Déposer une combinaison")
            print("b) Ne rien déposer")

            if len(plateau) != 0:
                print("c) Compléter une combinaison existante\nVoici les combinaisons déjà déposées:\n")
                for i, combi in enumerate(plateau):
                    print(f"Combinaison n°{i + 1}:\n")
                    cartes.afficher_cartes(combi)
                    print()
            choix = input("\nVotre choix:\t")

            print()

            if choix == 'a':
                cartes_a_deposer = actions.choix_deposer(distribution[player])
                if combinaison.valide(cartes_a_deposer):
                    print("Votre combinaison est valide !")
                    plateau.append(cartes_a_deposer)
                    cartes_non_valide = False
                else:
                    print("Votre combinaison n'est pas valide !")
                    distribution[player].extend(cartes_a_deposer)

            elif choix == 'c':
                choix_combinaison = -1
                while not (0 < choix_combinaison <= len(plateau)):
                    choix_combinaison = int(input("Choisissez le numéro de combinaison à compléter:\t"))

                etat_initial = distribution[player].copy()
                cartes_pour_completer = actions.choix_deposer(distribution[player])
                if len(cartes_pour_completer) != 0:
                    cartes_completees = cartes_pour_completer
                    cartes_completees.extend(plateau[choix_combinaison - 1])

                    if combinaison.valide(cartes_completees):
                        print("Votre combinaison est valide !")
                        plateau[choix_combinaison - 1] = cartes_completees
                        cartes_non_valide = False
                    else:
                        print("Votre combinaison n'est pas valide !")
                        distribution[player] = etat_initial
                else:
                    print("Aucune carte chosie.")

            elif choix == 'b':
                cartes_non_valide = False

        print()

        # ETAPE 3: DEFAUSSER UNE CARTE
        if len(distribution[player]) != 0:
            cartes.afficher_cartes(distribution[player])
            defausse.append(actions.defausser(distribution[player]))
            turn += 1
        if len(distribution[player]) == 0:
            running = False
            players.remove(player)
            print(f"\nJoueur n°{player + 1} a gagné !")

    # Affichage des points pour les players restants
    for player in players:
        total_points = cartes.compter_points(distribution[player])
        print(f"\nPoints du player n°{player + 1}: {total_points} pts")
"""
