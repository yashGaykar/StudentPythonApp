from flask import Flask, jsonify, make_response
from settings import JWT_SECRET_KEY
from .auth_module import auth_bp
from .student_module import student_bp


app = Flask(__name__)


app.secret_key=JWT_SECRET_KEY

# Registers the Blueprints
app.register_blueprint(auth_bp)
app.register_blueprint(student_bp)


@app.route('/')
def hello1():
    """DEMO ROUTE"""
    return jsonify("Hello")