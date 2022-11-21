#Adam Ignaciuk lab 4
# 02.11.2022
# static scrapping

import json
import requests
from bs4 import BeautifulSoup


url = "https://www.imdb.com/chart/bottom"
r = requests.get(url) #get albo post, to drugie nie jest w URL, session to coś do trzymana sesji

print(r.status_code) #200 to ok
#print(r.text)

soup = BeautifulSoup(r.text, 'html.parser')
classes = []
for element in soup.find_all(class_=True):
    classes.extend(element["class"])
#print(classes)
psy = soup.find('div', {'class':'seen-collection'})
#print(psy)


for film in psy.find_all('div',{'class' : 'global-sprite lister-sort-reverse descending'}):
    #span = film.find('title')
    #title = film.find('a')
    print(film)
    #print(span.text.strip(), title.text.strip(), title['href'])
#soup.select("product-desc")

