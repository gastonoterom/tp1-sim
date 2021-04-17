import random
from math import trunc
from math import log
from app import cache

# TP3: Genera una distribucion random uniforme


@cache.memoize()
def random_exponencial(cantidad_muestra, seed, media):

    # Array donde se van a guardar y enviar los numeros randoms
    random_array = []
    random_array_raw = []

    # Cantidad de cifras decimales donde va a ser truncado cada numero aleatorio
    cifras_decimales = 4

    # Usar lambda directamente si no hay media
    var_lambda = 1 / media

    random.seed(seed)
    for i in range(cantidad_muestra):

        random_num = -1 / var_lambda * log((1 - random.random()))
        random_array_raw.append(trunc(random_num * 10 ** cifras_decimales) /
                                10**cifras_decimales)
        random_array.append({
            'num': trunc(random_num * 10 ** cifras_decimales) /
            10**cifras_decimales
        })

    return random_array, random_array_raw
