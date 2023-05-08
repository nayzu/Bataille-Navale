import random

# Créer le plateau de jeu
board = []
for x in range(5):
    board.append(["O"] * 5)


# Fonction pour afficher le plateau de jeu
def afficher_plateau(plateau):
    for ligne in plateau:
        print(" ".join(ligne))


# Fonction pour générer une position aléatoire pour le navire
def generer_position_navire(plateau):
    return random.randint(0, len(plateau) - 1), random.randint(0, len(plateau[0]) - 1)


# Placer le navire sur le plateau de jeu
navire_x, navire_y = generer_position_navire(board)

# Boucle principale du jeu
for tour in range(4):
    print("Tour", tour + 1)
    afficher_plateau(board)

    # Demander au joueur de deviner la position du navire
    devine_x = int(input("Devine la coordonnée en X : "))
    devine_y = int(input("Devine la coordonnée en Y : "))

    # Vérifier si la devinette est correcte
    if devine_x == navire_x and devine_y == navire_y:
        print("Félicitations ! Tu as coulé le navire !")
        break
    else:
        if devine_x not in range(5) or devine_y not in range(5):
            print("Oops ! Coordonnées hors du plateau.")
        elif board[devine_x][devine_y] == "X":
            print("Tu as déjà essayé cette position.")
        else:
            print("Dommage ! Tu as manqué le navire.")
            board[devine_x][devine_y] = "X"
        if tour == 3:
            print("Fin du jeu ! Le navire était en position", navire_x, navire_y)
            board[navire_x][navire_y] = "#"
            afficher_plateau(board)
