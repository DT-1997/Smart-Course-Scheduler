from app.blueprints.algorithm import algorithm_bp

import pandas as pd
from flask import request, jsonify
from app.extensions import db, create_logger
from app.models import Class, Department, Teacher, Classroom, TeachingBuilding, Course, ScheduleTask, MajorDirection, Major



# Create a logger for the load module
logger = create_logger('upload', 'logs/upload.log')


"""例子"""
# @algorithm_bp.route('/', methods=['GET', 'POST'])
# def index():