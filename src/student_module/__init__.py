from flask import Blueprint
from .controller import *

# Creating a Blueprint
student_bp = Blueprint(
    'student', __name__, url_prefix='/api/student')

# GET RESULTS
student_bp.add_url_rule(
    '/getResults', 'getResults', getResults, methods=['POST'])

# # UPDATE RESULTS
# student_bp.add_url_rule(
#     '/updateResults', 'updateResults', updateResults, methods=['POST'])