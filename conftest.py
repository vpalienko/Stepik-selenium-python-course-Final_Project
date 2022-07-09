import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as Chrome_options
from selenium.webdriver.firefox.options import Options as Firefox_options


def pytest_addoption(parser):
    parser.addoption("--language", action="store", default="en",
                     help="Available language codes: ar, ca, cs, da, de, en-gb, el, es, fi, fr, it, ko, nl, pl, "
                          "pt, pt-br, ro, ru, sk, uk, zh-hans")
    parser.addoption("--browser_name", action="store", default="chrome",
                     help="Choose browser: chrome or firefox")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    language_code = request.config.getoption("language")
    if browser_name == "chrome":
        options = Chrome_options()
        options.add_experimental_option('prefs', {'intl.accept_languages': language_code})
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        options = Firefox_options()
        options.set_preference("intl.accept_languages", language_code)
        browser = webdriver.Firefox(options=options)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    browser.quit()
