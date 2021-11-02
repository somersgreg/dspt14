import pandas as pd

df = pd.DataFrame([[1, 1, 1], [2, 2, 3]])


def plus_1(array):
    if array.dtype not in [int, float]:
        raise Exception('Please convert your array to integer or float.')
    return array + 1


def times_2(array):
    if array.dtype not in [int, float]:
        raise Exception('Please convert your array to integer or float.')
    return array * 2
