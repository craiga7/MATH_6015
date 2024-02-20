# Source code for Assignment #3
# Name: YOUR NAME AARON CRAIG!!!!
#
# Problem #1: 
# Function: solve_pei(b, alpha)
#   Input: Size of the linear system N (integer) and a parameter alpha (float)
#   Output: 1D numpy.array of length N
#
# Problem #2: 
# Function: solve_fdm(N)
#   Input: Size of the linear system N (integer)
#   Output: 1D numpy.array of length N

import numpy as np
import scipy.linalg as la

# Problem #1
def solve_pei(N, alpha):
    # A = alpha*Identity + 1
    # alpha != 0 , -n
    # 1 = 
    A = alpha*np.eye((N)) + np.ones((N,N))
    # b_i = alpha + N
    b = (alpha + N)*np.ones((N,))

    # scipy.linalg.solve
    x = la.solve(A,b)

    return x

# Problem #2
def solve_fdm(N):    
    x = 0 
    return np.zeros(N)