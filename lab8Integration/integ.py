import sympy as sp
from sympy.plotting import plot, plot3d, PlotGrid
import matplotlib as plt
import numpy as np

S = sp.Function('S') #stock of susceptible population
I = sp.Function('I') #stock of infected
R = sp.Function('R') #stock of recovered
t = sp.Symbol('t') #time
b = sp.Symbol('beta') #???
gamma = sp.Symbol('gamma') #???

S(t)
I(t)
R(t)

right1 = -1*b*S(t)*I(t)
left1 = S(t).diff(t)
eq1 = sp.Eq(left1, right1) #Sus

right2 = b*S(t)*I(t)-1*gamma*I(t)
left2 = I(t).diff(t)
eq2 = sp.Eq(left2, right2)

right3 = gamma*I(t)
left3 = R(t).diff(t)
eq3 = sp.Eq(left3, right3)

print(eq1,eq2,eq3)

sp.solvers.ode.systems.dsolve_system([eq1,eq2,eq3],[S(t),I(t),R(t)])

#S0 = 10000

#sol2 = sp.dsolve(eq, S(t),ics ={S(0): S0})
#sol2.simplify
#print(sol2)

#I0 = 100
#b0 = 0.00001

#sol3 = sol2.subs([(I, I0),(b,b0)])

#print(sol3)

#sol3.lhs, sol3.rhs

#p1 = sp.plot(sol3.rhs, xlim = (-20,20), xlabel = ("time [s]"), ylabel = ("SIR population"))