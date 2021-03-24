from app import app
from flask import request, Response
from random import random
import json


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
