import random
from math import trunc
from app import cache
import numpy as np
from numba import njit
# TP3: Genera una distribucion random uniforme


@cache.memoize()
def random_uniforme(cantidad_muestra, seed, li, ls):

    np.random.seed(seed)
    py_random_array = np.random.rand(cantidad_muestra)

    return random_uniforme_numba(py_random_array, li, ls)


@njit
def random_uniforme_numba(py_random_array, li, ls):

    py_random_array_size = len(py_random_array)

    output_array = np.zeros(py_random_array_size)

    decimals = 4

    for ii in range(py_random_array_size):

        random_num = li + py_random_array[ii] * (ls - li)

        random_num_trunc = trunc(random_num * 10 ** decimals) / 10**decimals

        output_array[ii] = random_num_trunc

    return output_array
