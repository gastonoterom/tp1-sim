from app import app
from flask import request, Response
import json
from methods.randomUniforme import random_uniforme
import time


@app.route('/api/randomUniforme/')
def uniformeRandom():
    start = time.time()

    try:
        cantidad_muestra = int(request.args.get("cantidad_muestra"))
        seed = int(request.args.get("seed"))
        li = int(request.args.get("li"))
        ls = int(request.args.get("ls"))
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
    random_array = random_uniforme(cantidad_muestra, seed, li, ls)[0]

    random_array_sliced = random_array[(
        (pagina - 1) * pageSize):(pagina * pageSize)]

    end = time.time()

    print("Random generator time:", end - start)
    return Response(json.dumps(random_array_sliced), mimetype='application/json')
