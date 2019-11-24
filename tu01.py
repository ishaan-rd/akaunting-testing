from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://akaunting.com/login")
user = "ishaanrd6@gmail.com"
pwd = "6kDvRBTjjirr9i5"

# Login to akaunting main
driver.find_element_by_xpath('//*[@id="email"]').send_keys(user)
driver.find_element_by_xpath('//*[@id="password"]').send_keys(pwd)
driver.find_element_by_xpath('//*[@id="login-form"]/div[3]/label/input').click()
# driver.find_element_by_id("recaptcha-anchor-label").click()
time.sleep(30)
driver.find_element_by_xpath('//*[@id="login-form-submit"]').click()

# Login to company
driver.find_element_by_xpath('//*[@id="tab-companies"]/table/tbody/tr[1]/td[3]/button/span').click()
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
        driver.find_element_by_xpath('//*[@id="select2-customer_id-container"]').click()
        driver.find_element_by_xpath('//*[@id="select2-customer_id-result-p6mr-206843"]').click()

    i = input("Enter your option (Test Case ID or 'stop') : ")

print("Done now")