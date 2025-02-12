from selenium.webdriver.common.by import By


class Res_page:

    def __init__(self, driver):
        self._driver = driver

    def dang_color(self):
        alert_danger_color = "rgba(248, 215, 218, 1)"
        color_zip = self._driver.find_element(
            By.CSS_SELECTOR, '[id="zip-code"]').value_of_css_property(
                "background-color")
        assert color_zip == alert_danger_color
        print(color_zip)

    def suc_color(self):
        alert_success_color = "rgba(209, 231, 221, 1)"
        fields = self._driver.find_element(
            By.CSS_SELECTOR, '[id="last-name"]').value_of_css_property(
                "background-color")
        assert fields == alert_success_color
