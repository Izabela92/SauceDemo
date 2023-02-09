from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
from time import sleep
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

class LoginTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        # Prepare the test
        # self.driver = webdriver.Firefox()
        self.driver.get("https://www.saucedemo.com/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def testLoginWithIncorrectCredentials(self):
        driver = self.driver

        # Find and fill the username field
        username = driver.find_element(By.ID, "user-name")
        username.clear()
        username.send_keys("incorrect_username")

        # Find and fill the password field
        password = driver.find_element(By.ID, "password")
        password.clear()
        password.send_keys("incorrect_password")

        # Find and click the login button
        login_button = driver.find_element(By.CSS_SELECTOR, ".btn_action")
        login_button.click()

        # Verify that the error message is displayed
        error_message = driver.find_element(By.CSS_SELECTOR, ".error-message-container")
        self.assertTrue(error_message.is_displayed())

    def tearDown(self):
        self.driver.quit()