from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(
    ChromeDriverManager().install()))
driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
# ввод данных
firsr_name = driver.find_element(By.CSS_SELECTOR, '[name="first-name"]')
firsr_name.send_keys("Иван")

last_name = driver.find_element(By.CSS_SELECTOR, '[name="last-name"]')
last_name.send_keys("Петров")

address = driver.find_element(By.CSS_SELECTOR, '[name="address"]')
address.send_keys("Ленина, 55-3")

city = driver.find_element(By.CSS_SELECTOR, '[name="city"]')
city.send_keys("Москва")

сountry = driver.find_element(By.CSS_SELECTOR, '[name="country"]')
сountry.send_keys("Россия")

email = driver.find_element(By.CSS_SELECTOR, '[name="e-mail"]')
email.send_keys("test@skypro.com")

phone = driver.find_element(By.CSS_SELECTOR, '[name="phone"]')
phone.send_keys("+7985899998787")

job = driver.find_element(By.CSS_SELECTOR, '[name="job-position"]')
job.send_keys("QA")

company = driver.find_element(By.CSS_SELECTOR, '[name="company"]')
company.send_keys("SkyPro")

driver.find_element(
    By.CSS_SELECTOR, "button.btn.btn-outline-primary.mt-3").click()
# сравнение цветов элементов
alert_danger_color = "rgba(248, 215, 218, 1)"
color_zip = driver.find_element(
    By.CSS_SELECTOR, '[id="zip-code"]').value_of_css_property(
        "background-color")
assert color_zip == alert_danger_color
print(color_zip)

alert_success_color = "rgba(209, 231, 221, 1)"
fields = [
    firsr_name, last_name, address, city, сountry, email, phone, job, company]
fields = driver.find_element(
    By.CSS_SELECTOR, '[id="last-name"]').value_of_css_property(
        "background-color")
assert fields == alert_success_color

driver.quit()
