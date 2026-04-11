def calculatrice():
    print("=== Calculatrice ===")
    print("Opérations disponibles : +  -  *  /")

    while True:
        try:
            a = float(input("Premier nombre : "))
            op = input("Opérateur (+, -, *, /) : ")
            b = float(input("Deuxième nombre : "))

            if op == "+":
                resultat = a + b
            elif op == "-":
                resultat = a - b
            elif op == "*":
                resultat = a * b
            elif op == "/":
                if b == 0:
                    print("Erreur : division par zéro")
                    continue
                resultat = a / b
            else:
                print("Opérateur invalide")
                continue

            print("Résultat :", resultat)

        except ValueError:
            print("Entrée invalide")

        choix = input("Continuer ? (o/n) : ")
        if choix.lower() != "o":
            break

calculatrice()