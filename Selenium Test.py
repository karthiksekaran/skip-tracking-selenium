import os
import selenium
from selenium import webdriver
import time
from PIL import Image
import io
import requests
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException

driver = webdriver.Chrome(ChromeDriverManager().install())

USERNAME = "SKY0038024042"
PASSWORD = "3pyrLs"

driver.get("http://cyberautics.co.in/login.aspx")

login = driver.find_element_by_id('txtemailid').send_keys(USERNAME)
password = driver.find_element_by_id('txtpassword').send_keys(PASSWORD)
submit = driver.find_element_by_id('btnsignUP').click()

try:
    logout_button = driver.find_element_by_id("lnklogout")
    print('Successfully logged in')

except NoSuchElementException:
    print('Incorrect login/password')

driver.get("http://cyberautics.co.in/Users/Createform.aspx")

# get the image source

img = driver.find_element_by_id('ContentPlaceHolder1_Imgquestions')

src = img.get_attribute('src')

# download the image

import urllib3 as urllib

import urllib.request

urllib.request.urlretrieve(src, "form.png")