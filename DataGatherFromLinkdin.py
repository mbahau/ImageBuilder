# install dependencies
pip install selenium

# Dependencies
import numpy as np
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time

s
# Specify the path to chromedriver
chrome_driver_path = r'C:\Users\md.bahauddin\OneDrive - o9 Solutions\python  projects\ImageBuilder\chromebrowser\chromedriver_win32'

# Create the Service object
service = Service(executable_path=chrome_driver_path)

driver = webdriver.Chrome(executable_path='/path/to/chromedriver')
driver.get('https://www.linkedin.com/login')

email_input = driver.find_element(By.NAME, 'session_key')
password_input = driver.find_element(By.NAME, 'session_password')

email_input.send_keys('your_email')
password_input.send_keys('your_password')
password_input.send_keys(Keys.RETURN)

time.sleep(5)  # Waiting for the page to load
print("Login successful")

driver.quit()
