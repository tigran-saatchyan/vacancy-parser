from abc import ABC, abstractmethod

import requests


class Parser(ABC):

    __slots__ = (
        'keyword',
        'url',
        'headers',
        'per_page',
        'parameters'
    )

    @abstractmethod
    def parse_vacancies(self, keyword, count):
        pass


class ParserMixin:
    @staticmethod
    def make_request(url, parameters, headers):
        return requests.get(
            url,
            params=parameters,
            headers=headers
        ).json()
