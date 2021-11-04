import pytest
import numpy as np


@pytest.fixture()
def base_test_array():
    return np.array([1, 2, 3, 4, 5])


@pytest.fixture()
def null_test_array():
    return np.array([1, 2, np.NaN, 4, 5])


@pytest.fixture()
def string_test_array():
    return np.array([1, 2, 'hi', 4, 5])
