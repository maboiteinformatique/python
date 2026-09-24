# "Écris une fonction qui prend une chaîne de caractères et retourne le nombre de voyelles qu'elle contient."

""" 

b = 0
pour i dans la liste [olive]:
    si i est voyelle alors b = b + 1
return b

 """

def nbre_voyelles(a: str):
    b = 0
    for i in a:
        if i in "aeiouAEIOU":
            b = b + 1
    return b

print(nbre_voyelles("python"))