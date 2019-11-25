from selenium import webdriver

driver = webdriver.Edge()
driver.implicitly_wait(10)
driver.get("https://akaunting.com")