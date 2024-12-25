from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()
                                                ))
driver.get("http://the-internet.herokuapp.com/add_remove_elements/")
for x in range(1, 6):
    driver.find_element(By.CSS_SELECTOR, "button").click()

delete = driver.find_elements(By.CSS_SELECTOR, "button.added-manually")
print(len(delete))

driver.quit()
