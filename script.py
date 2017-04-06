from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os
import getpass

username = raw_input("Your Username: ")
password = getpass.getpass("Password: ")

getdriver = ("https://www.instagram.com/accounts/login/")

driver = webdriver.Firefox()
driver.get(getdriver)

time.sleep(3)


driver.find_element_by_xpath("//input[@name='username']").send_keys(username)
driver.find_element_by_xpath("//input[@name='password']").send_keys(password)
driver.find_element_by_xpath("//button[contains(.,'Log in')]").click()
time.sleep(5)
driver.find_element_by_xpath("//input[@class='_9x5sw _qy55y']").send_keys("yesss!!")

finduser = raw_input("Username: ")
getdriver = ("https://instagram.com/"+finduser+"/")
driver.get(getdriver)
os.system("cd images")
#driver.find_element_by_xpath("//a[@class='_8mlbc _vbtk2 _t5r8b']").click()
#driver.find_element_by_xpath("//a[@class='_8mlbc _vbtk2 _t5r8b']").click()

for image in driver.find_elements_by_xpath('//div[@class="_jjzlb"]//img[@src]'):
	imgg = image.get_attribute('src')
	os.system("curl -O "+imgg)



driver.quit()

