# from string import ascii_lowercase
import pytest
from flask import json
import requests
# from random import randint
# import random



class TestGetResults:

    @classmethod
    def setup_class(self):
        global url
        url = "http://localhost:5000/api/student/getResults"
        global data
        data = {"file_type":"csv","file_name":"students_list1"}


    def test_file_type_not_a_string(self):
        dict=data.copy()
        dict["file_type"]=88
        response=requests.post(url,json=dict)
        assert response.status_code == 400
        assert response.json() == {"Error": "{'file_type': ['Not a valid string.']}"}

    def test_file_type_invalid(self):
        dict=data.copy()
        dict["file_type"]="csvd"
        response=requests.post(url,json=dict)
        assert response.status_code == 400
        assert response.json() == {"Error": "{'file_type': ['Invalid value.']}"}

    def test_file_name_not_a_string(self):
        dict=data.copy()
        dict["file_name"]=88
        response=requests.post(url,json=dict)
        assert response.status_code == 400
        assert response.json() == {"Error": "{'file_name': ['Not a valid string.']}"}

    def test_login_required(self):
        dict=data.copy()
        requests.post("http://localhost:5000/api/auth/logout")
        response=requests.post(url,json=dict)
        assert response.status_code == 400
        assert response.json() == {"Error": "Login Required"}


    # def test_permission_denied(self):
    #     dict=data.copy()
    #     response=requests.post(url,json=dict)
    #     assert response.status_code == 400
    #     assert response.json() == {"error": f"Invalid Instance Id"}
