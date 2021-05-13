from sys import stderr
import requests
import json
import pandas as pd
import datetime as dt

today = dt.datetime.now().strftime("%Y_%m_%d")

class ApiService:
    def __init__(self, url):
        self.url = url

    def save_data(self, json):
        df_input = pd.DataFrame.from_dict(json, orient='index')
        df_input.to_csv("./storage/" + today + "_" + str(json['id']) + ".csv", sep=";", header=None)

    def run(self):
        with requests.session() as session:
            response = session.get(self.url)
            json_response = json.loads(response.text)

        for todo in json_response:
            self.save_data(todo)
