import pytest
import time
from selenium import webdriver

@pytest.fixture(scope="function")
def current_driver(request, browser_name1, env_name):
    if browser_name1 == "ch":
        driver = webdriver.Chrome()
    elif browser_name1 == "ff":
        driver = webdriver.Firefox()
    else:
        raise Exception(f"Browser value '{browser_name1}' is not correct or not supported\n"
                        f"please choose '--b ch' or '--br ff'")

    if env_name == "stage":
        url = "https://www.letskodeit.com/practice"
    elif env_name == "qa":
        url = "https://www.letskodeit.com/practice"
    else:
        url = "https://www.letskodeit.com/practice"
        # raise Exception(f"Env value '{env_name}' is not correct or not supported\n"
        #                 f"please choose '--env_stage' or '--env_qa'")

    if request.cls is not None:
        request.cls.driver1 = driver
    driver.maximize_window()

    driver.get(url=url)
    yield driver
    driver.close()
    driver.quit()


def pytest_addoption(parser):
    parser.addoption('--b')
    parser.addoption('--env')


@pytest.fixture(scope="session")
def browser_name1(request):
    value = request.config.getoption('--b')
    print(f"browser name = '{value}'")
    return value


@pytest.fixture(scope="session")
def env_name(request):
    value = request.config.getoption('--env')
    print(f"env name = '{value}'")
    return value


