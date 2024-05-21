# language.py
LANGUAGE = {'lang': 'english'}  # Default value


# Fonction pour définir la langue
def set_language(choice):
    LANGUAGE['lang'] = choice


# Fonction pour obtenir la langue
def get_language():
    return LANGUAGE['lang']


ui = {
    'french': {
        'player_number': "Nombre de joueurs",
        'player_name': "Nom du joueur n°",
        'turn': 'Tour du joueur n°',
        'your_letters': 'Voici vos lettres :',
        'choice': "\nMon choix:\t",
        'choose_action': {'q': 'Que voulez-vous faire ?',
                          'a': 'a)\tPlacer un mot',
                          'b': 'b)\tÉchanger lettre(s)',
                          'c': 'c)\tPasser'},
        'enter_word': "Mot à placer ('0' pour annuler):\t",
        'enter_direction': {
            'q': "Position du mot:\t",
            'a': "a)\tHorizontale",
            'b': "b)\tVerticale",
        },
        'cancel': 'c)\tAnnuler',
        'enter_x': "Colonne de la première lettre ('0' pour annuler):\t",
        'enter_y': "Ligne de la première lettre ('0' pour annuler):\t",
        'enter_letter': "Lettre ('0' pour annuler):\t",
        'column_must_number': 'La colonne doit être un nombre.',
        'line_must_number': 'La ligne doit être un nombre.',
        'centered': 'Le mot doit passer par la case centrale (8, 8) lors du premier tour.',
        'error_1': 'Les coordonnées du mot sont en dehors des limites du plateau.',
        'error_2': 'Le mot dépasse les limites du plateau en direction horizontale.',
        'error_3': 'Le mot dépasse les limites du plateau en direction verticale.',
        'error_4': 'Le mot ne peut pas être placé à cet endroit.',
        'error_5': 'Le mot et sa position ne sont pas compatibles avec les lettres sur le plateau.',
        'error_6': 'Le mot doit être adjacent à une autre lettre ou faire partie d\'un mot existant.',
        'game_over': 'Fin de la partie',
        'stats': 'Statistiques :',
        'winner': 'Le gagnant est',
        'points': 'points',
        'no_letters_left': 'Plus de lettres !'
    },
    'english': {
        'player_number': "Number of players",
        'player_name': 'Name of player n°',
        'turn': 'Turn of player n°',
        'your_letters': 'Here are your letters :',
        'choice': "\nMy choice:\t",
        'choose_action': {'q': 'What is your action ?',
                          'a': 'a)\tPlace a word',
                          'b': 'b)\tChange letter(s)',
                          'c': 'c)\tPass'},
        'enter_word': "Word to place ('0' to cancel):\t",
        'enter_direction': {
            'q': "Word Position:\t",
            'a': "a)\tHorizontal",
            'b': "b)\tVertical",
        },
        'cancel': 'c)\tCancel',
        'enter_x': "Column of the first letter ('0' to cancel):\t",
        'enter_y': "Line of the first letter ('0' to cancel):\t",
        'enter_letter': "Letter ('0' to cancel):\t",
        'column_must_number': 'The column must be a number.',
        'line_must_number': 'The line must be a number.',
        'centered': 'The word must pass through the center cell (8, 8) during the first turn.',
        'error_1': 'The word coordinates are out of the board limits.',
        'error_2': 'The word exceeds the board limits horizontally.',
        'error_3': 'The word exceeds the board limits vertically.',
        'error_4': 'The word cannot be placed at this location.',
        'error_5': 'The word and its position are not compatible with the letters on the board.',
        'error_6': 'The word must be adjacent to another letter or be part of an existing word.',
        'game_over': 'Game Over',
        'stats': 'Stats :',
        'winner': 'The winner is',
        'points': 'points',
        'no_letters_left': 'No letters left !'
    },
    'italian': {
        'player_number': "Numero di giocatori",
        'player_name': 'Nome del giocatore n°',
        'turn': 'Turno del giocatore n°',
        'your_letters': 'Ecco le tue lettere :',
        'choice': "\nLa mia scelta:\t",
        'choose_action': {'q': 'Cosa vuoi fare ?',
                          'a': 'a)\tPosiziona una parola',
                          'b': 'b)\tCambia lettera(e)',
                          'c': 'c)\tPassa'},
        'enter_word': "Parola da posizionare ('0' per annullare):\t",
        'enter_direction': {
            'q': "Posizione della parola:\t",
            'a': "a)\tOrizzontale",
            'b': "b)\tVerticale",
        },
        'cancel': 'c)\tAnnulla',
        'enter_x': "Colonna della prima lettera ('0' per annullare):\t",
        'enter_y': "Riga della prima lettera ('0' per annullare):\t",
        'enter_letter': "Lettera ('0' per annullare):\t",
        'column_must_number': 'La colonna deve essere un numero.',
        'line_must_number': 'La riga deve essere un numero.',
        'centered': 'La parola deve passare per la cella centrale (8, 8) durante il primo turno.',
        'error_1': 'Le coordinate della parola sono fuori dai limiti della scacchiera.',
        'error_2': 'La parola supera i limiti della scacchiera in orizzontale.',
        'error_3': 'La parola supera i limiti della scacchiera in verticale.',
        'error_4': 'La parola non può essere posizionata in questa posizione.',
        'error_5': 'La parola e la sua posizione non sono compatibili con le lettere sulla scacchiera.',
        'error_6': 'La parola deve essere adiacente a un\'altra lettera o far parte di una parola esistente.',
        'game_over': 'Fine del gioco',
        'scores': 'Punteggi :',
        'winner': 'Il vincitore è',
        'points': 'punti',
        'no_letters_left': 'Nessuna lettera rimasta !'
    }
}
