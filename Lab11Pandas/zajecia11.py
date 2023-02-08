#18.01.2023
#Pandas

import pandas as pd
import numpy as np

suicide = pd.read_csv("suicide-rates-by-age-detailed.csv")
#print(suicide)

suicide.head()
ogon = suicide.tail()
col = suicide.columns
gowno = suicide.index
print(col)
#print(gowno)
#print(ogon)

values = suicide.values
#print(values)

types = suicide.dtypes
#print(types)

year = suicide['Year']
#print(year)

uni = suicide.Year.unique()
counts = suicide.Year.value_counts().head(20)
#print(uni)
#print(counts)

max = suicide.Year.max()
#print(max)

des = suicide.Year.describe()
#print(des)

desall = suicide.describe()
#print(desall)

#print(suicide.Year.count(),suicide.Year.size)

missing_data = suicide.Year.isna().sum()
#print(missing_data)
suicide.Year.fillna(0) #wypełnia puste Not a number liczbami

obj = suicide.select_dtypes('object')
#print(obj)

#filter = suicide.filter(like = 'Year')
#print(filter)

sort = suicide.sort_values('Entity', ascending = False)
#print(sort)

iloc = suicide.iloc[[0,3]]
suicide.iloc[2:20,4]
loc = suicide.loc
#print(iloc)

isocode = suicide.Year == 'POL'
#print(isocode)

sel = suicide.loc[suicide.Year == 'POL']
#print(sel)

suicide.set_index('Year')
suicide.reset_index()

suicide.groupby('Year')

#groupby = suicide.groupby('Year').agg(total_new_case = ('Code',np.sum))
#print(groupby)
