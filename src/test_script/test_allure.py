import time
import allure


from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium import webdriver


def test_allure():
    with allure.step('Init browser driver'):
        service = Service(executable_path=ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)

    with allure.step('Open url'):
        driver.get('https://google.com')
        time.sleep(2)

    with allure.step('Quit browser driver')
        driver.quit()

