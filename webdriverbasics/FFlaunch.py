from selenium import webdriver
import time

driver=webdriver.Firefox(executable_path='F:\\geckodriver-v0.26.0-win64\\geckodriver.exe')
driver.get('https://www.google.com')
print(driver.title)
driver.maximize_window()
driver.find_element_by_name("q").send_keys("naveen automationLabs")
time.sleep(6)
driver.quit()