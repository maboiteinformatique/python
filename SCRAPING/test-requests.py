import requests
from bs4 import BeautifulSoup

url = "https://codeavecjonathan.com/scraping/techsport/"

HEADERS = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:148.0) Gecko/20100101 Firefox/148.0"}
def get_test_if_not_none(e):
    if e:
        return e.text.strip()
    return None

response = requests.get(url, headers=HEADERS)
response.encoding = response.apparent_encoding

if response.status_code ==200:
    html = response.text
    # print(html)

    f = open("SCRAPING/testrequest.html", "w")
    f.write(html)
    f.close()

else:
    print("ERREUR:", response.status_code)


#print("FIN")
