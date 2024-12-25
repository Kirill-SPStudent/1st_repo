from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(service=FirefoxService
                           (GeckoDriverManager().install()))

driver.get("http://the-internet.herokuapp.com/login")
driver.find_element(By.CSS_SELECTOR, "[type=text]").send_keys("tomsmith")
driver.find_element(By.CSS_SELECTOR, "[type=password]").send_keys(
    "SuperSecretPassword")
driver.find_element(By.CSS_SELECTOR, "[type=submit]").click

driver.quit()
