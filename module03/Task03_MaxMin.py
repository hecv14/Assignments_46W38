#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Task 3 is a simple script to find max and min values in a list. Use of print,
input, while, if, else, for, len and append is illustrated.
"""

# ======================================================================
# TASK 3: Max and Min Finder
# ======================================================================
#  Assume you have a list of number: $[x_1, x_2, ..., x_n]$, the task of the Python script is to find the minimal and
#  maximal numbers in the list.
#  Please note you are not allowed to use the build-in function min() or max(), or any other 3rd-party
#  functions, the learning only happens when you solve the program by yourself.
#  The function of the script can be divided in the following parts:
#  A. Getting the list of number
#  The script should get the numbers from user input with the built-in function input(). You should put
#  meaningful prompt message in this function, to reminder the user how to end the inputting process, like by
#  typing in end. Thus you need have a proper control flow to determine when this process should be stopped.
#  2 / 3
#  B. Finding the minimal and maximal
# 2025-09-11
#  The script should work with this list of numbers and find the minimal and maximal among them. In the special
#  case of an empty list, you should assume the minimal and maximal are both None.
#  C. Printing out the results
#  The script should print out the list, together with results, using proper formatted string. That can be
#  something like this:
#  The list of number is: [x_1, x_2, ..., x_n] 
# The minimal number is: x_min 
# The maximal number is: x_max 
# Note that in the message shown above, x_min, x_max and x_i should be the actually numbers.
#  D. Including proper documentaion
#  Please use proper Docstrings and Comments in your script, make it easy for others to understand your code.
#  The script should be named "min-max_finder.py" and included in the "module03" folder in your
#  "Assignments_46W38" repository.
#  Remember to version control the whole process, incrementally add, commit and push the changes along the
#  way.
#  Assumption: here we assume the user will only type in valid numbers, or a string (like 'end') to end the
#  inputting process. So don't worry about error handling for now.

# %% Task03
print('Script will find the max. and min. values in the list you will now input.\n' \
'type "end" when all elements have been input.')

input_list = [] # empty list
user_input = None

while user_input != "end":
    user_input = input("Input list element and type enter:")
    if user_input != "end":
        input_list.append(user_input)
print(f'The list of numbers is: {input_list}')

if len(input_list) == 0:
    max_val, min_val = None, None
else:
    max_val = input_list[0]
    min_val = input_list[0]
    for element in input_list:
        if element > max_val:
            max_val = element
        if  element < min_val:
            min_val = element

print(f"The minimal number is: {min_val}\nThe maximal number is: {max_val}")