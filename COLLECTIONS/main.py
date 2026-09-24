# personnes = ["mélanie","Jean","fabien","edouard","Alice","Pierre","Paul"]
# nvpersonne = "David"


# # del personnes[1]

# # # personnes.append(nvpersonne)
# # # for i in personnes:
# # #     print(i)

# # print(personnes)


# # def obtenir_informations():
# #     return "Mélanie", 37, 1.60

# # def afficher_informations(nom, age, taille):
# #     print(f"Informations: Nom: {nom}, age: {age}, taille:{taille}")
    

# # infos = obtenir_informations()
# # afficher_informations(*infos)
# # print(infos)
# # print(*infos)


# # slices

# for i in personnes[::-1]:
#     print(i)

# demander des noms de personnes


# noms = []

# while True:
#     nom = input ("quel est ton nom ? ")
#     if nom =="":
#         break
#     noms.append(nom)

# print()
# print("noms des personnes")
# noms.sort()
# for nom in noms:
#     print(" ", nom)


nom_chauffeur = ["mélanie","Jean","fabien","edouard","Alice","Pierre","Paul"]
distance = [1.5, 2.3, 0.4, 0.9, 7.1, 0.2, 0.6]

distancelpc = distance[0]
nom_chauffeurlpc = ""

for i in range(len(distance)):
    if distancelpc > distance[i] :
        distancelpc = distance[i]
        nom_chauffeurlpc = nom_chauffeur[i]


# print("la distance la plus courte est", distancelpc, "km et le nom du chauffeur est", nom_chauffeurlpc )
distance.sort()
print(distance)
print (distancelpc, nom_chauffeurlpc)