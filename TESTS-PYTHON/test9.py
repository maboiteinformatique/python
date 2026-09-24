""""Écris une fonction qui prend une chaîne de caractères et retourne True si tous les caractères sont uniques, 
False sinon."

Exemples :

"python"  → True
"bonjour" → False  (o apparaît deux fois) """

def unique(a: str):
    for i in range(len(a)):
        for j in range(i+1,len(a)):
            if a[i] == a[j]:
                return False
    else:
        return True

print(unique("python"))


# TODO : Faire la même fonction avec set 

def unique2(a: str):
    return len(set(a)) == len(a)

print(unique2("python"))       


