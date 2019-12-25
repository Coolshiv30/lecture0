from selenium import webdriver

driver = webdriver.Chrome('D:/chromedriver/chromedriver.exe')
driver.get('https://web.whatsapp.com/')
name = input("enter the user or group :")
msg = input("enter your message :")
count = int(input("enter the count :"))

input("enter anything after scanning QR code")

user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
user.click()
msg_box = driver.find_element_by_class_name("_3u328" )
for i in range(count):
    msg_box.send_keys(msg)
    button = driver.find_element_by_class_name("_3M-N-")
    button.click()
