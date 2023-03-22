from time import sleep
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class TestSauce():
    driver= webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https://www.saucedemo.com/")
    sleep(5)   
    
    def test_validUsername(self):
        driver=self.driver
        
        password=driver.find_element(By.ID,"password")
        password.send_keys("2")

        submit=driver.find_element(By.ID,"login-button").click()
        error_message=driver.find_element(By.XPATH,'//*[@id="login_button_container"]/div/form/div[3]')

        if error_message.text=="Epic sadface: Username is required":
            print(error_message.text)
        else:print("username has been typed.")


    def test_validPassword(self):
        driver=self.driver
        username=driver.find_element(By.ID,"user-name")
        username.send_keys("sauce")

        submit=driver.find_element(By.ID,"login-button").click()
        error_message=driver.find_element(By.XPATH,'//*[@id="login_button_container"]/div/form/div[3]/h3')

        if error_message.text=="Epic sadface: Password is required":
            print(error_message.text)
        else:print("password has been typed.")
    
    def test_invalidUser(self):
        driver=self.driver

        username=driver.find_element(By.ID,"user-name")
        username.send_keys("locked_out_user")

        password=driver.find_element(By.ID,"password")
        password.send_keys("secret_sauce")

        submit=driver.find_element(By.ID,"login-button").click()
        error_message=driver.find_element(By.XPATH,'//*[@id="login_button_container"]/div/form/div[3]/h3')
        
        expected_message="Epic sadface: Sorry, this user has been locked out."

        if error_message.text==expected_message:
            print(expected_message)
    def test_emptyInput(self):
        driver=self.driver

        username=driver.find_element(By.ID,"user-name")
        username.send_keys("")

        password=driver.find_element(By.ID,"password")
        password.send_keys("")
        
        submit=driver.find_element(By.ID,"login-button").click()
        sleep(3)

        error_button=driver.find_element(By.XPATH, '//*[@id="login_button_container"]/div/form/div[3]/h3/button').click()
    
    def redirecting_user(self):
        driver=self.driver

        username=driver.find_element(By.ID,"user-name")
        username.send_keys("standard_user")

        password=driver.find_element(By.ID,"password")
        password.send_keys("secret_sauce")
        submit=driver.find_element(By.ID,"login-button").click()

        print("Redirected to 'https://www.saucedemo.com/inventory.html'")

        #items
        listOfProducts=self.driver.find_elements(By.CLASS_NAME,"inventory_item")
        print(f"There are {len(listOfProducts)} products.")
        sleep(5)
        driver.quit()
        
        


test=TestSauce()
# test.test_validUsername
# test.test_validPassword()
# test.test_invalidUser()
# test.test_emptyInput()
test.redirecting_user()