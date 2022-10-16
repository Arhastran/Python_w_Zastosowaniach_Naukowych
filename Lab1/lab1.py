#Adam Ignaciuk 12.10.2022
#book reading script

#program is not optimized - long books take time to be fully read

from ascii_graph import Pyasciigraph
from ascii_graph.colors import *
from ascii_graph.colordata import hcolor
import tqdm
#import time
#from rich import print as rprint
#from rich.console import Console

def readfile(filename): #function to search file
    txt = []
    txt1 = []
    f = open(filename, "r")
    for element in f:
        txt.append(element.strip("\n"))
    for element in range(len(txt)):
        txt[element] = str(txt[element])
    for element in range(len(txt)):
        a = txt[element].split(" ")
        for element2 in a:
            txt1.append(str(element2))
    return txt1

def sort_key(number): #function for sorting
    return number[1]
def exclude(words): #function for excluding words
    return words

def histogram(wordlistin, wordnumber=10, wordLength=0, Sort=True): #histogram function
    wordlistout = []
    wordlistoutfinal = []
    if Sort == True:
        wordlistin.sort(key=sort_key, reverse=True)
    else:
        pass
    for element in range(len(wordlistin)):
       if len(wordlistin[element][0])>wordLength:
            wordlistout.append(wordlistin[element])
       else:
            pass
    for element in range(wordnumber):
        wordlistoutfinal.append(wordlistout[element])

    return wordlistoutfinal


a = readfile("Hamlet.txt")
#print(a)
list=[]
listcheck=[]


for element in tqdm.tqdm(range(len(a))):
    if a[element] not in listcheck:
        b = [a[element],a.count(a[element])]
        list.append(b)
        listcheck.append(a[element])
    else:
        pass

#print(list)



graph = Pyasciigraph()
numberofwords = 10
wordlenlimit = 0
list2 = histogram(list,numberofwords, wordlenlimit)


thresholds = {
   100: Red,
   200: Yel,
   300: Gre,
   500: Blu,
   1000: Pur,
}
list2 = hcolor(list2, thresholds)

for line in graph.graph('My Histogram', list2):
    print(line)












