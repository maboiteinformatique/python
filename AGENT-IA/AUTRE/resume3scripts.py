import os
import io
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload
from groq import Groq

SCOPES = ["https://www.googleapis.com/auth/drive.readonly"]

def get_drive_service():
    creds = None
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
            creds = flow.run_local_server(port=0)
        with open("token.json", "w") as token:
            token.write(creds.to_json())
    return build("drive", "v3", credentials=creds)


def recuperer_transcription():
    service = get_drive_service()
    results = service.files().list(
        q="name contains 'Transcription' and mimeType='application/vnd.google-apps.document'",
        orderBy="createdTime desc",
        pageSize=1,
        fields="files(id, name, createdTime)"
    ).execute()
    fichiers = results.get("files", [])
    if not fichiers:
        print("Aucune transcription trouvée.")
        return None
    fichier = fichiers[0]
    print(f"Transcription trouvée : {fichier['name']}")
    request = service.files().export_media(fileId=fichier["id"], mimeType="text/plain")
    contenu = io.BytesIO()
    downloader = MediaIoBaseDownload(contenu, request)
    done = False
    while not done:
        _, done = downloader.next_chunk()
    return contenu.getvalue().decode("utf-8")


def resumer_transcription(transcription):
    client = Groq(api_key="NOUVELLE_CLE_GROQ")
#   console.groq.com 
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": f"""Voici la transcription d'une réunion Google Meet.
Merci de fournir un résumé structuré avec :
- Les points clés discutés
- Les décisions prises
- Les actions à réaliser (avec les responsables si mentionnés)

Transcription :
{transcription}"""
            }
        ]
    )
    return response.choices[0].message.content


def envoyer_email(destinataire, sujet, corps_message):
    expediteur = "contact@maboiteinformatique.com"
    mot_de_passe = "NOUVEAU_MOT_DE_PASSE_A_CREER"
    # https://myaccount.google.com/u/1/apppasswords
    message = MIMEMultipart()
    message["From"] = expediteur
    message["To"] = destinataire
    message["Subject"] = sujet
    message.attach(MIMEText(corps_message, "plain"))
    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(expediteur, mot_de_passe)
            server.sendmail(expediteur, destinataire, message.as_string())
            print(f"E-mail envoyé avec succès à {destinataire} !")
    except smtplib.SMTPAuthenticationError:
        print("Erreur d'authentification : vérifiez vos identifiants.")
    except smtplib.SMTPException as e:
        print(f"Erreur SMTP : {e}")


if __name__ == "__main__":
    transcription = recuperer_transcription()
    if transcription:
        resume = resumer_transcription(transcription)
        print("\nRésumé :\n", resume)
        envoyer_email(
            destinataire="maboiteinformatique@gmail.com",
            sujet="Résumé de la réunion Google Meet",
            corps_message=resume
        )