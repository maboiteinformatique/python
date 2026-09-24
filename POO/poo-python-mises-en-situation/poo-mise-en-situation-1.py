# POO EXERCICE DE MISE EN SITUATION 1
# genre
#   False : Femme
#   True  : Homme
class Personne:
    def __init__(self, nom: str, age: int, genre: bool):
        self.nom = nom   # crée une variable d'instance : nom
        self.age = age
        self.genre = genre
        print("Constructeur personne " + self.nom)

    def SePresenter(self):
        # Bonjour, je m'appelle Jean, j'ai 30 ans
        # Je suis majeur

        print("Bonjour, je m'appelle " + self.nom + ", j'ai " + str(self.age) + " ans")
        
        if self.genre:
             
            strgenre = "Genre : Masculin"

            if self.EstMajeur():
                 
                strage = "Je suis majeur"
            else:
                strage = "Je suis mineur"     
        else:
            strgenre = "Genre : Féminin"

            if self.EstMajeur():
                 
                strage = "Je suis majeure"
            else:
                strage = "Je suis mineure" 

        print(strgenre)
        print(strage)
        print()

    def EstMajeur(self):
        return self.age >= 18

personne1 = Personne("Jean", 16, True)
personne1.SePresenter()

personne2 = Personne("Emilie", 17, False)
personne2.SePresenter()