from webdriver_manager.firefox import GeckoDriverManager
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.utils import ChromeType
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.microsoft import IEDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.google.com")
print(driver.title)
driver.maximize_window()
driver.find_element_by_name("q").send_keys("naveen automationLabs")
time.sleep(6)
driver.quit()
