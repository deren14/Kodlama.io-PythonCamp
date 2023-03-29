from time import sleep
from selenium import webdriver as webd
from selenium.webdriver.support.wait import WebDriverWait as wdwait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pytest



class Test_sauce:
    
    def setup_method(self):
        self.driver=webd.Chrome(ChromeDriverManager().install())
        self.driver.get("https://www.saucedemo.com/")

    def teardown_method(self):
        self.driver.close()

    def test_empty_login(self):
        driver=self.driver
        
        wdwait(driver, 10).until(ec.visibility_of_all_elements_located)
        
        driver.find_element(By.ID,"user-name").send_keys("")
        driver.find_element(By.ID,"password").send_keys("")
        
        driver.find_element(By.ID,"login-button").click()
        
        expected_warning="Epic sadface: Username is required"
        error_message=driver.find_element(By.XPATH,'//*[@id="login_button_container"]/div/form/div[3]/h3')
        
        assert error_message.text== expected_warning
        driver.save_screenshot("test_empty_login.png")
    def test_password(self):
        driver=self.driver

        
        wdwait(driver,10).until(ec.visibility_of_all_elements_located)
        
        driver.find_element(By.ID,"user-name").send_keys("akathen")
        driver.find_element(By.ID,"login-button").click()
        
        expected_message="Epic sadface: Password is required"
        error_message=driver.find_element(By.XPATH,'//*[@id="login_button_container"]/div/form/div[3]/h3')
        
        assert error_message.text==expected_message
        driver.save_screenshot("test_password.png")
    def test_lockedout_user(self):
        driver=self.driver

        wdwait(driver,10).until(ec.visibility_of_all_elements_located)

        driver.find_element(By.ID,"user-name").send_keys("locked_out_user")
        driver.find_element(By.ID,"password").send_keys("secret_sauce")

        driver.find_element(By.ID,"login-button").click()   

        expected_message="Epic sadface: Sorry, this user has been locked out."
        error_message=driver.find_element(By.XPATH,'//*[@id="login_button_container"]/div/form/div[3]/h3')

        assert error_message.text==expected_message
        driver.save_screenshot("test_lockedout_user.png")

    
    #Parametrize function
    @pytest.mark.parametrize("username",["standard_user","problem_user","performance_glitch_user"])
    def test_valid_login(self,username):
        driver=self.driver
        
        driver.find_element(By.ID,"user-name").send_keys(username)
        driver.find_element(By.ID,"password").send_keys("secret_sauce")

        driver.find_element(By.ID,"login-button").click()
        assert wdwait(driver,10).until(ec.url_changes)
        driver.save_screenshot("test_valid_login.png")

    def test_add_toChart(self):
        driver=self.driver
        
        driver.find_element(By.ID,"user-name").send_keys("standard_user")
        driver.find_element(By.ID,"password").send_keys("secret_sauce")
        driver.find_element(By.ID,"login-button").click()

        wdwait(driver,10).until(ec.visibility_of_all_elements_located)
        driver.find_element(By.ID,"add-to-cart-sauce-labs-backpack").click()
        
        assert wdwait(driver,10).until(ec.visibility_of_element_located((By.ID,"remove-sauce-labs-backpack")))
        driver.save_screenshot("test_add_toChart.png")
    def test_error_icon(self):
        driver=self.driver

        driver.find_element(By.ID,"user-name").send_keys("standart_user")
        driver.find_element(By.ID,"password").send_keys("secrett_sauce")
        driver.find_element(By.ID,"login-button").click()

        assert wdwait(driver,20).until(ec.visibility_of_element_located((By.CSS_SELECTOR,'#login_button_container > div > form > div:nth-child(1) > svg')))
        driver.save_screenshot("test_error_icon.png")

    def test_logout(self):
        driver=self.driver

        driver.find_element(By.ID,"user-name").send_keys("standard_user")
        driver.find_element(By.ID,"password").send_keys("secret_sauce")

        driver.find_element(By.ID,"login-button").click()
        
        wdwait(driver, 20).until(ec.element_to_be_clickable((By.ID, "react-burger-menu-btn"))).click()
        
        wdwait(driver, 20).until(ec.element_to_be_clickable((By.ID, "logout_sidebar_link"))).click()

        assert wdwait(driver,10).until(ec.url_to_be("https://www.saucedemo.com/"))
        driver.save_screenshot("test_logout.png")
        