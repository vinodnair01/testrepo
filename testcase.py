# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
binary = FirefoxBinary('/usr/lib/firefox/firefox')
driver = webdriver.Firefox(firefox_binary=binary)
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class ContactForm(unittest.TestCase):
    def setUp(self):
        from selenium import webdriver
	from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
	binary = FirefoxBinary('/usr/lib/firefox/firefox')
	self.driver = webdriver.Firefox(firefox_binary=binary)
	self.driver.implicitly_wait(30)
        self.base_url = "http://54.69.5.48"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_contact_form(self):
        driver = self.driver
        driver.get(self.base_url + "/contactform.htm")
        driver.find_element_by_id("Full_Name").clear()
        driver.find_element_by_id("Full_Name").send_keys("Test User")
        driver.find_element_by_id("Email_Address").clear()
        driver.find_element_by_id("Email_Address").send_keys("test@test.com")
        driver.find_element_by_id("Your_Message").clear()
        driver.find_element_by_id("Your_Message").send_keys("Test message")
        driver.find_element_by_id("AntiSpam").clear()
        driver.find_element_by_id("AntiSpam").send_keys("25")
        driver.find_element_by_css_selector("input[type=\"submit\"]").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
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
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
