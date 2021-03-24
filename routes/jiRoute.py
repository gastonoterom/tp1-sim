from app import app
from flask import request, Response
from classes.jiCuadrado import JiCuadradoClass
import json

@app.route('/jicuadrado', methods=['POST'])
def jiCuadrado():

    json_post_data = request.get_json()

    # Cantidad de intervalos
    intervalos = int(json_post_data["intervalos"])
    # Lista de numeros aleatorios
    random_array = json_post_data["random_array"]

    # Se crea el objeto JiCuadrado, y automaticamente llama a la funcion que cuenta la frecuencia por intervalos
    jicuadrado_obj = JiCuadradoClass(intervalos, random_array)

    return Response(json.dumps(jicuadrado_obj.estadistico_prueba), mimetype='application/json')
