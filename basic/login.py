from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome()


#deklarasi library chrome agar browser berjalan otomatis
# driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://barru.pythonanywhere.com/daftar') #url web yang dituju
time.sleep(2)
driver.find_element_by_id("email").send_keys("barru.kurniawan@gmail.com")
time.sleep(2)
driver.find_element_by_id("password").send_keys("sman60jakarta")
time.sleep(2)
driver.find_element_by_xpath("/html/body/div/div[2]/form/input[3]").click()
time.sleep(2)
