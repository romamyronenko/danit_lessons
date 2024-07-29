"""
питання?

beautifulsoup4

parse https://books.toscrape.com/

бот-парсер
"""

import requests
from bs4 import BeautifulSoup

response = requests.get("https://books.toscrape.com/")

html = response.text

soup = BeautifulSoup(html, "html.parser")

for li in soup.find_all("li", class_="col-xs-6 col-sm-4 col-md-3 col-lg-3"):
    print(li.h3.a["title"])
    price = li.find("p", class_="price_color").text
    print(price)
    print()
