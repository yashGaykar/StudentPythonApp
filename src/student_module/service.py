from http import HTTPStatus
import pandas as pd
from flask import jsonify

from src.utils import RequestsService


class StudentService:

    def __init__(self):
        self.request_service=RequestsService()
        
    def getResults(self,file_name,file_type):

        data=self.request_service.getRequest('/students')

        if (data.status_code != 200):
            raise Exception(data.json())
            
        rows = []
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

        if (file_type == "excel"):
            df.to_excel(f'{file_name}.xlsx', index=False)
        if (file_type == "csv"):
            df.to_csv(f'{file_name}.csv')

        return rows





def validate_file_type(file_type):
    if not (isinstance(file_type, str)):
        raise Exception("File Type must be a String")
    elif file_type not in ['csv','excel']:
        raise Exception("File Type must be csv or excel")

def validate_file_name(file_name):
    if not (isinstance(file_name, str)):
        raise Exception("File Name must be a String")
