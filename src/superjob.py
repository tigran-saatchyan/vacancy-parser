import requests

from src.constants import SUPER_JOB_API_SECRET
from src.engine_abc import Engine


class SuperJob(Engine):
    def get_vacancies(self, keyword):
        parameters = {
            'keywords[0][srws]': 1,
            'keywords[0][skwc]': 'or',
            'keywords[0][keys]': keyword
        }

        url = "https://api.superjob.ru/2.0/vacancies/"

        headers = {
            'X-Api-App-Id': SUPER_JOB_API_SECRET,
        }

        response = requests.get(
            url,
            headers=headers,
            params=parameters
        )

        return response.json()
