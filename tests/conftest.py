import pytest
from selene import browser


@pytest.fixture(scope="session", autouse=True)
def configure_browser():
    # Настройка браузера
    browser.config.window_height = 1000
    browser.config.window_width = 1200
    browser.config.browser_name = 'chrome'  # Используем Chrome

    # Открываем страницу
    browser.open('https://demoqa.com/automation-practice-form')

    # Возвращаем контроль в тест
    yield

    # Закрываем браузер после завершения всех тестов
    browser.quit()