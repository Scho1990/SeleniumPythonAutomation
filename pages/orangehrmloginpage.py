from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://opensource-demo.orangehrmlive.com/")
print(driver.title)
driver.maximize_window()
driver.find_element_by_name("q").send_keys("naveen automationLabs")
time.sleep(6)
driver.quit()
