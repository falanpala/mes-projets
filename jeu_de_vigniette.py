import random

nombre_secret = random.randint(1, 10)
essais = 0

while True:
    essai = int(input("Devine le nombre (1-10) : "))
    essais += 1

    if essai < nombre_secret:
        print("C'est plus")

    elif essai > nombre_secret:
        print("C'est moins")

    else:
        print("Vous avez réussi en", essais, "essai(s)")
        break
