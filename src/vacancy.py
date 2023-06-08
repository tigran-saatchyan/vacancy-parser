class Vacancy:

    def __init__(self, title, url, salary_from, salary_to, description):
        self.title = title
        self.url = url
        self.salary_from = salary_from
        self.salary_to = salary_to
        self.description = description
        self.salary = 0

        if isinstance(salary_from, int):
            if isinstance(salary_to, int):
                self.salary = max(salary_from, salary_to)
            else:
                self.salary = salary_from

    def __str__(self):
        return f'Title: {self.title}\n' \
               f'Salary: from - {self.salary_from}, to - {self.salary_to} \n' \
               f'Description: {self.description}\n' \
               f'Link: {self.url}\n' \
               f'___________________________________________________________\n'

    def __repr__(self):
        return f'Vacancy(title={self.title}, url={self.url}, salary_from=' \
               f'{self.salary_from}, salary_to={self.salary_to}, ' \
               f'description={self.description})'

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.salary == other.salary
        return NotImplemented

    def __ne__(self, other):
        if isinstance(other, self.__class__):
            return self.salary != other.salary
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, self.__class__):
            return self.salary < other.salary
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, self.__class__):
            return self.salary > other.salary
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, self.__class__):
            return self.salary <= other.salary
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, self.__class__):
            return self.salary >= other.salary
        return NotImplemented
