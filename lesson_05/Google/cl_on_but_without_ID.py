from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()
                                                ))
driver.get("https://uitestingplayground.com/dynamicid")

driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary").click()

driver.quit()
