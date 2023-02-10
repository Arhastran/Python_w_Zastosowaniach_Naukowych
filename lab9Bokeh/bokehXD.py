from bokeh.models import Div, RangeSlider, Spinner, Slider, CustomJS
from bokeh.plotting import figure, show
import numpy as np
from scipy.integrate import odeint
from bokeh.plotting import ColumnDataSource
from bokeh.layouts import column, row
from bokeh.io import curdoc
import pandas as pd


#COMMANDS:
#  bokeh serve --show bokehXD.py

def SIR(y,t,N,beta,gamma):
  S,I,R = y
  dS = -beta*S*I/N
  dI = beta*I*S/N-gamma*I
  dR = gamma*I
  return dS,dI,dR

t = np.linspace(0,50,100)
array_length = len(t)
last_element = t[array_length - 1]
N = 10000
S_0 = 8989
I_0 = N-S_0
R_0 = 0

y_0 = S_0, I_0, R_0
beta =0.5
gamma=0.25
t = np.linspace(0,60,100)

sol = odeint(SIR,y_0,t,(N,beta,gamma))
Results = pd.DataFrame({"t" : t, "S" : list(sol[:,0]), "I" : list(sol[:,1]), "R" : list(sol[:,2])})
source = ColumnDataSource(Results)

#p = figure(x_range=(1,9), width=500, height=250)
slider_beta = Slider(start =0, end = 1, step = 0.05, value=0.5, title='Beta')
slider_gamma = Slider(start =0, end = 1, step = 0.05, value=0.25, title='Gamma')
slider_N = Slider(start =0, end = 10000, step = 10, value=10000, title='N')
#slider_S_0 = Slider(start =0, end = 10000, step = 10, value=8900, title='S_0')

array_lengthy = len(sol)
last_elementy = sol[array_lengthy - 1]

fig = figure()

#res = list(sol[:,0])
#res2 = list(sol[:,1])
#res3 = list(sol[:,2])
#data1 = dict(x=t,y=res)
#data2 = dict(x=t,y=res2)
#data3 = dict(x=t,y=res3)

fig.line("t","S", color = "red", source=source)
fig.line("t","I", color = "green", source=source)
fig.line("t","R", color = "blue",  source=source)

def Update_beta(attr, old, new):
    global beta
    beta = new
    sol = odeint(SIR, y_0, t, (N, beta, gamma))
    new_results = pd.DataFrame({"t": t, "S": list(sol[:, 0]), "I": list(sol[:, 1]), "R": list(sol[:, 2])})
    source.data = ColumnDataSource.from_df(new_results)

def Update_gamma(attr,old,new):
    global gamma
    gamma = new
    sol = odeint(SIR, y_0, t, (N, beta, gamma))
    new_results = pd.DataFrame({"t": t, "S": list(sol[:, 0]), "I": list(sol[:, 1]), "R": list(sol[:, 2])})
    source.data = ColumnDataSource.from_df(new_results)

def Update_N(attr,old,new):
    global N
    N = new
    sol = odeint(SIR, y_0, t, (N, beta, gamma))
    new_results = pd.DataFrame({"t": t, "S": list(sol[:, 0]), "I": list(sol[:, 1]), "R": list(sol[:, 2])})
    source.data = ColumnDataSource.from_df(new_results)


slider_beta.on_change("value",Update_beta)
slider_gamma.on_change("value",Update_gamma)
slider_N.on_change("value",Update_N)


#layout = row(
#    plot,
#    column(slider_beta,slider_gamma),
#)

#print(source1.data)

#show(layout)

curdoc().add_root(row(column(Div(text = "<b>Model SIR</b>", align = "center"),slider_gamma,slider_beta,slider_N),fig))




