import random
from math import trunc
from app import cache

# TP3: Genera una distribucion random uniforme


@cache.memoize()
def random_uniforme(cantidad_muestra, seed, li, ls):

    # Array donde se van a guardar y enviar los numeros randoms
    random_array = []
    random_array_raw = []
    # Cantidad de cifras decimales donde va a ser truncado cada numero aleatorio
    cifras_decimales = 4
    random.seed(seed)
    for i in range(cantidad_muestra):

        random_num = li + random.random() * (ls - li)
        random_array_raw.append(trunc(random_num * 10 ** cifras_decimales) /
                                10**cifras_decimales)
        random_array.append({
            'num': trunc(random_num * 10 ** cifras_decimales) /
            10**cifras_decimales
        })

    return random_array, random_array_raw
