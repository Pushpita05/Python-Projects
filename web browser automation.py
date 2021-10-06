#https://sites.google.com/a/chromium.org/chromedriver/downloads
from selenium import webdriver

PATH = "C:\Program Files\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://www.google.co.in/")
print(driver.title)