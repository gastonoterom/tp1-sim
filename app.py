### Flask and sv imports
from jinja2 import Template
from flask import Flask, request, Response
import json
### Math imports
from random import random
from math import trunc
#import numpy
### Custom imports
from classes import JiCuadradoClass

app = Flask(__name__)


@app.route('/randomPython')
def randomPython():
    cantidad_muestra = int(request.args.get("cantidad_muestra"))

    # Array donde se van a guardar y enviar los numeros randoms
    random_array = []
    # Cantidad de cifras decimales donde va a ser truncado cada numero aleatorio
    cifras_decimales = 4

    for i in range(cantidad_muestra):
        random_num = random()
        random_array.append(
            trunc(random_num * 10 ** cifras_decimales)/10**cifras_decimales)

    return Response(json.dumps(random_array), mimetype='application/json')


# Esta funcion devuelve una lista de numeros aleatorios generados con el metodo congruencial
# lineal, pero si el parametro c es igual a 0, los genera con el congruencial multiplicativo
def random_lineal(semilla, a, c, m, cifras_decimales, cantidad_muestra):

    xi = semilla
    random_array = []
    for i in range(cantidad_muestra):
        xi_mas_uno = (a*xi+c) % m
        xi = xi_mas_uno
        random_number = trunc(
            xi/(m) * 10 ** cifras_decimales) / 10**cifras_decimales
        random_array.append(random_number)
    return random_array


@app.route('/randomLineal')
def randomLineal():

    # La semilla es X0
    semilla = int(request.args.get("semilla"))
    # La constante multiplicativa
    a = 1+4*int(request.args.get("k"))
    # La constante aditiva DEBE SER RELATIVAMENTE PRIMO A M
    # TODO validar que sea relativamente primo a m
    c = int(request.args.get("c"))
    # El modulo m, g DEBE SER ENTERO POSITIVO
    # TODO validar que sea entero positivo
    m = 2**int(request.args.get("g"))
    # Cantidad de la muestra requerida
    cantidad_muestra = int(request.args.get("cantidad_muestra"))

    # Cantidad de cifras decimales donde va a ser truncado cada numero aleatorio
    cifras_decimales = 4

    # Array donde se van a guardar y enviar los numeros randoms
    random_array = random_lineal(
        semilla, a, c, m, cifras_decimales, cantidad_muestra)

    return Response(json.dumps(random_array), mimetype='application/json')


@app.route('/randomMultiplicativo')
def randomMultiplicativo():

    # La semilla es X0
    semilla = int(request.args.get("semilla"))
    # La constante multiplicativa
    a = 3+8*int(request.args.get("k"))
    # El modulo m, G DEBE SER UN NUMERO ENTERO
    # TODO verificar que g sea numero entero
    m = 2**int(request.args.get("g"))
    # Cantidad de la muestra requerida
    cantidad_muestra = int(request.args.get("cantidad_muestra"))

    # Cantidad de cifras decimales donde va a ser truncado cada numero aleatorio
    cifras_decimales = 4

    # Array donde se van a guardar y enviar los numeros randoms
    random_array = random_lineal(
        semilla, a, 0, m, cifras_decimales, cantidad_muestra)

    return Response(json.dumps(random_array), mimetype='application/json')


@app.route('/jicuadrado', methods=['POST'])
def jiCuadrado():

    json_post_data = request.get_json()

    # Cantidad de intervalos
    intervalos = int(json_post_data["intervalos"])
    # Lista de numeros aleatorios
    random_array = json_post_data["random_array"]

    # Se crea el objeto JiCuadrado, y automaticamente llama a la funcion que cuenta la frecuencia por intervalos
    jicuadrado_obj = JiCuadradoClass(intervalos, random_array)

    return Response(json.dumps(jicuadrado_obj.__dict__), mimetype='application/json')
