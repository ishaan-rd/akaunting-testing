from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
from datetime import datetime
from datetime import timedelta

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://akaunting.com/login")
user = "tejasnitk@gmail.com"
pwd = "tejaskumark"

# Login to akaunting main
driver.find_element_by_xpath('//*[@id="email"]').send_keys(user)
driver.find_element_by_xpath('//*[@id="password"]').send_keys(pwd)
driver.find_element_by_xpath('//*[@id="login-form"]/div[3]/label/input').click()
# driver.find_element_by_id("recaptcha-anchor-label").click()
# time.sleep(20)
cont = input("Press any key after captcha is completed to continue testing : ")
driver.find_element_by_xpath('//*[@id="login-form-submit"]').click()

# Login to company
driver.find_element_by_xpath('//*[@id="tab-companies"]/table/tbody/tr[1]/td[3]/button').click()
new_window = driver.window_handles[1]
driver.switch_to.window(new_window)

# --- Enter your test code here ---
i = input("Enter your option ('go' or 'stop') : ")
while i != 'stop':
    driver.find_element_by_xpath('/html/body/div/aside/div/section/ul[2]/li[1]/a').click()

    driver.find_element_by_xpath('/html/body/div[1]/header/nav/div/ul/li[4]/a').click()
    driver.find_element_by_xpath('/html/body/div[1]/header/nav/div/ul/li[4]/ul/li[3]/div[2]/a').click()
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/form/div[1]/input').click()
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/form/div[1]/input').clear()
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/form/div[1]/input').send_keys('tejasnitk@gmail.com')
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/form/div[2]/input').click()
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/form/div[2]/input').clear()
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/form/div[2]/input').send_keys('tejaskumar')
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/form/div[3]/div[1]/div/label/div/ins').click()
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/form/div[3]/div[2]/button').click()

    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    driver.find_element_by_xpath('//*[@id="tab-companies"]/table/tbody/tr[1]/td[3]/button').click()
    new_window = driver.window_handles[1]
    driver.switch_to.window(new_window)

    i = input("Enter your option ('go' or 'stop') : ")

print("done now boi")
driver.close()