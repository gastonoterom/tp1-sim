from app import app
from flask import request, Response
import json
from methods.randomNums import random_nums
import time


@app.route('/api/randomPython')
def randomPython():
    start = time.time()

    cantidad_muestra = int(request.args.get("cantidad_muestra"))
    seed = int(request.args.get("seed"))

    req_pagina = request.args.get("pagina")
    if (req_pagina):
        pagina = int(req_pagina)
    else:
        pagina = 1

    req_pageSize = request.args.get("pageSize")
    if (req_pageSize):
        pageSize = int(req_pageSize)
    else:
        pageSize = cantidad_muestra

    # Method random_nums is cached
    random_array = random_nums(cantidad_muestra, seed)

    random_array_sliced = random_array[(
        (pagina - 1) * pageSize):(pagina * pageSize)]

    end = time.time()

    print("Random generator time:", end - start)
    return Response(json.dumps(random_array_sliced), mimetype='application/json')
