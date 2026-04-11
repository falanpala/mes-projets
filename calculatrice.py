print("=== CALCULATRICE ===")

premier_nombre = float(input("Premier nombre : "))
operation = input("Opération (+, -, *, /) : ")
deuxieme_nombre = float(input("Deuxième nombre : "))

if operation == "+":
    resultat = premier_nombre + deuxieme_nombre
    print("Résultat :", resultat)

elif operation == "-":
    resultat = premier_nombre - deuxieme_nombre
    print("Résultat :", resultat)

elif operation == "*":
    resultat = premier_nombre * deuxieme_nombre
    print("Résultat :", resultat)

elif operation == "/":
    if deuxieme_nombre != 0:
        resultat = premier_nombre / deuxieme_nombre
        print("Résultat :", resultat)
    else:
        print("Erreur : division par zéro")

else:
    print("Opération invalide")