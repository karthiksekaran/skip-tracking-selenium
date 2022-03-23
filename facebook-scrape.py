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

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://www.facebook.com/login")
username = "saravanan.bear@gmail.com"
password = "IAMJericho"

time.sleep(2)

email_in = driver.find_element_by_xpath('//*[@id="email"]')
email_in.send_keys(username)

password_in = driver.find_element_by_xpath('//*[@id="pass"]')
password_in.send_keys(password)

login_btn = driver.find_element_by_xpath('//*[@id="loginbutton"]')
login_btn.click()

from selenium.webdriver.support import expected_conditions as expect
#elem = WebDriverWait(driver, 120, 1).until(expect.visibility_of_element_located((By.XPATH, "//input[@placeholder='Search in your collabs']")))
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


try:
    #logout_button = driver.find_element_by_id("lnklogout")
    #search = driver.find_element_by_xpath('//*[@id="search"]')
    #search = driver.find_element_by_css_selector("div[aria-label='Search Facebook']").send_keys("Karthik Srinivas Vellore")
    #search2 = driver.find_element_by_css_selector("button[aria-label='Search']").send_keys("Hello")
    input_search = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, "//input[contains(@class,'oajrlxb2')]")))
    #input_search.click()
    driver.execute_script("arguments[0].click();", input_search)
    input_search.send_keys("Karthik Sekaran Vellore")
    input_search.submit()
    #from selenium.webdriver.common.keys import Keys
    #driver.find_element_by_name("Value").send_keys(Keys.RETURN, "Karthik Sekaran Vellore")
    #search = driver.find_element_by_class_name('hu5pjgll').click()
    """
    button = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//input[contains(@class,'hu5pjgll')]")))
    button.click()
    wait = WebDriverWait(driver, 10)
    element = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[contains(@class,'j83agx80')]")))
    element.click()
    """
    print('Successfully logged in')

except NoSuchElementException:
    print('Incorrect login/password')


"""
page_name = 'BillGates'
REQUEST_URL = f'https://www.facebook.com/{page_name}/settings/?tab=people_and_other_pages&ref=page_edit'

driver.get(REQUEST_URL)

time.sleep(2)
scrolls = 15
from bs4 import BeautifulSoup
for i in range(1,scrolls):
  driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
  time.sleep(3)

  page = driver.page_source
  soup = BeautifulSoup(page, "html.parser")
  names = soup.find_all('a', class_='_3cb8')
  people_who_liked_page = []
  for name in names:
    people_who_liked_page.append(name.text)

"""