import pytest
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_google_search_selenium(driver):
    driver.get("https://google.com/")

    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys('selene_github')
    search_box.send_keys(Keys.ENTER)

    expected_text = 'yashaka/selene: User-oriented Web UI browser tests in ...'

    h3_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(By.TAG_NAME, 'h3'))

    assert h3_element.text == expected_text


    #driver.find_element(By.NAME, "q").send_keys("selenium")

def test_google_search_selene():
    pass

