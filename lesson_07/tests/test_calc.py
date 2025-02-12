from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pages.calculator.main_page import MainPage
from pages.calculator.result_page import resultPage


def test_form():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager(
        ).install()))
    main = MainPage(driver)
    main.waitime()
    main.calcul()
    resu = resultPage(driver)
    resu.resss()
    driver.quit()
