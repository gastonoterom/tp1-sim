from flask import Flask
from flask_cors import CORS

app = Flask(__name__, template_folder='frontend/dist')
CORS(app)


import frontend
from routes import linearRoute, jiRoute, multiplicativeRoute, randomRoute
