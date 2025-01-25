from app.extensions import db, bcrypt


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # Unique username for the user
    username = db.Column(db.String(50), unique=True, nullable=False)
    # Unique email address for the user
    email = db.Column(db.String(100), unique=True, nullable=False)
    # Hashed password for secure authentication
    password_hash = db.Column(db.String(128), nullable=False)
    birth_date = db.Column(db.Date, nullable=True)  # User's date of birth
    gender = db.Column(db.String(10), nullable=True)  # User's gender

    country = db.Column(db.String(100), nullable=True)  # Country of residence
    # First name of the user
    firstname = db.Column(db.String(50), nullable=True)
    lastname = db.Column(db.String(50), nullable=True)  # Last name of the user
    # User's residential address
    address = db.Column(db.String(255), nullable=True)
    phone = db.Column(db.String(20), nullable=True)  # Contact phone number

    # Role of the user (e.g., 'user', 'admin')
    role = db.Column(db.String(50), nullable=False, default='user')

