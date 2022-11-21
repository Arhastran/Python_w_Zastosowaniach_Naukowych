#Adam Ignaciuk lab 4
# 02.11.2022
# static scrapping

import json
import requests
from bs4 import BeautifulSoup
from rich.console import Console
from rich.table import Table


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

console = Console()
table = Table(title="Worst movies from IMDB ")
table.add_column("Number", style="cyan")
table.add_column("Name of the bad bad movie", style="red")

films = []
for film in psy.find_all('a'):
    #span = film.find('title=')
    #title = film.find('a')
    #print(film)
    #print(span)
    films.append(film.text.strip())
    #print(film.text.strip())
#soup.select("product-desc")
newfilms = []
iter = 1
for i in range(len(films)):
    if (i % 2) == 0:
        pass
    else:
        newfilms.append(films[i])
        no = str(iter)
        table.add_row(no, films[i])
        iter += 1
console.print(table)


