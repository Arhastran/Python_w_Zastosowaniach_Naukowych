import sympy as sp
import matplotlib as plt
import numpy as np

sp.init_printing()

x = sp.Symbol('x')

x1 = sp.Symbol('x_1')

i = sp.Integer(10)

#power = sp.Pow(69,69)
#print(power)

sp.Float('0.3', 20) #najlepszy sposób na dokłane floaty

r = sp.Rational(10,3)
r.evalf(15)

2 * x**2 +1

n = sp.Symbol('n' , integer = True)

print(sp.sin(sp.pi*n))

a = sp.Symbol('a', positive = True)

ex = sp.exp(-a*x**2)

dex = ex.diff(x,2) #po czym, ile razy

sol = dex.subs({a:5,x:3}).evalf(15)
print(sol)

sp.integrate(ex,x)
inte = sp.integrate(ex,(x,-sp.oo,+sp.oo))
print(inte)

a,x,b,c = sp.symbols('a x b c')

kwad = a*x**2 + b*x + c

sol2 = sp.solve(kwad, x)

x, y = sp.symbols('x y')
sp.solve([x+y-5, x-y+5])

m = sp.Matrix([[0,1,0],[1,0,1],[0,1,0]])
print(m)

###############






