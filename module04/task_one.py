# %% imports
from MyModule import get_a_list_of_numbers, find_max, find_min, sort_numbers

# %% get list
test_list = get_a_list_of_numbers()
# %% find min and max
min_in_list = find_min(test_list, silent=False)
max_in_list = find_max(test_list, silent=False)
# %% extra: sort
list_asc = sort_numbers(test_list, asc=True)
list_desc = sort_numbers(test_list, asc=False)