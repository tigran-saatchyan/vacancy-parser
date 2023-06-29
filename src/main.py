"""Main app module."""
import os
from typing import List, Dict

from src.constants import FILE_PATH
from src.file_handler_json import JSONFileHandler
from src.parser_hh import HHParser
from src.parser_superjob import SuperJobParser
from src.vacancy import Vacancy
from src.vacancy_filter import SalaryRangeFilter


def hh_processor(
        count: int, word_ro_search: str, salary_filter: SalaryRangeFilter,
        salary_min_max: List[int]
) -> List[Vacancy]:
    """
    Process vacancies from HH.ru.

    Args:
        count (int): The number of vacancies to fetch.
        word_ro_search (str): The keyword to search for in vacancies.
        salary_filter (SalaryRangeFilter): The salary range filter.
        salary_min_max (List[int]): The salary range [min_salary, max_salary]
        for filtering.

    Returns:
        List[Vacancy]: The list of filtered vacancies from HH.ru.
    """
    hh_parser = HHParser()
    hh_vacancies = hh_parser.parse_vacancies(word_ro_search, count)

    hh_vacancy_obj_list = [
        Vacancy(
            platform='HH.ru',
            vacancy_id=vacancy['id'],
            title=vacancy['name'],
            url=vacancy['alternate_url'],
            salary_from=(
                vacancy['salary']['from'] if vacancy['salary'] else None
            ),
            salary_to=(
                vacancy['salary']['to'] if vacancy['salary'] else None
            ),
            currency=(
                vacancy['salary']['currency'] if vacancy['salary'] else None
            ),
            description=vacancy['snippet'][
                'requirement'
            ] if vacancy['snippet'][
                'requirement'
            ] else vacancy['snippet'][
                'responsibility'
            ]
        )
        for vacancy in hh_vacancies
    ]

    if salary_min_max.count(None) == 2:
        return hh_vacancy_obj_list
    else:
        return salary_filter.filter_vacancies(
            hh_vacancy_obj_list, salary_min_max
        )


def superjob_processor(
        count: int, word_ro_search: str, salary_filter: SalaryRangeFilter,
        salary_min_max: List[int | None]
) -> List[Vacancy]:
    """
    Process vacancies from SuperJob.ru.

    Args:
        count (int): The number of vacancies to fetch.
        word_ro_search (str): The keyword to search for in vacancies.
        salary_filter (SalaryRangeFilter): The salary range filter.
        salary_min_max (List[int | None]): The salary range
        [min_salary, max_salary] for filtering.

    Returns:
        List[Vacancy]: The list of filtered vacancies from SuperJob.ru.
    """
    sj_parser = SuperJobParser()
    sj_vacancies = sj_parser.parse_vacancies(word_ro_search, count)

    sj_vacancy_obj_list = [
        Vacancy(
            platform='SuperJob.ru',
            vacancy_id=vacancy['id'],
            title=vacancy['profession'],
            url=vacancy['link'],
            salary_from=vacancy['payment_from'],
            salary_to=vacancy['payment_to'],
            currency=vacancy['currency'],
            description=vacancy['vacancyRichText']
        )
        for vacancy in sj_vacancies
    ]

    if salary_min_max.count(None) == 2:
        return sj_vacancy_obj_list
    else:
        return salary_filter.filter_vacancies(
            sj_vacancy_obj_list, salary_min_max
        )


def print_vacancies(platforms_vacancies: Dict[str, List[Vacancy]]):
    """
    Print the list of vacancies for each platform.

    Args:
        platforms_vacancies (Dict[str, List[Vacancy]]): The dictionary of
        platform and corresponding vacancies.
    """

    for platform, vacancies in platforms_vacancies.items():

        print('\n', '-' * 20, platform, '-' * 20)
        print('-' * 20, len(vacancies), '-' * 20)
        if not vacancies:
            print("No vacancies matching the specified criteria.", end='\n\n')
            continue

        for vacancy in vacancies:
            print(vacancy)


