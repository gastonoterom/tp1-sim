from app import app
from flask import request, Response
import json
from methods.randomNormal import random_normal
import time


@app.route('/api/randomNormal/')
def normal_random():

    start = time.time()

    try:
        cantidad_muestra = int(request.args.get("cantidad_muestra"))
        seed = int(request.args.get("seed"))
    except Exception:
        return Response("Error: missing query parameters or not int")

    if(cantidad_muestra > 1000000):
        return Response("La cantidad de la muestra no puede ser mayor a un millon")

    try:
        mu = float(request.args.get("media"))
        sigma = float(request.args.get("sigma"))
    except Exception:
        mu = 0
        sigma = 1

    try:
        pagina = int(request.args.get("pagina"))
        pageSize = int(request.args.get("pageSize"))
    except Exception:
        pagina = 1
        pageSize = cantidad_muestra

    # Method random_nums is cached
    random_array = random_normal(cantidad_muestra, seed, mu, sigma)[0]

    random_array_sliced = random_array[(
        (pagina - 1) * pageSize):(pagina * pageSize)]

    end = time.time()

    print("Random generator time:", end - start)
    return Response(json.dumps(random_array_sliced), mimetype='application/json')
