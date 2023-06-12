import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Choose language")


@pytest.fixture(scope="function")
def browser(request):
    browser_language = request.config.getoption("language")
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    link = f'http://selenium1py.pythonanywhere.com/{browser_language}/catalogue/coders-at-work_207/'
    print(f'Start link: {link}')
    browser.get(link)
    yield browser
    print("\nquit browser..")
    browser.quit()