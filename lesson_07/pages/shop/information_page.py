from selenium.webdriver.common.by import By


class inf_p:

    def __init__(self, driver):
        self._driver = driver

    def input_fistName(self, term):
        self._driver.find_element(
            By.CSS_SELECTOR, '[id="first-name"]').send_keys(term)

    def input_lastName(self, term):
        self._driver.find_element(
            By.CSS_SELECTOR, '[id="last-name"]').send_keys(term)

    def input_postal(self, term):
        self._driver.find_element(
            By.CSS_SELECTOR, '[id="postal-code"]').send_keys(term)

    def to_overview(self):
        self._driver.find_element(By.CSS_SELECTOR, '[id="continue"]').click()
