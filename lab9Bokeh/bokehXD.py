from bokeh.models import Div, RangeSlider, Spinner, Slider, CustomJS
from bokeh.plotting import figure, show
import numpy as np
from scipy.integrate import odeint
from bokeh.plotting import ColumnDataSource
from bokeh.layouts import column, row

def SIR(y,t,N,beta,gamma):
  S,I,R = y
  dS = -beta*S*I/N
  dI = beta*I*S/N-gamma*I
  dR = gamma*I
  return dS,dI,dR

t = np.linspace(0,60,100)
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

#p = figure(x_range=(1,9), width=500, height=250)
slider_beta = Slider(start =0, end = 1, step = 0.05, value=0.5, title='Beta')
slider_gamma = Slider(start =0, end = 1, step = 0.05, value=0.25, title='Gamma')



array_lengthy = len(sol)
last_elementy = sol[array_lengthy - 1]


fig = figure()
plot = figure(x_range=(0, 1000), y_range=(0, 1000), width=350, height=350)
res = list(sol[:,0])
res2 = list(sol[:,1])
res3 = list(sol[:,2])
data1 = dict(x=t,y=res)
data2 = dict(x=t,y=res2)
data3 = dict(x=t,y=res3)
print(res)
source1 = ColumnDataSource(data=data1)
source2 = ColumnDataSource(data=data2)
source3 = ColumnDataSource(data=data3)


def Update_beta(attr, old, new):
    global beta
    beta = new
    sol = odeint(SIR, y_0, t, (new, gamma))
    new_data1 = dict(x=t,y=list(sol[:,0]))
    new_data2 = dict(x=t, y=list(sol[:, 1]))
    new_data3 = dict(x=t, y=list(sol[:, 2]))
    source1.data = new_data1
    source2.data = new_data2
    source3.data = new_data3

def Update_gamma(attr,old,new):
    global gamma
    gamma = new
    sol = odeint(SIR, y_0, t, (beta, new))
    new_data1 = dict(x=t, y=list(sol[:, 0]))
    new_data2 = dict(x=t, y=list(sol[:, 1]))
    new_data3 = dict(x=t, y=list(sol[:, 2]))
    source1.data = new_data1
    source2.data = new_data2
    source3.data = new_data3


plot.line(color = "red",legend_label="S", line_width=2,source=source1)
plot.line(color = "green",legend_label="I", line_width=2,source=source2)
plot.line(color = "blue",legend_label="R", line_width=2,source=source3)

slider_beta.on_change("value",Update_beta)
slider_gamma.on_change("value",Update_gamma)

layout = row(
    plot,
    column(slider_beta,slider_gamma),
)



show(layout)

#doc.add_root(column(slider_beta,slider_gamma, plot))

# creating the application and running the server local, (http://localhost:5000), port 5000 can be changed
#apps = {'/': Application(FunctionHandler(make_page))}
#server = Server(apps, port=5000)
#server.start()


