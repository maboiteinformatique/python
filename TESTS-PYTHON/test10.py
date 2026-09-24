""" Exercice algo 10

"Écris une fonction qui prend une liste de nombres et retourne la moyenne."

[1, 2, 3, 4, 5] → 3.0
[10, 20, 30]    → 20.0 """

def moyenne(a: list):
    b = 0
    for i in a:
            b = b + i
    return b/len(a)

print (moyenne(on e ne [10, 20, 30, 40]))
    
        
    
        