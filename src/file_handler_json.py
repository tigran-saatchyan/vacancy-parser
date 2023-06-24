""" This class handles the JSON files containing vacancies."""
import json
from json import JSONDecodeError
from typing import List, Dict, Any, Union

from src.file_handler import FileHandler
from src.vacancy import Vacancy


class JSONFileHandler(FileHandler):
    """A class for handling JSON files containing vacancies."""

    __file_path: str = 'vacancies.json'
    __data: List[Dict[str, Any]] = []

    def __init__(self) -> None:
        self._read_file(self.__file_path)

    @classmethod
    def _read_file(cls, file_path: str) -> None:
        """Reads the JSON file and loads the data into memory.

        Args:
            file_path (str): The path to the JSON file.

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
    def _save_file(cls, data: List[Dict[str, Any]], file_path: str) -> None:
        """Saves the data to the JSON file.

        Args:
            data (List[Dict[str, Any]]): The data to be saved.
            file_path (str): The path to the JSON file.

        """
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    def _add_vacancy(self, vacancy: Vacancy) -> None:
        """Adds a vacancy to the JSON file.

        Args:
            vacancy (Vacancy): The vacancy to be added.

        """
        self._read_file(self.__file_path)
        self.__data.append(vacancy.to_dict())
        self._save_file(self.__data, self.__file_path)

    def _get_vacancy(self, vacancy_id: int) -> Dict[str, Any]:
        """Retrieves a vacancy from the JSON file based on its ID.

        Args:
            vacancy_id (int): The ID of the vacancy.

        Returns:
            Dict[str, Any]: The vacancy data.

        """
        self._read_file(self.__file_path)
        return self.__data[vacancy_id]

    def _get_all_vacancies(self) -> List[Dict[str, Any]]:
        """Retrieves all vacancies from the JSON file.

        Returns:
            List[Dict[str, Any]]: The list of vacancies.

        """
        self._read_file(self.__file_path)
        return self.__data

    def _delete_vacancy(self, vacancy: Vacancy) -> None:
        """Deletes a vacancy from the JSON file based on its ID.

        Args:
            vacancy (Vacancy): The ID of the vacancy to be deleted.

        """
        self._read_file(self.__file_path)
        try:
            self.__data.remove(vacancy.to_dict())
        except ValueError:
            print(f'Vacancy "{vacancy.title}" not found')
        self._save_file(self.__data, self.__file_path)

    def _get_vacancy_by_salary(
            self, salary_range: List[Union[int, float]]
    ) -> List[Dict[str, Any]]:
        """Retrieves vacancies from the JSON file based on a salary range.

        Args:
            salary_range (List[Union[int, float]]): The salary
            range [min, max].

        Returns:
            List[Dict[str, Any]]: The list of vacancies within the
            specified salary range.

        """
        self._read_file(self.__file_path)
        vacancies = []
        for vacancy in self.__data:
            if salary_range[0] <= vacancy['avg_salary'] <= salary_range[1]:
                vacancies.append(vacancy)
        return vacancies

    def __save_all(self, vacancies: List[Vacancy]) -> None:
        """Saves all vacancies to the JSON file.

        Args:
            vacancies (List[Vacancy]): The list of vacancies to be saved.

        """
        new_vacancies = []
        for vacancy in vacancies:
            new_vacancies.append(vacancy.to_dict())
        self._save_file(new_vacancies, self.__file_path)

    def save_all_vacancies_to_json(self, vacancies: List[Vacancy]) -> None:
        """Saves all vacancies to the JSON file.

        Args:
            vacancies (List[Vacancy]): The list of vacancies to be saved.

        """
        self.__save_all(vacancies)

    def add_vacancy_to_json(self, vacancy: Vacancy) -> None:
        """Adds a vacancy to the JSON file.

        Args:
            vacancy (Vacancy): The vacancy to be added.

        """
        self._add_vacancy(vacancy)

    def get_vacancy_from_json(self, vacancy_id: int) -> Dict[str, Any]:
        """Retrieves a vacancy from the JSON file based on its ID.

        Args:
            vacancy_id (int): The ID of the vacancy.

        Returns:
            Dict[str, Any]: The vacancy data.

        """
        return self._get_vacancy(vacancy_id)

    def get_all_vacancies_from_json(self) -> List[Dict[str, Any]]:
        """Retrieves all vacancies from the JSON file.

        Returns:
            List[Dict[str, Any]]: The list of vacancies.

        """
        return self._get_all_vacancies()

    def delete_vacancy_from_json(self, vacancy: Vacancy) -> None:
        """Deletes a vacancy from the JSON file based on its ID.

        Args:
            vacancy (Vacancy): The ID of the vacancy to be deleted.

        """
        self._delete_vacancy(vacancy)

    def get_vacancy_by_salary_from_json(
            self,
            salary_range: List[Union[int, float]]
    ) -> List[Dict[str, Any]]:
        """Retrieves vacancies from the JSON file based on a salary range.

        Args:
            salary_range (List[Union[int, float]]): The salary
            range [min, max].

        Returns:
            List[Dict[str, Any]]: The list of vacancies within the
            specified salary range.

        """
        return self._get_vacancy_by_salary(salary_range)
