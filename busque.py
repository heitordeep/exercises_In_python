import requests
from bs4 import BeautifulSoup as bs
import csv
from time import sleep


class SearchArtist:

    def __init__(self):
        self.site = 'https://web.archive.org/web/20121007173054/http://www.nga.gov/collection/anF1.htm'
        self.body = 'BodyText'
        self.alpha = 'AlphaNav'
        self.href = 'a'

    def search(self):
        page = requests.get(self.site)
        soup = bs(page.text, 'html.parser')
        self.find_artist(soup)

    def find_artist(self, soup):
        last_links = soup.find(class_=self.alpha)
        last_links.decompose()
        artist_name_list = soup.find(class_=self.body)
        artist_name_list_items = artist_name_list.find_all(self.href)
        self.read(artist_name_list_items)

    def read(self, artist_name_list_items):
        f = csv.writer(open('artists/artist_name.csv', 'w'))
        f.writerow(['Names', 'Links'])

        for artist_name in artist_name_list_items:
            name = artist_name.contents[0]
            links = 'https://web.archive.org' + artist_name.get('href')
            print(name)
            print(links)
            sleep(0.3)
            f.writerow([name, links])


if __name__ == "__main__":
    result = SearchArtist()
    result.search()
