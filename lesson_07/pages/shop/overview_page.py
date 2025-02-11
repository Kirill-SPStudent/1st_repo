from selenium.webdriver.common.by import By


class overv_p:

    def __init__(self, driver):
        self._driver = driver

    def totl(self):
        total = self._driver.find_element(
            By.CSS_SELECTOR, 'div.summary_total_label').text
        assert total == "Total: $58.29"
