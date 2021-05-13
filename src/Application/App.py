from src.Services.ApiServiceSaveCsv import ApiServiceSaveCsv


class App:
    URL = 'https://jsonplaceholder.typicode.com/todos/'

    def __init__(self):
<<<<<<< HEAD
        self._api_service_save_csv = ApiServiceSaveCsv(self.URL)
=======
        self._api_service = ApiService('https://jsonplaceholder.typicode.com/todos/')
>>>>>>> d8928b21302032601f37f056ba1d9a6d2e5ecf59

    def api_service_save_csv(self) -> ApiServiceSaveCsv:
        return self._api_service_save_csv
