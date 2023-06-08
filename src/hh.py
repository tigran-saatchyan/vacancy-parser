import requests

from src.engine_abc import Engine


class HH(Engine):

    def get_vacancies(self, keyword):
        parameters = {
            'page': 0,
            'per_page': 10,
            'text': keyword
        }

        headers = {
            'HH-User-Agent': 'VacanSer/1.0 (mr.saatchyan@yandex.com)'
        }

        response = requests.get(
            'https://api.hh.ru/vacancies',
            params=parameters,
            headers=headers
        )

        return response.json()
