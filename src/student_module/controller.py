from flask import jsonify, session, request
import requests
import pandas as pd
from settings import NODE_APP
from http import HTTPStatus
from .service import *
from .schema import ExportResultsSchema
import logging


# Creating Logger object
logger = logging.getLogger("student")


def getResults():
    try:
        params = request.get_json()
        logger.info("Validating the Params")

        export_results_schema = ExportResultsSchema()
        errors = export_results_schema.validate(params)
        if errors:
            raise Exception(errors)

        # validate_file_type(params["file_type"])
        # validate_file_name(params["file_name"])

        if not ('token' in session.keys()):
            raise Exception("Login Required")

        student_service = StudentService()

        """Function creates file and return results"""
        response = student_service.getResults(
            params["file_name"], params["file_type"])
        
        logger.info(f'Records has been saved in {params["file_name"]}.{params["file_type"]}')
        return jsonify(response), HTTPStatus.OK

    except KeyError as e:
        return jsonify({"Error": f'{e} is required'}), HTTPStatus.BAD_REQUEST

    except Exception as e:
        logger.error(str(e))
        return jsonify({"Error": str(e)}), HTTPStatus.BAD_REQUEST
