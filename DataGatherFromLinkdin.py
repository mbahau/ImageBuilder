# install dependencies

# Dependencies
import numpy as np
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path=r'C:\Users\md.bahauddin\OneDrive - o9 Solutions\python  projects\ImageBuilder\chromebrowser\chromedriver_win32')
driver.get('https://www.linkedin.com/login')

email_input = driver.find_element(By.NAME, 'session_key')
password_input = driver.find_element(By.NAME, 'session_password')

email_input.send_keys('your_email')
password_input.send_keys('your_password')
password_input.send_keys(Keys.RETURN)

time.sleep(5)  # Waiting for the page to load
print("Login successful")

driver.quit()
