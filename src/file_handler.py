""" FileHandler abstract class module"""
from abc import ABC, abstractmethod


class FileHandler(ABC):
    """
    An abstract base class for handling file operations.
    """

    @abstractmethod
    def _add_vacancy(self, vacancy):
        """
        Adds a vacancy to the file.

        Args:
            vacancy (dict): The vacancy to be added.

        Returns:
            None
        """
        pass

    @abstractmethod
    def _get_vacancy(self, vacancy_id):
        """
        Retrieves a vacancy from the file based on its ID.

        Args:
            vacancy_id (int): The ID of the vacancy to be retrieved.

        Returns:
            dict: The vacancy with the specified ID.
        """
        pass

    @abstractmethod
    def _load_vacancies(
            self,
            platforms, count,
            word_to_search, salary_min_max
    ):
        """
        Loads vacancies from the file based on certain criteria.

        Args:
            platforms (list): A list of platforms to search for vacancies.
            count (int): The number of vacancies to retrieve.
            word_to_search (str): A word to search for in the vacancy
            description.
            salary_min_max (tuple): A tuple containing the minimum and
            maximum salaries to search for.

        Returns:
            list: A list of vacancies that match the search criteria.
        """
        pass

    @abstractmethod
    def _delete_vacancy(self, vacancy_id):
        """
        Deletes a vacancy from the file based on its ID.

        Args:
            vacancy_id (int): The ID of the vacancy to be deleted.

        Returns:
            None
        """
        pass
