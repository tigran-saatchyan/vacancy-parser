import threading
from queue import Queue

from src.file_handler_json import JSONFileHandler
from src.parser_hh import HHParser
from src.parser_superjob import SuperJobParser
from src.vacancy import Vacancy
from src.vacancy_filter import SalaryRangeFilter


def hh_processor(
        keyword, salary_filter,
        min_salary, max_salary, result_queue
):
    hh_parser = HHParser()
    hh_vacancies = hh_parser.parse_vacancies(keyword)
    hh_vacancy_items = hh_vacancies['items']

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
            description=vacancy['snippet']['requirement']
        )
        for vacancy in hh_vacancy_items
    ]

    hh_vacancies_filtered_by_salary = salary_filter.filter_vacancies(
        hh_vacancy_obj_list, min_salary, max_salary
    )

    result_queue.put(hh_vacancies_filtered_by_salary)


def superjob_processor(
        keyword, salary_filter,
        min_salary, max_salary, result_queue
):
    sj_parser = SuperJobParser()
    sj_vacancies = sj_parser.parse_vacancies(keyword)
    sj_vacancy_items = sj_vacancies['objects']

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
        for vacancy in sj_vacancy_items
    ]

    sj_vacancies_filtered_by_salary = salary_filter.filter_vacancies(
        sj_vacancy_obj_list, min_salary, max_salary
    )

    result_queue.put(sj_vacancies_filtered_by_salary)


def print_vacancies(vacancies, platform):
    print('-' * 20, platform, '-' * 20)
    if not vacancies:
        print("No vacancies matching the specified criteria.", end='\n\n')
        return
    for vacancy in vacancies:
        print(vacancy)


def main():
    keyword = 'python'
    min_salary = 10000
    max_salary = None

    salary_filter = SalaryRangeFilter()

    json_handler = JSONFileHandler()

    result_queue = Queue()

    hh_thread = threading.Thread(
        target=(
            hh_processor(
                keyword, salary_filter,
                min_salary, max_salary, result_queue
            )
        )
    )
    sj_thread = threading.Thread(
        target=(
            superjob_processor(
                keyword, salary_filter,
                min_salary, max_salary, result_queue
            )
        )
    )

    hh_thread.start()
    sj_thread.start()

    hh_thread.join()
    sj_thread.join()

    hh_vacancies_filtered_by_salary = result_queue.get()
    sj_vacancies_filtered_by_salary = result_queue.get()

    # print_vacancies(hh_vacancies_filtered_by_salary, 'HH.ru')
    # print_vacancies(sj_vacancies_filtered_by_salary, 'SuperJob.ru')

    all_vacancies = hh_vacancies_filtered_by_salary \
                    + sj_vacancies_filtered_by_salary

    # json_handler.save_all_vacancies_to_json(all_vacancies)

    test_vacancy = Vacancy(
        platform='SuperJob.ru',
        vacancy_id=0000000000,
        title='Pythonist',
        url='https://github.com/tigran-saatchyan',
        salary_from=15000,
        salary_to=20000,
        currency='USD',
        description='Test vacancy'
    )

    json_handler.delete_vacancy_from_json(test_vacancy)

    # vacancies = json_handler.get_vacancy_by_salary_from_json([100000, 300000])


if __name__ == '__main__':
    main()
