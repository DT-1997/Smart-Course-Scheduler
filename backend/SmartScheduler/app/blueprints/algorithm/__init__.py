from flask import Blueprint

algorithm_bp = Blueprint('algorithm', __name__)

from app.blueprints.algorithm import routes