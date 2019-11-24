from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
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

# -----
# Company dashboard has been loaded now
# -----

# Run an infinite loop asking the user to select the test case or to stop
i = input("Enter your option (Test Case ID or 'stop') : ")
while (i != 'stop'):
    if (i == 'tu05'):
        driver.find_element_by_xpath('/html/body/div[1]/aside/div/section/ul[2]/li[3]/a').click()
        driver.find_element_by_xpath('/html/body/div[1]/aside/div/section/ul[2]/li[3]/ul/li[1]/a/span').click()
        driver.find_element_by_xpath('/html/body/div[1]/div/section[1]/h1/span[1]/a').click()

        # select customer
        driver.find_element_by_xpath('//*[@id="select2-customer_id-container"]').click()
        customer = driver.find_element_by_xpath('/html/body/span/span/span[1]/input')
        customer.send_keys('c')
        customer.send_keys(Keys.RETURN)

        # enter due date (7 days from now)
        due_date = datetime.now().date() + timedelta(days=7)
        due_date_str = due_date.strftime('%Y-%m-%d')
        driver.find_element_by_xpath('//*[@id="due_at"]').send_keys(due_date_str)

        # enter item 1
        driver.find_element_by_xpath('//*[@id="item-name-0"]').send_keys("random item")
        driver.find_element_by_xpath('//*[@id="item-price-0"]').send_keys("500")

        # add item 2
        driver.find_element_by_xpath('//*[@id="button-add-item"]').click()
        driver.find_element_by_xpath('//*[@id="item-name-1"]').send_keys("random item 2")
        driver.find_element_by_xpath('//*[@id="item-quantity-1"]').send_keys("2")
        driver.find_element_by_xpath('//*[@id="item-price-1"]').send_keys("350")

        # select category
        driver.find_element_by_xpath('//*[@id="select2-category_id-container"]').click()
        ctg = driver.find_element_by_xpath('/html/body/span/span/span[1]/input')
        ctg.send_keys('d')
        ctg.send_keys(Keys.RETURN)

        # press the save button
        driver.find_element_by_xpath('/html/body/div/div/section[2]/div/form/div[2]/div/div/button').click()

        # go back to Dashboard
        driver.find_element_by_xpath('/html/body/div/header/a/span[2]').click()

    elif (i == 'tu06'):
        driver.find_element_by_xpath('/html/body/div[1]/aside/div/section/ul[2]/li[3]/a').click()
        driver.find_element_by_xpath('/html/body/div/aside/div/section/ul[2]/li[3]/ul/li[2]/a/span').click()
        driver.find_element_by_xpath('/html/body/div[1]/div/section[1]/h1/span[1]/a').click()

        # enter amount
        driver.find_element_by_xpath('//*[@id="amount"]').send_keys('500')

        # select customer
        driver.find_element_by_xpath('//*[@id="select2-customer_id-container"]').click()
        customer = driver.find_element_by_xpath('/html/body/span/span/span[1]/input')
        customer.send_keys('c')
        customer.send_keys(Keys.RETURN)

        # select category
        driver.find_element_by_xpath('//*[@id="select2-category_id-container"]').click()
        ctg = driver.find_element_by_xpath('/html/body/span/span/span[1]/input')
        ctg.send_keys('d')
        ctg.send_keys(Keys.RETURN)

        # press the save button
        driver.find_element_by_xpath('/html/body/div/div/section[2]/div/form/div[2]/div/div/button').click()

        # go back to Dashboard
        driver.find_element_by_xpath('/html/body/div/header/a/span[2]').click()


    i = input("Enter your option (Test Case ID or 'stop') : ")

print("Done now")
driver.close()