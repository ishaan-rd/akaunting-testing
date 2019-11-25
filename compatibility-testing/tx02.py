from selenium import webdriver

driver = webdriver.Firefox()
driver.implicitly_wait(10)
driver.get("https://akaunting.com")