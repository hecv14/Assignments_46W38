"""
Task 3 is a simple script to find max and min values in a list. Use of print,
input, while, if, else, for, len and append is illustrated.
"""
# ==============================================================================
# TASK 3: Max and Min Finder
# ==============================================================================
# Task03
#%% ask the user to create the list
input_list = [] # empty list
input_pend = True

while input_pend:
    user_input = input("Input number and press enter, or type 'end' if done:")
    if user_input == "end":
        # stop the while
        input_pend = False
        print(f'The list of numbers is: {input_list}')
    else:
        try:
            # the input was not "end" yet, try to convert to float and append
            input_list.append(float(user_input))
        except ValueError:
            print (f"The input: {user_input} was not valid it was skipped.")

#%% find the max and min in the list
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
