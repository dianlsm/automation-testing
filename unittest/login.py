from xml.etree.ElementPath import xpath_tokenizer
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from unittest import TestCase

options = webdriver.ChromeOptions()     
options.add_experimental_option('excludeSwitches', ['enable-logging'])
#options.headless =True 
class TestLogin(TestCase):
    def test_login_success(self):
        driver = webdriver.Chrome(executable_path='C:\chromedriver_win32\chromedriver.exe')
        driver.get('https://barru.pythonanywhere.com/daftar')    
        time.sleep(2)
        driver.find_element(By. ID, "email").send_keys("karimun_enam@gmail.com")
        time.sleep(2)
        driver.find_element(By. ID, "password").send_keys("karimun")
        time.sleep(2)
        driver.find_element(By. XPATH, "/html/body/div/div[2]/form/input[3]").click()
        time.sleep(2)
        response_message = driver.find_element(By. XPATH, "/html/body/div[2]/div/div[1]/h2").text
        response_data = driver.find_element(By. XPATH, "/html/body/div[2]/div/div[2]/div[1]").text
        assert("Welcome karimun ditolak" == response_message)
        assert("Anda Berhasil Login" == response_data)

        driver.close()      # menutup chrome web browser

    if __name__ == '__main__':
        TestCase.main()