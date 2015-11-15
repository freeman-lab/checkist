import pytest
import checkist


def test_opts_one():
    checkist.opts('cow', ['cow'])

def test_opts_one_error():
    with pytest.raises(ValueError):
        checkist.opts('cow', ['bear'])

def test_opts_many():
    checkist.opts('cow', ['cow', 'bear', 'cat'])

def test_opts_many_error():
    with pytest.raises(ValueError):
        checkist.opts('cow', ['bear', 'cat', 'owl'])