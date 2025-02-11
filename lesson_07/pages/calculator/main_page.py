from selenium.webdriver.common.by import By


class MainPage():

    def __init__(self, driver):
        self._driver = driver
        self._driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    def waitime(self):
        self._driver.find_element(By.CSS_SELECTOR, '[id="delay"]').clear()
        self._driver.find_element(
            By.CSS_SELECTOR, '[id="delay"]').send_keys("45")

    def calcul(self):
        self._driver.find_element(
            By.XPATH, '//*[@id="calculator"]/div[2]/span[1]').click()
        self._driver.find_element(
            By.XPATH, '//*[@id="calculator"]/div[2]/span[4]').click()
        self._driver.find_element(
            By.XPATH, '//*[@id="calculator"]/div[2]/span[2]').click()
        self._driver.find_element(
            By.XPATH, '//*[@id="calculator"]/div[2]/span[15]').click()
