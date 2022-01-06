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


