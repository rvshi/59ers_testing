import pytest
import sys
import mock
import logging
from logging_config import config

# init logging config
logging.basicConfig(**config)
logger = logging.getLogger(__name__)


def test_import():
    logger.debug('Begin testing import')
    # remove the numpy library
    with mock.patch.dict('sys.modules', {'numpy': None}):
        from listops import ListOps

        with pytest.raises(ImportError):
            ListOps([])
    logger.debug('Complete testing import')
