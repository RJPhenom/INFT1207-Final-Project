import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class EditAccount(unittest.TestCase):
    # Set a default customer id for the tests
    customerid = "alpha"

    @classmethod
    def setUpClass(cls):
        # Set up the Chrome webdriver
        cls.browser = webdriver.Chrome()
        cls.browser.maximize_window()
        # Open the website and login
        cls.browser.get("https://demo.guru99.com/V4/")
        cls.browser.find_element(By.NAME, "uid").clear()
        cls.browser.find_element(By.NAME, "uid").send_keys("mngr564281")
        cls.browser.find_element(By.NAME, "password").clear()
        cls.browser.find_element(By.NAME, "password").send_keys("bAgenAp")
        cls.browser.find_element(By.NAME, "btnLogin").click()
        # Navigate to the account editing section
        cls.browser.find_element(By.XPATH, "/html/body/div[3]/div/ul/li[6]/a").click()

    # Test cases for validating account number input

    def test_ea01_verify_account_number(self):
        # Verify account number cannot be empty
        self.browser.find_element(By.NAME, "accountno").click()
        self.browser.find_element(By.NAME, "accountno").send_keys(Keys.TAB)
        bozo = self.browser.find_element(By.XPATH, "//*[@id=\"message2\"]").text
        assert bozo == "Account Number must not be empty"

    def test_ea02_1_verify_account_number(self):
        # Verify characters are not allowed in account number
        self.browser.find_element(By.NAME, "accountno").send_keys("1234")
        bozo = self.browser.find_element(By.XPATH, "//*[@id=\"message2\"]").text
        assert bozo == "Characters are not allowed"

    def test_ea02_2_verify_account_number(self):
        # Verify special characters are not allowed in account number
        self.browser.find_element(By.NAME, "accountno").clear()
        self.browser.find_element(By.NAME, "accountno").send_keys("Acc1234")
        bozo = self.browser.find_element(By.XPATH, "//*[@id=\"message2\"]").text
        assert bozo == "Characters are not allowed"

    def test_ea03_1_verify_account_number(self):
        # Verify special characters are not allowed in account number
        self.browser.find_element(By.NAME, "accountno").clear()
        self.browser.find_element(By.NAME, "accountno").send_keys("!@#")
        bozo = self.browser.find_element(By.XPATH, "//*[@id=\"message2\"]").text
        assert bozo == "Special characters are not allowed"

    def test_ea03_2_verify_account_number(self):
        # Verify special characters are not allowed in account number
        self.browser.find_element(By.NAME, "accountno").clear()
        self.browser.find_element(By.NAME, "accountno").send_keys("Acc!@#")
        bozo = self.browser.find_element(By.XPATH, "//*[@id=\"message2\"]").text
        assert bozo == "Special characters are not allowed"

    def test_ea04_verify_account_number(self):
        # Verify spaces are not allowed in account number
        self.browser.find_element(By.NAME, "accountno").clear()
        self.browser.find_element(By.NAME, "accountno").send_keys("123 12" + Keys.TAB)
        bozo = self.browser.find_element(By.XPATH, "//*[@id=\"message2\"]").text
        assert bozo == "Characters are not allowed"

    def test_ea05_verify_account_number(self):
        # Verify first character cannot have space in account number
        self.browser.find_element(By.NAME, "accountno").clear()
        self.browser.find_element(By.NAME, "accountno").send_keys(" " + Keys.TAB)
        bozo = self.browser.find_element(By.XPATH, "//*[@id=\"message2\"]").text
        assert bozo == "First character cannot have space"

    def test_ea06_verify_account_number(self):
        # Verify account submission without errors
        self.browser.find_element(By.NAME, "accountno").send_keys("133771")
        self.browser.find_element(By.NAME, "AccSubmit").click()
        bozo = str(self.browser.find_element(By.XPATH, "//*[@id=\"error-information-popup-content\"]/div[2]").text)
        assert bozo != str('HTTP ERROR 500')

    def test_ea07_verify_account_number(self):
        # Verify alert for non-existing account
        self.browser.back()
        self.browser.find_element(By.NAME, "accountno").send_keys("123456")
        self.browser.find_element(By.NAME, "AccSubmit").click()
        bozo = self.browser.switch_to.alert.text
        assert bozo == "Account does not exist"
        self.browser.switch_to.alert.accept()

    def test_ea08_reset_button(self):
        # Verify reset button functionality
        self.browser.find_element(By.NAME, "accountno").clear()
        self.browser.find_element(By.NAME, "accountno").send_keys("123456")
        self.browser.find_element(By.NAME, "res").click()
        bozo = self.browser.find_element(By.NAME, "accountno").text
        assert bozo == ""

    @classmethod
    def tearDownClass(cls):
        # Close the browser after all tests are done
        cls.browser.quit()


if __name__ == '__main__':
    unittest.main()
