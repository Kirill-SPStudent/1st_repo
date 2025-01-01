from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(service=FirefoxService
                           (GeckoDriverManager().install()))

driver.get("http://the-internet.herokuapp.com/inputs")
number = driver.find_element(By.CSS_SELECTOR, "[type=number]")
number.send_keys("1000")
number.clear()
number.send_keys("999")
driver.quit()
