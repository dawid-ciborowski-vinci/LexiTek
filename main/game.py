from letters import read_letters, player_letters

languages = ['french', 'english']
ui = {
    'french': {
        'player_number': "Nombre de joueurs:\t"
    },
    'english': {
        'player_number': "Number of players:\t"
    }
}
MAX_PLAYERS = 4


# Function to run the LexiTek game
def game():
    # Language
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
    letters = read_letters(language)

    # Init Players and turn
    players = {}
    for i in range(players_number):
        my_letters = player_letters(letters)
        players[i] = my_letters
    turn = 0

    print(language)
    print(players)


"""
    running = True
    while running:
        index = tour % len(joueurs)
        joueur = joueurs[index]
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print(f"Tour du joueur n°{joueur + 1}\nVoici vos cartes:\n")
        # cartes.afficher_cartes(distribution[joueur])

        # ETAPE 1: PIOCHER CARTE
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
            distribution[joueur].append(carte_tiree)

        # ETAPE 2: DEPOSER COMBINAISON OU PAS
        choix = ''
        cartes_non_valide = True

        while cartes_non_valide or not choix in ['a', 'b', 'c']:
            print()
            cartes.afficher_cartes(distribution[joueur])
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
                cartes_a_deposer = actions.choix_deposer(distribution[joueur])
                if combinaison.valide(cartes_a_deposer):
                    print("Votre combinaison est valide !")
                    plateau.append(cartes_a_deposer)
                    cartes_non_valide = False
                else:
                    print("Votre combinaison n'est pas valide !")
                    distribution[joueur].extend(cartes_a_deposer)

            elif choix == 'c':
                choix_combinaison = -1
                while not (0 < choix_combinaison <= len(plateau)):
                    choix_combinaison = int(input("Choisissez le numéro de combinaison à compléter:\t"))

                etat_initial = distribution[joueur].copy()
                cartes_pour_completer = actions.choix_deposer(distribution[joueur])
                if len(cartes_pour_completer) != 0:
                    cartes_completees = cartes_pour_completer
                    cartes_completees.extend(plateau[choix_combinaison - 1])

                    if combinaison.valide(cartes_completees):
                        print("Votre combinaison est valide !")
                        plateau[choix_combinaison - 1] = cartes_completees
                        cartes_non_valide = False
                    else:
                        print("Votre combinaison n'est pas valide !")
                        distribution[joueur] = etat_initial
                else:
                    print("Aucune carte chosie.")

            elif choix == 'b':
                cartes_non_valide = False

        print()

        # ETAPE 3: DEFAUSSER UNE CARTE
        if len(distribution[joueur]) != 0:
            cartes.afficher_cartes(distribution[joueur])
            defausse.append(actions.defausser(distribution[joueur]))
            tour += 1
        if len(distribution[joueur]) == 0:
            running = False
            joueurs.remove(joueur)
            print(f"\nJoueur n°{joueur + 1} a gagné !")

    # Affichage des points pour les joueurs restants
    for joueur in joueurs:
        total_points = cartes.compter_points(distribution[joueur])
        print(f"\nPoints du joueur n°{joueur + 1}: {total_points} pts")
        
"""
