from selenium import webdriver
from selenium.webdriver.common.by import By
import pyautogui
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

# alamat 1
# driver.get("https://demoqa.com/upload-download")

# alamat 2
driver.get("https://gofile.io/uploadFiles")

# cara 1
# driver.find_element_by_id("uploadFile").send_keys("C:/Users/dianl/Desktop/Application.pdf")

# cara 2
driver.find_element(By.XPATH,'//*[@id="rowUploadButton"]/div/div/div/div/div/div[1]/div/button').click()
time.sleep(3)
pyautogui.write(r"C:\Users\dianl\Desktop\Application.pdf")
pyautogui.press("enter")

