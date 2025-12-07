import time
from selene import browser, by, be, have
from selenium.webdriver.common.keys import Keys

# Базовая конфигурация Selene
browser.config.base_url = 'https://demoqa.com/'
browser.config.timeout = 20

from pathlib import Path

def test_automation_practice_form():

    # Открываем страницу
    browser.open('automation-practice-form')

    # Вводим данные в форму
    browser.element('#firstName').type('Evgeniy')
    browser.element('#lastName').type('Student')
    browser.element('#userEmail').type('Stud_Evg@example.com')
    browser.element('label[for="gender-radio-1"]').click()
    browser.element('#userNumber').type('9321217654')

    # Работа с календариком даты рождения
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__year-select').click()
    browser.element('.react-datepicker__year-select option[value="2000"]').click()
    browser.element('.react-datepicker__month-select').click()
    browser.element('.react-datepicker__month-select option[value="05"]').click()
    browser.element(by.xpath("//div[@aria-label='Choose Tuesday, June 20th, 2000']")).click()


    # Выбираем предметы
    browser.element('#subjectsInput').type('Computer Science').press(Keys.ENTER)

    # Ставим галочку на хобби
    browser.element('label[for="hobbies-checkbox-1"]').click()

    browser.element('#uploadPicture').send_keys('./test.jpg')

    # Вводим адрес
    browser.element('#currentAddress').type('Москва, Красная площадь, д. 1')

    # Выбираем State и City
    browser.element('#state').click()
    browser.element('#react-select-3-input').type('NCR').press(Keys.ENTER)
    browser.element('#city').click()
    browser.element('#react-select-4-input').type('Delhi').press(Keys.ENTER)

    # Отправляем форму
    browser.element('#submit').click()

    # Проверяем успешную отправку
    browser.element('#example-modal-sizes-title-lg').should(be.visible)
    browser.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))

    # Проверяем данные в таблице
    rows = {
        'Student Name': 'Evgeniy Student',
        'Student Email': 'Stud_Evg@example.com',
        'Gender': 'Male',
        'Mobile': '9321217654',
        'Date of Birth': '20 June,2000',
        'Subjects': 'Computer Science',
        'Hobbies': 'Sports',
        'Picture': 'test.jpg',
        'Address': 'Москва, Красная площадь, д. 1',
        'State and City': 'NCR Delhi'
    }

    for key, value in rows.items():
        cell_value = browser.element(f'//td[normalize-space()="{key}"]/following-sibling::td')
        cell_value.should(have.exact_text(value))

    print("Форма успешно отправлена и проверена!")

if __name__ == "__main__":
    test_automation_practice_form()
    time.sleep(5)
    browser.quit()