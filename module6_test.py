# *************************************************************************************
# Title:        Group Project: Group 1 Module 6
# Author:       Robert Macklem
# Date:         April 14 2024
# Description:  Tests delete account functionality
# *************************************************************************************
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class Module6Test (unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("Module 6 >> Setting up...")

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

        cls.driver.get("https://demo.guru99.com/V4/manager/deleteAccountInput.php")

    @classmethod
    def tearDownClass(cls):
        print("Module 6 >> Tearing down...")
        cls.driver.quit()

    # VERIFY ACCOUNT NO.
    def test_DA01(self):
        print("Module 6 >> Running test DA1")
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

    def test_DA02_1(self):
        print("Module 6 >> Running test DA2.1")
        # Acc id must not have alpha chars

        # Step 1) Enter character value in ID field
        acc_field = self.driver.find_element(By.CSS_SELECTOR, "input[name='accountno']")

        # DATA 1
        acc_field.clear()
        acc_field.send_keys("1234")

        # Get element
        id_warning_present = self.driver.find_element(
            By.XPATH, "//*[contains(text(), 'Characters are not allowed')]").is_displayed()

        # Assert
        self.assertTrue(id_warning_present, "Text 'Characters are not allowed' is not present on the page")

    def test_DA02_2(self):
        print("Module 6 >> Running test DA2.2")
        # Acc id must not have alpha chars

        # Step 1) Enter character value in ID field
        acc_field = self.driver.find_element(By.CSS_SELECTOR, "input[name='accountno']")

        # DATA 2
        acc_field.clear()
        acc_field.send_keys("Acc123")

        # Get element
        id_warning_present = self.driver.find_element(
            By.XPATH, "//*[contains(text(), 'Characters are not allowed')]").is_displayed()

        # Assert
        self.assertTrue(id_warning_present, "Text 'Characters are not allowed' is not present on the page")

    def test_DA03_1(self):
        print("Module 6 >> Running test DA3.1")
        # Acc id must not have special chars

        # Step 1) Enter spec character value in ID field
        acc_field = self.driver.find_element(By.CSS_SELECTOR, "input[name='accountno']")

        # DATA 1
        acc_field.clear()
        acc_field.send_keys("123!@#")

        # Get element
        id_warning_present = self.driver.find_element(
            By.XPATH, "//*[contains(text(), 'Special characters are not allowed')]").is_displayed()

        # Assert
        self.assertTrue(id_warning_present, "Text 'Special characters are not allowed' is not present on the page")

    def test_DA03_2(self):
        print("Module 6 >> Running test DA3.2")
        # Acc id must not have special chars

        # Step 1) Enter spec character value in ID field
        acc_field = self.driver.find_element(By.CSS_SELECTOR, "input[name='accountno']")

        # DATA 2
        acc_field.clear()
        acc_field.send_keys("!@#")

        # Get element
        id_warning_present = self.driver.find_element(
            By.XPATH, "//*[contains(text(), 'Special characters are not allowed')]").is_displayed()

        # Assert
        self.assertTrue(id_warning_present, "Text 'Special characters are not allowed' is not present on the page")

    def test_DA04(self):
        print("Module 6 >> Running test DA4")
        # Acc id must not have blank space

        # Step 1) Enter character value in ID field
        acc_field = self.driver.find_element(By.CSS_SELECTOR, "input[name='accountno']")

        # DATA
        acc_field.clear()
        acc_field.send_keys("123 12")

        # Get element
        id_warning_present = self.driver.find_element(
            By.XPATH, "//*[contains(text(), 'Characters are not allowed')]").is_displayed()

        # Assert
        self.assertTrue(id_warning_present, "Text 'Characters are not allowed' is not present on the page")

    def test_DA05(self):
        print("Module 6 >> Running test DA5")
        # Acc id must not have leading space

        # Step 1) Enter space value in ID field
        acc_field = self.driver.find_element(By.CSS_SELECTOR, "input[name='accountno']")
        acc_field.clear()
        acc_field.send_keys(Keys.SPACE)
        acc_field.send_keys(Keys.TAB)

        # Get element
        id_warning_present = self.driver.find_element(
            By.XPATH, "//*[contains(text(), 'First character cannot have space')]").is_displayed()

        # Assert
        self.assertTrue(id_warning_present, "Text 'First character cannot have space' is not present on the page")

    # VERIFY SUBMIT
    def test_DA06(self):
        print("Module 6 >> Running test DA6")
        # Submit on valid account input

        # Step 1) Enter character value in ID field
        acc_field = self.driver.find_element(By.CSS_SELECTOR, "input[name='accountno']")

        # DATA
        acc_field.clear()
        acc_field.send_keys("133849")  # Input acc no. that is valid

        # Step 2) Submit
        submit_btn = self.driver.find_element(By.CSS_SELECTOR, "input[name='AccSubmit']")
        submit_btn.click()

        # Step 3) Confirm
        alert = self.driver.switch_to.alert
        alert.accept()

        error_alert = self.driver.switch_to.alert

        # Assert
        self.assertEqual(error_alert.text, "Account deleted successfully")

    def test_DA07(self):
        print("Module 6 >> Running test DA7")
        # Submit on invalid account input

        # Get back to page after last test
        self.driver.get("https://demo.guru99.com/V4/manager/deleteAccountInput.php")

        # Step 1) Enter character value in ID field
        acc_field = self.driver.find_element(By.CSS_SELECTOR, "input[name='accountno']")

        # DATA
        acc_field.clear()
        acc_field.send_keys("12345")

        # Step 2) Submit
        submit_btn = self.driver.find_element(By.CSS_SELECTOR, "input[name='AccSubmit']")
        submit_btn.click()

        # Step 3) Confirm
        alert = self.driver.switch_to.alert
        alert.accept()

        error_alert = self.driver.switch_to.alert

        # Assert
        self.assertEqual(error_alert.text, "Account does not exist")
        error_alert.accept()

    # VERIFY RESET
    def test_DA08(self):
        print("Module 6 >> Running test DA8")
        # Reset button

        # Get back
        self.driver.get("https://demo.guru99.com/V4/manager/deleteAccountInput.php")

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
