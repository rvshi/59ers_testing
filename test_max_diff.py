import logging
from logging_config import config

# init logging config
logging.basicConfig(**config)
logger = logging.getLogger(__name__)


def test_max_diff():
    logger.debug('Begin testing max difference function')
    from list_ops import get_max_diff
    input_list = ([1, 1, 3], [-1, 3, -16], [5, 5, 5, 5, 5])
    output_results = (2, 4, 0)
    for i, nums in enumerate(input_list):
        assert get_max_diff(nums) == output_results[i]
    logger.debug('Complete testing max difference function')
