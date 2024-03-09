import pytest
from project_folder.main import VacancyManager

@pytest.fixture
def vacancy_manager():
    return VacancyManager()

def test_get_vacancies_from_hh(monkeypatch, capsys, vacancy_manager):
    # Моделируем ввод данных пользователем
    monkeypatch.setattr('builtins.input', lambda _: 'Software Engineer')
    monkeypatch.setattr('builtins.int', lambda: 2)

    # Проверяем вывод на экран
    vacancy_manager.get_vacancies_from_hh()
    captured = capsys.readouterr()
    assert "Напишите название профессии:" in captured.out
    assert "Сколько страниц вывести?" in captured.out

def test_save_vacancies_to_json(monkeypatch, capsys, vacancy_manager):
    # Моделируем ввод данных пользователем
    monkeypatch.setattr('builtins.input', lambda _: 'да')

    # Проверяем вывод на экран
    vacancy_manager.save_vacancies_to_json(['vacancy1', 'vacancy2'])
    captured = capsys.readouterr()
    assert "Записать, отсортированные по зарплате данные в JSON файл?" in captured.out
    assert "Данные сохранены в JSON файл." in captured.out

# Другие тесты могут быть добавлены для остальных методов класса VacancyManager

