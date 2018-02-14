import logging
logging.basicConfig(filename='test.log', filemode='w', level=logging.DEBUG)
logger = logging.getLogger()


def test_sum():
    logger.debug('Begin testing sum function')
    from list_ops import get_sum
    input_lists = ([1, 1],
                   [2, 1, 5],
                   [-3, 2, 6, 8, 9])
    output_results = (2, 8, 22)
    for i, l in enumerate(input_lists):
        print(l)
        assert get_sum(l) == output_results[i]