from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pages.main_page import MainPage
from pages.result_page import resultPage


def test_form():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager(
        ).install()))
    main = MainPage(driver)
    main.waitime()
    main.calcul()
    resu = resultPage
    resu.resss()
    driver.quit()
