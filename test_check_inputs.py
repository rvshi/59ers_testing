import pytest
import logging
from logging_config import config

# init logging config
logging.basicConfig(**config)
logger = logging.getLogger(__name__)


def test_check_inputs():
    logger.debug('Begin testing check inputs function')
    from listops import BadNumbersException, ListOps
    error_input_list = (12,
                        [1, 2, 3.32],
                        [4, 'GTHC', 2, 333],
                        [85, -23, -2222222222222],
                        [33, 9001, -2],
                        [-9001],
                        [123, 3, 4, 321])

    error_output_list = (TypeError, TypeError, TypeError,
                         ValueError, ValueError, ValueError,
                         BadNumbersException)
    # loop over exception triggers and module functions
    for i, nums in enumerate(error_input_list):
        with pytest.raises(error_output_list[i]):
            ListOps(nums)
        with pytest.raises(error_output_list[i]):
            ListOps(nums)
        with pytest.raises(error_output_list[i]):
            ListOps(nums)
    logger.debug('Complete testing check inputs function')
