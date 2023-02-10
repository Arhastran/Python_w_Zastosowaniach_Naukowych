import sympy as sp
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure


def SIR(y,t,N,beta,gamma):
  S,I,R = y
  dS = -beta*S*I/N
  dI = beta*I*S/N-gamma*I
  dR = gamma*I
  return dS,dI,dR

N = 10000
S_0 = 8989
I_0 = N-S_0
R_0 = 0

y_0 = S_0, I_0, R_0
#beta =0.5
#gamma=0.25
t = np.linspace(0,60,100)

sol1 = odeint(SIR,y_0,t,(N,0.1,0.1))
sol2 = odeint(SIR,y_0,t,(N,0.45,0.32))
sol3 = odeint(SIR,y_0,t,(N,0.53,0.23))
sol4 = odeint(SIR,y_0,t,(N,0.66,0.20))
sol5 = odeint(SIR,y_0,t,(N,0.78,0.12))
sol6 = odeint(SIR,y_0,t,(N,0.90,0.1))

sol7 = odeint(SIR,y_0,t,(9000,0.90,0.1))
sol8 = odeint(SIR,y_0,t,(5000,0.90,0.1))

fig, ((fig1, fig2,fig3),(fig4, fig5, fig6)) = plt.subplots(2, 3)
fig.set_size_inches(10, 7)
leg = [("S"),("I"),("R")]

fig1.plot(t,sol1)
fig1.set_title("B=0.1, G=0.1")
fig1.legend(leg)
fig2.plot(t,sol2)
fig2.set_title("B=0.45, G=0.32")
fig2.legend(leg)
fig3.plot(t,sol3)
fig3.set_title("B=0.53, G=0.23")
fig3.legend(leg)
fig4.plot(t,sol4)
fig4.set_title("B=0.66, G=0.20")
fig4.legend(leg)
fig5.plot(t,sol5)
fig5.set_title("B=0.78, G=0.12")
fig5.legend(leg)
fig6.plot(t,sol6)
fig6.set_title("B=0.90, G=0.1")
fig6.legend(leg)

plt.show()
#plt.plot(t,sol)
#plt.show()
