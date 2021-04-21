from app import app, cache
from flask import request, Response

# utilities
import json
import time
import math

# histogram
import base64
from io import BytesIO
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from app import excel

# random methods
from methods.randomUniforme import random_uniforme
from methods.randomExponencial import random_exponencial
from methods.randomNormal import random_normal

# frequency methods
from methods.frequency import random_exponencial_frequency, random_uniforme_frequency, random_normal_frequency


@cache.memoize()
def generateHistogram(bins, random_array):
    # Generate the figure **without using pyplot**.
    fig = Figure()
    ax = fig.subplots()

    values, bin_bounds, bars = ax.hist(
        random_array, bins=bins)

    ax.set_title("Histograma de Frecuencias Obtenidas en Numeros Aleatorios")

    ax.set_xticks(bins)

    ax.tick_params(axis='x', labelrotation=45)

    ax.set_xlabel("Numeros aleatorios")
    ax.set_ylabel("Frecuencias observadas")
    # ---------------------------------------------

    # Save it to a temporary buffer.
    buf = BytesIO()
    fig.savefig(buf, format="png")
    return buf


@app.route('/api/histogram/<randomMethod>/')
def histogramGenerator(randomMethod):

    # Start time counter
    start = time.time()

    # -------------------

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
            li = float(request.args.get("li"))
            ls = float(request.args.get("ls"))
        except Exception:
            return Response("Error: missing query parameters or not int/float")

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

    # -------------------
    # Generate the histogram

    buf = generateHistogram(bins, random_array)

    # -----------------------------

    # End the counter

    end = time.time()

    print("Histogram generator time:", end - start)

    # ---------------

    return Response(buf.getvalue(), mimetype='image/png')
