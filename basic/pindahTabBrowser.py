from selenium import webdriver
import time 

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/windows")

time.sleep(3)
driver.find_element_by_link_text("Click Here").click()
time.sleep(3)
driver.switch_to.window(driver.window_handles[0])
time.sleep(3)
driver.find_element_by_link_text("Click Here").click()
time.sleep(3)
driver.switch_to.window(driver.window_handles[0])




