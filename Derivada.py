"""
Derivada Numérica
"""
from sympy import *
x = Symbol('x')
fx = 2 * x**3 + 5 * x
fderivada = fx.diff(x)  # Simbólica
print(fderivada)
numderivada = lambdify(x, fderivada, 'sympy')  # Derivada Numérica
print(numderivada(1))
