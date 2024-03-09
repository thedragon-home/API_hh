from dataclasses import dataclass

@dataclass
class Vacancy:
    """
    Информация о вакансии
    """

    vacancy_name: str
    city: str
    salary_from: int
    salary_to: int
    employment: str
    url: str

    def __str__(self):
        return f'название вакансии: {self.vacancy_name}\n' \
               f'город: {self.city}\n' \
               f'зарплата от: {self.salary_from}\n' \
               f'зарплата до: {self.salary_to}\n' \
               f'тип занятости: {self.employment}\n' \
               f'ссылка на вакансию: {self.url}\n'

    def to_dict(self):
        """
        Возвращает вакансию в виде словаря
        """
        return self.__dict__

    @staticmethod
    def from_dict(vacancy_dict):
        """Возвращает вакансию из словаря"""
        return Vacancy(**vacancy_dict)



@dataclass
class Vacancies:
    """Обработка списка вакансий"""

    all_vacancies: list

    def __init__(self):
        self.all_vacancies = []

    def add_vacancies(self, new_vacancies):
        self.all_vacancies += new_vacancies

    def delete_vacancies(self, old_vacancies):
        for i in old_vacancies:
            self.all_vacancies.remove(i)

    def sort_vacancies_by_salary(self):
        self.all_vacancies.sort(reverse=True)

    def to_list_dict(self):
        return [vacancy.to_dict() for vacancy in self.all_vacancies]
