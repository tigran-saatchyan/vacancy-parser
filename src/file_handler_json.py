"""
This class handles the JSON files containing vacancies.
"""

import json
from json import JSONDecodeError
from typing import List, Dict, Any

from src.constants import FILE_PATH
from src.file_handler import FileHandler
from src.vacancy import Vacancy
from src.vacancy_filter import SalaryRangeFilter


class JSONFileHandler(FileHandler):
    """
    A class that handles JSON files containing vacancies.
    """

    __file_path: str = FILE_PATH
    __data = []

    @classmethod
    def _read_file(cls, file_path: str) -> None:
        """
        Reads the JSON file and loads the data.

        Args:
            file_path (str): The path of the JSON file.

        Returns:
            None
        """
        try:
            with open(file_path, 'r') as f:
                cls.__data = json.load(f)
        except FileNotFoundError:
            print(f'File {file_path} not found, new file created')
            cls._save_file(cls.__data, cls.__file_path)
        except JSONDecodeError:
            print(f'File {file_path} is not valid JSON')

    @classmethod
    def _save_file(
            cls, data: List[Dict[str, Any]], file_path: str = FILE_PATH
    ) -> None:
        """
        Saves the data to a JSON file.

        Args:
            data (List[Dict[str, Any]]): The data to be saved.
            file_path (str): The path of the JSON file.

        Returns:
            None
        """
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    def _add_vacancy(self, vacancy: Vacancy) -> None:
        """
        Adds a vacancy to the JSON data.

        Args:
            vacancy (Vacancy): The vacancy object to be added.

        Returns:
            None
        """
        self._read_file(self.__file_path)
        self.__data.append(vacancy.to_dict())
        self._save_file(self.__data, self.__file_path)

    def _get_vacancy(self, vacancy_id: int) -> Dict[str, Any]:
        """
        Retrieves a vacancy from the JSON data based on the vacancy ID.

        Args:
            vacancy_id (int): The ID of the vacancy to retrieve.

        Returns:
            Dict[str, Any]: The vacancy data.
        """
        self._read_file(self.__file_path)
        return self.__data[vacancy_id]

    def _delete_vacancy(self, vacancy: Vacancy) -> None:
        """
        Deletes a vacancy from the JSON data.

        Args:
            vacancy (Vacancy): The vacancy object to be deleted.

        Returns:
            None
        """
        self._read_file(self.__file_path)
        try:
            self.__data.remove(vacancy.to_dict())
        except ValueError:
            print(f'Vacancy "{vacancy.title}" not found')
        self._save_file(self.__data, self.__file_path)

    def _load_vacancies(
            self,
            platforms, count,
            word_to_search, salary_min_max
    ):
        """
        Loads vacancies from the JSON data based on the given parameters.

        Args:
            platforms:
            count:
            word_to_search:
            salary_min_max:

        Returns:
            result (Dict): The loaded vacancies filtered by the given
            parameters.
        """
        self._read_file(self.__file_path)

        result = {}
        for platform, vacancies in self.__data.items():
            vacancies_obj_list = [
                Vacancy(
                    platform=vacancy['platform'],
                    vacancy_id=vacancy['vacancy_id'],
                    title=vacancy['title'],
                    url=vacancy['url'],
                    salary_from=vacancy['salary_from'],
                    salary_to=vacancy['salary_to'],
                    currency=vacancy['currency'],
                    description=vacancy['description']
                ) for vacancy in vacancies
            ]
            salary_filter = SalaryRangeFilter()
            vacancies_filtered = salary_filter.filter_vacancies(
                vacancies_obj_list, salary_min_max
            )
            result[platform] = vacancies_filtered
        return result

    def load_vacancies_from_json(
            self,
            platforms, count,
            word_to_search, salary_min_max
    ):
        """
        Loads vacancies from the JSON data based on the given parameters.

        Args:
            platforms:
            count:
            word_to_search:
            salary_min_max:

        Returns:
            result (Dict): The loaded vacancies filtered by the
            given parameters.
        """
        return self._load_vacancies(
            platforms, count,
            word_to_search, salary_min_max
        )

    def save_all_vacancies_to_json(self, vacancies) -> None:
        """
        Saves all the vacancies to the JSON file.

        Args:
            vacancies: The vacancies to be saved.

        Returns:
            None
        """
        self._save_file(vacancies)

    def add_vacancy_to_json(self, vacancy: Vacancy) -> None:
        """
        Adds a vacancy to the JSON data.

        Args:
            vacancy (Vacancy): The vacancy object to be added.

        Returns:
            None
        """
        self._add_vacancy(vacancy)

    def get_vacancy_from_json(self, vacancy_id: int) -> Dict[str, Any]:
        """
        Retrieves a vacancy from the JSON data based on the vacancy ID.

        Args:
            vacancy_id (int): The ID of the vacancy to retrieve.

        Returns:
            Dict[str, Any]: The vacancy data.
        """
        return self._get_vacancy(vacancy_id)

    def delete_vacancy_from_json(self, vacancy: Vacancy) -> None:
        """
        Deletes a vacancy from the JSON data.

        Args:
            vacancy (Vacancy): The vacancy object to be deleted.

        Returns:
            None
        """
        self._delete_vacancy(vacancy)
