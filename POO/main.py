
# Personne (classe)
# données: nom, age
# Actions: (méthodes) - se presenter, demander son nom


# definition
# nom: str
# age: int
# 1 - si age == 0
# => Bonjour, je m'appelle toto
# 2 - si nom == ""
# => Demander nom utilisateur
# => DemanderNom(...) -> inut("") -> nom

class Personne:
    def __init__(self, nom: str = "", age: int = 0):
        self.nom = nom # crée une variable d'instance: nom
        self.age = age
        if self.nom == "":
            self.DemanderNom()   
    
    def SePresenter(self):
        # Bonjour, je m'appelle jean et j'ai 30 ans
        # je suis majeur, je suis mineur
        infopersonne = "Bonjour, je m'appelle " + self.nom
        infopersonne1 = infopersonne + ", j'ai " + str(self.age)

        if self.age == 0:
            print(infopersonne) 
        elif self.EstMajeur():
            print(infopersonne1 + " et je suis majeur")
        else:
            print(infopersonne1 + " et je suis mineur")

    def EstMajeur(self):
        return self.age >= 18
    
    def DemanderNom(self):
        self.nom = input("que est ton nom ? ")
        

# utilisation
#personne1 = Personne("Jean", 16) # je crée une personne
#personne2 = Personne("Jacques", 24) # je crée une personne

liste_personne = (Personne("Jean", 16),Personne("Jacques", 24), Personne("Zoë", 56))

for i in liste_personne:
    i.SePresenter()






