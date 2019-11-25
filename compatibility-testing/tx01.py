from selenium import webdriver

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://akaunting.com")