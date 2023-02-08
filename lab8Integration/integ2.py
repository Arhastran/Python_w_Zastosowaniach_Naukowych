import sympy as sp
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def SIR(y,t,beta,gamma):
  S,I,R = y
  dS = -beta*S*I
  dI = beta*I*S-gamma*I
  dR = gamma*I
  return dS,dI,dR


S_0 = 1000
I_0 = 10
R_0 = 0

y_0 = S_0, I_0, R_0
beta =0.5
gamma=0.25
t = np.linspace(0,60,100)

sol = odeint(SIR,y_0,t,(beta,gamma))
print(sol)

plt.plot(t,sol)
plt.show()