from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pages.main_page import MainPage
from pages.result_page import Res_page


def test_form():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager(
        ).install()))
    Main_p = MainPage(driver)
    Main_p.input_fstName("Иван")
    Main_p.input_LstName("Петров")
    Main_p.input_adr("Ленина, 55-3")
    Main_p.input_city("Москва")
    Main_p.input_cnt("Россия")
    Main_p.input_mail("test@skypro.com")
    Main_p.input_phn("+7985899998787")
    Main_p.input_job("QA")
    Main_p.input_cmp("SkyPro")
    Main_p.button()
    result_p = Res_page(driver)
    result_p.dang_color()
    result_p.suc_color()
    driver.quit()
