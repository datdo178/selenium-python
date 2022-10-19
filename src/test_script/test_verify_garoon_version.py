import time
import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

browser = None


@pytest.fixture(scope='session', autouse=True)
def browser():
    global browser
    chrome_service = Service(executable_path=ChromeDriverManager().install())
    browser = webdriver.Chrome(service=chrome_service)
    browser = webdriver.Chrome()
    yield browser
    browser.quit()


def login():
    # Data
    username = 'Administrator'
    password = 'cybozu'

    # Locators
    USERNAME_TBX = '//input[@name="_account"]'
    PASSWORD_TBX = '//input[@name="_password"]'
    LOGIN_BTN = '//input[@name="login-submit"]'

    # Input credential and login
    browser.get("http://10.224.152.153/cgi-bin/cbgrn/grn.cgi")
    browser.find_element(By.XPATH, USERNAME_TBX).send_keys(username)
    browser.find_element(By.XPATH, PASSWORD_TBX).send_keys(password)
    browser.find_element(By.XPATH, LOGIN_BTN).click()


def verify_garoon_version_at_footer(url):
    # Data
    expected_version = '5.16.0'

    # Locators
    FOOTER = '//div[@class="credit"]/small'

    browser.get(url)
    time.sleep(2)
    footer_text = browser.find_element(By.XPATH, FOOTER).text

    assert expected_version in str(footer_text)


def test_case_1():
    # Data
    garoon_base_url = 'http://10.224.152.153/cgi-bin/cbgrn/grn.cgi/'
    personal_setting_url = garoon_base_url + 'personal/application_list?'
    system_setting_url = garoon_base_url + 'system/index?'
    end_user_url = garoon_base_url + 'index?'

    print('Login')
    login()

    print('Verify Garoon version at screen: "personal system"')
    verify_garoon_version_at_footer(personal_setting_url)

    print('Verify Garoon version at screen: "system setting"')
    verify_garoon_version_at_footer(system_setting_url)

    print('Verify Garoon version at screen: "end user (index page)"')
    verify_garoon_version_at_footer(end_user_url)
