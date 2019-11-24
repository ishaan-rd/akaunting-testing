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

driver.find_element_by_link_text("Incomes").click()
driver.find_element_by_xpath(
    "(.//*[normalize-space(text()) and normalize-space(.)='Revenues'])[1]/following::span[1]").click()
driver.find_element_by_name("search").click()
driver.find_element_by_name("search").clear()
driver.find_element_by_name("search").send_keys("erin")
driver.find_element_by_xpath(
    "(.//*[normalize-space(text()) and normalize-space(.)='Search:'])[1]/following::button[1]").click()