""" Parser implementation for the SuperJob website. """
from src.constants import SUPER_JOB_API_SECRET
from src.parser import Parser, ParserMixin


class SuperJobParser(Parser, ParserMixin):
    """
    Parser implementation for the SuperJob website.
    """

    def __init__(self):
        super().__init__()
        self.per_page: int = 20
        self.url: str = "https://api.superjob.ru/2.0/vacancies/"
        self.headers: dict = {'X-Api-App-Id': SUPER_JOB_API_SECRET}
        self.parameters: dict = {
            'page': 1,
            'count': self.per_page,
            'keywords[0][srws]': 1,
            'keywords[0][skwc]': 'or',
            'keywords[0][keys]': ''
        }

    def parse_vacancies(self, keyword: str, count: int) -> list[dict]:
        """
        Parses vacancies from the SuperJob website based on the given keyword
        and count.

        Args:
            keyword (str): The keyword to search for.
            count (int): The number of vacancies to retrieve.

        Returns:
            list[dict]: The parsed vacancies.
        """

        self.parameters.update(
            {'keywords[0][keys]': keyword if keyword else ''}
        )
        result = []
        pages = count // self.per_page + 1 \
            if count % self.per_page else count // self.per_page

        for page in range(0, pages):
            self.parameters.update({'page': page})

            response = self.make_request(
                self.url, self.parameters, self.headers
            )
            result.extend(response['objects'])
        return result
