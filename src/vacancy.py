from abc import ABC, abstractmethod


class Vacancy(ABC):

    @abstractmethod
    def get_vacancies(self):
        pass
