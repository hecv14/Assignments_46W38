# MyModule.py
"""MyModule contain simple functions to input a list, and find min/max."""

def get_a_list_of_numbers() -> list | None:
    """get_a_list_of_numbers asks the user to input a list of numerical values
    until "end" is pressed.
    """
    input_list = [] # empty list
    input_pend = True
    while input_pend:
        user_input = input("Input number & press enter, or type 'end' if done:")
        if user_input == "end":
            # stop the while
            input_pend = False
            print(f'The list of input numbers is: {input_list}')
            return input_list
        else:
            try:
                # the input was not "end" yet, try float() and .append
                input_list.append(float(user_input))
            except ValueError:
                print (f"The input: {user_input} was not valid it was skipped.")

def find_min(input_list, silent=True):
    """find_min from a list of numbers define min
    Args:
        input_list (int or float): list of numbers
    """
    if len(input_list) == 0:
        min_val = None
    elif len(input_list) > 0:
        min_val = input_list[0] # the first value is the minimum
        for element in input_list: # until we iterate
            if element < min_val: # and find a smaller one
                min_val = element
    if not silent:
        print(f"The min. number is: {min_val}")
    return min_val

def find_max(input_list, silent=True):
    """find_min from a list of numbers define min
    Args:
        input_list (int or float): list of numbers
    """
    if len(input_list) == 0:
        max_val = None
    elif len(input_list) > 0:
        max_val = input_list[0] # the first value is the minimum
        for element in input_list: # until we iterate
            if element > max_val: # and find a smaller one
                max_val = element
    if not silent:
        print(f"The max. number is: {max_val}")
    return max_val

def simple_sort(input_list, asc=True):
    """simple_sort: simple sort function
    Args:
        input_list (list): list of floats
        
        desc (bool, optional): order in descending way. Defaults to True.
    Returns:
        sorted list: list sorted in descending or ascending way
    """
    # for the sort we will find the min or max in the list, then remove it, and
    # repeat the find on the shortened list while we populate a new sorted list.
    sorted_list = [] # starts empty
    numbers = input_list[:] # we need a copy
    # do for all numbers in the list
    for number in input_list:
        if asc:
            # get the min 
            min_val = find_min(numbers)
            sorted_list.append(min_val)
            numbers.remove(min_val)
        else: # i.e. descending
            max_val = find_max(numbers)
            sorted_list.append(max_val)
            numbers.remove(max_val)
    return sorted_list
    print(sorted_list)