
# return (pas obligatoire)
# sortir de la fonction
# renvoyer une valeur (pas obligatoire)

#
# recuperer_et_afficher_infos_personne
# -> recuperer_infos_personne
# -> afficher_infos_personne (nom, age)
#       -> est_majeur()


# FONCTIONS

def est_majeur(age: int):
    if age >= 18:
        return True
    return False

def recuperer_infos_personne(numero_personne):
    nom_personne = input("que est le nom de la personne " + str(numero_personne) + "? ")
    age_personne = input("quel est l'age de la personne " + str(numero_personne) + "? ")
    return nom_personne, int(age_personne)

def afficher_infos_personne(numero_personne, nom, age: int):
    print("la personne", numero_personne, "s'appelle", nom, "et a", age, "ans")
    if est_majeur(age):
        print("je suis majeur")
    else:
        print("je suis mineur")

def recuperer_et_afficher_infos_personne(numero_personne):
    nom, age = recuperer_infos_personne(numero_personne)
    afficher_infos_personne(numero_personne, nom, age)

# EXECUTION

nb_personnes = 2
for i in range(nb_personnes):
    recuperer_et_afficher_infos_personne(i+1)

    # if age == 0:
    #     print("la personne s'appelle", nom)
    #     return
    # if nom == "":
    #     print ("vous n'avez pas donné de nom, l'age est", age)
    #     return
    # else:
    #     print("la personne s'appelle", nom, "et a", age, "ans")
    # if est_majeur(age):
    #     print("je suis majeur")
    # else:
    #     print("je suis mineur")


# def recuperer_et_afficher_infos_personne(numero_personne):

    # nom = input("que est le nom de la personne " + str(numero_personne) + "? ")
    # age = input("quel est l'age de la personne " + str(numero_personne) + "? ")

    # print("la personne", numero_personne, "s'appelle", nom, "et a ", age, "ans")

# nb_personnes = 2
# for i in range(nb_personnes):
#     recuperer_et_afficher_infos_personne(i+1)
