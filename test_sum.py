import logging
from logging_config import config

# init logging config
logging.basicConfig(**config)
logger = logging.getLogger(__name__)


def test_sum():
    from list_ops import get_sum
    input_lists = ([1, 1],
                   [2, 7001, 5],
                   [-3, 2, 6, 8, 8509])
    output_results = (2, 7008, 8522)
    for i, l in enumerate(input_lists):
        assert get_sum(l) == output_results[i]
    logger.debug('Complete testing sum function')
