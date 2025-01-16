import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


path = r"C:\\Users\\agrah\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe"    #path of chromedriver.exe file
service = Service(path)

driver = webdriver.Chrome(service= service)

# enter your username and passward
username = "+++++++++++" 
password = "*********" 
url = "https://leetcode.com/accounts/login/"

print("Opening the login page...")
driver.get(url)

print("Filling the username...")
driver.find_element(By.ID, 'id_login').send_keys(username)

print("Filling the password...")
driver.find_element(By.ID, 'id_password').send_keys(password)

print("Clicking the login button...")
driver.find_element(By.ID, 'signin_btn').click()

print("Login process  initiated...")
time.sleep(5)
print("login successfull!")
driver.get("https://leetcode.com/u/username/")    # you can add your profile link here
time.sleep(10)

driver.quit()





