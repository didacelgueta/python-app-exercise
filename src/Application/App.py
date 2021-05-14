from src.Services.ApiServiceSaveCsv import ApiServiceSaveCsv


class App:
    URL = 'https://jsonplaceholder.typicode.com/todos/'

    def __init__(self):
        self._api_service_save_csv = ApiServiceSaveCsv(self.URL)

    def api_service_save_csv(self) -> ApiServiceSaveCsv:
        return self._api_service_save_csv
