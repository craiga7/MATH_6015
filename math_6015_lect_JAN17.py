"""
Class: MATH6015
Date: JAN17
BY: AARON CRAIG
"""
import os
import sys
import math

# Other Floating - Point Error
# Round off error: Loss of precision when adding, subtracting, or multiplying of different magnitudes
a = 1e65
b = (1e65 + 1) - 1e65

print('Large Number: ', a)
print('Round-Off Type Error: ',b)

# Horhorners Method is different way of rewriting the polynomial equations. 
c = math.exp(709)
print('Overflow: ',c)
# d = math.exp(710)
# print('Overflow: ',d)

planet_avg = 6
star_avg = 1e11
galaxy_avg = 1e11
print('Average Stars in Galaxy: ',star_avg)
print('Average Planets in Galaxy: ',planet_avg*star_avg)
print('Estimate Planets in Universe: ',planet_avg*star_avg*galaxy_avg)

# STRINGS
# Types
testStr = "test"
print('Test String', testStr)
print("This is a "+ testStr) # '+' is used as a method of concatenation, for this use case strings are concatenated.
print(testStr[0])
print(testStr[-1])

# INTEGERS/FLOATS TO STRINGS
# Types
m = 13
x = math.sqrt(m)
print('Value of m: ', m)
print('Value of x: ', x)

## STRING FORMATTING
# Contain 'replacement fields' surrounded by {}
# Characters outside of {} are literal text
usStr = "Today's date is {0}/{1}/{2} (U.S.A.)"
ukStr = "Today's date is {1}/{0}/{2} (U.K.)"
day = 10
month = 1
year = 2016
print(usStr.format(month,day,year))
print(ukStr.format(month,day,year))
print("Curly Braces {{{}}}".format(day))

print("pi = {:5.5f}".format(math.pi))
print("pi = {:10.5f}".format(math.pi))
print("pi = {:^10.5f}".format(math.pi))
print("pi = {:~<10.5f}".format(math.pi))
print("pi = {:~>105.10f}".format(math.pi))

# Percents
print("Grade = {:.3%}".format(8/13))    # adding the '%' translates the number to a percent, hidden python string formatting feature

# Scientific notation
print("x = {:.3e}".format(math.exp(-10)))
print("x = {:.3E}".format(math.exp(-10)))
print("x = {:.3g}".format(math.exp(-3)))

# f string format
print(f"pi = {math.pi:5.5f}")

## INPUT/OUTPUT
# Inputs
name = input("Enter your first name: ")
print('The name you entered is: ', name)

# Always return a string
inStr = input("Please enter your age: ")
age = int(inStr)
print("Next year you will be: ", age+1)
finStr = input("Enter a number: ")
print("You entered {:.3g} to three digits".format(float(finStr)))

# DATA STRUCTURE
# ARRAYS, List, Dictionary/Map, Record/Tuple/Structure, SETS, Multimap, Stack
# Stack, Queue, Priority Queue, Tree, Graph


