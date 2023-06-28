class Vacancy:
    __slots__ = [
        '_platform',
        '_id',
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
            platform, vacancy_id, title, url, salary_from,
            salary_to, currency, description
    ):
        self._platform: str = platform
        self._id: int = int(vacancy_id)
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
        return self._title

    @property
    def url(self) -> str:
        return self._url

    @property
    def salary_from(self) -> int:
        return self._salary_from

    @property
    def salary_to(self) -> int:
        return self._salary_to

    @property
    def description(self) -> str:
        return self._description

    @property
    def avg_salary(self) -> int:
        return self._avg_salary

    def to_dict(self) -> dict:
        return {
            'platform': self._platform,
            'id': self._id,
            'title': self._title,
            'url': self._url,
            'salary_from': self._salary_from,
            'salary_to': self._salary_to,
            'currency': self._currency,
            'description': self._description,
            'avg_salary': self._avg_salary
        }

    def __str__(self):
        return (
            f'Platform: {self._platform}\n'
            f'ID: {self._id}\n'
            f'Title: {self._title}\n'
            f'Salary: {self._salary_from} {self._currency} - '
            f'{self._salary_to} {self._currency} \n'
            f'Description: {self._description}\n'
            f'Link: {self._url}\n'
            f'___________________________________________________________\n'
        )

    def __repr__(self):
        return (
            f'Vacancy(platform={self._platform}, '
            f'id={self._id}, '
            f'title={self._title}, '
            f'url={self._url}, '
            f'salary_from={self._salary_from} {self._currency.upper()}, '
            f'salary_to={self._salary_to} {self._currency.upper()}, '
            f'description={self._description})'
        )

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self._avg_salary == other._avg_salary
        return NotImplemented

    def __ne__(self, other):
        if isinstance(other, self.__class__):
            return self._avg_salary != other._avg_salary
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, self.__class__):
            return self._avg_salary < other._avg_salary
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, self.__class__):
            return self._avg_salary > other._avg_salary
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, self.__class__):
            return self._avg_salary <= other._avg_salary
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, self.__class__):
            return self._avg_salary >= other._avg_salary
        return NotImplemented
