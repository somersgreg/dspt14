import pandas as pd
import numpy as np


class MyPreprocessor:
    constant = None

    def __init__(self, constant):
        self.constant = constant

    def plus_constant(self, array):
        if not isinstance(array, np.ndarray):
            raise Exception('Only numpy arrays are accepted')
        if array.dtype not in [int, float]:
            raise Exception('Please convert your array to integer or float.')
        return array + self.constant

    def times_constant(self, array):
        if array.dtype not in [int, float]:
            raise Exception('Please convert your array to integer or float.')
        return array * self.constant

    def exponent_constant(self, array):
        if array.dtype not in [int, float]:
            raise Exception('Please convert your array to integer or float.')
        return array ** self.constant
