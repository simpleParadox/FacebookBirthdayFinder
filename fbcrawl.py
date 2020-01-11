# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 20:38:08 2020

@author: Rohan
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Chrome(r"C:\webdrivers\chromedriver.exe")
driver.get("https://www.facebook.com")
username = driver.find_element_by_id("email")
password = driver.find_element_by_id("pass")
submit = driver.find_element_by_id("loginbutton")

email = "<email>"
passkey = "<password>"

username.send_keys(email)
password.send_keys(passkey)
submit.click()

friend_profile = "<your_friends_profile_url>"

driver.get(friend_profile)
flag=0
while(flag==0):
    before_posts = driver.find_elements_by_xpath("//div[@data-testid='post_message']")
    before_para = driver.find_elements_by_xpath("//div[@data-testid='post_message']/p")
    last_post = before_posts[-1]
    for i in range(len(before_para)-1,-1,-1):
        if(before_para[i] is not None):
            if("birthday" in before_para[i].text or "Birthday" in before_para[i].text):
                flag = 1
                break
    if(flag==1):
        break
    html = driver.find_element_by_tag_name('html')
    html.send_keys(Keys.END)
    time.sleep(1)
#
#If you want the window to close after executing the program.
#driver.close()