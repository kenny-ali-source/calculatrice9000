def outer_calculator():
    num1 = float(input("Veuillez saisir le premier nombre : "))
    operator = input("Veuillez saisir un opérateur (+ - * /) : ")
    num2 = float(input("Veuillez saisir le deuxième nombre : "))
    result = 0

    if operator == "+":
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            print("Erreur : Division par zéro.")
            exit()
    else:
        print("Erreur : Opérateur non valide.")
        exit()

    print(round(result))
    inner_calculator(result)


def inner_calculator(result):
    historic = input("Voulez-vous conserver l'historique de votre calcul : oui ou non ?")

    if historic == "oui":
        history.append(result)
        print("Historique :", (history))
    elif historic == "non":
        exit()
    else:
        print("Erreur : Réponse non valide.")
        exit()

history = []
outer_calculator()

            


    


