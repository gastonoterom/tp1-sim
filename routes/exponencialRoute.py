from app import app
from flask import request, Response
import json
from methods.randomExponencial import random_exponencial
import time


@app.route('/api/randomExponencial/')
def exponencialRandom():

    start = time.time()

    try:
        cantidad_muestra = int(request.args.get("cantidad_muestra"))
        seed = int(request.args.get("seed"))
        media = float(request.args.get("media"))
    except Exception:
        return Response("Error: missing query parameters or not int")

    if(cantidad_muestra > 1000000):
        return Response("La cantidad de la muestra no puede ser mayor a un millon")

    try:
        pagina = int(request.args.get("pagina"))
        pageSize = int(request.args.get("pageSize"))
    except Exception:
        pagina = 1
        pageSize = cantidad_muestra

    # Method random_nums is cached
    random_array = random_exponencial(cantidad_muestra, seed, media)[0]

    random_array_sliced = random_array[(
        (pagina - 1) * pageSize):(pagina * pageSize)]

    end = time.time()

    print("Random generator time:", end - start)
    return Response(json.dumps(random_array_sliced), mimetype='application/json')
