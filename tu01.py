from selenium import webdriver

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://akaunting.com/login")
user = "ishaanrd6@gmail.com"
pwd = "6kDvRBTjjirr9i5"

driver.find_element_by_xpath('//*[@id="email"]').send_keys(user)
driver.find_element_by_xpath('//*[@id="password"]').send_keys(pwd)
driver.find_element_by_xpath('//*[@id="login-form"]/div[3]/label/input').click()
driver.find_element_by_id("recaptcha-anchor-label").click()
driver.find_element_by_xpath('//*[@id="login-form-submit"]').click()