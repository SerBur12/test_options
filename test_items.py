from selenium.webdriver.common.by import By


def test_check_exists(browser):
    browser.find_element(By.CSS_SELECTOR, '.btn-add-to-basket')
