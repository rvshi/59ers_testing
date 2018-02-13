import pytest
import sys
import mock


def test_import():
    # remove the numpy library
    with mock.patch.dict('sys.modules', {'numpy': None}):
        from list_ops import import_modules

        with pytest.raises(ImportError):
            import_modules()
