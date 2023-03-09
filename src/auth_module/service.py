import re
from flask import jsonify, request, session, redirect, url_for
import requests
from http import HTTPStatus

from settings import NODE_APP

from ..utils import RequestsService


class AuthService:
    """Auth Services"""

    def login(email,password):
        """Function to start a session with a token"""
        
        if ('token' in session.keys()):
            session.pop('token')
        
        data = ({"email": email, "password": password})
        response = requests.post(f'{NODE_APP}/admin/login', json=data)

        if response.status_code == 200:
            token = response.json()['token']
            session['token'] = token
            return response.json()

        else:
            raise Exception(response.json()["message"])

def validate_email(email):
    if not (isinstance(email, str)):
        raise Exception("Email must be a String")


def validate_password(password):
    if not (isinstance(password, str)):
        raise Exception("Password must be a String")
    elif not (re.search("^(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z])(?=.*[*.!@$%^&(){}[]:;<>,.?/~_+-=|\]).{8,32}$", password)):
        raise Exception("Password must contain one number,capital_alphabet, small_alphabet,and a special character")
