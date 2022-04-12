from selenium import webdriver
import time

driver = webdriver.Chrome()
#deklarasi library chrome agar browser berjalan otomatis

driver.get('https://barru.pythonanywhere.com/daftar') #url web yang dituju
time.sleep(2)
driver.find_element_by_id("email").send_keys("barru.kurniawan@gmail.com")
time.sleep(2)
driver.find_element_by_id("password").send_keys("sman60jakarta")
time.sleep(2)
driver.find_element_by_xpath("/html/body/div/div[2]/form/input[3]").click()
time.sleep(2)


response_message = driver.find_element_by_xpath("/html/body/div[2]/div/div[1]/h2").text
response_data = driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[1]").text
assert "Welcome Barru Kurniawan" in response_message
assert "Anda Berhasil Login" in response_data
driver.close() #menutup chrome web browser