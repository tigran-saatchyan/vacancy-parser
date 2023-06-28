from src.constants import SUPER_JOB_API_SECRET
from src.parser import Parser, ParserMixin


class SuperJobParser(Parser, ParserMixin):
    def __init__(self):
        super().__init__()
        self.keyword = ''
        self.per_page = 20
        self.url = "https://api.superjob.ru/2.0/vacancies/"
        self.headers = {'X-Api-App-Id': SUPER_JOB_API_SECRET}
        self.parameters = {
            'page': 1,
            'count': self.per_page,
            'keywords[0][srws]': 1,
            'keywords[0][skwc]': 'or',
            'keywords[0][keys]': self.keyword
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

            result.extend(response['objects'])
        return result
