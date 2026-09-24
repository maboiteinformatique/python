
# Questionnaire:

pays = ["France", "Italie", "Espagne"]
villes_France = ["Marseille", "Nantes", "Paris", "Rennes"]
villes_Italie = ["Rome", "Genes", "Naples", "Milan"]
villes_Espagne = ["Madrid", "Barcelone", "Santander", "valladolid"]
villes = ""

choix = ["a -","b -","c -","d -"]
solution_villes_France = "c"
solution_villes_Italie = "a"
solution_villes_Espagne = "a"
longueur_liste_pays = len(pays)
longueur_liste_villes = len(villes_France)

# ajouter une vérification qu'il s'agit d'une seule lettre a,b,c,d (préciser dans la question)
# réduire le code: 
#   -> les print répétés: choix input, vous êtes le meilleur, c'est faux
#   -> remplacer les pays par des appels dans les listes (pour pouvoir ajouter un pays) 
#      mettre une boucle:
#           for i in range len pays
#           pays = pays[i] 
#           do: if villes = pays[0] (remplacer villes par pays) 


def print_questionnaire(pays):

    if pays == "France":
        for i in range(longueur_liste_villes):
            print(choix[i],villes_France[i])
        print()
        choix_utilisateur = input ()
        if choix_utilisateur == solution_villes_France:
            print ("vous êtes le meilleur, c'est bon ! ")
        else:
            print(" Eh be c'est faux, une autre fois ;)")
    elif pays == "Italie":
        for i in range(longueur_liste_villes):
            print(choix[i],villes_Italie[i])
        print()
        choix_utilisateur = input ()
        if choix_utilisateur == solution_villes_Italie:
            print ("vous êtes le meilleur, c'est bon ! ")
        else:
            print(" Eh be c'est faux, une autre fois ;)")
    else:
        for i in range(longueur_liste_villes):
            print(choix[i],villes_Espagne[i])
        print()
        choix_utilisateur = input ()
        if choix_utilisateur == solution_villes_Espagne:
            print ("vous êtes le meilleur, c'est bon ! ")
        else:
            print(" Eh be c'est faux, une autre fois ;)")

for i in range(longueur_liste_pays):
    print()
    print ("Quelle est la capitale du pays", pays[i], "? ")
    print()
    print_questionnaire (pays[i])

