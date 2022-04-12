from selenium import webdriver

driver = webdriver.Chrome()
"""cukup ditulis 1x dalam satu file/project
setiap elemen akan dicek selama 10 detik 
driver.implicitly_wait(10)
"""
driver.get("https://demoqa.com/login")
driver.get("https://demoqa.com/books")
driver.find_element_by_id("login").click()
