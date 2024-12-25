from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(service=FirefoxService
                           (GeckoDriverManager().install()))

driver.get("http://the-internet.herokuapp.com/entry_ad")
sleep(6)

driver.find_element(By.CSS_SELECTOR, "div.modal-footer").click()
sleep(5)

driver.quit()
