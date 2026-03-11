import requests
from bs4 import BeautifulSoup
import json

URL = "https://www.ansa.it/sito/notizie/topnews/topnews.shtml"
BASE_URL = "https://www.ansa.it"  # Per trasformare i link relativi in assoluti

def get_news():
    response = requests.get(URL)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")
    div_annunci = soup.find('div', class_='span6 pp-column pull-right')

    # Trova tutti i tag <a> che contengono le notizie
    articles = div_annunci.find_all("a")  

    news_list = []
    for article in articles:
        title = article.text.strip()
        link = article["href"] if article.has_attr("href") else "Nessun link"
        
        # Trasforma i link relativi in assoluti
        if link.startswith("/"):
            link = BASE_URL + link

        # Aggiungi solo titoli validi con un link corretto
        if title and link.startswith("http"):
            news_list.append({"titolo": title, "link": link})

    return news_list

def save_to_json(data, filename="data.json"):
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    news = get_news()
    if news:
        save_to_json(news)
        print("✅ Notizie salvate con successo in data.json!")
    else:
        print("❌ Nessuna notizia trovata.")
