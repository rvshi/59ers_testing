import numpy as np


def get_sum(input_list):
    ''' returns the sum of a list

    :param input_list: list to sum
    :return: sum of list
    '''
    return sum(input_list)


def get_min_max(input_list):
    min_max = (np.amin(input_list), np.amax(input_list))
    return min_max


def get_max_diff(input_list):
    diff_arr = np.diff(input_list)
    max_diff = np.max(diff_arr)
    return max_diff
