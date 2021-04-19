from app import app
from flask import request, Response
import json
from methods.randomNormal import random_normal
import time


@app.route('/api/randomNormal/')
def normal_random():

    # Start time counter
    start = time.time()

    # -------------------

    # Get params

    try:
        cantidad_muestra = int(request.args.get("cantidad_muestra"))
        seed = int(request.args.get("seed"))
    except Exception:
        return Response("Error: missing query parameters or not int")

    try:
        mu = float(request.args.get("mu"))
        sigma = float(request.args.get("sigma"))
    except Exception:
        return Response("Error: missing query parameters or not int")

    try:
        pagina = int(request.args.get("pagina"))
        pageSize = int(request.args.get("pageSize"))
    except Exception:
        pagina = 1
        pageSize = cantidad_muestra

    # -------------

    # Generate random array
    random_array = random_normal(cantidad_muestra, seed, mu, sigma)

    # Slice random array
    random_array_sliced = random_array[(
        (pagina - 1) * pageSize):(pagina * pageSize)]

    # Parse the random array
    random_array_sliced_parsed = list(
        map(lambda x: {'num': x}, random_array_sliced))

    # ----------------------

    # End the counter

    end = time.time()

    print("Random generator time:", end - start)

    # ---------------

    return Response(json.dumps(random_array_sliced_parsed), mimetype='application/json')
