from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# load settings
#app.config.from_pyfile(os.path.join(os.getcwd(), 'instance', 'config.py'))

from app.api.routes import *