def main(
        selected_platforms: Dict[str, str],
        count: int, word_ro_search: str, salary_min_max: List[int]
) -> Dict[str, List[Vacancy]]:
    """
    The main function to execute the Vacant app.

    Args:
        selected_platforms (List[str]): The list of selected platforms.
        count (int): The number of vacancies to fetch.
        word_ro_search (str): The keyword to search for in vacancies.
        salary_min_max (List[int]): The salary range [min_salary, max_salary]
        for filtering.

    Returns:
        Dict[str, List[Vacancy]]: The dictionary of platform and
        corresponding filtered vacancies.
    """
    salary_filter = SalaryRangeFilter()

    hh_vacancies_filtered = []
    sj_vacancies_filtered = []

    if '1' in selected_platforms:
        hh_vacancies_filtered = hh_processor(
            count, word_ro_search, salary_filter,
            salary_min_max
        )

    if '2' in selected_platforms:
        sj_vacancies_filtered = superjob_processor(
            count, word_ro_search, salary_filter,
            salary_min_max
        )

    return {
        'HH.ru': hh_vacancies_filtered,
        'SuperJob.ru': sj_vacancies_filtered
    }


def user_interface():
    """
    User interface to interact with the Vacant app.
    """
    print('Welcome to Vacant app!')

    json_file_handler = JSONFileHandler()
    file_to_read = 'n'
    if os.path.exists(FILE_PATH):
        file_to_read = input('Do you want to read from file? (y/N): ')

    selected_platforms = {}
    while True:
        platform_selector = ''
        while platform_selector != '3':
            platform_selector = input(
                'Select platforms to search for vacancies: \n'
                '1. HH.ru \n'
                '2. SuperJob.ru \n'
                '3. Next \n'
                '>>> '
            )
            if platform_selector in selected_platforms.keys():
                print('This platform already selected.')
                continue

            if platform_selector == '1':
                selected_platforms['1'] = 'HH.ru'
            elif platform_selector == '2':
                selected_platforms['2'] = 'SuperJob.ru'

        if not selected_platforms:
            print('No platforms selected.')
            to_exit = input('Do you want to quit? (y/N): ')
            if to_exit == 'y':
                print('Exiting...')
                exit()
        else:
            break

    word_to_search = input('Enter keyword to search: ')

    min_salary, max_salary = None, None

    is_filtered = input('Salary range to be filtered? (y/N): ')

    if is_filtered == 'y':
        try:
            min_salary = int(
                input(
                    'Enter min salary (press enter to skip): '
                )
            )
        except ValueError:
            min_salary = None

        try:
            max_salary = int(
                input('Enter max salary (press enter to skip): ')
            )
        except ValueError:
            max_salary = None

    try:
        count = int(
            input(
                'How many vacancies will be shown '
                '(quantity must be divisible by 20)? '
                '(default: 100): '
            )
        )
    except ValueError:
        count = 100

    salary_min_max = [min_salary, max_salary]

    if file_to_read.lower() != 'y':
        all_vacancies = main(
            selected_platforms, count,
            word_to_search, salary_min_max
        )
    else:
        all_vacancies = (
            json_file_handler.load_vacancies_from_json(
                selected_platforms, count,
                word_to_search, salary_min_max
            )
        )

    print_vacancies(all_vacancies)

    if file_to_read.lower() != 'y':
        save_vacancies = input(
            'Do you want to save vacancies to json? (y/N): '
        )

        if save_vacancies == 'y':
            vacancies_to_save = {}
            for platform, vacancies in all_vacancies.items():
                vacancies_to_dict = [
                    vacancy.to_dict() for vacancy in vacancies
                ]
                vacancies_to_save[platform] = vacancies_to_dict
            json_file_handler.save_all_vacancies_to_json(vacancies_to_save)


if __name__ == '__main__':
    user_interface()
