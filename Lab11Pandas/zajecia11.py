import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import io
import scipy.special
from bokeh.layouts import gridplot
from bokeh.plotting import figure, show
from ascii_graph import Pyasciigraph
from ascii_graph.colors import *
from ascii_graph.colordata import hcolor


suicide = pd.read_csv("suicide-rates-by-age-detailed.csv")

year = suicide['Year']
col = suicide.columns
print(col)

#aha = suicide[col[7]].where(suicide[col[2]] == 1998)
#aha = suicide.agg({'Year' : ['1998']})
#print(aha)
group = suicide.groupby('Entity').agg(total_new_case = (col[5],np.sum))

kraje = suicide['Entity'].values.tolist()
kraje2 = []
for element in kraje:
    if element not in kraje2:
        kraje2.append(element)
    else:
        pass

samobuje = group['total_new_case'].values.tolist()

print(kraje2)
print(samobuje)
plt.bar(kraje2, samobuje)
plt.xlabel('Country')
plt.xticks(rotation = 90)
plt.ylabel('Sum of suicide rates')
plt.title('Sums of suicide rates in all ages in all countries in years 1990-2019')

plt.show()
#print(kraje2[156])
#print(samobuje[156])
#poland = suicide[col[5]].where(suicide['Entity'] == 'Poland')
#print(poland)
poland = suicide.loc[suicide['Entity'] == 'Poland', col[5]]
sum_of_poland = np.sum(poland)
print(sum_of_poland)

#graph = Pyasciigraph()
#for line in graph.graph('Histogram of suicides' ,samobuje):
#    print(line)
