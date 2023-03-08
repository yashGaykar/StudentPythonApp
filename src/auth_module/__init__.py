from flask import Blueprint
from .controller import *

# Creating a Blueprint
auth_bp = Blueprint(
    'auth', __name__, url_prefix='/api/auth')

# Login
auth_bp.add_url_rule(
    '/login', 'login', login, methods=['POST'])

# # Logout
# auth_bp.add_url_rule(
#     '/logout', 'logout', logout, methods=['POST'])
