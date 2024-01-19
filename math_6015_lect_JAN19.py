"""
Class: MATH6015
Date: JAN19
BY: AARON CRAIG
"""
import os
import sys
import math

## Python Built-In Structures
# List: sequence of inhomogeneous data
print("Working with Lists")
lst = [1, "Bob", math.pi]
print(lst[0])
print(lst[1])
lst[1] = "Pete"
print(lst[1])

# Tuples: Constrains a list to set values
print("working with Tuples")
tuple = (1, "Bob", 0, 3, "ten")
print(tuple[1])
# tuple[1] = "Pete"
print(tuple[1])

## List Comprehension
# Create lists from an iterable
# Any iterable is an object capable of returning members one at a time (list, tuple, strings)
# Can give a performance boost: preallocate memory instead of resizing
print("List Comprehension")
# x = "Fred"
list_var = [x for x in tuple]
print(list_var)

# For loops
print("Working with Loops")
test_str = "This is a test"
letters = list()
for letter in test_str:
    letters.append(letter)
print(letters)

## Set Operations
# Useful to test for comparing interger operations
print("Working with Sets")
aSet = set((1,2,3,4,3,2,1))
bSet = set((2,4,6,8))
cSet = set((1,2,3))
print(aSet|bSet)
print(cSet<=aSet)
print(aSet&bSet)

## Dictionary Operations
# Look up tables
print("Working with Dictionaries")
num2name = {47:"Montero", 44:"Rizzo", 18:"Zobrist"}
print(num2name[18])
num2name[27] = "Russell"
print(num2name)
num2name["Bryant"] = 17
print(num2name)
# Using hash functions can cause collisions which leads to improper boolean operations
in_name = hash("Bob")
num2name["In Name"] = in_name
print(num2name)

## Indexing and Slicing
# Indexing permits the access to individual elements of data structures
# Slicing takes a chunk of data structure with format START:STOP:STRIDE
print("working with slicing")
x = (0,1,2,3,4,5,6,7,8,9)
print(x[9])
print("Evens: ", x[::2])

## PROGRAM CONTROL
# Basic Structure
    # Precondition
    # Control Structure: Operations to Execute
    # Postcondition

## IF-THEN-ELSE
print("Working with Conditionals")
x = int(input("ENTER AN INTERGER, NOW... AGHGHGH: "))
if (x%2) == 0:
    print(x, "is an even integer")
else:
    print(x, "is an odd integer")

## SWITCH CASES
print("Working with MATCH Cases")
index = 1
match index:
    case 1:
        value = "Bob"
    case 2: 
        value = "Pete"
    case 3: 
        value = "Russ"
print(value)

# Dictionaries are better

## SHORT CIRCUIT LOGIC
# Based on method that evaluation of multiple conditions can lead to errors

## COMPARING FLOATS
print("WORKING WITH COMPARISON OF FLOATS")
x = 0.1 + 0.2
tol = 1e-10
if abs(x-0.3) < tol:        # Taking a sharp boundary and by using absolute value makes a blurred boundary
    print("Works as expected")
else:
    print("Doesn't Work!")

# FOR LOOPS
print("Playing with For Loops")
sum = 0
rng = range(1,10)
for i in rng:
    sum = sum + 1
print(sum)

# WHILE LOOPS
print("Playing with While Loops")
y = 0
limit = 1000
while y**2<limit:
    print(y, y**2)
    y += 1
print(y,y**2)
