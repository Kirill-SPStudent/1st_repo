from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(
    ChromeDriverManager().install()))
driver.get("https://www.saucedemo.com/")
# регистрация
driver.find_element(
    By.CSS_SELECTOR, '[id="user-name"]').send_keys("standard_user")
driver.find_element(
    By.CSS_SELECTOR, '[id="password"]').send_keys("secret_sauce")
driver.find_element(By.CSS_SELECTOR, '[id="login-button"]').click()
# товары
driver.find_element(
    By.CSS_SELECTOR, '[id="add-to-cart-sauce-labs-backpack"]').click()
driver.find_element(
    By.CSS_SELECTOR, '[id="add-to-cart-sauce-labs-bolt-t-shirt"]').click()
driver.find_element(
    By.CSS_SELECTOR, '[id="add-to-cart-sauce-labs-onesie"]').click()
driver.find_element(By.CSS_SELECTOR, 'a.shopping_cart_link').click()
# корзина
driver.find_element(By.CSS_SELECTOR, '[id="checkout"]').click()
# форма с данными
driver.find_element(
    By.CSS_SELECTOR, '[id="first-name"]').send_keys("имя")
driver.find_element(
    By.CSS_SELECTOR, '[id="last-name"]').send_keys("фамилия")
driver.find_element(
    By.CSS_SELECTOR, '[id="postal-code"]').send_keys("почтовый индекс")
driver.find_element(By.CSS_SELECTOR, '[id="continue"]').click()
# переход к оплате
total = driver.find_element(By.CSS_SELECTOR, 'div.summary_total_label').text
assert total == "Total: $58.29"

driver.quit()
