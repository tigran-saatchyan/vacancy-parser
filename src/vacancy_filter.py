from abc import ABC, abstractmethod


class VacancyFilter(ABC):
    @abstractmethod
    def filter_vacancies(self, vacancies, min_salary, max_salary):
        pass


class SalaryRangeFilter(VacancyFilter):
    def filter_vacancies(self, vacancies, min_salary, max_salary):
        filtered_vacancies = []
        for vacancy in vacancies:
            if vacancy.avg_salary == 0:
                continue
            if min_salary is not None and vacancy.avg_salary < min_salary:
                continue
            if max_salary is not None and vacancy.avg_salary > max_salary:
                continue
            filtered_vacancies.append(vacancy)
        return filtered_vacancies
