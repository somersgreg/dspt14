import pytest
import numpy as np
from dspt14.example import plus_1
from numpy.testing import assert_array_equal


def test_plus_1():
    array = np.array([1, 2, 3, 4, 5])
    assert_array_equal(np.array([2, 3, 4, 5, 6]), plus_1(array))
