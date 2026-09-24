
facteur_conversion = 2.54

def convertisseur(valeur,choix_fonction,facteur_conversion):
    valeur = float(valeur)
    if choix_fonction == "1":
        valeur = round(valeur * facteur_conversion,2)
        print (f"le résutat de la conversion est {valeur} cm")
    elif choix_fonction == "2":
        valeur = round(valeur * (1/facteur_conversion),2)
        print (f"le résutat de la conversion est {valeur} pouces")

print ("Souhaitez-vous convertir des pouces vers cm ou des cm vers pouces ? ") 

message_choix = "1 = pouces vers cm, 2 = cm vers pouces (choix 1 ou 2 - ou q pour quitter) : "

# demande du choix 1 ou 2 ou q
# vérification si c'est 1 ou 2 qui est entré, si oui on continue
# vérification si q, si on sort


while True:
    choix = input(message_choix)
    if choix in ("1", "2"):
        break
    if choix == "q":
        exit()
    message_choix = "choix invalide, veuillez entrer 1 ou 2 (q pour quitter): "


# demande de la valeur à entrer
# vérification si c'est un decimal qui est entré

message_valeur = "Entrez la valeur à convertir : "
while True:
    valeur = input(message_valeur)
    try:
        float(valeur)
        break
    except ValueError:
        message_valeur = "Valeur invalide, veuillez entrer un decimal: "

# conversion de la valeur

convertisseur(valeur, choix, facteur_conversion)

