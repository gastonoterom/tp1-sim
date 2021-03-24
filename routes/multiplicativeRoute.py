from app import app
from flask import request, Response
from classes.randomGenerator import MultiplicativeGenerator
import json


@app.route('/randomMultiplicativo')
def randomMultiplicativo():

    # La semilla es X0
    semilla = int(request.args.get("semilla"))
    # La constante multiplicativa
    k = int(request.args.get("k"))
    # El modulo m, G DEBE SER UN NUMERO ENTERO
    # TODO verificar que g sea numero entero
    g = int(request.args.get("g"))

    multiplicativeGenerator = MultiplicativeGenerator(k, semilla, g)
    random_array = multiplicativeGenerator.generateNumbers()
    return Response(json.dumps(random_array), mimetype='application/json')
