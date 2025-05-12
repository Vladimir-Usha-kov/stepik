
import pytest
from selenium import webdriver

from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='Chrome')
    parser.addoption('--user_language', action='store', default='en')




@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption('browser_name')
    user_language = request.config.getoption('user_language')

    if browser_name == 'Chrome':
        browser = webdriver.Chrome()
        browser.implicitly_wait(5)
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=options)
    else:
        raise pytest.UsageError('choise type cmd --browser_name="your browser"')
    yield browser
    browser.quit()