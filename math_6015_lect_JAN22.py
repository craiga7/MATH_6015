"""
Class: MATH6015
Date: JAN22
BY: AARON CRAIG
"""
import os
import sys
import math
import random

## BREAK STATEMENTS
# Can use the BREAK or CONTINUE

## WHILE vs FOR
# FOR is useful for a known amount of operations
# WHILE is best for an unknown amount of iterations/operations

x = random.random()
while x < 0.75:
    print('Still Looking...')
    x = random.random()
print(f'Found a number greater than 3/4! {x:5.2f}')

## Find the largest prime number less than a given number
# N = int(input('Provide a Maximum Integer: '))
max_num = 4
numbers = range(max_num-1,2,-1)
for test_num in numbers:
    flag = True
    test_num_range = range(2,test_num)
    for test_factor in test_num_range:
        if (test_num % test_factor) == 0:
            flag = False
            break
    if flag:
            break
print(f" {test_num:5g} is the largest prime less than {max_num:10g}")

# Think about the methods of max_num less than 4 and what happens when someone puts in a string

## PAST PROJECT EXAMPLE

## CREATE FUNCTION
def HelloWorld():
     print("Hellow World!")

HelloWorld()        # Callable object, using () invokes the call

print(HelloWorld)

## Functions (which are objects) can change names
def HelloWorld(person):
    person = str(person)
    print(f"Hellow World and {person}")
    return
    if True:
        print('Goodbye')

HelloWorld('Bob')

## USING RETURN FOR PASSING OUTPUTS
def dosomemath(x):
     return x**2,x**3

x = 3
x2, x3 = dosomemath(x)

print(f"If {x} is squared, then it equals {x2:5g}, if cubed it is {x3:5g}")





