import pytest
import numpy as np
from dspt14.example import plus_1, times_2
from numpy.testing import assert_array_equal


def test_plus_1(base_test_array):
    assert_array_equal(np.array([2, 3, 4, 5, 6]), plus_1(base_test_array))


def test_times_2(base_test_array):
    assert_array_equal(np.array([2, 4, 6, 8, 10]), times_2(base_test_array))


def test_plus_1_null(null_test_array):
    assert_array_equal(np.array([2, 3, np.NaN, 5, 6]), plus_1(null_test_array))


def test_times_2_null(null_test_array):
    assert_array_equal(np.array([2, 4, np.NaN, 8, 10]), times_2(null_test_array))


def test_plus_1_string(string_test_array):
    try:
        plus_1(string_test_array)
    except Exception:
        pass
    else:
        assert False


def test_times_2_string(string_test_array):
    try:
        times_2(string_test_array)
    except Exception:
        pass
    else:
        assert False
