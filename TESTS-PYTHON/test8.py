""" "Écris une fonction qui prend une liste de mots et retourne un dictionnaire avec chaque mot et sa longueur."

Exemples :

["chat", "éléphant", "rat"] → {"chat": 4, "éléphant": 8, "rat": 3} """


def transfo(x: list):
    y={}
    for i in x:
        len(i)
        y[i]=len(i)
    return y

print(transfo(["chat", "éléphant", "rat"]))