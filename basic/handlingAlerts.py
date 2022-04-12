from selenium import webdriver
import time 
 
driver = webdriver.Chrome()
driver.get("https://demoqa.com/alerts")


# 1. satu tombol
# time.sleep(2)
# driver.find_element_by_id("alertButton").click()

# time.sleep(2)
# driver.switch_to.alert.accept()

# 2. confirm alert
# time.sleep(2)
# driver.find_element_by_id("confirmButton").click()
# time.sleep(2)
# # confirm OK
# # driver.switch_to.alert.accept()

# confirm cancel
# driver.switch_to.alert.dismiss()

# 3. Prompt Alert
time.sleep(2)
driver.find_element_by_id("promtButton").click()
time.sleep(2)
driver.switch_to.alert.send_keys("Quality Assurance")
time.sleep(2)
driver.switch_to.alert.accept()

