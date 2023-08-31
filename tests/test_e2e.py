import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import pytest
from Utilities.BaseClass import BaseClass
import inspect
import logging


@pytest.mark.usefixtures("setup")

class Testone(BaseClass):
#GHG
    def test_e2e(self, setup):
        log = self.getLogger()
        self.driver.find_element(By.CSS_SELECTOR, "a[href*=shop]").click()
        products = self.driver.find_elements(By.CSS_SELECTOR, "div[class='card h-100']")
        log.info("gettting all cart details")

        for product in products:
            productName = product.find_element(By.XPATH, "div/h4/a").text
            log.info(productName)
            if productName == "Blackberry":
                product.find_element(By.XPATH, "div[2]/button").click()

        self.driver.find_element(By.XPATH, "//a[@class='nav-link btn btn-primary']").click()
        # self.driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()
        self.driver.find_element(By.CSS_SELECTOR, "button[class='btn btn-success']").click()
        self.driver.find_element(By.XPATH, "//a[@class='nav-link btn btn-primary']").click()
        self.driver.find_element(By.ID, "country").send_keys("ind")
        log.info("Entering Country Name as ind")
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
        self.driver.find_element(By.LINK_TEXT, "India").click()
        log.info("country selected as India")
        self.driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
        self.driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()

        successText = self.driver.find_element(By.XPATH, "//strong[normalize-space()='Success!']").text
        assert "Success!" in successText
        log.info(successText)

        print(successText)

        time.sleep(2)