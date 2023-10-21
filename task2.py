#!/usr/bin/python3

import sympy as sp

x = sp.Symbol('x')
f = sp.Pow(sp.E, x) - 1 - x - sp.Pow(x, 2)/2 - sp.Pow(x, 3)/6 - sp.Pow(x, 4)/24
a = 0
b = 1
h = 0.1


def compute_integral_by_right_rectangles(a, b, h, func):
    initial = a+h
    sum = 0
    while initial <= b:
        sum += func.subs(x, initial)
        initial += h
    
    res = h*sum
    return res

res = compute_integral_by_right_rectangles(a, b, h, f)
print(res)