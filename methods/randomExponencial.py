import random
from math import trunc
from math import log
from app import cache
import numpy as np
from numba import njit

# TP3: Genera una distribucion random uniforme


@cache.memoize()
def random_exponencial(cantidad_muestra, seed, mu):

    np.random.seed(seed)
    py_random_array = np.random.rand(cantidad_muestra)

    return random_exp_numba(py_random_array, mu)


@njit
def random_exp_numba(py_random_array, mean):

    size = len(py_random_array)

    output_array = np.zeros(size)

    decimals = 4

    var_lambda = 1 / mean

    for ii in range(size):

        random_num = -1 / var_lambda * log((1 - py_random_array[ii]))
        random_num_trunc = trunc(random_num * 10 ** decimals) / 10**decimals

        output_array[ii] = random_num_trunc

    return output_array
