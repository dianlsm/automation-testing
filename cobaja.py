
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

s = Service('C:/chromedriver_win32/chromedriver.exe')
driver = webdriver.Chrome(service=s)