import pandas as pd

df = pd.DataFrame([[1, 1, 1], [2, 2, 3]])


class my_preprocessor():
    constant = None

    def __init__(self, constant):
        self.constant = constant

    def plus_constant(self, array):
        if array.dtype not in [int, float]:
            raise Exception('Please convert your array to integer or float.')
        return array + self.constant

    def times_constant(self, array):
        if array.dtype not in [int, float]:
            raise Exception('Please convert your array to integer or float.')
        return array * self.constant
