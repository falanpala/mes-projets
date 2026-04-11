import random


def jeu_devine_nombre():
    print("Bienvenue dans le jeu 'Devine le nombre' !")

    # Le nombre à deviner est choisi aléatoirement entre 1 et 100
    nombre_a_deviner = random.randint(1, 100)

    essais = 0
    trouve = False

    # Boucle de jeu
    while not trouve:
        # Demander à l'utilisateur de deviner le nombre
        essai = int(input("Devine un nombre entre 1 et 100 : "))
        essais += 1

        # Vérifier si la réponse est correcte
        if essai < nombre_a_deviner:
            print("Le nombre est plus grand !")
        elif essai > nombre_a_deviner:
            print("Le nombre est plus petit !")
        else:
            print(f"Bravo ! Vous avez deviné le nombre {nombre_a_deviner} en {essais} essais.")
            trouve = True


# Lancer le jeu
jeu_devine_nombre()
