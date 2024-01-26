# Source code for Assignment #2
# Required function definitions:
#
#    Problem #1: 
#        Function: stirling(n, r)
#        Input: n (integer), r (integer)
#        Output: stirling number S(n, r) (integer)       
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
#        Output: Value of pi to at least 12 digits of accuracy
#
#
#  How to run the test script:
#    1) Ensure that your source code and this test script are in the current
#           working directory
#
#    2) Run the python script MATH6015_HW2_Test.py in the conda prompt using the command:
#           python MATH6015_HW2_Test
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
#    5) Depending on how fast your computer is, Test #3 might take a few
#           seconds to a minute to finish
#   
#    6) If the test script hangs, then you probably have an error in the 
#           find_narcissistic function and the script cannot find the required 
#           twenty numbers

import math
import importlib

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

def test_problem_1(stirling):    

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
                return False

    print_stirling_table(computed_values)
        
    
    print("\nProblem #1 Test Finished.")
    
    return True

def test_problem_2(is_narcissistic):    
    true_list  = list(range(1,10)) + [153, 9474, 93084, 32164049651]
    false_list = [17, 186, 1395, 65479, 984315, 6527416, 23486475]

    for n in true_list:
        if (not is_narcissistic(n)):
            print(f"***** Error in Problem #2: n = {n} is narcissitic but function returned false.")
            return False

    for n in false_list:
        if (is_narcissistic(n)):
            print(f"***** Error in Problem #2: n = {n} is not narcissitic but function returned true.")
            return False

    print("Problem #2 Test Finished.")
    
    return True

def test_problem_3(find_narcissistic):    
    narc_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 153, 370, 371, 407, 1634, 8208, 9474, 54748, 92727, 93084, 548834]
    test_list = find_narcissistic(20)

    if (narc_list != test_list):
        print("***** Error in Problem #3: Compute list of narcissistic numbers is not correct")
        print("*****    ", narc_list)
        print("*****    ", test_list)
        return False

    print("Problem #3 Test Finished.")
    
    return True

def test_problem_4(compute_pi):
    tol = 1e-15
    cPi = compute_pi()
    
    delta = abs(math.pi - cPi)
    
    if (delta > tol):
        print(f"***** Error in Problem #4: Estimate of pi is not within {tol:.0e}")
        print(f"*****     Computed pi = {cPi} \t delta = {delta:3.2e}")
        return False
    
    print("Problem #4 Test Finished.")
    
    return True

def HW2_Test(filename):            
    mod = importlib.import_module(filename)    
    stirling          = getattr(mod, "stirling"         )
    is_narcissistic   = getattr(mod, "is_narcissistic"  )
    find_narcissistic = getattr(mod, "find_narcissistic")
    compute_pi        = getattr(mod, "compute_pi"       )
            
    passed = test_problem_1(stirling) and test_problem_2(is_narcissistic) and test_problem_3(find_narcissistic) and test_problem_4(compute_pi)
        
    print("Tests {}!".format("passed" if passed else "failed" ))
        
    return passed
        

if __name__ == "__main__":    
    filename = input("Enter Filename of the Source Code to Test without the Extension: ")

    passed = HW2_Test(filename)
