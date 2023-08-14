import requests
from bs4 import BeautifulSoup

r = requests.get('https://edition.cnn.com/travel/article/scenic-airport-landings-2020/index.html')
soup = BeautifulSoup(r.content, 'html.parser')
title = soup.title.get_text() 

par = soup.find_all('p')
parText = ""
for e in par: 
    parText = parText + e.get_text()

date = soup.find('meta', property='article:modified_time')['content'] 

byline = soup.find('meta', attrs ={'name': 'author'}) 
byline = byline['content']

print("Date published: ", date)
print("Byline: ", byline)
print("Title: ", title)
print("Article Content: ", parText)

