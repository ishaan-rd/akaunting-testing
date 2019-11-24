#register
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re


class C1(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_c1(self):
        driver = self.driver
        driver.get("https://akaunting.com/")
        driver.find_element_by_xpath("//div[@id='top-download']/a/i").click()
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='our'])[1]/following::span[1]").click()
        driver.find_element_by_id("register-form-first-name").click()
        driver.find_element_by_id("register-form-first-name").clear()
        driver.find_element_by_id("register-form-first-name").send_keys("Ajay")
        driver.find_element_by_id("register-form-email").clear()
        driver.find_element_by_id("register-form-email").send_keys("ckrishnanaik666@gmail.com")
        driver.find_element_by_id("register-form-password").click()
        driver.find_element_by_id("register-form-password").clear()
        driver.find_element_by_id("register-form-password").send_keys("Tejasku@11")
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | index=0 | ]]
        # driver.find_element_by_xpath("//span[@id='recaptcha-anchor']/div").click()
        time.sleep(100)
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | relative=parent | ]]
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Privacy Policy'])[1]/following::span[1]").click()

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
