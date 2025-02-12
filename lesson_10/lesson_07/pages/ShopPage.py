import allure
from selenium.webdriver.common.by import By


class ShopPage:
    """"Этот класс пердставляет страницу веб-магазина.
    Авторизованный пользователь может выбрать вещи,
    посомтреть окончательную сумму покупки и оплатить ее"""

    def __init__(self, driver):
        self.driver = driver
        self.driver.get('https://www.saucedemo.com/')
        self.driver.implicitly_wait(5)

    @allure.step("Авторизация пользователя")
    def autorization(self):
        self.driver.find_element(By.ID, "user-name").send_keys("standard_user")
        self.driver.find_element(By.ID, "password").send_keys("secret_sauce")
        self.driver.find_element(By.ID, "login-button").click()

    @allure.step("Добавление товаров в корзину")
    def add_product(self):
        self.driver.find_element(
            By.ID, "add-to-cart-sauce-labs-backpack").click()
        self.driver.find_element(
            By.ID, "add-to-cart-sauce-labs-onesie").click()
        self.driver.find_element(
            By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()

    @allure.step("переход в корзину и оформление покупки")
    def shopping_cart_and_checkout(self):
        self.driver.find_element(By.ID, "shopping_cart_container").click()
        self.driver.find_element(By.ID, "checkout").click()

    @allure.step("заполнение формы оплаты")
    def form_of_payment(self, name: str, last_name: str, index: int):
        self.driver.find_element(By.ID, "first-name").send_keys(name)
        self.driver.find_element(By.ID, "last-name").send_keys(last_name)
        self.driver.find_element(By.ID, "postal-code").send_keys(index)
        self.driver.find_element(By.ID, "continue").click()

    @allure.step("окончательная цена покупик")
    def total_price(self):
        self.driver.find_element(
            By.CLASS_NAME, "summary_total_label").get_attribute("textContent")

    @allure.step("закрытие браузера")
    def close(self):
        self.driver.find_element(
            By.CSS_SELECTOR, "#finish").click()
        self.driver.quit()
