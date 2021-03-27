from app import app
from flask import request, Response
import random
from math import trunc
import json
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


@app.route('/randomPython')
def randomPython():

    cantidad_muestra = int(request.args.get("cantidad_muestra"))
    pagina = int(request.args.get("pagina"))
    pageSize = int(request.args.get("pageSize"))
    seed = int(request.args.get("seed"))

    if (cantidad_muestra > 1000000):
        cantidad_muestra = 1000000

    random_array = random_nums(cantidad_muestra, seed)
    random_array_sliced = random_array[(
        (pagina - 1) * pageSize):(pagina * pageSize)]
    print(random_array_sliced)
    return Response(json.dumps(random_array_sliced), mimetype='application/json')
