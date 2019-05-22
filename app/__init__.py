# app.py or app/__init__.py
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

# custom
# import models

app = Flask(__name__, instance_relative_config=True)
basedir = os.path.abspath(os.path.dirname(__file__))
# Load the default configuration
app.config.from_object('config.default')

# Load the configuration from the instance folder
app.config.from_pyfile('config.py')

# Load the file specified by the APP_CONFIG_FILE environment variable
# The value of the environment variable should be the absolute path to a configuration file.
# Variables defined here will override those in the default configuration
app.config.from_envvar('APP_CONFIG_FILE')

app.config["BASEDIR"]

# Now we can access the configuration variables via app.config["VAR_NAME"].
app.config["SQLALCHEMY_ECHO"]
app.config["SQLALCHEMY_DATABASE_URI"]
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]

# Create the SqlAlchemy db instance
db = SQLAlchemy(app)

# Initialize Marshmallow
ma = Marshmallow(app)


from . import views