try:
    import numpy as np
except ImportError:
    raise ImportError('''Could not import numpy. Please make sure to have the
                      package installed''')


def get_sum(input_list):
    '''
    Returns the sum of a list
    '''
    return sum(input_list)


def get_min_max(input_list):
    min_max = (np.amin(input_list), np.amax(input_list))
    return min_max


def get_max_diff(input_list):
    if(not all([type(num) is int for num in input_list])):
        raise TypeError('All inputs must be integers.')
    diff_arr = np.diff(input_list)
    max_diff = np.max(diff_arr)
    return max_diff
