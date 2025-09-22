# ==============================================================================
# TASK 4: Simple Sort
# ==============================================================================
# %% custom functions
def get_list():
    """get_list asks the user to input a list of numerical values until "end" is pressed.
    """
    input_list = [] # empty list
    input_pend = True

    while input_pend:
        user_input = input("Input number and press enter, or type 'end' if done:")
        if user_input == "end":
            # stop the while
            input_pend = False
            print(f'The list of numbers is: {input_list}')
            return input_list
        else:
            try:
                # the input was not "end" yet, try to convert to float and append
                input_list.append(float(user_input))
            except ValueError:
                print (f"The input: {user_input} was not valid it was skipped.")

def get_max_min(input_list):
    """get_max_min from a list of numbers define max and min
    Args:
        input_list (int or float): list of numbers
    """
    if len(input_list) == 0:
        max_val, min_val = None, None
    else:
        max_val = input_list[0]
        min_val = input_list[0]
        # check 1 by 1 for max and min
        for element in input_list:
            if element > max_val:
                max_val = element
            if  element < min_val:
                min_val = element
    print(f"The minimal number is: {min_val}\nThe maximal number is: {max_val}")
    return max_val, min_val

# %% sort
# for the sort we will find the min or max in the list, then remove it, and
# repeat as we populate a sorted list

# debug list (no need to input it)
input_list = [3, 0, -3, 2.22, -1000, 99]


sorted_list = [] # starts empty
numbers = input_list[:] # we need a copy
asc = False # ascending

# do for all numbers in the list
for number in input_list:
    if asc==False:
        # get the min 
        min_val, _ = get_max_min(numbers)
        sorted_list.append(min_val)
        numbers.remove(min_val)
    elif asc==True:
        _, max_val = get_max_min(numbers)
        sorted_list.append(max_val)
        numbers.remove(max_val)

print(sorted_list)