# from string import ascii_lowercase
import pytest
from flask import json
import requests
# from random import randint
# import random


class TestLogin:

    @classmethod
    def setup_class(self):
        global url
        url = "http://localhost:5000/api/auth/login"
        global data
        data = {
            "email": "yash@gmail.com",
            "password": "yash@123"
        }

    # @classmethod
    # def teardown_class(self):
        

    def test_email_not_a_string(self):
        dict = data.copy()
        dict["email"]=88
        response = requests.post(url, json=dict)
        assert response.status_code == 400
        assert response.json() == {"Error": "{'email': ['Not a valid email address.']}"}

    def test_password_invalid(self):
        dict = data.copy()
        dict["password"]=88
        response = requests.post(url, json=dict)
        assert response.status_code == 400
        assert response.json() == {"Error": "{'password': ['Not a valid string.']}"}

    def test_auth_failed(self):
        dict = data.copy()
        dict["password"]="yash"
        response = requests.post(url, json=dict)
        assert response.status_code == 400
        assert response.json() == {"Error": "Auth Failed"}

    def test_successful_login(self):
        dict = data.copy()
        response = requests.post(url, json=dict)
        assert response.status_code == 200
        assert response.json() == {"message": "Logged in Successfully"}
