from selenium.webdriver.common.by import By


class main_p:

    def __init__(self, driver):
        self._driver = driver

    def adding_items(self):
        self._driver.find_element(
            By.CSS_SELECTOR, '[id="add-to-cart-sauce-labs-backpack"]').click()
        self._driver.find_element(
            By.CSS_SELECTOR,
            '[id="add-to-cart-sauce-labs-bolt-t-shirt"]').click()
        self._driver.find_element(
            By.CSS_SELECTOR, '[id="add-to-cart-sauce-labs-onesie"]').click()
        self._driver.find_element(
            By.CSS_SELECTOR, 'a.shopping_cart_link').click()
