import pytest


def test_check_inputs():

    import list_ops as lops
    error_input_list = (12,
                        [1, 2, 3.32],
                        [4, 'GTHC', 2, 333],
                        [85, -23, -2222222222222],
                        [33, 123123123, -2])

    error_output_list = (TypeError, TypeError, TypeError,
                         ValueError, ValueError)
    # loop over exception triggers and module functions
    for i, nums in enumerate(error_input_list):
        with pytest.raises(error_output_list[i]):
            lops.get_sum(nums)
        with pytest.raises(error_output_list[i]):
            lops.get_min_max(nums)
        with pytest.raises(error_output_list[i]):
            lops.get_max_diff(nums)
