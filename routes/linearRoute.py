from app import app
from flask import request, Response
from classes.randomGenerator import LinearGenerator
import json

@app.route('/randomLineal')
def randomLineal():

    # La semilla es X0
    semilla = int(request.args.get("semilla"))
    # La constante multiplicativa
    k = int(request.args.get("k"))
    # La constante aditiva DEBE SER RELATIVAMENTE PRIMO A M
    # TODO validar que sea relativamente primo a m
    c = int(request.args.get("c"))
    # El modulo m, g DEBE SER ENTERO POSITIVO
    # TODO validar que sea entero positivo
    g = int(request.args.get("g"))

    linearGenerator = LinearGenerator(k, c, semilla, g)
    random_array = linearGenerator.generateNumbers()

    return Response(json.dumps(random_array), mimetype='application/json')


