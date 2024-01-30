# Source code for Assignment #2
# Required function definitions:
#
#    Problem #1: 
#        Function: stirling(n, r)
#        Input: n (integer), r (integer)
#        Output: Stirling number S(n, r) (integer)       
#
#    Problem #2: 
#        Function: is_narcissistic(n)
#        Input: n (integer)
#        Output: True/False (boolean)
#  
#    Problem #3:
#        Function: find_narcissistic(N)
#        Input: N (integer) # of narcissistic numbers to find
#        Output: List of the first N narcissistic numbers
#
#    Problem #4:
#        Function: compute_pi()
#        Input: None
#        Output: Value of pi to at least 14 digits of accuracy
#

# Problem #1--------------------------------------------------------------------------
def stirling(n, r):    
    import math
    import numpy as np
    # Compute a Stirling number (value) of the second kind with the recursion relation
    # S(n,r) = r*S(n-1,r) + S(n-1,r-1)
    # Initialize a values list 
    S_array = np.zeros((n,r),dtype=int)

    # Assumption test, that n,r are greater than or equal to 1
    if n < 1 or r < 1:
        print("Values of n or r are less than one")
        return None
    else:
        None

    # Define the stirling number relationships
    def stir_relation(n,r):         
        # Relations to adjust the value
        # S(n,r) = 0, if r > n
        if r > n:
            value = 0
        # S(n,n) = 1
        elif r == n:
            value = 1
        # S(n,n-1) = [[n], [2]]  
        elif r == (n-1):
            value = math.comb(n,2)
        # S(n,n-2) = [[n],[3]] + 3*[[n],[4]]
        elif r == (n-2):
            value = math.comb(n,3) + 3*math.comb(n,4)
        # S(n,1) = 1
        elif r == 1:
            value = 1
        # S(n,2) = 2**(n-1)-1              
        elif r == 2:
            value = 2**(n-1) - 1
        elif r == 0:
            value = 0
        # if no condition is met, handle in recursion relation
        else:               
            value = None
        return value
    
    # Define the recursion relation for previously attained values
    # Here (r+1) since python reference is -1
    def S(array,n,r):
        value = (r+1)*array[n-1,r] + array[n-1,r-1]
        return value

    # Conduct a loop for all values leading up to final recursion value
    for i in range(n):
        for j in range(r):
            value = stir_relation(i+1,j+1)
            # If no relations met, compute with previous values
            if value == None:   
                value = S(S_array,i,j)
                S_array[i,j] = value
            else:
                S_array[i,j] = value

    return value
    
# Problem #2----------------------------------------------------------
def is_narcissistic(n):    
    # Determine number of digits from base-10 number (num_len)
    d_str = str(n)
    N = len(d_str)
    d = [int(d) for d in str(n)]
    # print(d)

    # Function for computing base10 and digit summation
    def x(d,N):
        x_base10 = 0
        x_dig = 0
        for i in range(1,N+1):
            x_base10 += d[-i]*(10**(i-1))
            x_dig += d[i-1]**N

        return x_base10, x_dig
    
    # Boolean for testing single-digit integers less than ten or 
    # running the number through function
    if N < 2:                        
        narcissistic = True
    else:
        x_base10, x_dig = x(d,N)
        if x_base10 == x_dig:
            narcissistic = True
        else:
            narcissistic = False

    # Return a boolean True/False    
    return narcissistic

# Problem #3----------------------------------------------------------
def find_narcissistic(N):        
    # Create an empty list and initial variable (v)
    narcs = list()
    v = 0
    iter = 0

    # Create a loop to fill the list
    while len(narcs) < N:
        # Compute the current sum
        v += 1
        # determine if narcissistic and add to list
        if is_narcissistic(v):
            narcs.append(v)
        else:
            None

        # define information for print
        narc_len = len(narcs)
        print("Finding narcissistic values, at current value {} with narc length of {}".format(v,narc_len))
        
    return narcs

# Problem #4----------------------------------------------------------
def compute_pi():
    import math
    def f(x):               # Function for computation
        x = x + math.sin(x)
        return x
    x_0 = 3                 # Initial guess
    tol = 1e-15             # Tolerance for 14 decimal places
    n = 0                   # Initial iteration
    error = 0.1             # Initial error
    while error > tol:      # Loop to get to value of pi!
        n += 1
        x = f(x_0)
        error = abs(x-x_0)
        x_0 = x
        iter_str = "Computing Pi, current iteration: {:5.14f} and current value is {:5.14f}, U.S.A.!"
        print(iter_str.format(n,x))
    print("pi = {:5.14f}".format(x))
    return x

