import allure
from selenium import webdriver
from lesson_07.pages.ShopPage import ShopPage


@allure.id("Internet_mag")
@allure.epic("Интернет магазин")
@allure.severity("blocker")
@allure.story("Покупка товаров")
@allure.feature("CREATE")
@allure.title("Выбор товара, работа с корзиной и оплата")
@allure.suite("Тесты на работу с интернет-магазином")
def test_purpage():
    with allure.step("Открытие страницы веб-браузера"):
        driver = webdriver.Chrome()
    with allure.step("Создание переменной,"
                     " которая хранит экзампляр класса InternetMagPage"):
        pur_page = ShopPage(driver)

    price = pur_page.autorization()
    pur_page.add_product()
    pur_page.shopping_cart_and_checkout()
    pur_page.form_of_payment("Name", "Last_Name", "Postal")
    total_price = pur_page.total_price()
    with allure.step("Проверить,что ожидаемая и фактическая стоимость равны"):
        assert price == total_price
