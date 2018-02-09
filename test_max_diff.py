def test_max_diff():
    from list_ops import get_max_diff
    input_list = ([1, 1, 3], [-1, 3, -16], [5, 5, 5, 5, 5], [3.4, 5, 6.3, 2])
    output_results = (2, 4, 0, 1.6)
    for i, nums in enumerate(input_list):
        assert get_max_diff(nums) == output_results[i]
