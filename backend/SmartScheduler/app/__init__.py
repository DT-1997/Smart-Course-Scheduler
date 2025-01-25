from flask import Flask, send_from_directory
from app.extensions import init_extensions, db
from app.config import Config
from app.blueprints import register_blueprints
import pymysql
pymysql.install_as_MySQLdb()


def create_app():
    # Initialize Flask app with static file settings
    app = Flask(__name__, static_folder="../dist", static_url_path="")
    app.config.from_object(Config)  # Load configuration from Config class

    # Initialize extensions (e.g., database, authentication, etc.)
    init_extensions(app)

    # Register blueprints for modular routing
    register_blueprints(app)

    # Create the database and tables within the application context
    with app.app_context():
        db.create_all()  # Ensure all database tables are created

    # Add routes for serving static files
    @app.route('/')
    def serve_vue():
        # Return dist/index.html
        return send_from_directory(app.static_folder, 'index.html')

    @app.route('/<path:path>')
    def static_files(path):
        # Return files from the dist folder
        return send_from_directory(app.static_folder, path)

    return app
