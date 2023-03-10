from flask import jsonify, session
import requests

from settings import NODE_APP


class RequestsService:
    def __init__(self):
        """Request service constructor"""
        self.path= NODE_APP,
        self.headers={"Authorization": f'Bearer {session["token"]}'}
    
    def getRequest(self,url):
        """Authenticated GET Request"""
        return requests.get(self.path[0]+url,headers=self.headers)

    def postRequest(self,url,data):
        """Authenticated POST Request"""
        return requests.post(self.path[0]+url,headers=self.headers, json=data)

    def putRequest(self,url,data):
        """Authenticated PUT Request"""

        return requests.put(self.path[0]+url,headers=self.headers,json=data)

    def patchRequest(self,url,data):
        """Authenticated PATCH Request"""
        return requests.patch(self.path[0]+url,headers=self.headers,json=data)

    def deleteRequest(self,url):
        """Authenticated DELETE Request"""
        return requests.delete(self.path[0]+url,headers=self.headers)

    