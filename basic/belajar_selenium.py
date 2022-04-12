# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
# import time


# # driver = webdriver.Chrome(ChromeDriverManager().install())      # deklarasi library chrome agar browser berjalan otomatis
# # driver.get('https://barru.pythonanywhere.com/daftar')       # url web yang dituju
# # time.sleep(5)       # delay 5 detik
# # driver.close()      # menutup chrome web browser


# # //*[@id="email"]  --> XPATH itu copy id saja
# # /html/body/div/div[2]/form/input[1] --> full XPATH itu copy path keseluruhan

# # deklarasi library chrome agar browser berjalan otomatis
# driver = webdriver.Chrome(ChromeDriverManager().install())
# driver.get('https://barru.pythonanywhere.com/daftar')    # url web yang dituju
# time.sleep(2)
# # -------------------form email //*[@id="email"]
# driver.find_element_by_id("email").send_keys("karimun_enam@gmail.com")
# time.sleep(2)
# # -------------------form password //*[@id="password"]
# driver.find_element_by_id("password").send_keys("karimun")
# time.sleep(2)
# # -------------------button sign in /html/body/div/div[2]/form/input[3]
# driver.find_element_by_xpath("/html/body/div/div[2]/form/input[3]").click()
# time.sleep(2)

# # ---------------------------- Validation response
# # /html/body/div[2]/div/div[1]/h2
# response_message = driver.find_element_by_xpath("/html/body/div[2]/div/div[1]/h2").text
# # /html/body/div[2]/div/div[2]/div[1]
# response_data = driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[1]").text
# assert("Welcome karimun ditolak" == response_message)
# assert("Anda Berhasil Login" == response_data)

# driver.close()      # menutup chrome web browser
