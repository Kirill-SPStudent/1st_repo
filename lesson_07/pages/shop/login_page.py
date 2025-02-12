from selenium.webdriver.common.by import By


class login_p:

    def __init__(self, driver):
        self._driver = driver
        self._driver.get("https://www.saucedemo.com/")

    def log_in(self):
        self._driver.find_element(
            By.CSS_SELECTOR, '[id="user-name"]').send_keys("standard_user")
        self._driver.find_element(
            By.CSS_SELECTOR, '[id="password"]').send_keys("secret_sauce")
        self._driver.find_element(
            By.CSS_SELECTOR, '[id="login-button"]').click()
