from src.file_handler_json import JSONFileHandler
from src.parser_hh import HHParser
from src.parser_superjob import SuperJobParser
from src.vacancy import Vacancy
from src.vacancy_filter import SalaryRangeFilter


def hh_processor(
        count, word_ro_search, salary_filter,
        salary_min_max
):
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
        count, word_ro_search, salary_filter,
        salary_min_max
):
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


def print_vacancies(platforms_vacancies):

    for platform, vacancies in platforms_vacancies.items():
        print('-' * 20, platform, '-' * 20)
        print('-' * 20, len(vacancies), '-' * 20)
        if not vacancies:
            print(
                "No vacancies matching the specified criteria.", end='\n\n'
            )
            continue

        for vacancy in vacancies:
            print(vacancy)


def main(selected_platforms, count, word_ro_search, salary_min_max):
    salary_filter = SalaryRangeFilter()

    json_handler = JSONFileHandler()

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
    print('Welcome to Vacant app!')
    selected_platforms = []

    while True:
        platform_selector = 0
        while platform_selector != '3':
            platform_selector = input(
                'Select platforms to search for vacancies: \n'
                '1. HH.ru \n'
                '2. SuperJob.ru \n'
                '3. Next \n'
                '>>> '
            )
            if platform_selector in selected_platforms:
                print('This platform already selected.')
                continue

            if (
                    platform_selector in ['1', '2']
            ) and (
                    platform_selector not in selected_platforms
            ):
                selected_platforms.append(platform_selector)

        if not selected_platforms:
            print('No platforms selected.')
            is_to_exit = input('Do you want to quit? (y/N): ')
            if is_to_exit == 'y':
                print('Exiting...')
                exit()
        else:
            break

    word_to_search = input('Enter keyword to search: ')

    min_salary, max_salary = None, None

    is_filtered = input('Salary range to be filtered? (y/N): ')

    if is_filtered == 'y':
        try:
            min_salary = int(input('Enter min salary (press enter to skip): '))
        except ValueError:
            min_salary = None

        try:
            max_salary = int(input('Enter max salary (press enter to skip): '))
        except ValueError:
            max_salary = None

    count = (
            int(
                input(
                    'How many vacancies will be shown '
                    '(quantity must be divisible by 20)? '
                    '(default: 100): '
                )
            ) or 100
    )

    salary_min_max = [min_salary, max_salary]

    all_vacancies = main(
        selected_platforms, count,
        word_to_search, salary_min_max
    )

    print_vacancies(all_vacancies)


if __name__ == '__main__':
    user_interface()
