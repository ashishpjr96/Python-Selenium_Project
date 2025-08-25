
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="browser selection"
    )

@pytest.fixture(scope="function")
def browserInstance(request):

    browser_name=request.config.getoption("browser_name")

    if browser_name=='chrome':
        driver=webdriver.Chrome()
        driver.maximize_window()
        print(driver.title)
        print(driver.current_url)
        driver.implicitly_wait(4)
    elif browser_name =="firefox":
        driver = webdriver.Firefox()
        print(driver.title)
        print(driver.current_url)
        driver.implicitly_wait(5)

        driver.implicitly_wait(5)
    yield driver
    driver.close()
