from abc import abstractmethod, ABC


class FileHandler(ABC):

    @abstractmethod
    def _add_vacancy(self, vacancy):
        pass

    @abstractmethod
    def _get_vacancy(self, vacancy_id):
        pass

    @abstractmethod
    def _get_all_vacancies(self):
        pass

    @abstractmethod
    def _delete_vacancy(self, vacancy_id):
        pass

    @abstractmethod
    def _get_vacancy_by_salary(self, salary_range):
        pass
