#!/usr/bin/python3

import sympy as sp

x = sp.Symbol('x')
f = 1/(1 + sp.Pow(x, 3))
a = 2
b = 500
e = 0.0025

print("a: ", a)
print("b: ", b)
print("precision: ", e)
print("The function: ", f)

def compute_integral_by_average_rectangles(a, b, h, func):
    initial = a+h/2
    sum = 0
    while initial < b:
        sum += func.subs(x, initial)
        initial += h
    
    res = h*sum
    return res

def calculate_precision(res1, res2):
    return sp.Abs((res1-res2)/3)

def compute_integral_with_precision(a, b, func, epsilon):
    if a == b:
        return 0
    h1 = (a+b)/500
    h2 = h1/2

    res1 = compute_integral_by_average_rectangles(a, b, h1, func)
    res2 = compute_integral_by_average_rectangles(a, b, h2, func)

    while calculate_precision(res1, res2) > epsilon:
        h1 = h2
        h2 = h1/2
        res1 = compute_integral_by_average_rectangles(a, b, h1, func)
        res2 = compute_integral_by_average_rectangles(a, b, h2, func)

    return res1


res = compute_integral_with_precision(a, b, f, e)
print(res)