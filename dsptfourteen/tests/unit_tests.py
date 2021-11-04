import numpy as np
from dsptfourteen.dsptfourteen import MyPreprocessor
from numpy.testing import assert_array_equal


def test_plus_1(base_test_array):
    pp = MyPreprocessor(constant=1)
    assert_array_equal(np.array([2, 3, 4, 5, 6]), pp.plus_constant(base_test_array))


def test_times_2(base_test_array):
    pp = MyPreprocessor(constant=2)
    assert_array_equal(np.array([2, 4, 6, 8, 10]), pp.times_constant(base_test_array))


def test_exponent_2(base_test_array):
    pp = MyPreprocessor(constant=2)
    assert_array_equal(np.array([1**2, 2**2, 3**2, 4**2, 5**2]), pp.times_constant(base_test_array))


def test_plus_1_null(null_test_array):
    pp = MyPreprocessor(constant=1)
    assert_array_equal(np.array([2, 3, np.NaN, 5, 6]), pp.plus_constant(null_test_array))


def test_times_2_null(null_test_array):
    pp = MyPreprocessor(constant=2)
    assert_array_equal(np.array([2, 4, np.NaN, 8, 10]), pp.times_constant(null_test_array))


def test_plus_1_string(string_test_array):
    pp = MyPreprocessor(constant=1)
    try:
        pp.times_constant(string_test_array)
    except Exception:
        pass
    else:
        assert False


def test_times_2_string(string_test_array):
    pp = MyPreprocessor(constant=2)
    try:
        pp.times_constant(string_test_array)
    except Exception:
        pass
    else:
        assert False
