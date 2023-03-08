from flask import jsonify, session, request
import requests
import pandas as pd
from settings import  NODE_APP
from http import HTTPStatus
from .service import *


def getResults():
    try:
        params= request.get_json()
        validate_file_type(params["file_type"])
        validate_file_name(params["file_name"])

        if not ('token' in session.keys()):
            raise Exception("Login Required")

        url = f'{NODE_APP}/students'
        headers = {"Authorization": f'Bearer {session["token"]}'}
        data = requests.get(url, headers=headers)
        rows = []

        if (data.status_code != 200):
            return jsonify(data.json()), HTTPStatus.BAD_REQUEST

        for student in data.json():
            if (student["results"] != []):
                for result in student["results"]:
                    stud_data = {
                        'student_id': student["_id"],
                        'name': student["name"],
                        'gender': student["gender"],
                        'email': student["email"],
                        'password': student["password"],
                        'role': student["role"],
                        'result_id': result['_id'],
                        'result_exam_name': result['exam_name'],
                        'result_physics': result['physics'],
                        'result_chemistry': result['chemistry'],
                        'result_mathematics': result['mathematics'],
                        'result_biology': result['biology'],
                        'result_status': result['status']
                    }
                    if (result["percentage"]):
                        stud_data["result_total"] = result['total']
                        stud_data["result_percentage"] = result['percentage']
                    rows.append(stud_data)

        df = pd.DataFrame(rows)

        if (params["file_type"] == "excel"):
            df.to_excel(f'{params["file_name"]}.xlsx', index=False)
        if (params["file_type"] == "csv"):
            df.to_csv(f'{params["file_name"]}.csv')

        return jsonify(rows), HTTPStatus.OK
    except Exception as e:
        return jsonify({"Error":str(e)}), HTTPStatus.BAD_REQUEST

