# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 19:13:44 2024

@author: aleja
"""

from sympy import *
init_printing()

# Parámetros Bono
r, B = 1.037, 101
# Parámetros Acción
u, d, S0 = 1.007967483, 0.993949331, 433.01

W = Matrix([[-B, -S0], [r*B, u*S0],[r*B, d*S0]])
print(W)
print()

pi_u, pi_d = symbols('pi_u pi_d')
pi = Matrix([[1],[pi_u],[pi_d]])
print(pi)
print()

NA=pi.transpose()*W
print(NA)
print()

# Solver tutorial
# https://docs.sympy.org/latest/modules/solvers/solvers.html
piNA=solve([NA[0],NA[1]],[pi_u,pi_d],dict=True)
print(piNA)
print()

# Parámetros Opción
q3 = 195.79
K = 240
# Parámetros Bono
r, B = 1.037, 101
# Parámetros Acción
u, d, S0 = 1.007967483, 0.993949331, 433.01
W = Matrix([[-B, -S0, -q3], [r*B, u*S0, max(0,u*S0-K)],[r*B, d*S0, max(0,d*S0-K)]])
print(W)
print()

u,r,d = symbols('u r d')
Prices=Matrix([[1],[piNA[0][pi_u]],[piNA[0][pi_d]]]).transpose()*W
print(Prices)
print()

Prices.subs([(d,0.99758),(u,1.00905),(r,0.037)])