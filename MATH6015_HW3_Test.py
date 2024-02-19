# Tests student's code for Assignment #3
# Required function definitions:
#
#  Problem #1: 
#  Function: solve_pei(b, alpha)
#    Input: Size of the linear system N (integer) and a parameter alpha (float)
#    Output: 1D numpy.array of length N
#
#  Problem #2: 
#  Function: solve_fdm(N)
#    Input: Size of the linear system N (integer)
#    Output: 1D numpy.array of length N
#
#
#  How to run the test script:
#    1) Ensure that your source code and this test script are in the current
#           working directory
#
#    2) Run the python script MATH6015_HW3_Test.py in the conda prompt using the command:
#           python MATH6015_HW3_Test
#
#    3) At the prompt, enter the FILENAME with the actual filename of the code you want to
#           test using quotes and without the py extension. 
#			Example: 
# 
#           Enter Filename of the Source Code to Test without the Extension: fileTestCode 
#                   
#           will test the code in the fileTestCode.py
#    
#    4) The test script will output "Tests Passed" if the code passes all the 
#           tests otherwise it will output which tests have failed
#

import importlib
import numpy as np    
import scipy.linalg as la

import zlib, base64
from time import time

def test_problem_1(solve_pei, alpha=100, N=7000, tol=1e-10):
    print(f'Solving a {N}x{N} Pei system...')
    
    print(f'Using alpha = {alpha}')
    
    print('\nComputing your solution...')
    start_time = time()
    
    z = solve_pei(N, alpha)
    
    print('Computed solution in {:.2f} seconds.'.format(time() - start_time))

    print('\nSolving solution using analytical inverse...')
    start_time = time()

    b = (alpha + N)*np.ones((N,))

    # Compute the analytical inverse of the Pei matrix
    d = alpha + 1
    p = -1/(d*(d+N-2) - (N-1))
    invA = p*np.ones((N,N)) - (p*(d+N-1))*np.eye(N) 
    
    ze = invA@b
    print('Computed analytic solution in {:3.2f} seconds.'.format(time() - start_time))
    

    err = la.norm(z-ze, np.inf)
    
    if err > tol:
        print(f"*** Error in Problem #1! (Difference = {err:.3e})\n")
        return False
    else: 
        print(f'Test passed. (Difference = {err:.3e})\n')
        return True
        
def test_problem_2(solve_fdm, N=500000, tol=1e-6):
    print('Solving FDM system...')

    print('\nComputing your solution...')
    start_time = time()
    
    z = solve_fdm(N)

    print('Computed solution in {:3.2f} seconds.'.format(time() - start_time))

    print('\nSolving benchmark solution...')
    start_time = time()

    local_vars = {'N': N}
    exec(zlib.decompress(base64.b64decode('eJxztM0r0KtKLcov1tAw1vHT1ORyjDbQsYq11TUEsgxBLAUjIMsIKpZkq2ukBdSSn5darOGnqa/hp22oqaVlxFWVapuTqFecn1OWGp+UmJeSmqKhYahjqKnjqJOkyQUAduYbHg==')), globals(), local_vars)
    ze = local_vars['ze']
    
    print('Computed benchmark solution in {:3.2f} seconds.'.format(time() - start_time))
    
    err = la.norm(z-2*ze, np.inf)
    
    if err > tol:
        print(f"*** Error in Problem #2! (Difference = {err:.3e})")
        return False
    else:
        print(f'Test passed. (Difference = {err:.3e})\n')
        return True

def HW3_Test(filename):
    # Dynamically load the module to test        
    mod = importlib.import_module(filename)    
    solve_pei = getattr(mod, "solve_pei")
    solve_fdm = getattr(mod, "solve_fdm")
    
    passed = test_problem_1(solve_pei) and test_problem_2(solve_fdm)
    
    print("Tests {}!".format("passed" if passed else "failed" ))
        
    return passed

if __name__ == "__main__":
    filename = input("Enter Filename of the Source Code to Test without the Extension: ")

    passed = HW3_Test(filename)
