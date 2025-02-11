from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class resultPage:
    def __init__(self, driver):
        self._driver = driver

    def resss(self):
        waiter = WebDriverWait(self._driver, 45)
        waiter.until(EC.text_to_be_present_in_element((
            By.CSS_SELECTOR, "div.screen"), "15"))
        res = self._driver.find_element(By.CSS_SELECTOR, "div.screen").text
        assert res == "15"
