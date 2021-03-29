import random
from math import trunc
from app import cache


@cache.memoize()
def random_nums(cantidad_muestra, seed):
    # Array donde se van a guardar y enviar los numeros randoms
    random_array = []
    # Cantidad de cifras decimales donde va a ser truncado cada numero aleatorio
    cifras_decimales = 4
    random.seed(seed)
    for i in range(cantidad_muestra):
        random_num = random.random()
        random_array.append({
            'num': trunc(random_num * 10 ** cifras_decimales) /
            10**cifras_decimales
        })
    return random_array
