# LES COLLECTIONS : PROJET QUESTIONNAIRE
#
# Partez de ce code source pour réaliser la version 2 du projet questionnaire
#
#############################################################################
# FORMATION COMPLÈTE "DÉVELOPPEUR PYTHON"
# 
# Pour progresser en programmation et aller plus loin avec le langage Python,
# découvrez ma formation complète ici : 
# https://codeavecjonathan.com/formations.html
#############################################################################

question1 = ("Quelle est la capitale de la France ?", ("Marseille", "Nice", "Paris", "Nantes", "Aix"), "Paris")
question2 = ("Quelle est la capitale de l'Italie ?", ("Rome", "Venise", "Pise", "Florence"), "Rome")


def demander_reponse_numerique_utilisateur(min, max):
    reponse_str = input("Votre réponse (entre " + str(min) + " et " + str(max) + ") :")
    try:
        reponse_int = int(reponse_str)
        if min <= reponse_int <= max:
            return reponse_int
        print("ERREUR: vous devez entrer un nombre entre", min, "et", max)
    except:
        print("ERREUR: veuillez entrer unioquement des chiffres")
    return demander_reponse_numerique_utilisateur(min,max)

def poser_question(question):
    choix = question[1]
    bonne_reponse = question[2]
    global score
    print("QUESTION")
    print(" ", question[0])
    for i in range(len(choix)):
        print ("  ", i+1, "-", choix[i])
    print()
    reponse_int = demander_reponse_numerique_utilisateur(1, len(choix))
    if choix[reponse_int-1] == bonne_reponse:
        print("Bonne réponse")
        score += 1
    else:
        print("Mauvaise réponse")    
    print()


score = 0

poser_question(question1)
poser_question(question2)

print("Score final :", score)

