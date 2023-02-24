import pytest
from selenium.webdriver.common.by import By


@pytest.mark.parametrize(
    "url",
    [
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/",
    ],
)
def test_check_language(browser, url):
    browser.get(url)
    add_button = browser.find_element(By.XPATH, '//button[@value="Ajouter au panier"]')
    print("add_button.text: ", add_button.text)
    assert add_button.text == "Ajouter au panier"
