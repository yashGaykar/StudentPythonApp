import json
from flask import jsonify, request, session, redirect, url_for
import requests
from settings import ACCESS_TOKEN, NODE_APP
from http import HTTPStatus
from time import time

def login():

    params = request.get_json()
    try:
        if ('token' in session.keys()):
            session.pop('token')
        
        url = f'{NODE_APP}/admin/login'
        data = ({"email": params["email"], "password": params["password"]})
        response = requests.post(url, json=data)
        if response.status_code == 200:
            token = response.json()['token']
            session['token'] = token
            return jsonify({"message": "Logged In Succesfully"}), HTTPStatus.OK
        else:
            raise Exception(response.json()["message"])
    except Exception as err:
        # print(response)
        return jsonify({"Error": err}), HTTPStatus.BAD_REQUEST


def logout():
    if ('token' in session.keys()):
        session.pop("token")
        return jsonify({"message":"Successfully Logged Out"})
    else:
        return jsonify({"message":"Already logged out"})
