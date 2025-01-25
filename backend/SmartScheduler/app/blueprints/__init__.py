from app.blueprints.auth import auth_bp
from app.blueprints.admin import admin_bp
from app.blueprints.upload import upload_bp
from app.blueprints.algorithm import algorithm_bp


def register_blueprints(app):
    # Register Blueprints
    app.register_blueprint(auth_bp, url_prefix='/api/auth')
    app.register_blueprint(admin_bp, url_prefix='/api/admin')
    app.register_blueprint(upload_bp, url_prefix='/api/upload')
    app.register_blueprint(algorithm_bp, url_prefix='/api/algorithm')
