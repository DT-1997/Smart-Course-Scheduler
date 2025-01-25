import random
import string

from datetime import timedelta, datetime, timezone

import pandas as pd
from flask import request, jsonify
from app.extensions import db, mail, bcrypt, create_logger
from app.models import Class
from app.blueprints.auth import auth_bp
from flask_jwt_extended import (create_access_token,
                                jwt_required, get_jwt_identity)
from flask_mail import Message

# Create a logger for the auth module
logger = create_logger('auth', 'logs/auth.log')





