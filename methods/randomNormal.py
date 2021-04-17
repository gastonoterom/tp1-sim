import random
from math import trunc
from math import log
from math import sqrt
from math import cos
from math import sin
import math
from app import cache

# TP3: Genera una distribucion random uniforme


def random_norma_estandar(cantidad_muestra, seed):
    return random_normal(cantidad_muestra, seed, mu=0, sigma=1)


@cache.memoize()
def random_normal(cantidad_muestra, seed, mu=0, sigma=1):

    # Array donde se van a guardar y enviar los numeros randoms
    random_array = []
    random_array_raw = []

    # Cantidad de cifras decimales donde va a ser truncado cada numero aleatorio
    cifras_decimales = 4

    random.seed(seed)

    for i in range(cantidad_muestra):

        if (i % 2 == 0):
            random1 = random.random()
            random2 = random.random()

            random_num = (sqrt(-2 * log(random1)) *
                          cos(2 * math.pi * random2)) * sigma + mu
        else:
            random_num = (sqrt(-2 * log(random1)) *
                          sin(2 * math.pi * random2)) * sigma + mu

        random_array_raw.append(
            trunc(random_num * 10 ** cifras_decimales) / 10**cifras_decimales)
        random_array.append({
            'num': trunc(random_num * 10 ** cifras_decimales) / 10**cifras_decimales
        })

    return random_array, random_array_raw
