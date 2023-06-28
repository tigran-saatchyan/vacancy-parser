import requests

from src.parser import Parser, ParserMixin


class HHParser(Parser, ParserMixin):

    def __init__(self):
        super().__init__()
        self.keyword = ''
        self.per_page = 20
        self.url = 'https://api.hh.ru/vacancies'
        self.headers = {
            'HHParser-User-Agent': 'Vacant/1.0 (mr.saatchyan@yandex.com)'
        }
        self.parameters = {
            'page': 1,
            'per_page': self.per_page,
            'text': self.keyword
        }

    def parse_vacancies(self, keyword, count):
        result = []
        pages = count // self.per_page + 1 \
            if count % self.per_page else count // self.per_page

        for page in range(1, pages + 1):

            self.parameters.update({'page': page})

            response = self.make_request(
                self.url, self.parameters, self.headers
            )
            result.extend(response['items'])

        return result
