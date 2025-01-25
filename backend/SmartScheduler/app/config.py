import os

# Get the base directory of the current file
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    # Database configuration
    # Use SQLite database and define its location within the 'instance' folder
    SQLALCHEMY_DATABASE_URI = f"mysql://root:%40%23lurn12138@localhost/smart_scheduler"
    # Disable SQLAlchemy event notifications for better performance
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Application secret keys
    SECRET_KEY = 'Nwfl'  # Secret key for session management
    JWT_SECRET_KEY = 'Nwfl'  # Secret key for JWT authentication

    # Flask-Mail configuration
    # Use qq's SMTP server for sending emails
    MAIL_SERVER = 'smtp.qq.com'
    MAIL_PORT = 465  # SMTP port for SSL
    MAIL_USE_TLS = False  # Do not use TLS encryption
    MAIL_USE_SSL = True  # Use SSL encryption for secure communication
    MAIL_USERNAME = '3026678597@qq.com'  # Your email address
    # Your email password (ensure this is kept secure)
    MAIL_PASSWORD = 'bqkgnzhlwqdodeij'
    # Default sender for outgoing emails
    MAIL_DEFAULT_SENDER = ('MelodyHaven', '3026678597@qq.com')

    # Logging configuration
    # Directory for storing log files
    LOG_FOLDER = os.path.join(os.getcwd(), 'logs')
