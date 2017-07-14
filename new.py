from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os
import getpass
import glob, shutil
import shutil
import requests

username = raw_input("Your Username: ")
password = getpass.getpass("Password: ")

getdriver = ("https://www.instagram.com/accounts/login/")
os.system("mkdir images")
chromedriver = "/Users/adam/Documents/chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)
driver.get(getdriver)

driver.find_element_by_xpath("//input[@name='username']").send_keys(username)
driver.find_element_by_xpath("//input[@name='password']").send_keys(password)
driver.find_element_by_xpath("//button[contains(.,'Log in')]").click()
time.sleep(3)
os.system("cd images")
for a in range(1, input("how many images? ")):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    image =  driver.find_element_by_id("pImage_%s"%a).get_attribute("src")
    url = image
    response = requests.get(url, stream=True)
    with open('images/%s.png'%a, 'wb') as out_file:
        shutil.copyfileobj(response.raw, out_file)
    del response

driver.quit()
