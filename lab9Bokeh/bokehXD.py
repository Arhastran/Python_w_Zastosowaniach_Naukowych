from bokeh.models import Div, RangeSlider, Spinner, Slider
from bokeh.plotting import figure, show
from bokeh.layouts import layout
import numpy as np
from scipy.integrate import odeint
import pandas as pd

def SIR(y,t,beta,gamma):
  S,I,R = y
  dS = -beta*S*I
  dI = beta*I*S-gamma*I
  dR = gamma*I
  return dS,dI,dR

t = np.linspace(0,60,100)
print(t)
array_length = len(t)
last_element = t[array_length - 1]
S_0 = 1000
I_0 = 10
R_0 = 0

y_0 = S_0, I_0, R_0
beta =0.5
gamma=0.25
t = np.linspace(0,60,100)

sol = odeint(SIR,y_0,t,(beta,gamma))

p = figure(x_range=(1,9), width=500, height=250)
slider_beta = Slider(start =0, end = 1, step = 0.05, value=0.5, title='Beta')
slider_gamma = Slider(start =0, end = 1, step = 0.05, value=0.25, title='Gamma')

def Update_beta(attr, old, new):
    global beta
    beta = new
    sol = odeint(SIR, y_0, t, (beta, gamma))

def Update_gamma(attr,old,new):
    global gamma
    gamma = new
    sol = odeint(SIR, y_0, t, (beta, gamma))

array_lengthy = len(sol)
last_elementy = sol[array_lengthy - 1]

slider_beta.on_change("value", Update_beta)
slider_gamma.on_change("value", Update_gamma)
fig = figure()
plot = figure(x_range=(0, 100), y_range=(0, 100), width=350, height=350)
source = {'t': t[:],'S': sol[:,0], 'I': sol[:,1], 'R': sol[:,2]}
source2 = pd.DataFrame(data=source)
line = plot.line(source=source2['t','S'])

layout = layout([
    [slider_beta],
    [slider_gamma],
    [plot],
    [line],
    [p],
])

show(layout)


