import os
from selene import browser, have, by, be
from selene.support.conditions import be as sbe  # импортируем нужные условия

# Функция для получения абсолютного пути к картинке
def get_image_path(image_name):
    # Получаем абсолютный путь к картинке
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(current_dir, image_name)

# Тест
def test_automation_practice_form():
    # Открываем форму с использованием относительного пути
    browser.open('/automation-practice-form')

    # Удаляем баннеры, если они есть
    browser.driver.execute_script("$('#fixedban').remove()")
    browser.driver.execute_script("$('footer').remove()")

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
    browser.element('#uploadPicture').send_keys(image_path)

    # Заполняем текущий адрес
    browser.element('#currentAddress').type('Moscow, Russia')

    # Заполняем поля State и City
    browser.element('#state').click()
    browser.element('#state').element(by.text("NCR")).click()  # Выбираем "NCR"
    browser.element('#city').click()
    browser.element('#city').element(by.text("Delhi")).click()  # Выбираем "Delhi"

    # Отправляем форму
    browser.element('#submit').click()

    # Проверка, что данные отображаются в модальном окне
    # Дожидаемся появления модального окна
    browser.element('.modal-dialog').should(sbe.visible)

    # Проверка каждого поля
    browser.element('.modal-body').should(have.text('Evgeniy'))
    browser.element('.modal-body').should(have.text('Student'))
    browser.element('.modal-body').should(have.text('Stud_Evg@example.com'))
    browser.element('.modal-body').should(have.text('9321217654'))
    browser.element('.modal-body').should(have.text('2000'))
    browser.element('.modal-body').should(have.text('June'))
    browser.element('.modal-body').should(have.text('15'))
    browser.element('.modal-body').should(have.text('Moscow, Russia'))
    browser.element('.modal-body').should(have.text('NCR'))
    browser.element('.modal-body').should(have.text('Delhi'))