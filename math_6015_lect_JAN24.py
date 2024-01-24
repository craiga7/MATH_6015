"""
Class: MATH6015
Date: JAN22
BY: AARON CRAIG
"""
import os
import sys
import math
import random

## LAMBDA FUNCTIONS
def f(x):
    return 10*x

g = lambda x: 10*x

print(f(5))
print(g(5))
print((lambda x: 10*x)(5))

## SCOPE
# Determines where a variable is called from four categories
# Local: current function, current class,...
# Enclosing: functions, classes,...
# Global: Entire program
# Built-in

def f():
    print(x)

x = "in global scope"
f()

def g():
    x = "in local scope (g)"
    print(x)
x = "In global scope"
print(x)
g() 

# Variable Scope in Python
# def f():
#     print(x)
#     x = "changed in f"
# x = "in global scope"
# f()
# print(x)

# Using Global Variables
def f():
    print(x)
def g():
    global x        # use here pulls x from any current address assignment
    print(x)
    x = "changed in g"
x = "in global scope"
f()
g()
f()

# ALWAYS ASSIGN VARIABLES TO FUNCTIONS EXPLICITLY

def f(x):
    print("x before =",x,"(f)")
    x = x+1
    print("x afer =",x,"(f)")

x = 1                   # this is an interger which is immutable
print("x before =",x)
f(x)
print("x after =",x)






