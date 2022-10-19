# import pytest
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# # from selenium.webdriver.chrome.options import Options
#
# browser = None
#
#
# @pytest.fixture(scope='module')
# def browser():
#     global browser
#     chrome_service = Service(executable_path="./chromedriver")
#     # chrome_option = Options()
#     # chrome_option.capabilities = {
#     #     "browserName": "Chrome",
#     #     "browserVersion": "105.0",
#     #     "platformName": "MacOS Big Sur"
#     # }
#     # driver = webdriver.Chrome(service=chrome_service, options=chrome_option)
#     browser = webdriver.Chrome(service=chrome_service)
#     yield browser
#     browser.quit()
#
# # CONFEST.PY có thể dùng để chứa các fixtures - tài nguyên dùng chung cho đầu vào của các test file
# #  - Import các package cần thiết chung 1 lần
# #  - Khởi tạo webdriver session 1 lần
#
# #
