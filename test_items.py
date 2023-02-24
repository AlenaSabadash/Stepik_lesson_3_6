import pytest
from selenium.webdriver.common.by import By


@pytest.mark.parametrize(
    "url",
    [
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/",
    ],
)
def test_is_add_button_enabled(browser, url):
    browser.get(url)
    add_button = browser.find_element(By.CLASS_NAME, "btn-add-to-basket").is_enabled()
    assert add_button is True
