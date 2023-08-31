from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from Utilities.BaseClass import BaseClass
import pytest
from TestData.HomePageData import HomePageData


class TestHomePage(BaseClass):

        def test_formsubmission(self, getData):
            log = self.getLogger()

            self.driver.find_element(By.NAME, "name").send_keys(getData["firstname"])                  # Find the element with the name attribute and send the keys "Jitendra"
            log.info("First Name Is " + getData["firstname"])

            self.driver.find_element(By.NAME, "email").send_keys(getData["email"])  # Find the element with the name attribute and send the keys "Jitendra@gmail.com"
            log.info("Email Is " + getData["email"])

            self.driver.find_element(By.ID, "exampleInputPassword1").send_keys(getData["Pass"])  # Find the element with the ID attribute and send the keys "123456"
            log.info("Password Is " + str(getData["Pass"]))         #we use str bcz can only concatenate str (not "int") to str, so we convert firstly integer value into string by using str

            self.driver.find_element(By.ID,"exampleCheck1").click()  # Find the element with the ID attribute and click on it

            # -- XPath  -- //tagname[@attributes='value']  --Example --> //input[@type='Submit']
            # -- XPath is used as a locator strategy to find the element with the specified attribute and value.
            self.driver.find_element(By.XPATH, "//input[@value='Submit']").click()  # Find the element using XPath and click on it

            # -- CssSelector -- tagname[attributes='value']
            # -- CssSelector is used as a locator strategy to find the element with the specified attribute and value.   -- Another way using #id & .classname in selectorshub
            self.driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("Jiten")  # Find the element using CSS Selector and send the keys "Jiten" to it
            self.driver.find_element(By.CSS_SELECTOR, "#inlineRadio1").click()  # We can find element (ID) using #ID
            self.driver.find_element(By.CSS_SELECTOR,".form-check-input").click()  # We can find element (Classname) using .classsname

            # -- ClassName -- Error Handling -- Use .text to know message and then by using variable print that
            # -- ClassName is used as a locator strategy to find the element with the specified class name
            message = self.driver.find_element(By.CLASS_NAME,'alert-success').text  # Find the element using ClassName and retrieve its text
            print(message)

            self.driver.refresh()               # use refresh method to refresh page because we have two test case to run on same page

