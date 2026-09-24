
from groq import Groq

def resumer_transcription(transcription):
    client = Groq(api_key="coucou")

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        max_tokens=1024,
        messages= [
            {
                "role": "user",
                "content": f"""Voici la transmission d'une réunion Google Meet.
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

if __name__ == "__main__":
    transcription = """
    Jean : Bonjour tout le monde, on commence la réunion.
    Marie : On doit décider du budget pour le projet X.
    Jean : On fixe le budget à 10 000€, Marie s'occupe du devis.
    Pierre : Je prends en charge la communication client d'ici vendredi.
    """

    resume = resumer_transcription(transcription)
    print(resume)