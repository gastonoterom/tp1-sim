from app import app
from flask import request, Response
from classes.randomGenerator import MultiplicativeGenerator
import json
from app import cache
import time


@cache.memoize()
def randomMultCache(k, semilla, g, cantidad_muestra):
    return (MultiplicativeGenerator(k, semilla, g)).generateNumbers(cantidad_muestra)


@app.route('/api/randomMultiplicativo')
def randomMultiplicativo():
    start = time.time()
    # La semilla es X0
    semilla = int(request.args.get("semilla"))
    # La constante multiplicativa
    k = int(request.args.get("k"))
    # El modulo m, G DEBE SER UN NUMERO ENTERO
    g = int(request.args.get("g"))
    # Cantidad de elementos a mostrar
    cantidad_muestra = int(request.args.get("cantidad_muestra"))

    req_pagina = request.args.get("pagina")
    if (req_pagina):
        pagina = int(req_pagina)
    else:
        pagina = 1

    req_pageSize = request.args.get("pageSize")
    if (req_pageSize):
        pageSize = int(req_pageSize)
    else:
        pageSize = cantidad_muestra

    random_array = randomMultCache(k, semilla, g, cantidad_muestra)
    random_array_sliced = random_array[(
        (pagina - 1) * pageSize):(pagina * pageSize)]

    end = time.time()
    print("Multiplicative time:", end - start)
    return Response(json.dumps(random_array), mimetype='application/json')
