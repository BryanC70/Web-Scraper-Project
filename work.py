import requests
from bs4 import BeautifulSoup

r = requests.get('https://edition.cnn.com/travel/article/scenic-airport-landings-2020/index.html')
soup = BeautifulSoup(r.content, 'html.parser')
title = soup.title
header = soup.header
print(title)
