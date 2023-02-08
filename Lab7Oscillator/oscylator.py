import sympy as sp
import matplotlib as plt
import numpy as np

x = sp.Function('x')
w0 = sp.Symbol('omega_0', real = True, positive = True)
t = sp.Symbol('t')
x0 = sp.Symbol('x_0', real = True)
v0 = sp.Symbol('v_0', real = True)


x(t), w0, t

left = x(t).diff(t,t)
right = -w0**2*x(t)

eq = sp.Eq(left, right)

x(t).diff(t).subs(t,0)

sol = sp.dsolve(eq, x(t),ics ={x(0): x0, x(t).diff(t).subs(t,0):v0})
sol.simplify()
print(sol)

sol.lhs, sol.rhs

sp.plot(sol.rhs.subs({x0:1, v0:-1, w0:2}))

sp.lambdify()


