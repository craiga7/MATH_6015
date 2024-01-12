"""
CLASS: MATH 6015
NAME: A. JASPER CRAIG
AFFILIATION: University of Cincinnati
DATE: 17JAN24
ASSIGNMENT: HW 1
"""

# Prompt user for their name
name = input("Enter your first name: ")

# Initialize a variable for storing the results
value = 0

# Loop through each character in the name, 
# converting each to its ASCII value, and add to the running value
for c in name:
    value += ord(c) # ord(C) obtains the ASCII value of character
    
# Print the resulting value
print(name, " becomes ", value)