import os
import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--language", default="fr")
    parser.addoption("--drivers", default=os.path.expanduser("~/Downloads/chromedriver_mac_arm64_1"))


@pytest.fixture
def base_url(request):
    return request.config.getoption("--url")


@pytest.fixture
def browser(request):
    drivers = request.config.getoption("--drivers")
    language = request.config.getoption("--language")
    options = webdriver.ChromeOptions()
    options.add_experimental_option("prefs", {f"intl.accept_languages": f"{language}"})
    driver = webdriver.Chrome(executable_path=os.path.join(drivers, "chromedriver"), options=options)

    def fin():
        driver.quit()

    request.addfinalizer(fin)

    return driver
