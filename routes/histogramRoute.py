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


@app.route('/api/histogram/<randomMethod>/')
def histogramGenerator(randomMethod):
    try:
        intervalos = int(request.args.get("intervalos"))
    except Exception:
        return Response("Error: enviar cantidad de intervalos")

    # Generar el vector aleatorio de a cuerdo a cada metodo
    if (randomMethod == "uniforme"):

        try:
            cantidad_muestra = int(request.args.get("cantidad_muestra"))
            seed = int(request.args.get("seed"))
            li = int(request.args.get("li"))
            ls = int(request.args.get("ls"))
        except Exception:
            return Response("Error: missing query parameters or not int")

        if(cantidad_muestra > 1000000):
            return Response("La cantidad de la muestra no puede ser mayor a un millon")

        random_array = random_uniforme(cantidad_muestra, seed, li, ls)[1]

    if (randomMethod == "exponencial"):
        try:
            cantidad_muestra = int(request.args.get("cantidad_muestra"))
            seed = int(request.args.get("seed"))
            media = float(request.args.get("media"))
        except Exception:
            return Response("Error: missing query parameters or not int")

        if(cantidad_muestra > 1000000):
            return Response("La cantidad de la muestra no puede ser mayor a un millon")

        # Method random_nums is cached
        random_array = random_exponencial(cantidad_muestra, seed, media)[1]

    if (randomMethod == "normal"):
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

        #  Method random_nums is cached
        random_array = random_normal(cantidad_muestra, seed, mu, sigma)[1]

    # Generate the figure **without using pyplot**.
    fig = Figure()
    ax = fig.subplots()

    bins = [math.trunc(1 / intervalos * i * 10000) /
            10000 for i in range(intervalos + 1)]

    values, bin_bounds, bars = ax.hist(
        random_array, bins=bins)
    ax.set_title("Histograma de Frecuencias Obtenidas en Numeros Aleatorios")

    ax.set_xlabel("Numeros aleatorios")
    ax.set_ylabel("Frecuencias observadas")

    # Save it to a temporary buffer.
    buf = BytesIO()
    fig.savefig(buf, format="png")

    # Embed the result in the html output.
    # data = base64.b64encode(buf.getbuffer()).decode("ascii")
    return Response(buf.getvalue(), mimetype='image/png')
