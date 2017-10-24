# all the imports
from flask import Flask

app = Flask(__name__, instance_relative_config=True) # create the application instance :)
app.config.from_pyfile('config.py')
app.config.from_envvar('FLASKR_SETTINGS', silent=True)

import webdj.views
