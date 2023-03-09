import json
from flask import jsonify, request, session, redirect, url_for
import requests
from settings import NODE_APP
from http import HTTPStatus
from time import time
from .service import *


def login():

    params = request.get_json()
    try:
        validate_email(params["email"])
        validate_password(params["password"])

        auth_service = AuthService()

        response=auth_service.login(params["email"],params["password"])

        return jsonify(response), HTTPStatus.OK   

    except Exception as err:
        return jsonify({"Error": str(err)}), HTTPStatus.BAD_REQUEST


def logout():
    if ('token' in session.keys()):
        session.pop("token")
        return jsonify({"message": "Successfully Logged Out"})
    else:
        return jsonify({"message": "Already logged out"})
