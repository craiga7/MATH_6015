"""
Class: MATH6015
Date: FEB12
BY: AARON CRAIG
"""
import os
import sys
import math
import random
import numpy as np
import matplotlib.pyplot as plt

# Solves a pentadiagonal FDM matrix using LU factorization
import numpy as np
import scipy.linalg as sla

N = 1000    # Size of the system

# Create banded storage matrix
B = np.zeros((5, N))
B[0,2:N  ] =  1; B[1,1:N  ] = -4
B[2, :   ] =  6
B[3,0:N-1] = -4; B[4,0:N-2] =  1 
   
# Create RHS vector
b = np.zeros(N)
b[  0] =  3; b[N-1] =  3
b[  1] = -1; b[N-2] = -1

# Exact solution
xe = np.ones(N)

x = sla.solve_banded((2,2), B, b)
print("Banded Matrix LU Solve:")
print("   2-Norm Error = {:.3e}".format(sla.norm(x-xe)/np.sqrt(N)))
print("   ∞-Norm Error = {:.3e}".format(sla.norm(x-xe, np.inf)))







 













