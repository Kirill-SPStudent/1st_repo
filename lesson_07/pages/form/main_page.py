from selenium.webdriver.common.by import By


class MainPage():

    def __init__(self, driver):
        self._driver = driver
        self._driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    def input_fstName(self, term):
        self._driver.find_element(
            By.CSS_SELECTOR, '[name="first-name"]').send_keys(term)

    def input_LstName(self, term):
        self._driver.find_element(
            By.CSS_SELECTOR, '[name="last-name"]').send_keys(term)

    def input_adr(self, term):
        self._driver.find_element(
            By.CSS_SELECTOR, '[name="address"]').send_keys(term)

    def input_city(self, term):
        self._driver.find_element(
            By.CSS_SELECTOR, '[name="city"]').send_keys(term)

    def input_cnt(self, term):
        self._driver.find_element(
            By.CSS_SELECTOR, '[name="country"]').send_keys(term)

    def input_mail(self, term):
        self._driver.find_element(
            By.CSS_SELECTOR, '[name="e-mail"]').send_keys(term)

    def input_phn(self, term):
        self._driver.find_element(
            By.CSS_SELECTOR, '[name="phone"]').send_keys(term)

    def input_job(self, term):
        self._driver.find_element(
            By.CSS_SELECTOR, '[name="job-position"]').send_keys(term)

    def input_cmp(self, term):
        self._driver.find_element(
            By.CSS_SELECTOR, '[name="company"]').send_keys(term)

    def button(self):
        self._driver.find_element(
            By.CSS_SELECTOR, "button.btn.btn-outline-primary.mt-3").click()
