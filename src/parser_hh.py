""" Parser implementation for the HH.ru website. """
from src.parser import Parser, ParserMixin


class HHParser(Parser, ParserMixin):
    """
    Parser implementation for the HH.ru website.
    """

    def __init__(self):
        super().__init__()
        self.per_page: int = 20
        self.url: str = 'https://api.hh.ru/vacancies'
        self.headers: dict = {
            'HHParser-User-Agent': 'Vacant/1.0 (mr.saatchyan@yandex.com)'
        }
        self.parameters: dict = {
            'page': 1,
            'per_page': self.per_page,
            'text': '',
            'search_field': 'name'
        }

    def parse_vacancies(self, keyword: str, count: int) -> list[dict]:
        """
        Parses vacancies from the HH.ru website based on the given keyword
        and count.

        Args:
            keyword (str): The keyword to search for.
            count (int): The number of vacancies to retrieve.

        Returns:
            list[dict]: The parsed vacancies.
        """
        self.parameters.update({'text': keyword if keyword else ''})
        result = []
        pages = count // self.per_page + 1 \
            if count % self.per_page else count // self.per_page

        for page in range(0, pages):
            self.parameters.update({'page': page})

            response = self.make_request(
                self.url, self.parameters, self.headers
            )
            result.extend(response['items'])
        return result
