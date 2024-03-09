import requests
import json
from abc import ABC, abstractmethod
from project_folder.src.vacancy import *


class GetVacancy(ABC):
    """
    Абстрактный класс для load_data
    """

    @abstractmethod
    def get_vacancy(self, job_name, pages):
        pass


class JSON_read_write(ABC):
    """
    Запись и чтения json файла
    """

    @abstractmethod
    def write_file(self):
        pass

    @abstractmethod
    def read_file(self):
        pass


class HeadHunterAPI(GetVacancy):
    """Класс для подключения к сайту HH.ru"""

    def get_vacancy(self, job_name, pages):
        hh_list = []

        for i in range(pages):
            params = {
                'text': job_name,
                'per_page': '5',
                'page': i
            }

            response = requests.get('https://api.hh.ru/vacancies', params=params)
            response_json = response.json()

            for job in response_json['items']:
                hh_name = job['name']
                hh_city = job['area']['name'] if job['area'] else None
                salary_from = job['salary']['from'] if job['salary'] and job['salary']['from'] else 0
                salary_to = job['salary']['to'] if job['salary'] and 'to' in job['salary'] else 0
                hh_employment = job['employment']['name']
                hh_url = job['alternate_url']

                hh_vacancy = Vacancy(hh_name, hh_city, salary_from, salary_to, hh_employment, hh_url)
                hh_list.append(hh_vacancy)

        return hh_list


class JSON_file:
    """Запись и чтения JSON файла"""

    def __init__(self, file_name="vacancies.json"):
        self.file_name = file_name

    def file_writer(self, data):
        """Запись данных в JSON файл"""
        with open(self.file_name, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    def file_reader(self):
        """Чтение данных из JSON файла"""
        with open(self.file_name, 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data

    def write_vacancies_to_file(self, vacancies):
        """Записывает список вакансий в JSON файл"""
        vacancies_dict = [vacancy.to_dict() for vacancy in vacancies]
        self.file_writer(vacancies_dict)

