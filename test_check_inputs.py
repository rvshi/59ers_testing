import pytest


def test_max_diff():
    from list_ops import get_max_diff
    error_input_list = (12, [1, 2, 3.32], [4, 'GTHC', 2, 333],
                        [85, -23, -2222222222222], [33, 123123123, -2])
    error_output_list = (TypeError, TypeError, TypeError,
                         ValueError, ValueError)
    for i, nums in enumerate(error_input_list):
        with pytest.raises(error_output_list[i]):
            get_max_diff(nums)
