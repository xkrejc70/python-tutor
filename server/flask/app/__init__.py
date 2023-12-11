from flask import Flask

app = Flask(__name__)

# load settings
#app.config.from_pyfile(os.path.join(os.getcwd(), 'instance', 'config.py'))

from app.api.routes import *