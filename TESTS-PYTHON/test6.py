""" 

"Écris une fonction qui prend une liste de nombres
 et retourne la liste triée dans l'ordre croissant 
 — sans utiliser sort() ni sorted()."

tri du premier élément:


def tri(x: list):
    y = []
    a = x[0]
    for i in range(len(x)):
        if x[i] < a:
            a = x[i]
    y.append(a)
    x.remove(a)

    for i in range(len(x)):
        if x[i] < b:
            b = x[i]
    y.append(b)
    x.remove(b)

    return y


def tri(x: list):
        y = []
        while a < len(x):
            a = x[0]
            for i in range(len(x)):
                if x[i] < a:
                    a = x[i]
            y.append(a)
            x.remove(a)
        return y

"""

def tri(x: list):
        y = []
        while len(x) > 0:
            a = x[0]
            for i in range(len(x)):
                if x[i] < a:
                    a = x[i]
            y.append(a)
            x.remove(a)
        return y

print(tri([2,1,4,3,8,7]))