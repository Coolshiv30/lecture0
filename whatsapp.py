#whatsapp automation
# Here, with the help of python code we will write text- messages to our friends or other members in whatsapp
# Here, User has to scan QR-Code of their whatsapp web  
from selenium import webdriver

driver = webdriver.Chrome('D:/chromedriver/chromedriver.exe')
driver.get('https://web.whatsapp.com/')
name = input("enter the user or group :")
msg = input("enter your message :")
count = int(input("enter the count :"))

input("enter anything after scanning QR code")

user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
user.click()
msg_box = driver.find_element_by_class_name("_3u328" ) #class_name("3u328") is different for different user who try to run this code. At first they have to open their whatsapp in any browser then they have to right click the message box and then click on inspect then again right click the message box and click on inspect then they have to write the class name from the <div tag> that is selected that is selected here. 
for i in range(count):
    msg_box.send_keys(msg)
    button = driver.find_element_by_class_name("_3M-N-")#class_name("_3M-N-") is different for different user who try to run this code. At first they have to open their whatsapp in any browser then they have to right click the message box and then click on inspect then again right click on message box and click on inspect then findout the tag that starts with <button> and copy the class name of that tag here.


    button.click()
