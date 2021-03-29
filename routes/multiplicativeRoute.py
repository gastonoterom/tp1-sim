from app import app
from flask import request, Response
from classes.randomGenerator import MultiplicativeGenerator
import json
from app import cache
import time


@cache.memoize()
def randomMultCache(k, semilla, g):
    return (MultiplicativeGenerator(k, semilla, g)).generateNumbers()


@app.route('/api/randomMultiplicativo')
def randomMultiplicativo():
    start = time.time()
    # La semilla es X0
    semilla = int(request.args.get("semilla"))
    # La constante multiplicativa
    k = int(request.args.get("k"))
    # El modulo m, G DEBE SER UN NUMERO ENTERO
    g = int(request.args.get("g"))
    

    random_array = randomMultCache(k, semilla, g)

    end = time.time()
    print("Multiplicative time:", end - start)
    return Response(json.dumps(random_array), mimetype='application/json')
