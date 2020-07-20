from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
import chromedriver_binary
import time
driver = webdriver.Chrome()
driver.get('http://web.whatsapp.com')
input('enter any key')
time.sleep(5)
to = input("enter the recipient name like in whatsapp")
names=[to]
for name in names:
    person=driver.find_element_by_xpath('//span[@title="{}"]'.format(name))
    person.click()
    for i in range(1,3):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        msg_got = driver.find_elements_by_css_selector("span.selectable-text.invisible-space.copyable-text")
        msg=[message.text for message in msg_got]
        msg="hello"
        cc=int(input("enter the count"))
        count=cc
        #you want to set your path for this
        reply=driver.find_element_by_xpath("/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]")
        reply.clear()
        for i in range(count):
            reply.send_keys("hello I am virtual assistant for krishnan he is busy right now he will reply to your message when he was free!")
            reply.send_keys(Keys.RETURN)

            






