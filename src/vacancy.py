""" Vacancy class module"""


class Vacancy:
    """
    Class representing a job vacancy.
    """

    __slots__ = [
        '_platform',
        '_vacancy_id',
        '_title',
        '_url',
        '_salary_from',
        '_salary_to',
        '_currency',
        '_description',
        '_avg_salary'
    ]

    def __init__(
            self,
            platform: str, vacancy_id: int, title: str, url: str,
            salary_from: int,
            salary_to: int, currency: str, description: str
    ):
        self._platform: str = platform
        self._vacancy_id: int = int(vacancy_id)
        self._title: str = title
        self._url: str = url
        self._salary_from: int = salary_from
        self._salary_to: int = salary_to
        self._currency: str = currency
        self._description: str = (
            description[:200] if len(description) > 200 else description
        ) if description is not None else "Missing description"
        self._avg_salary: int = 0

        if isinstance(salary_from, int):
            if isinstance(salary_to, int):
                self._avg_salary = max(salary_from, salary_to)
            else:
                self._avg_salary = salary_from
        elif isinstance(salary_to, int):
            self._avg_salary = salary_to

    @property
    def title(self) -> str:
        """
        Get the title of the vacancy.

        Returns:
            str: The title of the vacancy.
        """
        return self._title

    @property
    def platform(self) -> str:
        """
        Get the platform of the vacancy.

        Returns:
            str: The platform of the vacancy.
        """
        return self._platform

    @property
    def vacancy_id(self) -> int:
        """
        Get the ID of the vacancy.

        Returns:
            int: The ID of the vacancy.
        """
        return self._vacancy_id

    @property
    def url(self) -> str:
        """
        Get the URL of the vacancy.

        Returns:
            str: The URL of the vacancy.
        """
        return self._url

    @property
    def salary_from(self) -> int:
        """
        Get the starting salary of the vacancy.

        Returns:
            int: The starting salary of the vacancy.
        """
        return self._salary_from

    @property
    def salary_to(self) -> int:
        """
        Get the ending salary of the vacancy.

        Returns:
            int: The ending salary of the vacancy.
        """
        return self._salary_to

    @property
    def description(self) -> str:
        """
        Get the description of the vacancy.

        Returns:
            str: The description of the vacancy.
        """
        return self._description

    @property
    def avg_salary(self) -> int:
        """
        Get the average salary of the vacancy.

        Returns:
            int: The average salary of the vacancy.
        """
        return self._avg_salary

    def to_dict(self) -> dict:
        """
        Convert the vacancy object to a dictionary.

        Returns:
            dict: The vacancy object as a dictionary.
        """
        return {
            'platform': self._platform,
            'vacancy_id': self._vacancy_id,
            'title': self._title,
            'url': self._url,
            'salary_from': self._salary_from,
            'salary_to': self._salary_to,
            'currency': self._currency,
            'description': self._description,
            'avg_salary': self._avg_salary
        }

    def __str__(self):
        """
        Return a string representation of the vacancy.

        Returns:
            str: String representation of the vacancy.
        """
        return (
            f'Platform: {self._platform}\n'
            f'ID: {self._vacancy_id}\n'
            f'Title: {self._title}\n'
            f'Salary: {self._salary_from} {self._currency} - '
            f'{self._salary_to} {self._currency} \n'
            f'Description: {self._description}\n'
            f'Link: {self._url}\n'
            f'___________________________________________________________\n'
        )

    def __repr__(self):
        """
        Return a string representation of the vacancy for debugging purposes.

        Returns:
            str: String representation of the vacancy.
        """
        return (
            f'Vacancy(platform={self._platform}, '
            f'vacancy_id={self._vacancy_id}, '
            f'title={self._title}, '
            f'url={self._url}, '
            f'salary_from={self._salary_from} {self._currency}, '
            f'salary_to={self._salary_to} {self._currency}, '
            f'description={self._description})'
        )

    def __eq__(self, other):
        """
        Compare two vacancies for equality based on average salary.

        Args:
            other (Vacancy): The other vacancy to compare.

        Returns:
            bool: True if the vacancies are equal, False otherwise.
        """
        if isinstance(other, self.__class__):
            return self._avg_salary == other._avg_salary
        return NotImplemented

    def __ne__(self, other):
        """
        Compare two vacancies for inequality based on average salary.

        Args:
            other (Vacancy): The other vacancy to compare.

        Returns:
            bool: True if the vacancies are not equal, False otherwise.
        """
        if isinstance(other, self.__class__):
            return self._avg_salary != other._avg_salary
        return NotImplemented

    def __lt__(self, other):
        """
        Compare two vacancies to check if the current vacancy has a lower average salary.

        Args:
            other (Vacancy): The other vacancy to compare.

        Returns:
            bool: True if the current vacancy has a lower average salary, False otherwise.
        """
        if isinstance(other, self.__class__):
            return self._avg_salary < other._avg_salary
        return NotImplemented

    def __gt__(self, other):
        """
        Compare two vacancies to check if the current vacancy has a higher average salary.

        Args:
            other (Vacancy): The other vacancy to compare.

        Returns:
            bool: True if the current vacancy has a higher average salary, False otherwise.
        """
        if isinstance(other, self.__class__):
            return self._avg_salary > other._avg_salary
        return NotImplemented

    def __le__(self, other):
        """
        Compare two vacancies to check if the current vacancy has a lower or equal average salary.

        Args:
            other (Vacancy): The other vacancy to compare.

        Returns:
            bool: True if the current vacancy has a lower or equal average salary, False otherwise.
        """
        if isinstance(other, self.__class__):
            return self._avg_salary <= other._avg_salary
        return NotImplemented

    def __ge__(self, other):
        """
        Compare two vacancies to check if the current vacancy has a higher or equal average salary.

        Args:
            other (Vacancy): The other vacancy to compare.

        Returns:
            bool: True if the current vacancy has a higher or equal average salary, False otherwise.
        """
        if isinstance(other, self.__class__):
            return self._avg_salary >= other._avg_salary
        return NotImplemented
