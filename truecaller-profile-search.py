from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

import os
import selenium
from selenium import webdriver
import time
from PIL import Image
import io
import requests
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://www.truecaller.com/auth/sign-in")

#print(WebDriverWait(driver, 10).until(
#    EC.visibility_of_element_located((By.XPATH, "//input[contains(@class,'flex')]"))).get_attribute('href'))
link_list = []
for links in driver.find_elements_by_xpath('.//a'):
    print(links.get_attribute('href'))
    link_order = links.get_attribute('href')
    link_list.append(link_order)
substring = "accounts.google.com"
#substring_in_list = any(substring in string for string in link_list)
substring_in_list = [string for string in link_list if substring in string]
#print(substring_in_list)

for link in substring_in_list:
    driver.get(link)

username = "xploriaindia@gmail.com"
password = "Xploria@123"

driver.get("https://stackoverflow.com/users/login?ssrc=head&returnurl=https%3a%2f%2fstackoverflow.com%2f")

uname = driver.find_element_by_id("email").send_keys(username)
passw = driver.find_element_by_id("password").send_keys(password)

login_btn = driver.find_element_by_id("submit-button")
login_btn.click()


time.sleep(2)

input_search = WebDriverWait(driver, 20)
search_query = "xploriaindia@gmail.com"
xpath_value = "//input[contains(@class,'whsOnd ')]"
input_search.until(EC.presence_of_element_located((By.XPATH, xpath_value))).send_keys(search_query)
input_search.until(EC.presence_of_element_located((By.XPATH, xpath_value))).send_keys(Keys.RETURN)

#oauth2_client_link = str(substring_in_list)
#print(oauth2_client_link)
#print(type(oauth2_client_link))












"""
username = "xploriaindia@gmail.com"
password = ""

time.sleep(2)

email_in = driver.find_element_by_xpath('//*[@id="email"]')
email_in.send_keys(username)

password_in = driver.find_element_by_xpath('//*[@id="pass"]')
password_in.send_keys(password)

login_btn = driver.find_element_by_xpath('//*[@id="loginbutton"]')
login_btn.click()


from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

try:
    input_search = WebDriverWait(driver, 20)
    search_query = "9597195110"
    xpath_value = "//input[contains(@class,'px-4')]"
    input_search.until(EC.presence_of_element_located((By.XPATH, xpath_value))).send_keys(search_query)
    input_search.until(EC.presence_of_element_located((By.XPATH, xpath_value))).send_keys(Keys.RETURN)
    
    element = driver.find_element_by_xpath("//input[contains(@class,'oajrlxb2')]")
    link = element.get_attribute("href")
    print(link)
    
    print(WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//input[contains(@class,'oajrlxb2')]"))).get_attribute('href'))
    #for links in driver.find_elements_by_xpath('.//a'):
    #    print(links.get_attribute('href'))
    
    #input_search.submit()
    print('Successfully logged in')

except NoSuchElementException:
    print('Incorrect login/password')

print(WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//input[contains(@class,'oajrlxb2')]"))).get_attribute('href'))
"""