from app import app
from flask import request, Response
from classes.randomGenerator import LinearGenerator
from app import cache
import json
import time


@cache.memoize()
def randomLinearCache(semilla, k, c, g, cantidad):
    return (LinearGenerator(k, c, semilla, g)).generateNumbers(cantidad)


@app.route('/api/randomLineal')
def randomLineal():
    start = time.time()

    # La semilla es X0
    semilla = int(request.args.get("semilla"))
    # La constante multiplicativa
    k = int(request.args.get("k"))
    # La constante aditiva DEBE SER RELATIVAMENTE PRIMO A M
    c = int(request.args.get("c"))
    # El modulo m, g DEBE SER ENTERO POSITIVO
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

    random_array = randomLinearCache(semilla, k, c, g, cantidad_muestra)
    random_array_sliced = random_array[(
        (pagina - 1) * pageSize):(pagina * pageSize)]

    end = time.time()
    print("Linear time:", end - start)
    return Response(json.dumps(random_array_sliced), mimetype='application/json')
