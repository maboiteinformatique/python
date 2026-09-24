# exercices tables de multiplication
# afficher la table de multiplication de 4 avec en entrée un min et un max
# et une vérification qui retourne une erreur si le min > max



def afficher_table(tb, min = 1, max = 10):
    tb = input("entrer le nombre dont vous voulez afficher la table de multiplication: ")
    if int(min) > int(max):
        print("Erreur: le minimum doit être inférieur au maximum.")
        return
    for i in range(int(min), int(max) + 1):
        print(tb,"x",i,"=",int(tb)*i)

afficher_table(4,6,5)




