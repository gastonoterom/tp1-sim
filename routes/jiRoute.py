from app import app, cache
from flask import request, Response
from classes.jiCuadrado import JiCuadradoClass
from methods.randomNums import random_nums
import json
import time
import math
# histogram
import base64
from io import BytesIO
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from routes.linearRoute import randomLinearCache
from routes.multiplicativeRoute import randomMultCache


@cache.memoize()
def getJiCuadradoObjectRandom(cantidad_muestra, seed, intervalos):
    random_array = random_nums(cantidad_muestra, seed)
    return JiCuadradoClass(intervalos, random_array)


@cache.memoize()
def getJiCuadradoObjectLinear(semilla, k, c, g, intervalos, cantidad_muestra):
    print(cantidad_muestra, "CANTIDAD MUESTRA \n\n\n\n")
    random_array = randomLinearCache(semilla, k, c, g, cantidad_muestra)
    return JiCuadradoClass(intervalos, random_array)


@cache.memoize()
def getJiCuadradoObjectMult(k, semilla, g, intervalos, cantidad_muestra):
    random_array = randomMultCache(semilla, k, g, cantidad_muestra)
    return JiCuadradoClass(intervalos, random_array)


@app.route('/api/jicuadrado/<randomMethod>/')
def jiCuadrado(randomMethod):
    start = time.time()

    intervalos = int(request.args.get("intervalos"))

    # Generar el vector aleatorio de a cuerdo a cada metodo
    if (randomMethod == "random"):
        cantidad_muestra = int(request.args.get("cantidad_muestra"))
        seed = int(request.args.get("seed"))

        # Se crea el objeto JiCuadrado, y automaticamente llama a la funcion que cuenta la frecuencia por intervalos
        jicuadrado_obj = getJiCuadradoObjectRandom(
            cantidad_muestra, seed, intervalos)

    if (randomMethod == "linear"):
        # La semilla es X0
        seed = int(request.args.get("seed"))
        # La constante multiplicativa
        k = int(request.args.get("k"))
        # La constante aditiva DEBE SER RELATIVAMENTE PRIMO A M
        c = int(request.args.get("c"))
        # El modulo m, g DEBE SER ENTERO POSITIVO
        g = int(request.args.get("g"))
        # Tamaño de la muestra a mostrar
        cantidad_muestra = int(request.args.get("cantidad_muestra"))

        jicuadrado_obj = getJiCuadradoObjectLinear(
            seed, k, c, g, intervalos, cantidad_muestra)

    if (randomMethod == "multiplicative"):
        # La semilla es X0
        seed = int(request.args.get("seed"))
        # La constante multiplicativa
        k = int(request.args.get("k"))
        # El modulo m, g DEBE SER ENTERO POSITIVO
        g = int(request.args.get("g"))
        cantidad_muestra = int(request.args.get("cantidad_muestra"))

        jicuadrado_obj = getJiCuadradoObjectMult(
            k, seed, g, intervalos, cantidad_muestra)

    end = time.time()

    print("Ji cuadrado response time:", end - start)

    return Response(json.dumps(jicuadrado_obj.rows), mimetype='application/json')


@app.route('/api/histogram/<randomMethod>/')
def histogramGenerator(randomMethod):

    intervalos = int(request.args.get("intervalos"))

    # Generar el vector aleatorio de a cuerdo a cada metodo
    if (randomMethod == "random"):
        cantidad_muestra = int(request.args.get("cantidad_muestra"))
        seed = int(request.args.get("seed"))

        # Se crea el objeto JiCuadrado, y automaticamente llama a la funcion que cuenta la frecuencia por intervalos
        jicuadrado_obj = getJiCuadradoObjectRandom(
            cantidad_muestra, seed, intervalos)

    if (randomMethod == "linear"):
        # La semilla es X0
        seed = int(request.args.get("seed"))
        # La constante multiplicativa
        k = int(request.args.get("k"))
        # La constante aditiva DEBE SER RELATIVAMENTE PRIMO A M
        c = int(request.args.get("c"))
        # El modulo m, g DEBE SER ENTERO POSITIVO
        g = int(request.args.get("g"))
        # Tamaño de la muestra a mostrar
        cantidad_muestra = int(request.args.get("cantidad_muestra"))

        jicuadrado_obj = getJiCuadradoObjectLinear(
            seed, k, c, g, intervalos, cantidad_muestra)

    if (randomMethod == "multiplicative"):
        # La semilla es X0
        seed = int(request.args.get("seed"))
        # La constante multiplicativa
        k = int(request.args.get("k"))
        # El modulo m, g DEBE SER ENTERO POSITIVO
        g = int(request.args.get("g"))
        cantidad_muestra = int(request.args.get("cantidad_muestra"))

        jicuadrado_obj = getJiCuadradoObjectMult(
            k, seed, g, intervalos, cantidad_muestra)

    # Generate the figure **without using pyplot**.
    fig = Figure()
    ax = fig.subplots()

    bins = [math.trunc(1 / intervalos * i * 10000) /
            10000 for i in range(intervalos + 1)]

    values, bin_bounds, bars = ax.hist(
        jicuadrado_obj.random_array, bins=bins)
    ax.set_title("Histograma de Frecuencias Obtenidas en Numeros Aleatorios")

    ax.set_xlabel("Numeros aleatorios")
    ax.set_ylabel("Frecuencias observadas")
    # Save it to a temporary buffer.
    buf = BytesIO()
    fig.savefig(buf, format="png")
    # Embed the result in the html output.
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    return Response(buf.getvalue(), mimetype='image/png')
