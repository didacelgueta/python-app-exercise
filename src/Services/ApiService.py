from sys import stderr
import requests
import json
<<<<<<< HEAD
=======
import pandas as pd
import datetime as dt

today = dt.datetime.now().strftime("%Y_%m_%d")
>>>>>>> d8928b21302032601f37f056ba1d9a6d2e5ecf59

class ApiService:
    def __init__(self, url):
        self.url = url
<<<<<<< HEAD

    def run(self):
        with requests.session() as session:
            self.response = session.get(self.url)
            self.json_response = json.loads(self.response.text)
=======

    def save_data(self, json):
        df_input = pd.DataFrame.from_dict(json, orient='index')
        df_input.to_csv("./storage/" + today + "_" + str(json['id']) + ".csv", sep=";", header=None)

    def run(self):
        with requests.session() as session:
            response = session.get(self.url)
            json_response = json.loads(response.text)

        for todo in json_response:
            self.save_data(todo)
>>>>>>> d8928b21302032601f37f056ba1d9a6d2e5ecf59
