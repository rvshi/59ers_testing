import numpy as np


def get_sum(input_list):
    '''
    Returns the sum of a list
    '''
    return sum(input_list)


def get_min_max(input_list):
    """ Returns min and max in a list

    :param input_list: (int) list to get min and max of
    :return: min and max of list in a tuple
    :raises TypeError: Input must be lists
    :raises TypeError: Input elements must be integers
    :raises ValueError: All input elements must be between -9,000 and 9,000
    """
    min_max = (np.amin(input_list), np.amax(input_list))
    return min_max


def get_max_diff(input_list):
    diff_arr = np.diff(input_list)
    max_diff = np.max(diff_arr)
    return max_diff
