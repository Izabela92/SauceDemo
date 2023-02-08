from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import unittest


class LoginTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://www.saucedemo.com/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def test_login(self):
        driver = self.driver

        # Input username
        username = driver.find_element(By.ID,"user-name")
        username.send_keys("standard_user")

        # Input password
        password = driver.find_element(By.ID,"password")
        password.send_keys("secret_sauce")

        # Click the login button
        driver.find_element(By.CLASS_NAME,"btn_action").click()

        # Wait for the page to load
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "inventory_filter_container")))

        # Check if login was successful by checking if the user's account name is displayed
        assert "standard_user" in driver.find_element(By.CLASS_NAME,"product_label").text

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
