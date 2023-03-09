from flask import jsonify, session, request
import requests
import pandas as pd
from settings import NODE_APP
from http import HTTPStatus
from .service import *


def getResults():
    try:
        params = request.get_json()
        validate_file_type(params["file_type"])
        validate_file_name(params["file_name"])

        if not ('token' in session.keys()):
            raise Exception("Login Required")

        student_service = StudentService()
        response = student_service.getResults(
            params["file_name"], params["file_type"])
       

        return jsonify(response), HTTPStatus.OK
    except Exception as e:
        return jsonify({"Error": str(e)}), HTTPStatus.BAD_REQUEST
