
""" 

1 - Demander à l'utilisateur si il souhaite convertir de "pouces vers cm" ou "cm vers pouces" 
2 - Demander à l'utilisateur de rentrer la valeur à convertir (en réaffichant l’unité demandée)
3 - Afficher la valeur convertie (et l'unité : cm ou pouces)
                                  
- fin du programme.

 """
# mettre unite 1 et 2 dans les variables conversion
# mettre un choix a ou b, et vérifier que l'utilisateur a bien écrit a ou b
# réafficher l'unité
# regarder pour faire une fonction

conversion1 = "pouces en cm"
conversion2 = "cm en pouces"
unite1 = "pouces"
unite2 = "cm"
facteur_multiplicatif = 2.54
valeur_convertie = 0
reponse_utilisateur = ""


# def verification_int(choix):
#     if choix == "1" or choix == "2":
#         return True
#     else:
#         print("Votre choix doit être 1 ou 2")
#         return False

# return True: l'utilisateur veut quitter le programme  
# return false: l'utilisateur a donné une valeur

def effectuer_conversion(unit1,unit2,facteur):
    valeur = input(f"conversion {unit1} vers {unit2}, rentrer la valeur en {unit1} ou bien q pour sortir: ")
    if valeur == "q":
        return True
    try:
        valeur_float = float(valeur)
    except ValueError:
        print ("veuillez rentrer un decimal")
        return effectuer_conversion(unit1,unit2,facteur)
    
    valeur_convertie = round(float(valeur) * facteur, 2)
    print (f"resultat de la conversion: {valeur} {unit1} = {valeur_convertie} {unit2}")
    return False

while True: 
    print("ce programme vous permet de faire les conversion pouces cm et vice versa")
    print("1 - Pouces vers cm")
    print("2 - cm vers pouces")
    choix = input("votre choix (1 ou 2): ")
    if choix =="1" or choix =="2":
        break
    print ("erreur, vous devez entrer 1 ou 2")


while True:
    if choix == "1":
        if effectuer_conversion(unite1,unite2,facteur_multiplicatif):
            break
    else:
        if effectuer_conversion(unite2,unite1,1/facteur_multiplicatif):
            break







