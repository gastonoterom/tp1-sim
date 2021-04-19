import random
from math import trunc
from math import log
from math import sqrt
from math import cos
from math import sin
import math
from app import cache
import numpy as np
from numba import njit
# TP3: Genera una distribucion random normal


@cache.memoize()
def random_normal(cantidad_muestra, seed, mu, sigma):

    np.random.seed(seed)
    py_random_array = np.random.rand(cantidad_muestra + 1)

    return random_normal_numba(py_random_array, cantidad_muestra, mu, sigma)


@njit
def random_normal_numba(py_random_array, size, mu, sigma):

    output_array = np.zeros(size)

    decimals = 4

    for ii in range(size):

        if (ii % 2 == 0):
            random1 = py_random_array[ii]
            random2 = py_random_array[ii + 1]

            random_num = (sqrt(-2 * log(random1)) *
                          cos(2 * math.pi * random2)) * sigma + mu
        else:
            random_num = (sqrt(-2 * log(random1)) *
                          sin(2 * math.pi * random2)) * sigma + mu

        random_num_trunc = trunc(random_num * 10 ** decimals) / 10**decimals

        output_array[ii] = random_num_trunc

    return output_array
