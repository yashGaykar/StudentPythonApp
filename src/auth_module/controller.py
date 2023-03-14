import json
from flask import jsonify, request, session, redirect, url_for
import requests
from settings import NODE_APP
from http import HTTPStatus
from time import time
from .service import *
from .schema import UserSchema
import logging

# Creating Logger object
logger = logging.getLogger("auth")

def login():
    """User Login"""

    params = request.get_json()

    try:
        logger.info("Validating the Params")
        user_schema = UserSchema()
        errors = user_schema.validate(params)
        if errors:
            raise Exception(errors)
        # validation
        # validate_email(params["email"])
        # validate_password(params["password"])

        # Login Service
        logger.info(f'Logging in with email {params["email"]}')
        response = AuthService.login(params["email"], params["password"])
        logger.info(f'Logged in with email {params["email"]}')
        return jsonify({"message": "Logged in Successfully"}), HTTPStatus.OK

    except KeyError as e:
        return jsonify({"Error": f'{e} is required'}), HTTPStatus.BAD_REQUEST
    except Exception as err:
        logger.error(str(err))
        return jsonify({"Error": str(err)}), HTTPStatus.BAD_REQUEST


def logout():
    """User Logout"""

    if ('token' in session.keys()):
        session.pop("token")
        logger.info("Successfully Logged Out")
        return jsonify({"message": "Successfully Logged Out"})
    else:
        logger.info("Already Logged out")
        return jsonify({"message": "Already logged out"})
