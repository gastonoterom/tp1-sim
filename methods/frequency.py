from numba import njit
import numpy as np
import math


def random_uniforme_frequency(random_array, bins):
    return random_frequency(random_array, bins)


def random_exponencial_frequency(random_array, bins):
    return random_frequency(random_array, bins)


def random_normal_frequency(random_array, bins):
    return random_frequency(random_array, bins)


@njit
def random_frequency(random_array, bins, uniform=False, li=None, ls=None):
    result, bins = np.histogram(random_array, bins=bins)
    bins = [math.trunc(x * 10000) / 10000 for x in bins]
    #bins = map(lambda x: (math.trunc(x * 10000) / 10000), bins)
    return result, bins
