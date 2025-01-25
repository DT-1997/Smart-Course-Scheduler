import logging
import os
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_mail import Mail

# Create a Mail instance
mail = Mail()

# Create a JWT instance
jwt = JWTManager()

# Create a CORS instance
cors = CORS()

# Create a SQLAlchemy instance
db = SQLAlchemy()

# Create a Bcrypt instance (used for password hashing and verification)
bcrypt = Bcrypt()


def create_logger(name, log_file, level=logging.INFO):
    """
    Create and configure a logger.
    :param name: Name of the logger (e.g., module name)
    :param log_file: Path to the log file
    :param level: Logging level (default: logging.INFO)
    :return: Configured logger instance
    """
    # Create logger
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Create logs directory if it doesn't exist
    os.makedirs(os.path.dirname(log_file), exist_ok=True)

    # Define the log format
    formatter = (logging.Formatter
                 ('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))

    # Create a file handler for logging
    file_handler = logging.FileHandler(log_file)
    file_handler.setFormatter(formatter)

    # Create a console handler for logging
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    # Add handlers to the logger
    if not logger.handlers:  # Avoid adding multiple handlers
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

    return logger


def init_logging(app):
    """
    Initialize global logging for the Flask application.
    :param app: Flask application instance
    """
    # Use the create_logger function to configure the app logger
    app.logger = create_logger('melody_haven', 'logs/app.log')

    # Test log output
    app.logger.info('Logging is successfully configured!')


def init_extensions(app):
    """
    Initialize Flask extensions.
    :param app: Flask application instance
    """
    # Initialize SQLAlchemy
    db.init_app(app)

    # Initialize Bcrypt
    bcrypt.init_app(app)

    # Initialize CORS
    cors.init_app(app)

    # Initialize JWT
    jwt.init_app(app)

    # Initialize Mail
    mail.init_app(app)

    # Initialize logging
    init_logging(app)
