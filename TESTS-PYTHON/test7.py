"""  

Exercice algo 7

"Écris une fonction qui prend deux listes et retourne les éléments communs aux deux."

Exemples :
[1, 2, 3, 4], [3, 4, 5, 6] → [3, 4]
[1, 2, 3], [4, 5, 6]       → []


pour i dans A --> verif si i dans B --> true --> append c avec i

"""

def fcom(a: list, b: list):
    c=[]
    for i in a:
        for j in b:
            if i==j:
                c.append(i)
    return c

print(fcom([1, 2, 3, 4], [3, 4, 5, 6]))
