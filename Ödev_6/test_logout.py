# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from webdriver_manager.chrome import ChromeDriverManager

class TestLogout():
  def setup_method(self, method):
    self.driver = webdriver.Chrome(ChromeDriverManager().install())
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_logout(self):
    self.driver.get("https://www.saucedemo.com/")
    self.driver.set_window_size(692, 728)
    WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "*[data-test=\"username\"]")))
    self.driver.find_element(By.ID, "user-name").click()
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"username\"]").send_keys("standard_user")
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"password\"]").click()
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"password\"]").send_keys("secret_sauce")
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"password\"]").send_keys(Keys.ENTER)
    WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located((By.ID, "react-burger-menu-btn")))
    self.driver.find_element(By.ID, "react-burger-menu-btn").click()
    WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located((By.ID, "logout_sidebar_link")))
    self.driver.find_element(By.ID, "logout_sidebar_link").click()
  
