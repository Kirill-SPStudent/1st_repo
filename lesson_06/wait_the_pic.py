from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(
    ChromeDriverManager().install()))
driver.implicitly_wait(20)
driver.get(
    "https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

pic = driver.find_element(By.CSS_SELECTOR, ("#award")).get_attribute("src")
print(pic)

driver.quit
