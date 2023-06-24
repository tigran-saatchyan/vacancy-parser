import requests

from src.parser import Parser


class HHParser(Parser):

    def parse_vacancies(self, keyword):
        parameters = {
            'page': 0,
            'per_page': 10,
            'text': keyword
        }

        headers = {
            'HHParser-User-Agent': 'Vacant/1.0 (mr.saatchyan@yandex.com)'
        }

        response = requests.get(
            'https://api.hh.ru/vacancies',
            params=parameters,
            headers=headers
        )

        return response.json()
