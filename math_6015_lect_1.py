"""
Class: MATH6015
BY: AARON CRAIG
"""
import os
import sys

## VARIABLES
m = 2
x = 2.0
z = 2.0 + 0j

print('Types of Variable Relationships')
print(type(m))
print(type(x))
print(type(z))
print(type(m+x))
print(type(x+z))
print(type(m/m))
print(type(m//m))

# Truth Testing/Boolean Variables
print('Truth Testing:')
# z = 2.0
print(z is x)

# Special values
a = 0.1
b = a + a
c = a + b

print('Special Values')
print(a)
print(b)
print(c)

print((0.1+0.2)==0.3)
print((1+2)/10 == 0.3)


