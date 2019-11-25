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

    # --- Component Testing --- #
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
        driver.find_element_by_id("select2-vendor_id-container").send_keys('c')
        driver.find_element_by_id("select2-vendor_id-container").send_keys(Keys.RETURN)
        driver.find_element_by_id("bill_number").click()
        driver.find_element_by_id("bill_number").clear()
        driver.find_element_by_id("bill_number").send_keys("12546")
        driver.find_element_by_id("item-name-0").click()
        driver.find_element_by_id("item-name-0").clear()
        driver.find_element_by_id("item-name-0").send_keys("random item")
        driver.find_element_by_id("item-price-0").click()
        driver.find_element_by_id("item-price-0").clear()
        driver.find_element_by_id("item-price-0").send_keys('550')
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

    elif (i == 'tu12'): # search income customers based on keyword
        driver.find_element_by_xpath('/html/body/div[1]/aside/div/section/ul[2]/li[3]/a').click()
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

    elif (i == 'tu15'):
        driver.find_element_by_xpath('/html/body/div[1]/aside/div/section/ul[2]/li[2]/a').click()
        driver.find_element_by_xpath('/html/body/div/div/section[1]/h1/span[2]/a').click()
        driver.find_element_by_xpath('/html/body/div/div/section[2]/div/form/div[1]/div[2]/div/div/button').click()
        driver.find_element_by_xpath('/html/body/div/div/section[2]/div/form/div[2]/div/div/button').click()

    elif (i == 'tu16'):
        driver.find_element_by_xpath('/html/body/div[1]/aside/div/section/ul[2]/li[2]/a').click()
        driver.find_element_by_xpath('/html/body/div/div/section[1]/h1/span[2]/a').click()
        driver.find_element_by_xpath('/html/body/div/div/section[2]/div/form/div[1]/div[2]/div/div/button').click()
        driver.find_element_by_xpath('/html/body/div/div/section[2]/div/form/div[2]/div/div/button').click()

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

    if (i == 'tu49'):
        driver.find_element_by_xpath("//li[4]/a/i").click()
        driver.find_element_by_link_text("Users").click()
        driver.find_element_by_xpath("//table[@id='tbl-users']/tbody/tr[4]/td[4]/div/button/i").click()
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Disable'])[4]/following::button[1]").click()
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Cathy'])[2]/following::button[1]").click()
        driver.find_element_by_xpath("/html/body/div[1]/header/a/span[2]").click()

    elif (i == 'tu48'):
        driver.find_element_by_link_text("Settings").click()
        driver.find_element_by_link_text("General").click()
        driver.find_element_by_link_text("Localisation").click()
        driver.find_element_by_id("select2-percent_position-container").click()
        driver.find_element_by_id("select2-percent_position-container").click()
        driver.find_element_by_id("select2-timezone-container").click()
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Allowed File Types'])[1]/following::button[1]").click()


    elif (i == 'tu46'):
        driver.find_element_by_link_text("Tekas").click()
        driver.find_element_by_link_text("Logout").click()

    elif (i == 'tu45'):
        driver.find_element_by_xpath("//li[2]/a/i").click()
        driver.find_element_by_link_text("English (GB)").click()

    elif (i == 'tu44'):
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Toggle navigation'])[1]/following::a[1]").click()
        driver.find_element_by_link_text("Account").click()
        driver.find_element_by_id("name").clear()
        driver.find_element_by_id("name").send_keys("hj")
        driver.find_element_by_id("number").click()
        driver.find_element_by_id("number").clear()
        driver.find_element_by_id("number").send_keys("45")
        driver.find_element_by_id("opening_balance").click()
        driver.find_element_by_id("bank_name").click()
        driver.find_element_by_id("bank_name").clear()
        driver.find_element_by_id("bank_name").send_keys("canara")
        driver.find_element_by_id("bank_phone").click()
        driver.find_element_by_id("bank_phone").clear()
        driver.find_element_by_id("bank_phone").send_keys("9885423655")
        driver.find_element_by_id("bank_address").click()
        driver.find_element_by_id("bank_address").clear()
        driver.find_element_by_id("bank_address").send_keys("kekdnndjs")
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='No'])[2]/following::button[1]").click()


    elif (i == 'tu43'):
        driver.find_element_by_xpath("//i").click()
        driver.find_element_by_link_text("Vendor").click()
        driver.find_element_by_id("name").clear()
        driver.find_element_by_id("name").send_keys("abc")
        driver.find_element_by_id("email").clear()
        driver.find_element_by_id("email").send_keys("abc@gmail.com")
        driver.find_element_by_id("tax_number").click()
        driver.find_element_by_id("tax_number").clear()
        driver.find_element_by_id("tax_number").send_keys("251")
        driver.find_element_by_id("phone").click()
        driver.find_element_by_id("phone").clear()
        driver.find_element_by_id("phone").send_keys("9886752314")
        driver.find_element_by_id("website").click()
        driver.find_element_by_id("website").clear()
        driver.find_element_by_id("website").send_keys("abc.com")
        driver.find_element_by_id("address").click()
        driver.find_element_by_id("address").clear()
        driver.find_element_by_id("address").send_keys("abcv")
        driver.find_element_by_id("reference").click()
        driver.find_element_by_id("reference").clear()
        driver.find_element_by_id("reference").send_keys("atoz")
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Reference'])[1]/following::button[1]").click()

    elif (i == 'tu42'):
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Toggle navigation'])[1]/following::a[1]").click()
        driver.find_element_by_link_text("Payment").click()
        driver.find_element_by_id("description").click()
        driver.find_element_by_id("description").clear()
        driver.find_element_by_id("description").send_keys("paid")
        driver.find_element_by_id("select2-category_id-container").click()
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Select File'])[1]/following::button[1]").click()

    elif (i == 'tu41'):
        driver.get("https://app.akaunting.com/")
        driver.find_element_by_xpath("//i").click()
        driver.find_element_by_link_text("Bill").click()
        driver.find_element_by_id("select2-vendor_id-container").click()
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='New Bill'])[1]/following::div[2]").click()
        driver.find_element_by_id("bill_number").click()
        driver.find_element_by_id("bill_number").clear()
        driver.find_element_by_id("bill_number").send_keys("250")
        driver.find_element_by_id("order_number").click()
        driver.find_element_by_id("order_number").clear()
        driver.find_element_by_id("order_number").send_keys("45")
        driver.find_element_by_id("item-name-0").click()
        driver.find_element_by_id("item-name-0").clear()
        driver.find_element_by_id("item-name-0").send_keys("card")
        driver.find_element_by_id("item-price-0").click()
        driver.find_element_by_xpath("//input[@type='search']").click()
        driver.find_element_by_xpath("//input[@type='search']").clear()
        driver.find_element_by_xpath("//input[@type='search']").send_keys("40")
        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='₹2,000.00'])[1]/following::td[3]").click()
        driver.find_element_by_id("select2-category_id-container").click()
        driver.find_element_by_xpath("//button/span").click()


    elif (i == 'tu40'):
        driver.find_element_by_xpath("//i").click()
        driver.find_element_by_link_text("Invoice").click()
        driver.find_element_by_id("select2-customer_id-container").click()
        driver.find_element_by_id("due_at").click()
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Su'])[1]/following::td[31]").click()
        driver.find_element_by_id("order_number").click()
        driver.find_element_by_id("order_number").clear()
        driver.find_element_by_id("order_number").send_keys("45")
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Total'])[1]/following::td[2]").click()
        driver.find_element_by_id("item-name-0").click()
        driver.find_element_by_id("item-name-0").clear()
        driver.find_element_by_id("item-name-0").send_keys("card")
        driver.find_element_by_id("item-price-0").click()
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='New Invoice'])[1]/following::div[2]").click()
        driver.find_element_by_id("select2-category_id-container").click()
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Select File'])[1]/following::button[1]").click()

    elif (i == 'tu39'):
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Toggle navigation'])[1]/following::a[1]").click()
        driver.find_element_by_link_text("Customer").click()
        driver.find_element_by_id("name").clear()
        driver.find_element_by_id("name").send_keys("Anil")
        driver.find_element_by_id("email").click()
        driver.find_element_by_id("email").clear()
        driver.find_element_by_id("email").send_keys("Anil@gmail.com")
        driver.find_element_by_id("tax_number").click()
        driver.find_element_by_id("tax_number").clear()
        driver.find_element_by_id("tax_number").send_keys("244")
        driver.find_element_by_id("phone").click()
        driver.find_element_by_id("phone").clear()
        driver.find_element_by_id("phone").send_keys("9563214589")
        driver.find_element_by_id("website").click()
        driver.find_element_by_id("website").clear()
        driver.find_element_by_id("website").send_keys("anil.com")
        driver.find_element_by_id("address").click()
        driver.find_element_by_xpath("//div[@id='customer-create-user']/div/ins").click()
        driver.find_element_by_xpath("//div[@id='customer-create-user']/div/ins").click()
        driver.find_element_by_id("address").clear()
        driver.find_element_by_id("address").send_keys("jjwkjkdk")
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Allow Login?'])[1]/following::button[1]").click()

    elif (i == 'tu38'):
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Toggle navigation'])[1]/following::a[1]").click()
        driver.find_element_by_link_text("Revenue").click()
        driver.find_element_by_id("select2-customer_id-container").click()
        driver.find_element_by_id("description").click()
        driver.find_element_by_id("description").clear()
        driver.find_element_by_id("description").send_keys("Paid")
        driver.find_element_by_id("select2-category_id-container").click()
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Select File'])[1]/following::button[1]").click()

    elif (i == 'tu37'):
        driver.find_element_by_xpath("//span[2]/i").click()
        driver.find_element_by_link_text("Invoices").click()
        driver.find_element_by_xpath("//table[@id='tbl-invoices']/tbody/tr/td[7]/div/button/i").click()
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Duplicate'])[1]/following::button[1]").click()
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Invoices'])[2]/following::button[1]").click()

    elif (i == 'tu36'):
        driver.find_element_by_link_text("Banking").click()
        driver.find_element_by_link_text("Reconciliations").click()
        driver.find_element_by_link_text("Add New").click()
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='New Reconciliation'])[1]/following::div[4]").click()
        driver.find_element_by_id("started_at").click()
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Su'])[1]/following::td[26]").click()
        driver.find_element_by_id("ended_at").click()
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Su'])[1]/following::td[31]").click()
        driver.find_element_by_id("closing_balance").click()
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Cash'])[2]/following::button[1]").click()
        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='₹0.00'])[2]/following::button[1]").click()

    elif (i == 'tu35'):
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Last login 36 minutes ago'])[1]/preceding::span[1]").click()
        driver.find_element_by_link_text("Users").click()
        driver.find_element_by_link_text("Add New").click()
        driver.find_element_by_id("name").click()
        driver.find_element_by_id("name").clear()
        driver.find_element_by_id("name").send_keys("Abc")
        driver.find_element_by_id("email").clear()
        driver.find_element_by_id("email").send_keys("Abc123@gmail.com")
        driver.find_element_by_id("password").click()
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("abc123")
        driver.find_element_by_xpath("//ins").click()
        driver.find_element_by_xpath("//div[2]/div/ins").click()
        driver.find_element_by_id("password_confirmation").clear()
        driver.find_element_by_id("password_confirmation").send_keys("abc123")
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='New User'])[1]/following::form[1]").click()
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Enabled'])[1]/following::span[1]").click()
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='No'])[1]/following::button[1]").click()

    elif (i == 'tu34'):
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Last login 38 minutes ago'])[1]/preceding::span[1]").click()
        driver.find_element_by_link_text("Profile").click()
        driver.find_element_by_id("picture").click()
        driver.find_element_by_id("picture").clear()
        driver.find_element_by_id("picture").send_keys("C:\\fakepath\\Sketch (1).png")
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Select File'])[1]/following::button[1]").click()

    elif (i == 'tu33'):
        driver.find_element_by_link_text("Settings").click()
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Categories'])[1]/following::span[1]").click()
        driver.find_element_by_link_text("Add New").click()
        driver.find_element_by_id("name").clear()
        driver.find_element_by_id("name").send_keys("pao")
        driver.find_element_by_id("select2-code-container").click()
        driver.find_element_by_id("rate").click()
        driver.find_element_by_id("rate").clear()
        driver.find_element_by_id("rate").send_keys("5")
        driver.find_element_by_id("symbol").click()
        driver.find_element_by_id("symbol").clear()
        driver.find_element_by_id("symbol").send_keys("^")
        driver.find_element_by_id("symbol_first").click()
        Select(driver.find_element_by_id("symbol_first")).select_by_visible_text("Before Amount")
        driver.find_element_by_id("symbol_first").click()
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='No'])[2]/following::button[1]").click()

    elif (i == 'tu32'):
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Profit & Loss'])[1]/following::span[1]").click()
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Settings'])[1]/following::span[2]").click()
        driver.find_element_by_link_text("Defaults").click()
        driver.find_element_by_id("select2-default_currency-container").click()
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Allowed File Types'])[1]/following::button[1]").click()

        # elif(i=='tu31'):

    elif (i == 'tu30'):
        driver.find_element_by_link_text("Settings").click()
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Settings'])[1]/following::span[2]").click()
        driver.find_element_by_link_text("System").click()
        driver.find_element_by_id("session_lifetime").click()
        driver.find_element_by_id("session_lifetime").clear()
        driver.find_element_by_id("session_lifetime").send_keys("40")
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Allowed File Types'])[1]/following::button[1]").click()

    elif (i == 'tu29'):
        driver.find_element_by_link_text("Banking").click()
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Transfers'])[1]/following::span[1]").click()
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Search:'])[1]/following::button[1]").click()
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Custom Range'])[1]/following::button[1]").click()
        driver.find_element_by_xpath("//input[@type='search']").click()
        driver.find_element_by_xpath("(//input[@type='search'])[2]").click()
        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='×'])[2]/following::button[1]").click()

    elif (i == 'tu28'):
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Settings'])[1]/following::span[2]").click()
        driver.find_element_by_id("company_tax_number").click()
        driver.find_element_by_id("company_tax_number").clear()
        driver.find_element_by_id("company_tax_number").send_keys("25")
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Allowed File Types'])[1]/following::button[1]").click()

    elif (i == 'tu27'):
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Vendors'])[1]/following::span[1]").click()
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Accounts'])[1]/following::span[1]").click()
        driver.find_element_by_link_text("Add New").click()
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='From Account'])[1]/following::span[5]").click()
        driver.find_element_by_id("select2-to_account_id-container").click()
        driver.find_element_by_id("amount").click()
        driver.find_element_by_id("description").click()
        driver.find_element_by_id("description").clear()
        driver.find_element_by_id("description").send_keys("payment")
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Reference'])[1]/following::button[1]").click()

    elif (i == 'tu26'):
        driver.find_element_by_link_text("Reports").click()
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Tax Summary'])[1]/following::span[1]").click()
        driver.find_element_by_name("status").click()
        Select(driver.find_element_by_name("status")).select_by_visible_text("Paid")
        driver.find_element_by_name("status").click()
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Jan-Mar'])[1]/preceding::button[1]").click()

    elif (i == 'tu25'):
        driver.find_element_by_link_text("Reports").click()
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Expense Summary'])[1]/following::span[1]").click()
        driver.find_element_by_xpath("//input[@type='search']").click()
        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='×'])[1]/following::button[1]").click()

    # --- Usability Testing --- #
    elif (i == 'tv01'):
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Toggle navigation'])[1]/preceding::b[1]")
        driver.find_element_by_id("BiyWqLogjO")
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Total Incomes'])[1]/following::span[1]")
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Total Expenses'])[1]/following::span[1]")
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Total Profit'])[1]/following::span[1]")
        driver.find_element_by_id("bNTmKUhfIV")
        driver.find_element_by_id("BJekypGYis")
        driver.find_element_by_xpath("//img[@alt='MyApp']")
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Logout'])[1]/following::p[1]")
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Last login 15 minutes ago'])[1]/preceding::span[1]")

    elif (i == 'tv02'):
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Manage Companies'])[1]/following::span[2]").click()
        driver.find_element_by_link_text("Items").click()
        driver.find_element_by_link_text("Incomes").click()
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Incomes'])[1]/following::span[2]").click()
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Invoices'])[1]/following::span[1]").click()
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Revenues'])[1]/following::span[1]").click()
        driver.find_element_by_link_text("Expenses").click()
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Expenses'])[1]/following::span[2]").click()
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Bills'])[1]/following::span[1]").click()
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Payments'])[1]/following::span[1]").click()
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Vendors'])[1]/following::span[1]").click()
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Banking'])[2]/following::span[2]").click()
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Accounts'])[1]/following::span[1]").click()
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Transfers'])[1]/following::span[1]").click()
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Transactions'])[1]/following::span[1]").click()
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Reconciliations'])[1]/following::span[1]").click()
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Reports'])[1]/following::span[2]").click()
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Income Summary'])[1]/following::span[1]").click()
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Expense Summary'])[1]/following::span[1]").click()
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Income vs Expense'])[1]/following::span[1]").click()
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Tax Summary'])[1]/following::span[1]").click()
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Profit & Loss'])[1]/following::span[1]").click()
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Settings'])[1]/following::span[2]").click()
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='General'])[1]/following::span[1]").click()
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Categories'])[1]/following::span[1]").click()
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Currencies'])[1]/following::span[1]").click()
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Tax Rates'])[1]/following::span[1]").click()

    elif (i == 'tv03'):
        driver.find_element_by_link_text("Tekas").click()
        driver.find_element_by_link_text("Profile").click()

    elif (i == 'tv05'):
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

    elif(i == 'tv04'):
        driver.find_element_by_xpath("//div/ul/li/a/i").click()
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Apps'])[1]/following::section[1]").click()

    elif(i == 'tv15'):
        driver.find_element_by_xpath("//li[7]/a/span[2]/i").click()
        driver.find_element_by_xpath("//li[7]/a/span[2]/i").click()

    elif(i == 'tv14'):
        driver.find_element_by_xpath("//li[6]/a/span[2]/i").click()
        driver.find_element_by_xpath("//li[6]/a/span[2]/i").click()

    elif(i == 'tv13'):
        driver.find_element_by_xpath("//li[5]/a/span[2]/i").click()
        driver.find_element_by_xpath("//li[5]/a/span[2]/i").click()

    elif(i == 'tv12'):
        driver.find_element_by_xpath("//li[4]/a/span[2]/i").click()
        driver.find_element_by_xpath("//li[4]/a/span[2]/i").click()

    elif(i == 'tv11'):
        driver.find_element_by_xpath("//span[2]/i").click()
        driver.find_element_by_xpath("//span[2]/i").click()

    elif(i == 'tv10'):
        driver.find_element_by_xpath("//div[4]/div/div/div/div/button/i").click()

    elif(i == 'tv09'):
        driver.find_element_by_xpath("//div[2]/div/div/div/button/i").click()

    elif(i == 'tv08'):
        driver.find_element_by_xpath("//div/button/i").click()

    elif(i == 'tv07'):
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Toggle navigation'])[1]/preceding::b[1]").click()

    elif( i == 'tv06'):
        driver.find_element_by_xpath("//span[2]/i").click()
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Incomes'])[1]/following::span[2]").click()


    i = input("Enter your option (Test Case ID or 'stop') : ")

print("Done now")
driver.close()