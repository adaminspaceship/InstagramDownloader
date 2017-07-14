from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os
import getpass
import glob, shutil
import shutil
import requests
import json

username = raw_input("Your Username: ")
password = getpass.getpass("Password: ")

getdriver = ("https://www.instagram.com/accounts/login/")
os.system("mkdir images")
chromedriver = "/Users/adam/Documents/chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)
driver.get(getdriver)
imagesarray = []
driver.find_element_by_xpath("//input[@name='username']").send_keys(username)
driver.find_element_by_xpath("//input[@name='password']").send_keys(password)
driver.find_element_by_xpath("//button[contains(.,'Log in')]").click()
time.sleep(3)
os.system("cd images")
theinput = input("how many images? ")
with open("images.txt","wb") as i:
    for a in range(1, theinput):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        image =  driver.find_element_by_id("pImage_%s"%a).get_attribute("src")
        imagesarray.append(image)
        url = image
        response = requests.get(url, stream=True)
        with open('images/%s.png'%a, 'wb') as out_file:
            shutil.copyfileobj(response.raw, out_file)
        del response
        i.write('images/%s.png 4:10'%a)
        i.write('\n')

os.system("python vision.py -i images.txt -o vision.json")

data = open('vision.json', 'rb').read()
response = requests.post(url='https://vision.googleapis.com/v1/images:annotate?key=AIzaSyCoHwBpWuve8dXFS8CssZg3yd1Mblq5Eyk',
    data=data,
    headers={'Content-Type': 'application/json'})
with open("data.json", "wb") as new_file:
    new_file.write(response.text)

#start checking if exists keyword -> Clothes in post...
with open('data.json') as data_file:    
    data = json.load(data_file)
with open("show.html","wb") as html:
    html.write("<html><body>")
    for img in imagesarray:
        newdata = data["responses"][imagesarray.index(img)]["labelAnnotations"][0]["description"]
        html.write("<img src="+img+"><br><h2> In the image you can see - "+str(newdata)+"</h2><br><br>")
    html.write("</body></html>")





driver.quit()
