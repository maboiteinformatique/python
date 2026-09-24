# Agent IA qui résume les conversations dans un meet google et qui envoie un résumé par email

#import Playwright
#import requests

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def envoyer_resume_client(destinataire, sujet, corps_message):
    # identifiants(à sécuriser via des variables d'environnement):
    expediteur = "contact@maboiteinformatique.com"
    mot_de_passe = "tkhz ehdx fqcs venm"

    # création du message
    message = MIMEMultipart()
    message["From"] = expediteur
    message["To"] = destinataire
    message["Subject"] = sujet

# ajout du corps de l'email généré par l'IA

    message.attach(MIMEText(corps_message, "plain"))

    try:
        # connexion au serveur smtp
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(expediteur, mot_de_passe)
        #Envoi de l'email
            server.sendmail(expediteur, destinataire, message.as_string())
            print(f"Email envoyé avec succès à {destinataire} !")
    except smtplib.SMTPException as e:
        print(f"Erreur SMTP : {e}")
    except Exception as e:
        print (f"Erreur lors de l'envoi: {e}")

# exemple d'utilisation après le traitement de l'agent IA
suivi_ia = """Bonjour, voici le résumé de notre échange..."""
if __name__ =="__main__":
    envoyer_resume_client("maboiteinformatique@gmail.com","Compte-rendu de notre appel", suivi_ia)

# todo
# - améliorer la partie sécurité (emvoi d'email via une authent mot de passe avec google, mot de passe en clair), OAuth2 avec Gmail (complexe mais propre)
# Brevo (simple, gratuit, 300 mails/jour)
