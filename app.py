from flask import Flask
from flask_cors import CORS
from flask_caching import Cache
import flask_excel as excel

app = Flask(__name__, template_folder='frontend/dist')

config = {
    "DEBUG": True,          # some Flask specific configs
    "CACHE_TYPE": "SimpleCache",  # Flask-Caching related configs
    "CACHE_DEFAULT_TIMEOUT": 300
}

# tell Flask to use the above defined config
app.config.from_mapping(config)
cache = Cache(app)
excel.init_excel(app)
CORS(app)


#import frontend
from routes import linearRoute, jiRoute, multiplicativeRoute, randomRoute
