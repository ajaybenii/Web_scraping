from selenium import webdriver
from selenium.webdriver.support.ui import Select

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

from PIL import Image
from pytesseract import pytesseract
from pytesseract import image_to_string

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, select
from selenium.common.exceptions import TimeoutException


tehsil = 'Panipat'
# tehsil = int(input("Eneter the  tehsil name")) #this input use for insert the tehsil name
tehsil_name = tehsil[0].upper() + tehsil[1:] #Captilaize first letter of input

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)
driver.get("https://jamabandi.nic.in/DSNakal/ShowDeedFile")

print("Website open and load tehsil...")

select = Select(driver.find_element_by_id('ctl00_ContentPlaceHolder1_drptehsil'))
select.select_by_visible_text(tehsil_name)



#Take the screenshot of full page after selection of the tehsil
img = driver.save_screenshot("screenshot.png")
captcha_path = "screenshot.png"
img = Image.open(captcha_path)
 
# Setting the points for cropped image
left = 272
top = 365
right = 368
bottom = 400
 
# Cropped image of above dimension
# (It will not change original image)
img = img.crop((left, top, right, bottom))

img=img.save('captcha.png')
captcha_path = 'captcha.png'
img = Image.open(captcha_path)

#By Pytessract we get text from image 
pytesseract.tesseract_cmd = r'tessract\tesseract.exe' #Path of tesseract app
text = pytesseract.image_to_string(img)
code = text[:-1]
print("Here is the captcha text = ",code)

search = driver.find_element_by_id('ctl00_ContentPlaceHolder1_txtCaptcha')
search.send_keys(code)
search_button = driver.find_element_by_id('ctl00_ContentPlaceHolder1_btnsbmit')
search_button.click()

x=2 
#Start the page loop with page number 2 because existing page is 1
try:
    for i in range (2):
        no = str(x)
        page = "Page$"
        post = "__doPostBack"
        link = "'ctl00$ContentPlaceHolder1$GridView1'"
        x2 = str(post+"("+link+","+"'"+page+no+"'"+")")
        check = driver.execute_script(x2)
        x+=1
        print("This is page number",no,"wait for 10 to 15 second for next page.." )
    # print(no," is last page or server issue from website")

except TimeoutException:
    print (no," is last page or server issue from website")


# Importing necessary modules]

from audioop import add
import time

import csv
from typing import List
from unicodedata import category
import pandas as pd
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

import csv
from selenium.webdriver.chrome.options import Options

# WebDriver Chrome
options = Options()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(executable_path=r"chromedriver.exe",chrome_options=options)

with open('UT_URLS.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)


url_value = 300
#1-500
result = []

#Create empty csv file
binary_file_name = open("name1-300.txt", "wb")
binary_file_address = open("address1-300.txt", "wb")
binary_file_category = open("category1-300.txt", "wb")
binary_status = open("status1-300.txt", "wb")

for i in range (url_value,450):

    new_lst=(','.join(data[url_value]))
    res = str(new_lst)


    try:
        driver.get(res)    
        name = (driver.find_element(By.XPATH,'//*[@id="entity_content"]/div[2]').text)
        name = (name+"\n")

        address = (driver.find_element(By.XPATH,'//*[@id="entity_content"]/div[10]/div[1]').text)
        address = (address+'\n')

        Category = (driver.find_element(By.XPATH,'//*[@id="entity_content"]/div[10]/div[2]').text)
        Category = (Category+'\n')

        Status = (driver.find_element(By.XPATH,'//*[@id="entity_content"]/div[10]/div[3]').text)
        Status = (Status+'\n')
        print(url_value)

        binary_file_name.write(name.encode())
        binary_file_address.write(address.encode())
        binary_file_category.write(Category.encode())
        binary_status.write(Status.encode())
       
        # binary_file.write(name.encode())
        # binary_file.write(raw_data.encode())
    except:
        pass

    url_value = url_value +1

binary_file_name.close()
binary_file_address.close()
binary_file_category.close()
binary_status.close()
time.sleep(1)
