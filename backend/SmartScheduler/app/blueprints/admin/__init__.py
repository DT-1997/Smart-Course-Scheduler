from flask import Blueprint

admin_bp = Blueprint('admin', __name__)

from app.blueprints.admin import routes  # noqa: F401, E402
