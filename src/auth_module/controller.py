import json
from flask import jsonify, request, session, redirect, url_for
import requests
from settings import NODE_APP
from http import HTTPStatus
from time import time
from .service import *
from .schema import UserSchema


def login():
    """User Login"""

    params = request.get_json()

    try:
        user_schema = UserSchema()
        errors = user_schema.validate(params)
        if errors:
            return {"errors": errors}, HTTPStatus.BAD_REQUEST

        # validation
        # validate_email(params["email"])
        # validate_password(params["password"])

        # Login Service
        response = AuthService.login(params["email"], params["password"])

        return jsonify({"message": "Logged in Successfully"}), HTTPStatus.OK

    except KeyError as e:
        return jsonify({"Error": f'{e} is required'}), HTTPStatus.BAD_REQUEST
    except Exception as err:
        return jsonify({"Error": str(err)}), HTTPStatus.BAD_REQUEST


def logout():
    """User Logout"""

    if ('token' in session.keys()):
        session.pop("token")
        return jsonify({"message": "Successfully Logged Out"})
    else:
        return jsonify({"message": "Already logged out"})
