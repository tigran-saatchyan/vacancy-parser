from abc import ABC, abstractmethod


class Parser(ABC):

    @abstractmethod
    def parse_vacancies(self, keyword):
        pass
