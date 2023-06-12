from selenium.webdriver.common.by import By


def test_check_exists_button_add_to_cart(browser):

    button = browser.find_element(By.CSS_SELECTOR, '.btn-add-to-basket')
    assert button, 'Button is missing'
