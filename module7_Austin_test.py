import unittest
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from time import sleep

class BankTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Construct webdriver chrome instance
        cls.browser = webdriver.Chrome()

        # Login
        cls.browser.get("http://demo.guru99.com/V4/")

        mgr_id = "mngr564281"
        mgr_pass = "bAgenAp"

        mgr_id_field = cls.browser.find_element(By.CSS_SELECTOR, "input[name='uid']")
        mgr_pass_field = cls.browser.find_element(By.CSS_SELECTOR, "input[name='password']")
        login_btn = cls.browser.find_element(By.CSS_SELECTOR, "input[name='btnLogin']")

        mgr_id_field.send_keys(mgr_id)
        mgr_pass_field.send_keys(mgr_pass)
        login_btn.click()

        cls.browser.get("https://demo.guru99.com/V4/manager/BalEnqInput.php")

    def test_BE01_no_data(self):
        balance_field = self.browser.find_element(By.XPATH, '//tbody/tr[6]/td[2]/input[1]')
        balance_field.clear()
        balance_field.send_keys(Keys.TAB)

        space_alert = self.browser.find_element(By.XPATH, "//label[@id='message2']")
        alert_text = space_alert.text
        expected_alert = "Account Number must not be blank"
        self.assertEqual(alert_text, expected_alert, "not correct alert")

    def test_BE02_chars(self):
        balance_field = self.browser.find_element(By.XPATH, '//tbody/tr[6]/td[2]/input[1]')
        balance_field.clear()
        balance_field.send_keys('1234acc123')
        balance_field.send_keys(Keys.TAB)

        char_alert = self.browser.find_element(By.XPATH, "//label[@id='message2']")
        alert_text = char_alert.text
        expected_alert = "Characters are not allowed"
        self.assertEqual(alert_text, expected_alert, "not correct alert")

    def test_BE03_special(self):
        balance_field = self.browser.find_element(By.XPATH, '//tbody/tr[6]/td[2]/input[1]')
        balance_field.clear()
        balance_field.send_keys('123!@#!@#')
        balance_field.send_keys(Keys.TAB)

        specialchar_alert = self.browser.find_element(By.XPATH, "//label[@id='message2']")
        alert_text = specialchar_alert.text
        expected_alert = "Special characters are not allowed"
        self.assertEqual(alert_text, expected_alert, "not correct alert")

    def test_BE04_space(self):
        balance_field = self.browser.find_element(By.XPATH, '//tbody/tr[6]/td[2]/input[1]')
        balance_field.clear()
        balance_field.send_keys(" ")
        balance_field.send_keys(Keys.TAB)

        specialchar_alert = self.browser.find_element(By.XPATH, "//label[@id='message2']")
        alert_text = specialchar_alert.text
        expected_alert = "Characters are not allowed"
        self.assertEqual(alert_text, expected_alert, "not correct alert")

    def test_BE05_valid_account(self):
        # next perform a balance enquiry
        balance_button = self.browser.find_element(By.XPATH, "//a[contains(text(),'Balance Enquiry')]")
        balance_button.click()
        self.browser.refresh()
        balance_button = self.browser.find_element(By.XPATH, "//a[contains(text(),'Balance Enquiry')]")
        balance_button.click()

        balance_field = self.browser.find_element(By.XPATH, '//tbody/tr[6]/td[2]/input[1]')
        balance_field.click()
        balance_field.send_keys('134139')
        balance_field.send_keys(Keys.TAB)

    def test_BE06_invalid_account(self):
        balance_field = self.browser.find_element(By.XPATH, '//tbody/tr[6]/td[2]/input[1]')
        balance_field.click()
        balance_field.send_keys("12345")
        balance_field.send_keys(Keys.TAB)
        account_no_submit = self.browser.find_element(By.XPATH, "//input[@name='AccSubmit']")
        account_no_submit.click()

        alert_text = self.browser.switch_to.alert
        popup_text = alert_text.text
        expected_alert = "Account does not exist"
        assert expected_alert in popup_text, (f"Popup content does not match expected content. "
                                              f"Expected: {expected_alert}, Actual: {popup_text}")
        alert_text.accept()

    def test_BE07_reset_button(self):
        balance_field = self.browser.find_element(By.XPATH, '//tbody/tr[6]/td[2]/input[1]')
        balance_field.click()
        balance_field.send_keys('qwer123456')
        # next hit reset
        reset_button = self.browser.find_element(By.XPATH, '//tbody/tr[11]/td[2]/input[2]')
        reset_button.click()

        balance_field_text = balance_field.text
        self.assertNotEqual(balance_field_text, None, "Element has text")

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()


if __name__ == '__main__':
    unittest.main()
