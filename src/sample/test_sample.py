import pytest

import sample


def test_version():
    assert isinstance(sample.__version__, str)


def test_some_function():
    res = sample.some_function()
    assert res is not None


def test_some_other_function():
    res = sample.some_other_function()
    assert res is not None


def test_one_more_function():
    res = sample.wrong_name()
    assert res is not None