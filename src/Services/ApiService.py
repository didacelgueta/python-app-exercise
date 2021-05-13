from sys import stderr
import requests
import json

class ApiService:
    def __init__(self, url):
        self.url = url

    def run(self):
        with requests.session() as session:
            self.response = session.get(self.url)
            self.json_response = json.loads(self.response.text)
