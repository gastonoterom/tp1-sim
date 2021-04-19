from app import app, cache
from flask import request, Response

# utilities
import json
import time
import math


# random methods
from methods.randomUniforme import random_uniforme
from methods.randomExponencial import random_exponencial
from methods.randomNormal import random_normal

# frequency methods
from methods.frequency import random_exponencial_frequency, random_uniforme_frequency, random_normal_frequency


@app.route('/api/frequency/<randomMethod>/')
def frequencyTable(randomMethod):

    # Get params

    try:
        intervalos = int(request.args.get("intervalos"))
        cantidad_muestra = int(request.args.get("cantidad_muestra"))
        seed = int(request.args.get("seed"))

    except Exception:
        return Response("Error: enviar cantidad de intervalos")
    # -----------

    # Generate random array depending which method was selected

    # # Uniform method
    if (randomMethod == "uniforme"):

        try:
            li = int(request.args.get("li"))
            ls = int(request.args.get("ls"))
        except Exception:
            return Response("Error: missing query parameters or not int")

        if(cantidad_muestra > 1000000):
            return Response("La cantidad de la muestra no puede ser mayor a un millon")

        random_array = random_uniforme(cantidad_muestra, seed, li, ls)
        freq, bins = random_uniforme_frequency(
            random_array, intervalos)
    # # -----------------

    # # Exponential method

    if (randomMethod == "exponencial"):
        try:
            media = float(request.args.get("media"))
        except Exception:
            return Response("Error: missing query parameters or not int")

        if(cantidad_muestra > 1000000):
            return Response("La cantidad de la muestra no puede ser mayor a un millon")

        random_array = random_exponencial(cantidad_muestra, seed, media)
        freq, bins = random_exponencial_frequency(random_array, intervalos)

    # # -----------------

    # # Normal method

    if (randomMethod == "normal"):

        try:
            mu = float(request.args.get("media"))
            sigma = float(request.args.get("sigma"))
        except Exception:
            mu = 0
            sigma = 1

        random_array = random_normal(cantidad_muestra, seed, mu, sigma)
        freq, bins = random_normal_frequency(random_array, intervalos)

    # # -----------------

    freq_parsed = [{'Intervalo': (i + 1), 'Frecuencia obtenida': x, 'Limite inferior': bins[i], 'Limite superior': bins[i + 1]}
                   for i, x in enumerate(freq.tolist())]

    # -------------------

    return Response(json.dumps(freq_parsed), mimetype='application/json')
