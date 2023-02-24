import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--language", default="fr")


@pytest.fixture
def base_url(request):
    return request.config.getoption("--url")


@pytest.fixture
def browser(request):
    language = request.config.getoption("--language")
    options = webdriver.ChromeOptions()
    options.add_experimental_option("prefs", {"intl.accept_languages": language})
    driver = webdriver.Chrome(options=options)

    def fin():
        driver.quit()

    request.addfinalizer(fin)

    return driver
