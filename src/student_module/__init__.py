from flask import Blueprint
from .controller import *

# Creating a Blueprint
student_bp = Blueprint(
    'student', __name__, url_prefix='/api/student')

# Get Results in excel or csv
student_bp.add_url_rule(
    '/getResults', 'getResults', getResults, methods=['POST'])

