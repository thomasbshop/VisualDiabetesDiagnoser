from flask import Blueprint

diagnoser = Blueprint('diagnoser', __name__)

from . import views, classify
