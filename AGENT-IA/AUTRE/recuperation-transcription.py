import os
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload
import io

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

    request = service.files().export_media(
        fileId=fichier["id"],
        mimeType="text/plain"
    )
    contenu = io.BytesIO()
    downloader = MediaIoBaseDownload(contenu, request)

    done = False
    while not done:
        _, done = downloader.next_chunk()

    return contenu.getvalue().decode("utf-8")


if __name__ == "__main__":
    transcription = recuperer_transcription()
    if transcription:
        print(transcription)