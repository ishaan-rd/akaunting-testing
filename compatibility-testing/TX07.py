from selenium import webdriver

driver = webdriver.Ie(executable_path='C:/Users/HP/Desktop/IEDriverServer.exe' )
driver.implicitly_wait(10)
driver.get("https://akaunting.com")