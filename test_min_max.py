import logging
logging.basicConfig(filename='test.log', filemode='w', level=logging.DEBUG)
logger = logging.getLogger()


def test_min_max():
    logger.debug('Begin testing min/max function')
    from list_ops import get_min_max
    input_lists = ([1, 1],
                   [3, 4, 9],
                   [7, 10, -2, -2])
    output_results = ((1, 1),
                      (3, 9),
                      (-2, 10))
    for i, list in enumerate(input_lists):
        min_max_output = get_min_max(list)
        assert min_max_output == output_results[i]
