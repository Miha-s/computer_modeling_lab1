#!/usr/bin/python3

import sympy as sp
import numpy as np
x = sp.Symbol('x')
f = -sp.ln(sp.cos(x))
a = 0
b = sp.pi.evalf()/2
h = sp.pi.evalf()/36
precision_digits = 2

print("a: ", a)
print("b: ", b)
print("precision: ", precision_digits)
print("The function: ", f)

def print_bold_divisor():
    print("===============================")
def print_thin_divisor():
    print("-------------------------------")

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

def power_of_first_nonzero_digit(number):
    num_str = str(number)
    
    found_digit = '0'
    for digit in num_str:
        if digit != '0' and digit != '.':
            found_digit = digit
            break
    
    first_digit_index = num_str.index(found_digit)
    point_index = 0
    try:
        point_index = num_str.index('.')
    except:
        point_index = len(num_str)
    
    return point_index - first_digit_index


def get_precision_by_digits(approximate_result, digits):
    power = power_of_first_nonzero_digit(approximate_result)
    epsilon = 10**(power-digits)
    epsilon /= 2
    return epsilon


def compute_integral_with_precision(a, b, func, digits):
    if a == b:
        return 0
    h1 = (a+b)/5
    h2 = h1/2

    res1 = compute_integral_by_average_rectangles(a, b, h1, func)
    res2 = compute_integral_by_average_rectangles(a, b, h2, func)
    epsilon = get_precision_by_digits(res2, digits)
    while calculate_precision(res1, res2) > epsilon:
        h1 = h2
        h2 = h1/2
        res1 = compute_integral_by_average_rectangles(a, b, h1, func)
        res2 = compute_integral_by_average_rectangles(a, b, h2, func)

    return res1

def create_function_table(a, b, step, func, precision_digits):
    current_x = a
    result_table = []
    while current_x <= b:
        current_y = compute_integral_with_precision(0, current_x, func, precision_digits)
        result_table.append([current_x, current_y])
        current_x += step
    
    return result_table

def print_result(result):
    for x, y in result:
        format_string = "{:.1e}"
        x_f = "{:.3f}".format(x)
        y_f = format_string.format(y)
        print(x_f, ": ", y_f)

res = create_function_table(a, b, h, f, precision_digits)
print_result(res)

