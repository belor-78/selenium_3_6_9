import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='firefox',
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default='es',
                     help='Choose language: en, ru, etc')


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption('language')
    browser = None
    if browser_name == "chrome":
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=options)
        print("\nstart chrome browser for test..")
    elif browser_name == "firefox":
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", user_language)
        browser = webdriver.Firefox(firefox_profile=fp)
        print("\nstart firefox browser for test..")
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
<<<<<<< HEAD
    time.sleep(5) # пять секунд хватит
=======
    time.sleep(5) # пяти секунд за глаза хватит
>>>>>>> e09278c613fb32140c30fddf4a7e3bf13312c606
    print("\nquit browser..")
    browser.quit()
