from project_folder.data.load_data import HeadHunterAPI
from project_folder.data.load_data import JSON_file

class VacancyManager:
    def __init__(self):
        self.hh_api = HeadHunterAPI()
        self.json_saver = JSON_file()

    def get_vacancies_from_hh(self):
        keyword = input('Напишите название профессии: \n')
        print('Сколько страниц вывести? \n')
        pages = int(input())
        from_hh = self.hh_api.get_vacancy(keyword, pages)
        return from_hh

    def display_vacancies(self, vacancies):
        print('Список вакансий с сайта "HeadHunter": \n')
        for i in vacancies:
            print(i)

    def save_vacancies_to_json(self, vacancies):
        user_answer = input('Записать, отсортированные по зарплате данные в JSON файл? (Да/Нет) \n').lower()
        if user_answer == 'да':
            self.json_saver.add_vacancies(vacancies)
            self.json_saver.sort_vacancies_by_salary()
            self.json_saver.file_writer()
            print('Данные сохранены в JSON файл.')
        else:
            print('Спасибо за использование программы!')

    def run(self):
        vacancies = self.get_vacancies_from_hh()
        self.display_vacancies(vacancies)
        self.save_vacancies_to_json(vacancies)

if __name__ == '__main__':
    manager = VacancyManager()
    manager.run()
