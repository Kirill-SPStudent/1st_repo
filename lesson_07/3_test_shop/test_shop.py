from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pages.login_page import login_p
from pages.main_page import main_p
from pages.cart_page import cart_p
from pages.information_page import inf_p
from pages.overview_page import overv_p


def test_form():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager(
        ).install()))
    login = login_p(driver)
    login.log_in()
    main = main_p(driver)
    main.adding_items()
    crt = cart_p
    crt.next()
    inf = inf_p
    inf.input_fistName("Name")
    inf.input_lastName("Last_Name")
    inf.input_postal("Postal")
    inf.to_overview()
    total = overv_p
    total.totl()
