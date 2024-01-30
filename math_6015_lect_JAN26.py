"""
Class: MATH6015
Date: JAN22
BY: AARON CRAIG
"""
import os
import sys
import math
import random

## PYTHON PASS BY VALUE OR REFERENCE?
## IMMUTABLE OR MUTABLE
# Mutable: lists, sets, dictionaries
# Immutable: tuples, integers, floats, strings

def f(x):
    print("x before =",x,"(f)")
    x = x+1
    print("x afer =",x,"(f)")
    return x

x = 1                   # this is an interger which is immutable
print("x before =",x)
x = f(x)
print("x after =",x)

# def g(y):
#     print("y before = ", y[0], "g")
#     y[0] = y[0] + 1
#     print("y after =",y[0], "(g)")

# y = [1]
# print("y before = ", y[0])
# g(y)
# print("y after =", y[0])

# # Make copies of mutable objects before changing as to retain the original values
# y = [1]
# print("y before =",y[0])
# g(y[:])                     # Passes a copy of y into g()
# print("y after =",y[0])

# import builtins
# # print(dir(builtins))



