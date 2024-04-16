# *************************************************************************************
# Title:        Group Project: Group 1 Module 8
# Author:       Robert Macklem
# Date:         April 14 2024
# Description:  Tests mini statement functionality
# *************************************************************************************
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class Module8Test (unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("Module 8 >> Setting up...")

        # Construct webdriver chrome instance
        cls.driver = webdriver.Chrome()

        # Login
        cls.driver.get("http://demo.guru99.com/V4/")

        mgr_id = "mngr564281"
        mgr_pass = "bAgenAp"

        mgr_id_field = cls.driver.find_element(By.CSS_SELECTOR, "input[name='uid']")
        mgr_pass_field = cls.driver.find_element(By.CSS_SELECTOR, "input[name='password']")
        login_btn = cls.driver.find_element(By.CSS_SELECTOR, "input[name='btnLogin']")

        mgr_id_field.send_keys(mgr_id)
        mgr_pass_field.send_keys(mgr_pass)
        login_btn.click()

        cls.driver.get("https://demo.guru99.com/V4/manager/MiniStatementInput.php")

    @classmethod
    def tearDownClass(cls):
        print("Module 8 >> Tearing down...")
        cls.driver.quit()

    # VERIFY ACCOUNT NO.
    def test_MS01(self):
        print("Module 8 >> Running test MS1")
        # Account No. cannot be empty

        # Step 1) Do nothing in ID Field
        acc_field = self.driver.find_element(By.CSS_SELECTOR, "input[name='accountno']")
        acc_field.clear()

        # Step 2) Tab to next Field
        acc_field.send_keys(Keys.TAB)

        # Get element
        id_warning_present = self.driver.find_element(
            By.XPATH, "//*[contains(text(), 'Account Number must not be blank')]").is_displayed()

        # Assert
        self.assertTrue(id_warning_present)

    def test_MS02_1(self):
        print("Module 8 >> Running test MS2.1")
        # Account No. cannot have char

        # Step 1) Input chars in field
        acc_field = self.driver.find_element(By.CSS_SELECTOR, "input[name='accountno']")
        acc_field.clear()

        # DATA 1
        acc_field.send_keys("1234")

        # Get element
        id_warning_present = self.driver.find_element(
            By.XPATH, "//*[contains(text(), 'Characters are not allowed')]").is_displayed()

        # Assert
        self.assertTrue(id_warning_present)

    def test_MS02_2(self):
        print("Module 8 >> Running test MS2.2")
        # Account No. cannot have char

        # Step 1) Input chars in field
        acc_field = self.driver.find_element(By.CSS_SELECTOR, "input[name='accountno']")
        acc_field.clear()

        # DATA 2
        acc_field.send_keys("Acc123")

        # Get element
        id_warning_present = self.driver.find_element(
            By.XPATH, "//*[contains(text(), 'Characters are not allowed')]").is_displayed()

        # Assert
        self.assertTrue(id_warning_present)

    def test_MS03_1(self):
        print("Module 8 >> Running test MS3.1")
        # Account No. cannot have special char

        # Step 1) Input spec chars in field
        acc_field = self.driver.find_element(By.CSS_SELECTOR, "input[name='accountno']")
        acc_field.clear()

        # DATA 1
        acc_field.send_keys("123!@#")

        # Get element
        id_warning_present = self.driver.find_element(
            By.XPATH, "//*[contains(text(), 'Special characters are not allowed')]").is_displayed()

        # Assert
        self.assertTrue(id_warning_present)

    def test_MS03_2(self):
        print("Module 8 >> Running test MS3.2")
        # Account No. cannot have special char

        # Step 1) Input spec chars in field
        acc_field = self.driver.find_element(By.CSS_SELECTOR, "input[name='accountno']")
        acc_field.clear()

        # DATA 2
        acc_field.send_keys("!@#")

        # Get element
        id_warning_present = self.driver.find_element(
            By.XPATH, "//*[contains(text(), 'Special characters are not allowed')]").is_displayed()

        # Assert
        self.assertTrue(id_warning_present)

    def test_MS04(self):
        print("Module 8 >> Running test MS4")
        # Account No. cannot have space

        # Step 1) Include space in acc input
        acc_field = self.driver.find_element(By.CSS_SELECTOR, "input[name='accountno']")
        acc_field.clear()

        # DATA
        acc_field.send_keys("123 12")

        # Get element
        id_warning_present = self.driver.find_element(
            By.XPATH, "//*[contains(text(), 'Characters are not allowed')]").is_displayed()

        # Assert
        self.assertTrue(id_warning_present)

    def test_MS05(self):
        print("Module 8 >> Running test MS5")
        # Account No. cannot have leading space

        # Step 1) Do nothing in ID Field
        acc_field = self.driver.find_element(By.CSS_SELECTOR, "input[name='accountno']")
        acc_field.clear()

        # DATA
        acc_field.send_keys(Keys.SPACE)
        acc_field.send_keys(Keys.TAB)

        # Get element
        id_warning_present = self.driver.find_element(
            By.XPATH, "//*[contains(text(), 'First character cannot have space')]").is_displayed()

        # Assert
        self.assertTrue(id_warning_present)

    # VERIFY SUBMIT
    def test_MS06(self):
        print("Module 8 >> Running test MS6")
        # Submit on valid account input

        # Step 1) Enter valid value in ID field
        acc_field = self.driver.find_element(By.CSS_SELECTOR, "input[name='accountno']")

        # DATA
        acc_field.clear()
        acc_field.send_keys("133849")  # Input acc no. that is valid

        # Step 2) Submit
        submit_btn = self.driver.find_element(By.CSS_SELECTOR, "input[name='AccSubmit']")
        submit_btn.click()

        # Get element
        statement_present = self.driver.find_element(
            By.XPATH, "//*[contains(text(), '133849')]").is_displayed()

        # Assert
        self.assertTrue(statement_present)

    def test_MS07(self):
        print("Module 8 >> Running test MS7")
        # Submit on invalid account input

        # Get back
        self.driver.get("https://demo.guru99.com/V4/manager/MiniStatementInput.php")

        # Step 1) Enter valid value in ID field
        acc_field = self.driver.find_element(By.CSS_SELECTOR, "input[name='accountno']")

        # DATA
        acc_field.clear()
        acc_field.send_keys("12345")

        # Step 2) Submit
        submit_btn = self.driver.find_element(By.CSS_SELECTOR, "input[name='AccSubmit']")
        submit_btn.click()

        # Get alert
        alert = self.driver.switch_to.alert

        # Assert
        self.assertTrue(alert.text == "Account does not exist")
        alert.accept()

    # VERIFY RESET
    def test_MS08(self):
        print("Module 8 >> Running test MS8")
        # Reset button

        # Get back
        self.driver.get("https://demo.guru99.com/V4/manager/MiniStatementInput.php")

        # Step 1) Enter any value in account field
        acc_field = self.driver.find_element(By.CSS_SELECTOR, "input[name='accountno']")

        # DATA
        acc_field.clear()
        acc_field.send_keys("qwer 123456")

        # Step 2) Submit
        submit_btn = self.driver.find_element(By.CSS_SELECTOR, "input[name='res']")
        submit_btn.click()

        # Assert
        self.assertTrue(acc_field.get_attribute("value") == "")


if __name__ == '__main__':
    unittest.main()
