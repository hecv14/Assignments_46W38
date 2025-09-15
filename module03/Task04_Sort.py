# %% custom functions
def get_list(default_list=False):
    """_get_list asks the user to input a list of numerical values until "end" is pressed._
    """
    user_input = None
    while user_input != "end":
        user_input = input("Input list element and type enter (when done type 'end'):")
        if user_input != "end":
            input_list.append(user_input)
    print(f'The list of numbers is: {input_list}')
    return(input_list)

def get_max_min(input_list):
    """_get_max_min from a list of numbers define max and min_
    Args:
        input_list (_numbers_): _list of numbers_
    """
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
    return(min_val, max_val)


# %% sort
#input_list = get_list()
input_list = [3, 0, -3, 2.22, -1000, 99]
min_val, _ = get_max_min(input_list)

sorted_list = []
numbers = input_list[:]
asc = False

for number in input_list:
    if asc==True:
        min_val, _ = get_max_min(numbers)
        sorted_list.append(min_val)
        numbers.remove(min_val)
    else:
        _, max_val = get_max_min(numbers)
        sorted_list.append(max_val)
        numbers.remove(max_val)
