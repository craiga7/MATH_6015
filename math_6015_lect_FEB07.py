"""
Class: MATH6015
Date: FEB07
BY: AARON CRAIG
"""
import os
import sys
import math
import random
import numpy as np
import matplotlib.pyplot as plt

# Create a vector
vec = np.array([1, 2, 3, 4, 5])
print(vec)

# Create a matrix
mat = np.array([
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11,12,13,14,15],
    [16,17,18,19,20],
    [21,22,23,24,25]
]
)
print(mat)

# Create a zero matrix
mat = np.zeros((5,5),dtype=float)
for i in range(5):
    for j in range(5):
        mat[i,j] = 5*i + j + 1

print(mat)

# Create an identity matrix
N = 10
mat = np.eye(N)

plt.spy(mat,marker='s')
plt.show()



