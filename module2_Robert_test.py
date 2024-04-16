# *************************************************************************************
# Title:        Group Project: Group 1 Module 2
# Author:       Robert Macklem
# Date:         April 14 2024
# Description:  Tests edit customer functionality
# *************************************************************************************
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class Module2Test (unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("Module 2 >> Setting up...")

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

        cls.driver.get("https://demo.guru99.com/V4/manager/EditCustomer.php")

    @classmethod
    def tearDownClass(cls):
        print("Module 2 >> Tearing down...")
        cls.driver.quit()

    # VERIFY CUSTOMER ID
    def test_EC01(self):
        print("Module 2 >> Running test EC1")
        # Customer ID must not be empty

        # Step 1) Do nothing in ID Field
        cust_id_field = self.driver.find_element(By.CSS_SELECTOR, "input[name='cusid']")
        cust_id_field.click()

        # Step 2) Tab to next Field
        cust_id_field.send_keys(Keys.TAB)

        # Get element
        id_warning_present = self.driver.find_element(
            By.XPATH, "//*[contains(text(), 'Customer ID is required')]").is_displayed()

        # Assert
        self.assertTrue(id_warning_present)

    def test_EC02_1(self):
        print("Module 2 >> Running test EC2.1")
        # Customer id must not have alpha chars

        # Step 1) Enter character value in ID field
        cust_id_field = self.driver.find_element(By.CSS_SELECTOR, "input[name='cusid']")

        # DATA 1
        cust_id_field.clear()
        cust_id_field.send_keys("1234Acc")

        # Get element
        id_warning_present = self.driver.find_element(
            By.XPATH, "//*[contains(text(), 'Characters are not allowed')]").is_displayed()

        # Assert
        self.assertTrue(id_warning_present, "Text 'Characters are not allowed' is not present on the page")

    def test_EC02_2(self):
        print("Module 2 >> Running test EC2.2")
        # Customer id must not have alpha chars

        # Step 1) Enter character value in ID field
        cust_id_field = self.driver.find_element(By.CSS_SELECTOR, "input[name='cusid']")

        # DATA 2
        cust_id_field.clear()
        cust_id_field.send_keys("Acc1234")

        # Get element
        id_warning_present = self.driver.find_element(
            By.XPATH, "//*[contains(text(), 'Characters are not allowed')]").is_displayed()

        # Assert
        self.assertTrue(id_warning_present, "Text 'Characters are not allowed' is not present on the page")

    def test_EC03_1(self):
        print("Module 2 >> Running test EC3.1")
        # Customer id must not have special chars

        # Step 1) Enter character value in ID field
        cust_id_field = self.driver.find_element(By.CSS_SELECTOR, "input[name='cusid']")

        # DATA 1
        cust_id_field.clear()
        cust_id_field.send_keys("123!@#")

        # Get element
        id_warning_present = self.driver.find_element(
            By.XPATH, "//*[contains(text(), 'Special characters are not allowed')]").is_displayed()

        # Assert
        self.assertTrue(id_warning_present, "Text 'Special characters are not allowed' is not present on the page")

    def test_EC03_2(self):
        print("Module 2 >> Running test EC3.2")
        # Customer id must not have special chars

        # Step 1) Enter character value in ID field
        cust_id_field = self.driver.find_element(By.CSS_SELECTOR, "input[name='cusid']")

        # DATA 2
        cust_id_field.clear()
        cust_id_field.send_keys("!@#")

        # Get element
        id_warning_present = self.driver.find_element(
            By.XPATH, "//*[contains(text(), 'Special characters are not allowed')]").is_displayed()

        # Assert
        self.assertTrue(id_warning_present, "Text 'Special characters are not allowed' is not present on the page")

    def test_EC04(self):
        print("Module 2 >> Running test EC4")
        # Valid customer ID

        # Step 1) Enter character value in ID field
        cust_id_field = self.driver.find_element(By.CSS_SELECTOR, "input[name='cusid']")
        cust_id_field.clear()
        cust_id_field.send_keys("64100")  # Edit here to swap cust ID on test

        # Step 2) Submit
        submit_btn = self.driver.find_element(By.CSS_SELECTOR, "input[name='AccSubmit']")
        submit_btn.click()

        # Assert
        self.assertEqual(self.driver.current_url, "https://demo.guru99.com/V4/manager/editCustomerPage.php",
                         "Redirect failed.")

    # VERIFY ADDRESS
    def test_EC05(self):
        print("Module 2 >> Running test EC5")
        # Verify address field

        # Step 1) Do not add a value in addr field
        addr_field = self.driver.find_element(By.CSS_SELECTOR, "textarea[name='addr']")
        addr_field.clear()

        # Step 2) Tab off
        addr_field.send_keys(Keys.TAB)

        # Get element
        addr_warning_present = self.driver.find_element(
            By.XPATH, "//*[contains(text(), 'Address Field must be blank')]").is_displayed()

        # Assert
        self.assertTrue(addr_warning_present)

    # VERIFY CITY
    def test_EC06(self):
        print("Module 2 >> Running test EC6")
        # Verify city field, cannot be empty

        # Step 1) Do not enter a value in city field
        city_field = self.driver.find_element(By.CSS_SELECTOR, "input[name='city']")
        city_field.clear()

        # Step 2) Tab off
        city_field.send_keys(Keys.TAB)

        # Get element
        city_warning_present = self.driver.find_element(
            By.XPATH, "//*[contains(text(), 'City Field must not be blank')]").is_displayed()

        # Assert
        self.assertTrue(city_warning_present)

    def test_EC07_1(self):
        print("Module 2 >> Running test EC7.1")
        # Verify city field, cannot be numeric

        # Step 1) Enter invalid value in city field
        city_field = self.driver.find_element(By.CSS_SELECTOR, "input[name='city']")

        # DATA 1
        city_field.clear()
        city_field.send_keys("1234")

        # Get element
        city_warning_present = self.driver.find_element(
            By.XPATH, "//*[contains(text(), 'Numbers are allowed')]").is_displayed()

        # Assert
        self.assertTrue(city_warning_present)

    def test_EC07_2(self):
        print("Module 2 >> Running test EC7.2")
        # Verify city field, cannot be numeric

        # Step 1) Enter invalid value in city field
        city_field = self.driver.find_element(By.CSS_SELECTOR, "input[name='city']")

        # DATA 2
        city_field.clear()
        city_field.send_keys("city123")

        # Get element
        city_warning_present = self.driver.find_element(
            By.XPATH, "//*[contains(text(), 'Numbers are allowed')]").is_displayed()

        # Assert
        self.assertTrue(city_warning_present)

    def test_EC08_1(self):
        print("Module 2 >> Running test EC8.1")
        # Verify city field, cannot be special char

        # Step 1) Enter invalid value in city field
        city_field = self.driver.find_element(By.CSS_SELECTOR, "input[name='city']")

        # DATA 1
        city_field.clear()
        city_field.send_keys("City!@#")

        # Get element
        city_warning_present = self.driver.find_element(
            By.XPATH, "//*[contains(text(), 'Special characters are not allowed')]").is_displayed()

        # Assert
        self.assertTrue(city_warning_present)

    def test_EC08_2(self):
        print("Module 2 >> Running test EC8.2")
        # Verify city field, cannot be special char

        # Step 1) Enter invalid value in city field
        city_field = self.driver.find_element(By.CSS_SELECTOR, "input[name='city']")

        # DATA 2
        city_field.clear()
        city_field.send_keys("!@#")

        # Get element
        city_warning_present = self.driver.find_element(
            By.XPATH, "//*[contains(text(), 'Special characters are not allowed')]").is_displayed()

        # Assert
        self.assertTrue(city_warning_present)

    # VERIFY STATE
    def test_EC09(self):
        print("Module 2 >> Running test EC9")
        # Verify state field, cannot be empty

        # Step 1) Enter no value in state field
        state_field = self.driver.find_element(By.CSS_SELECTOR, "input[name='state']")
        state_field.clear()

        # Step 2) Tab off
        state_field.send_keys(Keys.TAB)

        # Get element
        state_warning_present = self.driver.find_element(
            By.XPATH, "//*[contains(text(), 'State must be blank')]").is_displayed()

        # Assert
        self.assertTrue(state_warning_present)

    def test_EC10_1(self):
        print("Module 2 >> Running test EC10.1")
        # Verify state field, cannot be numeric

        # Step 1) Enter numeric chars in state field
        state_field = self.driver.find_element(By.CSS_SELECTOR, "input[name='state']")

        # DATA 1
        state_field.clear()
        state_field.send_keys("1234")

        # Get element
        state_warning_present = self.driver.find_element(
            By.XPATH, "//*[contains(text(), 'Numbers are not allowed')]").is_displayed()

        # Assert
        self.assertTrue(state_warning_present)

    def test_EC10_2(self):
        print("Module 2 >> Running test EC10.2")
        # Verify state field, cannot be numeric

        # Step 1) Enter numeric chars in state field
        state_field = self.driver.find_element(By.CSS_SELECTOR, "input[name='state']")

        # DATA 2
        state_field.clear()
        state_field.send_keys("State123")

        # Get element
        state_warning_present = self.driver.find_element(
            By.XPATH, "//*[contains(text(), 'Numbers are not allowed')]").is_displayed()

        # Assert
        self.assertTrue(state_warning_present)

    def test_EC11_1(self):
        print("Module 2 >> Running test EC11.1")
        # Verify state field, cannot be special char

        # Step 1) Enter numeric chars in state field
        state_field = self.driver.find_element(By.CSS_SELECTOR, "input[name='state']")

        # DATA 1
        state_field.clear()
        state_field.send_keys("State!@#")

        # Get element
        state_warning_present = self.driver.find_element(
            By.XPATH, "//*[contains(text(), 'Special characters are not allowed')]").is_displayed()

        # Assert
        self.assertTrue(state_warning_present)

    def test_EC11_2(self):
        print("Module 2 >> Running test EC11.2")
        # Verify state field, cannot be special char

        # Step 1) Enter numeric chars in state field
        state_field = self.driver.find_element(By.CSS_SELECTOR, "input[name='state']")

        # DATA 2
        state_field.clear()
        state_field.send_keys("!@#")

        # Get element
        state_warning_present = self.driver.find_element(
            By.XPATH, "//*[contains(text(), 'Special characters are not allowed')]").is_displayed()

        # Assert
        self.assertTrue(state_warning_present)

    # VERIFY PIN
    def test_EC12_1(self):
        print("Module 2 >> Running test EC12.1")
        # Verify PIN field, must be numeric

        # Step 1) Enter value in pin field
        pin_field = self.driver.find_element(By.CSS_SELECTOR, "input[name='pinno']")

        # DATA 1
        pin_field.clear()
        pin_field.send_keys("1234")

        # Get element
        pin_warning_present = self.driver.find_element(
            By.XPATH, "//*[contains(text(), 'Characters are not allowed')]").is_displayed()

        # Assert
        self.assertTrue(pin_warning_present)

    def test_EC12_2(self):
        print("Module 2 >> Running test EC12.2")
        # Verify PIN field, must be numeric

        # Step 1) Enter value in pin field
        pin_field = self.driver.find_element(By.CSS_SELECTOR, "input[name='pinno']")

        # DATA 2
        pin_field.clear()
        pin_field.send_keys("1234PIN")

        # Get element
        pin_warning_present = self.driver.find_element(
            By.XPATH, "//*[contains(text(), 'Characters are not allowed')]").is_displayed()

        # Assert
        self.assertTrue(pin_warning_present)

    def test_EC13(self):
        print("Module 2 >> Running test EC13")
        # Verify pin field, cannot be empty

        # Step 1) Enter no value in pin field
        pin_field = self.driver.find_element(By.CSS_SELECTOR, "input[name='pinno']")
        pin_field.clear()

        # Step 2) Tab off
        pin_field.send_keys(Keys.TAB)

        # Get element
        pin_warning_present = self.driver.find_element(
            By.XPATH, "//*[contains(text(), 'PIN Code must not be blank')]").is_displayed()

        # Assert
        self.assertTrue(pin_warning_present)

    def test_EC14_1(self):
        print("Module 2 >> Running test EC14.1")
        # Verify PIN field, must be 6 digits
        pin_field = self.driver.find_element(By.CSS_SELECTOR, "input[name='pinno']")

        # Step 1) > 6 digits

        # DATA
        pin_field.clear()
        pin_field.send_keys("1234567")

        # Get element
        pin_warning_present = self.driver.find_element(
            By.XPATH, "//*[contains(text(), 'PIN Code must have 6 Digits')]").is_displayed()

        # Assert
        self.assertTrue(pin_warning_present)

    def test_EC14_2(self):
        print("Module 2 >> Running test EC14.2")
        # Verify PIN field, must be 6 digits
        pin_field = self.driver.find_element(By.CSS_SELECTOR, "input[name='pinno']")

        # Step 2) < 6 digits

        # DATA
        pin_field.clear()
        pin_field.send_keys("123")

        # Get element
        pin_warning_present = self.driver.find_element(
            By.XPATH, "//*[contains(text(), 'PIN Code must have 6 Digits')]").is_displayed()

        # Assert
        self.assertTrue(pin_warning_present)

    def test_EC15_1(self):
        print("Module 2 >> Running test EC15.1")
        # Verify PIN field, must not have special chars

        # Step 1) Enter value in pin field
        pin_field = self.driver.find_element(By.CSS_SELECTOR, "input[name='pinno']")

        # DATA 1
        pin_field.clear()
        pin_field.send_keys("!@#")

        # Get element
        pin_warning_present = self.driver.find_element(
            By.XPATH, "//*[contains(text(), 'Special characters are not allowed')]").is_displayed()

        # Assert
        self.assertTrue(pin_warning_present)

    def test_EC15_2(self):
        print("Module 2 >> Running test EC15.2")
        # Verify PIN field, must not have special chars

        # Step 1) Enter value in pin field
        pin_field = self.driver.find_element(By.CSS_SELECTOR, "input[name='pinno']")

        # DATA 2
        pin_field.clear()
        pin_field.send_keys("123!@#")

        # Get element
        pin_warning_present = self.driver.find_element(
            By.XPATH, "//*[contains(text(), 'Special characters are not allowed')]").is_displayed()

        # Assert
        self.assertTrue(pin_warning_present)

    # VERIFY MOBILE NUMBER
    def test_EC16(self):
        print("Module 2 >> Running test EC16")
        # Verify phone field, cannot be empty

        # Step 1) Enter no value in pin field
        phone_field = self.driver.find_element(By.CSS_SELECTOR, "input[name='telephoneno']")
        phone_field.clear()

        # Step 2) Tab off
        phone_field.send_keys(Keys.TAB)

        # Get element
        phone_warning_present = self.driver.find_element(
            By.XPATH, "//*[contains(text(), 'Telephone no must not be blank')]").is_displayed()

        # Assert
        self.assertTrue(phone_warning_present)

    def test_EC17_1(self):
        print("Module 2 >> Running test EC17.1")
        # Verify phone field, must not have special chars

        # Step 1) Enter value in pin field
        phone_field = self.driver.find_element(By.CSS_SELECTOR, "input[name='pinno']")

        # DATA 1
        phone_field.clear()
        phone_field.send_keys("886636!@12")

        # Get element
        phone_warning_present = self.driver.find_element(
            By.XPATH, "//*[contains(text(), 'Special characters are not allowed')]").is_displayed()

        # Assert
        self.assertTrue(phone_warning_present)

    def test_EC17_2(self):
        print("Module 2 >> Running test EC17.2")
        # Verify phone field, must not have special chars

        # Step 1) Enter value in pin field
        phone_field = self.driver.find_element(By.CSS_SELECTOR, "input[name='pinno']")

        # DATA 2
        phone_field.clear()
        phone_field.send_keys("!@88662682")

        # Get element
        phone_warning_present = self.driver.find_element(
            By.XPATH, "//*[contains(text(), 'Special characters are not allowed')]").is_displayed()

        # Assert
        self.assertTrue(phone_warning_present)

    def test_EC17_3(self):
        print("Module 2 >> Running test EC17.3")
        # Verify phone field, must not have special chars

        # Step 1) Enter value in pin field
        phone_field = self.driver.find_element(By.CSS_SELECTOR, "input[name='pinno']")

        # DATA 3
        phone_field.clear()
        phone_field.send_keys("88663682!@")

        # Get element
        phone_warning_present = self.driver.find_element(
            By.XPATH, "//*[contains(text(), 'Special characters are not allowed')]").is_displayed()

        # Assert
        self.assertTrue(phone_warning_present)

    # VERIFY EMAIL
    def test_EC18(self):
        print("Module 2 >> Running test EC18")
        # Verify email field, cannot be empty

        # Step 1) Enter no value in pin field
        email_field = self.driver.find_element(By.CSS_SELECTOR, "input[name='emailid']")
        email_field.clear()

        # Step 2) Tab off
        email_field.send_keys(Keys.TAB)

        # Get element
        email_warning_present = self.driver.find_element(
            By.XPATH, "//*[contains(text(), 'Email-ID must not be blank')]").is_displayed()

        # Assert
        self.assertTrue(email_warning_present)

    def test_EC19_1(self):
        print("Module 2 >> Running test EC19.1")
        # Verify email field, email must be valid format

        # Step 1) Enter value in pin field
        email_field = self.driver.find_element(By.CSS_SELECTOR, "input[name='emailid']")

        # DATA 1
        email_field.clear()
        email_field.send_keys("guru99@gmail")

        # Get element
        email_warning_present = self.driver.find_element(
            By.XPATH, "//*[contains(text(), 'Email-ID is not valid')]").is_displayed()

        # Assert
        self.assertTrue(email_warning_present)

    def test_EC19_2(self):
        print("Module 2 >> Running test EC19.2")
        # Verify email field, email must be valid format

        # Step 1) Enter value in pin field
        email_field = self.driver.find_element(By.CSS_SELECTOR, "input[name='emailid']")

        # DATA 2
        email_field.clear()
        email_field.send_keys("guru99")

        # Get element
        email_warning_present = self.driver.find_element(
            By.XPATH, "//*[contains(text(), 'Email-ID is not valid')]").is_displayed()

        # Assert
        self.assertTrue(email_warning_present)

    def test_EC19_3(self):
        print("Module 2 >> Running test EC19.3")
        # Verify email field, email must be valid format

        # Step 1) Enter value in pin field
        email_field = self.driver.find_element(By.CSS_SELECTOR, "input[name='emailid']")

        # DATA 3
        email_field.clear()
        email_field.send_keys("Guru99@")

        # Get element
        email_warning_present = self.driver.find_element(
            By.XPATH, "//*[contains(text(), 'Email-ID is not valid')]").is_displayed()

        # Assert
        self.assertTrue(email_warning_present)

    def test_EC19_4(self):
        print("Module 2 >> Running test EC19.4")
        # Verify email field, email must be valid format

        # Step 1) Enter value in pin field
        email_field = self.driver.find_element(By.CSS_SELECTOR, "input[name='emailid']")

        # DATA 4
        email_field.clear()
        email_field.send_keys("gurugmail.com")

        # Get element
        email_warning_present = self.driver.find_element(
            By.XPATH, "//*[contains(text(), 'Email-ID is not valid')]").is_displayed()

        # Assert
        self.assertTrue(email_warning_present)

    def test_EC20(self):
        print("Module 2 >> Running test EC20")
        # Submit after changes

        # Step 1) Enter value in pin field
        submit_btn = self.driver.find_element(By.CSS_SELECTOR, "input[name='sub']")
        submit_btn.click()


if __name__ == '__main__':
    unittest.main()
