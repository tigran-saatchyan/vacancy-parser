""" Vacancy filter module"""
from abc import ABC, abstractmethod
from typing import List

from src.vacancy import Vacancy


class VacancyFilter(ABC):
    @abstractmethod
    def filter_vacancies(
            self,
            vacancies: List[Vacancy],
            salary_range: List[int]
    ) -> List[Vacancy]:
        """
        Abstract method to filter vacancies based on a salary range.

        Args:
            vacancies (List[Vacancy]): The list of vacancies to filter.
            salary_range (List[int]): The salary range [min_salary, max_salary] to filter the vacancies.

        Returns:
            List[Vacancy]: The filtered list of vacancies.
        """
        pass


class SalaryRangeFilter(VacancyFilter):
    def filter_vacancies(
            self, vacancies: List[Vacancy], salary_range: List[int]
    ) -> List[Vacancy]:
        """
        Filter vacancies based on a salary range.

        Args:
            vacancies (List[Vacancy]): The list of vacancies to filter.
            salary_range (List[int]): The salary range [min_salary, max_salary] to filter the vacancies.

        Returns:
            List[Vacancy]: The filtered list of vacancies.
        """
        min_salary, max_salary = salary_range
        filtered_vacancies = []

        for vacancy in vacancies:
            if vacancy.avg_salary == 0:
                continue
            if min_salary is not None and vacancy.avg_salary <= min_salary:
                continue
            if max_salary is not None and vacancy.avg_salary >= max_salary:
                continue
            filtered_vacancies.append(vacancy)
        return filtered_vacancies
