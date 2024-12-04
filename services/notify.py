import requests


class Notify:

    def __init__(self):
        self.__base_url = 'https://webhook.site'
    
    def send_event(self, data):
        requests.post(
            url=f'{self.__base_url}/8b3b3b7d-1b7d-4b7b-8b7b-3b7b7b7b7b7b',
            json=data
        )
        