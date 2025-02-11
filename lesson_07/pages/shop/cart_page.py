from selenium.webdriver.common.by import By


class cart_p:

    def __init__(self, driver):
        self._driver = driver

    def next(self):
        self._driver.find_element(
            By.CSS_SELECTOR, '[id="checkout"]').click()
