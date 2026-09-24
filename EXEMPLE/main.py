def afficher_informations_personne(nom,age,taille=0):
    print (f"je m'appelle {nom} et j'ai {age} ans")
    print ("l'année prochaine j'aurai " + str(age+1) + " ans")
#    print ("l'année prochaine j'aurai %s ans " % (age+1))
    condition = age >= 18
    if age ==1 or age ==2:
        print("Vous êtes un bébé")
    elif age < 10:
        print ("Vous êtes enfant")
    elif age == 17:
        print ("Vous êtes presque majeur")
    elif  12 <= age < 18:
        print ("Vous êtes adolescent")
    elif age == 18:
        print ("Vous êtes tout juste majeur")
    elif age >= 18:
        print("vous êtes majeur")
    elif age > 68:
        print ("Vous êtes senior")
    else:
        print("vous êtes mineur")
    
    # afficher la taille
    if not taille == 0:
        print("Votre taille : " + str(taille) + " m")

def demander_nom():
    reponse_nom = ""
    while reponse_nom == "":
        reponse_nom = input("Quel est votre nom ? ")
    else:
        return (reponse_nom)


def demander_age(personne):
    age_int = 1
    while age_int == 1:
        age_int = input(personne + " Quel est votre âge ? ")
    try:
        age_int = int(age_int)
    except:
        print("Erreur : veuillez entrer un nombre valide pour l'âge.")
    return (age_int)   


#nom1 = demander_nom()
#nom2 = demander_nom()
#nom1 = "personne1"
#nom2 = "personne2"
#age1  = demander_age(nom1)
#age2  = demander_age(nom2)

NB_PERSONNES = 1
for i in range(0, NB_PERSONNES):
    nom = "personne" + str(i+1)
    age = demander_age(nom)
    afficher_informations_personne(nom,age, 1.60)

print("""
az
       az 
            az
      
      """)
#afficher_informations_personne(nom1,age1)
#afficher_informations_personne(nom2,age2)

#nom1 = demander_nom()
#nom2 = demander_nom()
#age1 = demander_age(nom1)
#age2 = demander_age(nom2)

# afficher les résultats

#print ("je m'appelle " + nom1 + " et j'ai " + str(age1) + " ans")
#print ("l'année prochaine j'aurai " + str(age1+1) + " ans")
#print ("je m'appelle " + nom2 + " et j'ai " + str(age2) + " ans")
#print ("l'année prochaine j'aurai " + str(age2+1) + " ans")



    








 


