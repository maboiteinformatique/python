# POO EXERCICE DE MISE EN SITUATION 4

# ---
class Personne:
    def __init__(self, nom: str):
        self.nom = nom

    def SePresenter(self):
        print("Bonjour, je m'appelle " + self.nom)

# ---
nombre_personne = 2
noms = []

for i in range(nombre_personne):
       noms.append(Personne(input("nom de la personne " + str(i+1)+ ": " )))                

for i in noms:
    i.SePresenter()