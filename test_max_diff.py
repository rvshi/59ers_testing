import pytest


def test_max_diff():
    from list_ops import get_max_diff
    input_list = ([1, 1, 3], [-1, 3, -16], [5, 5, 5, 5, 5])
    output_results = (2, 4, 0)
    for i, nums in enumerate(input_list):
        assert get_max_diff(nums) == output_results[i]
    type_error_list = ([1, 2, 3.32], [4, 'GTHC', 2, 333])
    for nums in type_error_list:
        with pytest.raises(TypeError):
            get_max_diff(nums)
