#Harmonic oscillator with SymPy library

import sympy as sp
from sympy.plotting import plot, plot3d, PlotGrid
import matplotlib as plt
import numpy as np

#####################
#Harmonic damped

x = sp.Function('x')
b = sp.Symbol('beta')
omega = sp.Symbol("omega_0")
t = sp.Symbol('t')
x0 = sp.Symbol('x_0', real = True)
v0 = sp.Symbol('v_0', real = True)

x(t)

right = 0
left = x(t).diff(t,t) + 2*b*x(t).diff(t)+omega**2*x(t)

eq = sp.Eq(left, right)

sol = sp.dsolve(eq, x(t))
sol.simplify
print("Solution of damped harmonic oscillator:", sol)

x0 = -10
v0 = 1

sol2 = sp.dsolve(eq, x(t),ics ={x(0): x0, x(t).diff(t).subs(t,0):v0})
sol2.simplify
print("Solution with starting position and speed", sol2)

beta_1 = 3
omega_0 = 25

sol3 = sol2.subs([(b, beta_1), (omega, omega_0)])


sol3.lhs, sol3.rhs

#####################
#Harmonic forced

x2 = sp.Function('x')
b2 = sp.Symbol('beta')
omega2 = sp.Symbol("omega_0")
t2 = sp.Symbol('t')
x02 = sp.Symbol('x_0', real = True)
v02 = sp.Symbol('v_0', real = True)
A = sp.Symbol('A')

x2(t2)

left2 = x2(t2).diff(t2,t2) + 2*b2*x2(t2).diff(t2)+omega2**2*x2(t2)
right2 = A*sp.cos(omega2*t2)
eq2 = sp.Eq(left2, right2)
solforced = sp.dsolve(eq2, x2(t2))
solforced.simplify
print("Equation of forced harmonic oscillator:", solforced)
x02 = -10
v02 = 1

solforced2 = sp.dsolve(eq2, x2(t2),ics ={x2(0): x02, x2(t2).diff(t2).subs(t2,0):v02})
solforced2.simplify
print("Solution with starting speed and position:", solforced2)

beta_12 = -0.1
omega_02 = 10
A2 = 10

solforced3 = solforced2.subs([(b2, beta_12), (omega2, omega_02),(A,A2)])
print(solforced3)

solforced3.lhs, solforced3.rhs

p1 = sp.plot(sol3.rhs, xlim = (-10,0), xlabel = ("time [s]"), ylabel = ("a.u."), show=False)
p2 = sp.plot(solforced3.rhs, xlim = (-10,0),xlabel = ("time [s]"), ylabel = ("a.u."),show=False)
xd = PlotGrid(1, 2, p1, p2)
#p1.extend(p2)


