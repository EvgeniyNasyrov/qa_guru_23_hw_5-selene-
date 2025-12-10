import os
from selene import browser, have, by, be

# Функция для получения абсолютного пути к картинке
def get_image_path(image_name):
    # Получаем абсолютный путь к картинке
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(current_dir, image_name)

# Тест
def test_automation_practice_form():
    # Открываем страницу
    browser.open('https://demoqa.com/automation-practice-form')

    # Заполняем личные данные
    browser.element('#firstName').type('Evgeniy')
    browser.element('#lastName').type('Student')
    browser.element('#userEmail').type('Stud_Evg@example.com')
    browser.element('label[for="gender-radio-1"]').click()
    browser.element('#userNumber').type('9321217654')

    # Устанавливаем дату рождения
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__year-select').click()
    browser.element('.react-datepicker__year-select').element(by.text("2000")).click()
    browser.element('.react-datepicker__month-select').click()
    browser.element('.react-datepicker__month-select').element(by.text("June")).click()
    browser.element('.react-datepicker__day--015').click()

    # Загрузка изображения (с использованием функции для получения пути)
    image_path = get_image_path('test.jpg')
    browser.element('#uploadPicture').send_keys(image_path)  # Путь к картинке

    # Заполняем текущий адрес
    browser.element('#currentAddress').type('Moscow, Russia')

    # Проверка, что First Name заполнено
    browser.element('#firstName').should(have.value('Evgeniy'))