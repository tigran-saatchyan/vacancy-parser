## Vacancy Parser Project

The vacancy parser terminal app is a software tool designed to extract job postings from the websites hh.ru and superjob.ru, focusing on specific criteria defined by the user. This application enables users to gather relevant job information quickly and efficiently.

Here's a brief overview of how the vacancy parser terminal app works:

- User Input: The user provides specific criteria, such as job title, location, salary range, or any other relevant filters.

- Data Retrieval: The app utilizes web scraping techniques to extract job listings from hh.ru and superjob.ru based on the provided criteria. It navigates through the websites' pages, collects the relevant information, and saves it for further processing.

- Data Parsing: The extracted job data, such as job title, company name, location, salary, and description, is parsed and organized into a structured format for easy access and manipulation.

- Filtering and Sorting: The app applies the user-defined criteria to filter and sort the parsed job data. For example, it can exclude certain job titles or locations that don't match the user's preferences, sort jobs by salary range, or prioritize specific companies.

- Presentation: The filtered and sorted job listings are presented to the user in a clear and concise manner, typically in a terminal interface. The user can view the relevant details of each job, such as the job title, company name, location, and salary, facilitating easy comparison and decision-making.

- Additional Actions: Depending on the app's capabilities, users may have options to save or export the filtered job listings for future reference, apply directly through the app, or perform additional actions like sending job details via email or integrating with other tools.

Overall, the vacancy parser terminal app simplifies the process of searching and analyzing job postings on hh.ru and superjob.ru by allowing users to define specific criteria and quickly access relevant job information in a structured format, saving time and effort in the job search process.

## Prerequisites

Make sure you have the following installed on your system:

- Python (version 3.10.6+)
- [Poetry (version 1.5.1)](https://python-poetry.org/docs/)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/tigran-saatchyan/vacancy-parser
   ```

2. Navigate to the project directory:

   ```bash
   cd vacancy-parser
   ```

3. Install the project dependencies using Poetry:

   ```bash
   poetry install
   ```

## Usage

1. Run the console app using Poetry:

   ```bash
   poetry run python src/main.py
   ```

2. Follow the prompts or provide the necessary command-line arguments to interact with the app.

## Additional Notes

- Make sure you have valid API credentials or any other required configurations set up before running the app.
- Customize the functionality of the app by modifying the `main.py` file according to your project's requirements.

## Contributing

If you'd like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch.
3. Make your changes and commit them.
4. Push your changes to your forked repository.
5. Submit a pull request.

## License

This project is licensed under the [MIT License](https://github.com/tigran-saatchyan/vacancy-parser/blob/develop/LICENSE).

## Links
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/tigran-o-saatchyan/)