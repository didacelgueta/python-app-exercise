from src.Services.ApiService import ApiService
import pandas as pd
import datetime as dt


class ApiServiceSaveCsv(ApiService):
    DELIMITER = ";"

    def run(self):
        super().run()
        for todo in self.json_response:
            self.save_data(todo)

        print("Task done!")

    def generate_file_name(self, json):
        today = dt.datetime.now().strftime("%Y_%m_%d")
        return "./storage/" + today + "_" + str(json['id']) + ".csv"

    def save_data(self, json):
        df_input = pd.DataFrame.from_dict(json, orient='index')
        df_input.to_csv(self.generate_file_name(json), sep=self.DELIMITER, header=None)
