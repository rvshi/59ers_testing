import numpy as np

def get_sum(input_list):
    '''
    Returns the sum of a list
    '''
    return sum(input_list)


def get_min_max(input_list):
    pass


def get_max_diff(input_list):
    diff_arr = np.diff(input_list)
    max_diff = np.max(diff_arr)
    return max_diff
