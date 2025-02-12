from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pages.shop.login_page import login_p
from pages.shop.main_page import main_p
from pages.shop.cart_page import cart_p
from pages.shop.information_page import inf_p
from pages.shop.overview_page import overv_p


def test_form():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager(
        ).install()))
    login = login_p(driver)
    login.log_in()
    main = main_p(driver)
    main.adding_items()
    crt = cart_p(driver)
    crt.next()
    inf = inf_p(driver)
    inf.input_fistName("Name")
    inf.input_lastName("Last_Name")
    inf.input_postal("Postal")
    inf.to_overview()
    total = overv_p(driver)
    total.totl()
