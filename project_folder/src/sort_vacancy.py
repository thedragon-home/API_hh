from abc import ABC, abstractmethod
import json


with open('../data/vacancies.json', 'r', encoding='utf-8') as file:
    data_file = json.load(file)


class AbstractVacancySorter(ABC):
    @abstractmethod
    def sort_by_city(self, city):
        pass

    @abstractmethod
    def sort_by_salary(self, salary):
        pass

    @abstractmethod
    def sort_by_keyword(self, keyword):
        pass


class VacancySorter(AbstractVacancySorter):
    def __init__(self, vacancies_file):
        with open(vacancies_file, 'r', encoding='utf-8') as file:
            self.vacancies = json.load(file)

    def sort_by_city(self, city):
        return [vacancy for vacancy in self.vacancies if vacancy['area']['name'] == city]

    def sort_by_salary(self, salary):
        return [vacancy for vacancy in self.vacancies if vacancy.salary >= salary]

    def sort_by_keyword(self, keyword):
        return [vacancy for vacancy in self.vacancies if keyword in vacancy.description]


