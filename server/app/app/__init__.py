from flask import Flask
import os
from app.uploads.config import UploadsConfig

app = Flask(__name__)

# load settings
#app.config.from_pyfile(os.path.join(os.getcwd(), 'instance', 'config.py'))
# Config
app.config.from_object(UploadsConfig)

from app.api.routes import *