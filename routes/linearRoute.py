from app import app
from flask import request, Response
from classes.randomGenerator import LinearGenerator
from app import cache
import json
import time


@cache.memoize()
def randomLinearCache(semilla, k, c, g):
    return (LinearGenerator(k, c, semilla, g)).generateNumbers()


@app.route('/api/randomLineal')
def randomLineal():
    start = time.time()

    # La semilla es X0
    semilla = int(request.args.get("semilla"))
    # La constante multiplicativa
    k = int(request.args.get("k"))
    # La constante aditiva DEBE SER RELATIVAMENTE PRIMO A M
    # TODO validar que sea relativamente primo a m
    c = int(request.args.get("c"))
    # El modulo m, g DEBE SER ENTERO POSITIVO
    # TODO validar que sea entero positivo
    g = int(request.args.get("g"))

    random_array = randomLinearCache(semilla, k, c, g)

    end = time.time()
    print("Linear time:", end - start)
    return Response(json.dumps(random_array), mimetype='application/json')
