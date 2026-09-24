import requests
from bs4 import BeautifulSoup

url = "https://codeavecjonathan.com/scraping/recette_js"

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

    f = open("SCRAPING/recette.html", "w")
    f.write(html)
    f.close()

    soup = BeautifulSoup(html, "html5lib")
    titre = soup.find("h1").text
    description = get_test_if_not_none(soup.find("p", class_="description"))
 #   print(description)

    # Ingrédients
    div_ingredients = soup.find("div", class_="ingredients")
    ingredients = div_ingredients.find_all("p")
    for ingredient in ingredients:
        print("INGREDIENTS", ingredient.text)

    # éléments préparation
    preparation = soup.find("table", class_="preparation")
    etapes = preparation.find_all("td", class_="preparation_etape")
    for i in etapes:
        print("ETAPE", i.text)

else:
    print("ERREUR:", response.status_code)


#print("FIN")
