from hashlib import new

import xlrd
from selenium import webdriver
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.orangehrm.com/orangehrm-30-day-trial/")
print(driver.title)
driver.maximize_window()
url_domain = driver.find_element_by_id("Form_submitForm_subdomain")
first_name1 = driver.find_element_by_id("Form_submitForm_FirstName")
last_name1 = driver.find_element_by_id("Form_submitForm_LastName")
email_id = driver.find_element_by_id("Form_submitForm_Email")
job_title = driver.find_element_by_id("Form_submitForm_JobTitle")
no_of_emp = driver.find_element_by_id("Form_submitForm_NoOfEmployees")
company_name = driver.find_element_by_id("Form_submitForm_CompanyName")
industry_name = driver.find_element_by_id("Form_submitForm_Industry")
phone_no = driver.find_element_by_id("Form_submitForm_Contact")
country_name = driver.find_element_by_id("Form_submitForm_Country")

industry_nameSelect = Select(industry_name)
country_nameSelect = Select(country_name)

workbook = xlrd.open_workbook("C://Users//santo//Desktop//Wipro_Cadidate_ID//DataSheet.xlsx")
sheet = workbook.sheet_by_name("Sheet1")
rowsCount = sheet.nrows
print(rowsCount)
colsCount = sheet.ncols
print(colsCount)
for curr_row in range(1, rowsCount):
    url = sheet.cell_value(curr_row, 0)
    firstname = sheet.cell_value(curr_row, 1)
    lastname = sheet.cell_value(curr_row, 2)
    email = sheet.cell_value(curr_row, 3)
    title = sheet.cell_value(curr_row, 4)
    employees = sheet.cell_value(curr_row, 5)
    company = sheet.cell_value(curr_row, 6)
    industry = sheet.cell_value(curr_row, 7)
    phone = sheet.cell_value(curr_row, 8)
    country = sheet.cell_value(curr_row, 9)
    print(firstname + " " + lastname + " " + email + " " + title + " " + employees + " " + company + " " + industry + " " + phone + " " + country)

    url_domain.clear()
    url_domain.send_keys(url)
    first_name1.clear()
    first_name1.send_keys(firstname)
    last_name1.clear()
    last_name1.send_keys(lastname)
    email_id.clear()
    email_id.send_keys(email)
    job_title.clear()
    job_title.send_keys(title)
    industry_nameSelect.select_by_visible_text(industry)
    country_nameSelect.select_by_visible_text(country)
    phone_no.clear()
    phone_no.send_keys(phone)

driver.quit()

