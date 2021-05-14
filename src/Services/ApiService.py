from sys import stderr
import requests
import json
import pandas as pd
import datetime as dt

today = dt.datetime.now().strftime("%Y_%m_%d")

class ApiService:
    def __init__(self, url):
        self.url = url

    def run(self):
        with requests.session() as session:
            self.response = session.get(self.url)
            self.json_response = json.loads(self.response.text)
