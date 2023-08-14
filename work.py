import requests
from bs4 import BeautifulSoup

r = requests.get('https://edition.cnn.com/travel/article/scenic-airport-landings-2020/index.html')
soup = BeautifulSoup(r.content, 'html.parser')
title = soup.title.get_text() # grabs the title from the article

par = soup.find_all('p') # looks through article and finds all instances of a "p" tag and puts them in a list
parText = ""
for e in par: # for loops that looks through the list and extracts all of the text from the list 
    parText = parText + e.get_text()

print(title)
print(parText)

