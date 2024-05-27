import urllib.request
from bs4 import BeautifulSoup

class Scraper:
    def __init__(self, site):
        self.site = site

    def scrape(self):
        response = urllib.request.urlopen(self.site)
        xml = response.read()
        parser = "html.parser"
        scrap = BeautifulSoup(xml, parser)

        for item in scrap.find_all("item"):
            title = item.find("title")
            if title is None:
                continue
            else:
                print("\n" + title.text)

news = "https://news.google.com/news/rss/headlines"
Scraper(news).scrape()
    