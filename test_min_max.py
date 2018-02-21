import logging
from logging_config import config

# init logging config
logging.basicConfig(**config)
logger = logging.getLogger(__name__)


def test_min_max():
    logger.debug('Begin testing min/max function')
    from listops import ListOps
    input_lists = ([1, 1],
                   [3, 4, 9],
                   [7, 10, -2, -2])
    output_results = ((1, 1),
                      (3, 9),
                      (-2, 10))
    for i, nums in enumerate(input_lists):
        l = ListOps(nums)
        assert l.get_min_max() == output_results[i]
    logger.debug('Complete testing min/max function')
