"""
Test bed for code
By: Aaron Craig
"""

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
    
    if N < 2:                        # Boolean for testing single-digit integers less than ten
        narcissistic = True
    else:
        x_base10, x_dig = x(d,N)

        if x_base10 == x_dig:
            narcissistic = True
        else:
            narcissistic = False

    # Return a boolean True/False    
    return narcissistic



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

        # define iteration for checking progress
        iter += 1
        narc_len = len(narcs)
        print("Finding narcissistic values, at iteration {} with narc length of {}".format(iter,narc_len))
        
    return narcs

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

# test = stirling(10,10)
# print(test)

def print_stirling_table(data):    
    max_length = 1

    for ii in range(len(data)):           
        for jj in range(ii+1):            
            n_char = len(str(data[ii][jj]))
            max_length = max(n_char, max_length)

    header = "n\k | " + "{{:{}}} ".format(max_length)*(len(data))
    header = header.format(*range(1, (len(data))+1))
    print(header)
    print('-'*len(header))

    for ii in range(len(data)):
        n = ii+1
        line = f"{n:^3} | "
        
        for jj in range(ii+1):        
            k = jj+1
            line += "{{:>{}}} ".format(max_length).format(data[ii][jj])

        print(line)
    
    return 

true_values = [[1                                                  ], 
                [1,   1                                             ], 
                [1,   3,    1                                       ],
                [1,   7,    6,     1                                ],
                [1,  15,   25,    10,     1                         ],
                [1,  31,   90,    65,    15,     1                  ],
                [1,  63,  301,   350,   140,    21,    1            ],
                [1, 127,  966,  1701,  1050,   266,   28,   1       ],
                [1, 255, 3025,  7770,  6951,  2646,  462,  36,  1   ],
                [1, 511, 9330, 34105, 42525, 22827, 5880, 750, 45, 1],
                ] 

computed_values = list()

for n in range(1, len(true_values)+1):
    values = list()

    for k in range(1, n+1):
        values.append(stirling(n, k))
        
    computed_values.append(values)

for ii, (a, b) in enumerate(zip(true_values, computed_values)):
    for jj, (s1, s2) in enumerate(zip(a, b)):
        if s1 != s2:
            print(f'"***** Error in Problem #1: S({ii+1}, {jj+1}) = {s2} != {s1}')


print_stirling_table(computed_values)
    

print("\nProblem #1 Test Finished.")