from flask import jsonify, session
import requests

from settings import NODE_APP


class RequestsService:
    def __init__(self):
        self.path= NODE_APP,
        self.headers={"Authorization": f'Bearer {session["token"]}'}
    
    def getRequest(self,url):
        print(self.path)
        return requests.get(self.path[0]+url,headers=self.headers)

    def postRequest(self,url,data):
        return requests.post(self.path[0]+url,headers=self.headers, json=data)

    def putRequest(self,url,data):
        return requests.put(self.path[0]+url,headers=self.headers,json=data)

    def patchRequest(self,url,data):
        return requests.patch(self.path[0]+url,headers=self.headers,json=data)

    def deleteRequest(self,url):
        return requests.delete(self.path[0]+url,headers=self.headers)

    