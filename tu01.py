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

# -----
# Company dashboard has been loaded now
# -----

# Run an infinite loop asking the user to select the test case or to stop
i = input("Enter your option (Test Case ID or 'stop') : ")
while (i != 'stop'):

    driver.find_element_by_xpath('/html/body/div/aside/div/section/ul[2]/li[1]/a').click()

    if (i == 'tu05'): # add new income invoice
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

        price = driver.find_element_by_xpath('//*[@id="item-price-0"]')
        price.send_keys(Keys.CONTROL + 'a')
        price.send_keys(Keys.BACK_SPACE)
        price.send_keys('500')

        # add item 2
        driver.find_element_by_xpath('//*[@id="button-add-item"]').click()
        driver.find_element_by_xpath('//*[@id="item-name-1"]').send_keys("random item 2")

        price = driver.find_element_by_xpath('//*[@id="item-price-1"]')
        price.send_keys(Keys.CONTROL + 'a')
        price.send_keys(Keys.BACK_SPACE)
        price.send_keys('350')

        # select category
        driver.find_element_by_xpath('//*[@id="select2-category_id-container"]').click()
        ctg = driver.find_element_by_xpath('/html/body/span/span/span[1]/input')
        ctg.send_keys('d')
        ctg.send_keys(Keys.RETURN)

        # press the save button
        driver.find_element_by_xpath('/html/body/div/div/section[2]/div/form/div[2]/div/div/button').click()

    elif (i == 'tu06'): # add new income revenue
        driver.find_element_by_xpath('/html/body/div[1]/aside/div/section/ul[2]/li[3]/a').click()
        driver.find_element_by_xpath('/html/body/div/aside/div/section/ul[2]/li[3]/ul/li[2]/a/span').click()
        driver.find_element_by_xpath('/html/body/div[1]/div/section[1]/h1/span[1]/a').click()

        # enter amount
        amount = driver.find_element_by_xpath('//*[@id="amount"]')
        amount.send_keys(500)

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

    elif (i == 'tu07'): # add new income customer
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Items'])[1]/following::span[1]").click()
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Revenues'])[1]/following::span[1]").click()
        driver.find_element_by_link_text("Add New").click()
        driver.find_element_by_id("name").click()
        driver.find_element_by_id("name").clear()
        driver.find_element_by_id("name").send_keys("random name")
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Allow Login?'])[1]/following::button[1]").click()

    elif (i == 'tu08'): # add new category
        driver.find_element_by_link_text("Incomes").click()
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Incomes'])[1]/following::span[2]").click()
        driver.find_element_by_link_text("Add New").click()
        driver.find_element_by_id("button-category").click()
        driver.find_element_by_id("name").click()
        driver.find_element_by_id("name").clear()
        driver.find_element_by_id("name").send_keys("Random category")
        driver.find_element_by_xpath("//button[@id='button-create-category']/span").click()

    elif (i == 'tu09'): # add new expense bill
        driver.find_element_by_link_text("Expenses").click()
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Expenses'])[1]/following::span[2]").click()
        driver.find_element_by_link_text("Add New").click()
        driver.find_element_by_id("select2-vendor_id-container").click()
        driver.find_element_by_id("bill_number").click()
        driver.find_element_by_id("bill_number").clear()
        driver.find_element_by_id("bill_number").send_keys("12546")
        driver.find_element_by_id("item-name-0").click()
        driver.find_element_by_id("item-name-0").clear()
        driver.find_element_by_id("item-name-0").send_keys("random item")
        driver.find_element_by_id("item-price-0").click()
        driver.find_element_by_id("select2-category_id-container").click()
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Select File'])[1]/following::button[1]").click()

    elif (i == 'tu11'): # add new expense vendor
        driver.find_element_by_link_text("Expenses").click()
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Payments'])[1]/following::span[1]").click()
        driver.find_element_by_link_text("Add New").click()
        driver.find_element_by_id("name").click()
        driver.find_element_by_id("name").clear()
        driver.find_element_by_id("name").send_keys("random name")
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Reference'])[1]/following::button[1]").click()

    elif (i == '12'): # search income customers based on keyword
        driver.find_element_by_link_text("Incomes").click()
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Revenues'])[1]/following::span[1]").click()
        driver.find_element_by_name("search").click()
        driver.find_element_by_name("search").clear()
        driver.find_element_by_name("search").send_keys("erin")
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Search:'])[1]/following::button[1]").click()

    elif (i == 'tu13'): # change appearance to dark
        driver.find_element_by_link_text("Settings").click()
        driver.find_element_by_link_text("General").click()
        driver.find_element_by_link_text("Appearance").click()
        driver.find_element_by_id("select2-admin_theme-container").click()
        driver.find_element_by_xpath("//input[@type='search']").clear()
        driver.find_element_by_xpath("//input[@type='search']").send_keys("d")
        driver.find_element_by_xpath("//input[@type='search']").send_keys(Keys.ENTER)
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Allowed File Types'])[1]/following::button[1]").click()

    elif (i == 'tu14'): # display customers in decreasing alphabetical order
        driver.find_element_by_link_text("Incomes").click()
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Revenues'])[1]/following::span[1]").click()
        driver.find_element_by_link_text("Name").click()

    elif (i == 'tu17'): # export items
        driver.find_element_by_link_text("Items").click()
        driver.find_element_by_link_text("Export").click()

    elif (i == 'tu18'): # cash flow on dashboard with custom dates
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Quarterly'])[1]/following::span[1]").click()
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Last 12 Months'])[1]/following::li[1]").click()
        driver.find_element_by_name("daterangepicker_start").click()
        driver.find_element_by_name("daterangepicker_start").clear()
        driver.find_element_by_name("daterangepicker_start").send_keys("07/09/2019")
        driver.find_element_by_name("daterangepicker_end").click()
        driver.find_element_by_name("daterangepicker_end").clear()
        driver.find_element_by_name("daterangepicker_end").send_keys("30/11/2019")
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Custom Range'])[1]/following::button[1]").click()

    elif (i == 'tu19'): # switch companies
        driver.find_element_by_link_text("Switch").click()
        driver.find_element_by_link_text("jojiii").click()
        driver.find_element_by_link_text("Switch").click()
        driver.find_element_by_link_text("MyApp").click()

    elif (i == 'tu20'): # display income invoices based on date
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Items'])[1]/following::span[1]").click()
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Incomes'])[1]/following::span[2]").click()
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Search:'])[1]/following::span[9]").click()
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Yesterday'])[1]/following::li[1]").click()

    elif (i == 'tu21'): # expense summary
        driver.find_element_by_link_text("Reports").click()
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Income Summary'])[1]/following::span[1]").click()
        driver.find_element_by_xpath("//input[@type='search']").click()
        driver.find_element_by_xpath("//input[@type='search']").clear()
        driver.find_element_by_xpath("//input[@type='search']").send_keys("c")
        driver.find_element_by_xpath("//input[@type='search']").send_keys(Keys.ENTER)
        driver.find_element_by_xpath("(//input[@type='search'])[2]").click()
        driver.find_element_by_xpath("(//input[@type='search'])[2]").clear()
        driver.find_element_by_xpath("(//input[@type='search'])[2]").send_keys("b")
        driver.find_element_by_xpath("(//input[@type='search'])[2]").send_keys(Keys.ENTER)
        driver.find_element_by_xpath("(//input[@type='search'])[3]").click()
        driver.find_element_by_xpath("(//input[@type='search'])[3]").clear()
        driver.find_element_by_xpath("(//input[@type='search'])[3]").send_keys("o")
        driver.find_element_by_xpath("(//input[@type='search'])[3]").send_keys(Keys.ENTER)
        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='×'])[3]/following::button[1]").click()

    elif (i == 'tu22'): # change no. of display values in income
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Items'])[1]/following::span[1]").click()
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Incomes'])[1]/following::span[2]").click()
        driver.find_element_by_name("limit").click()
        Select(driver.find_element_by_name("limit")).select_by_visible_text("100")
        driver.find_element_by_name("limit").click()

    elif (i == 'tu23'): # printing expense summary
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Reconciliations'])[1]/following::span[1]").click()
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Income Summary'])[1]/following::span[1]").click()
        driver.find_element_by_link_text("Print").click()

    elif (i == 'tu24'): # add new bank account
        driver.find_element_by_link_text("Banking").click()
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Banking'])[2]/following::span[2]").click()
        driver.find_element_by_link_text("Add New").click()
        driver.find_element_by_id("name").click()
        driver.find_element_by_id("name").click()
        driver.find_element_by_id("name").clear()
        driver.find_element_by_id("name").send_keys("Tender")
        driver.find_element_by_id("number").click()
        driver.find_element_by_id("number").clear()
        driver.find_element_by_id("number").send_keys("1234567890")
        driver.find_element_by_id("opening_balance").click()
        driver.find_element_by_id("opening_balance").send_keys("2500")
        driver.find_element_by_id("opening_balance").click()
        driver.find_element_by_id("bank_name").click()
        driver.find_element_by_id("bank_name").clear()
        driver.find_element_by_id("bank_name").send_keys("SBI")
        driver.find_element_by_id("default_account_0").click()
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='No'])[2]/following::button[1]").click()

    i = input("Enter your option (Test Case ID or 'stop') : ")

print("Done now")
driver.close()