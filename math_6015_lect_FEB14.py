"""
Class: MATH6015
Date: FEB14
BY: AARON CRAIG
"""
import os
import sys
import math
import random
import numpy as np
import matplotlib.pyplot as plt

## BLOCK MATRICES
# Considering a main matrix, A wrt R_nXn
# Decompose the blocks of the matrix A into A_11, A_12, A_21, A_22
# Assuming we have A_11 = L_11*U_11

# Python implementation
# Write the function tha tsolvs a block tridiagonal matrix
# What are inputs?
    # Three arrays (A, B, C) size rXr
    # RHS vector b of size r
    # other things
# What is our output
    # vector x
    # other things: return L and U matrices
# Do we allocate memory for L and U or overwrite A and C?
    # allocating memory increase the required memory to increase

def algorithm(A,B,C,b,R,M,N):
    x = 0
    ## Algorithm
    # Allocate memory to U and L
    U = np.zeros((R,R,M))
    L = np.zeros((R,R,M-1))

    # Block tridiagonal LU factorization

    # Forward solve

    # Back solve

    return x





 













