import pytest


<<<<<<< HEAD
<<<<<<< Updated upstream
=======
>>>>>>> master
def test_max_diff():
    from list_ops import get_max_diff
    error_input_list = (12, [1, 2, 3.32], [4, 'GTHC', 2, 333],
                        [85, -23, -2222222222222], [33, 123123123, -2])
    error_output_list = (TypeError, TypeError, TypeError,
                         ValueError, ValueError)
<<<<<<< HEAD
=======
def test_check_inputs():

    import list_ops as lops
    error_input_list = (12,
                        [1, 2, 3.32],
                        [4, 'GTHC', 2, 333],
                        [85, -23, -2222222222222],
                        [33, 9001, -2],
                        [-9001])

    error_output_list = (TypeError, TypeError, TypeError,
                         ValueError, ValueError, ValueError)
    # loop over exception triggers and module functions
>>>>>>> Stashed changes
=======
>>>>>>> master
    for i, nums in enumerate(error_input_list):
        with pytest.raises(error_output_list[i]):
            get_max_diff(nums)
