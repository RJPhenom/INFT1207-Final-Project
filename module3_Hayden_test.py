import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class DeleteCustomer(unittest.TestCase):
    # opens the browser logs into the manager and clicks on the delete customer tab
    @classmethod
    def setUpClass(cls):
        cls.browser = webdriver.Chrome()
        cls.browser.maximize_window()
        cls.browser.get("https://demo.guru99.com/V4/")
        cls.browser.find_element(By.NAME, "uid").clear()
        cls.browser.find_element(By.NAME, "uid").send_keys("mngr564281")
        cls.browser.find_element(By.NAME, "password").clear()
        cls.browser.find_element(By.NAME, "password").send_keys("bAgenAp")
        cls.browser.find_element(By.NAME, "btnLogin").click()
        cls.browser.find_element(By.XPATH, "/html/body/div[3]/div/ul/li[4]/a").click()

    # tests no value in customer id field
    def test_dc01_verify_customer_id(self):
        self.browser.find_element(By.NAME, "cusid").send_keys(Keys.TAB)
        # asserts that the message is the same as the other message
        message = self.browser.find_element(By.ID, "message14").text
        assert message == "Customer ID can not be blank"
        self.browser.refresh()

    # tests numbers in customer id field
    def test_dc02_1_verify_customer_id(self):
        # enters text in the customer id field
        self.browser.find_element(By.NAME, "cusid").send_keys("1234")
        # asserts that the message is the same as the other message
        message = self.browser.find_element(By.ID, "message14").text
        assert message == "Characters are not allowed"

    # tests numbers in customer id field
    def test_dc02_2_verify_customer_id(self):
        self.browser.find_element(By.NAME, "cusid").clear()
        # enters text in the customer id field
        self.browser.find_element(By.NAME, "cusid").send_keys("Acc123")
        # asserts that the message is the same as the other message
        message = self.browser.find_element(By.ID, "message14").text
        assert message == "Characters are not allowed"
        self.browser.refresh()

    # tests special characters in customer id field
    def test_dc03_1_verify_customer_id(self):
        self.browser.find_element(By.NAME, "cusid").clear()
        # enters text in the customer id field
        self.browser.find_element(By.NAME, "cusid").send_keys("123!@#")
        # asserts that the message is the same as the other message
        message = self.browser.find_element(By.ID, "message14").text
        assert message == "Special characters are not allowed"

    # tests special characters in customer id field
    def test_dc03_2_verify_customer_id(self):
        self.browser.find_element(By.NAME, "cusid").clear()
        # enters text in the customer id field
        self.browser.find_element(By.NAME, "cusid").send_keys("!@#")
        # asserts that the message is the same as the other message
        message = self.browser.find_element(By.ID, "message14").text
        assert message == "Special characters are not allowed"
        self.browser.refresh()

    # tests blank spaces in customer id field
    def test_dc04_verify_customer_id(self):
        self.browser.find_element(By.NAME, "cusid").clear()
        # enters text in the customer id field
        self.browser.find_element(By.NAME, "cusid").send_keys("123 12")
        # asserts that the message is the same as the other message
        message = self.browser.find_element(By.ID, "message14").text
        assert message == "Characters are not allowed"
        self.browser.refresh()

    # tests blank space in customer id field
    def test_dc05_verify_customer_id(self):
        self.browser.find_element(By.NAME, "cusid").clear()
        # enters text in the customer id field
        self.browser.find_element(By.NAME, "cusid").send_keys(" ")
        self.browser.find_element(By.NAME, "cusid").send_keys(Keys.TAB)
        # asserts that the message is the same as the other message
        message = self.browser.find_element(By.ID, "message14").text
        assert message == "First character cannot have space"

    # tests incorrect customer id in customer id field
    def test_dc06_submit_button(self):
        self.browser.refresh()
        # enters text in the customer id field
        self.browser.find_element(By.NAME, "cusid").send_keys("123456")
        self.browser.find_element(By.NAME, "AccSubmit").click()
        # asserts that the message is the same as the other message
        self.browser.switch_to.alert.accept()
        msg = self.browser.switch_to.alert.text
        message = msg
        assert message == "Customer does not exist!!"
        self.browser.switch_to.alert.accept()
        self.browser.back()
        self.browser.refresh()

    # tests correct customer id
    def test_dc07_submit_button(self):
        self.browser.find_element(By.NAME, "cusid").clear()
        # enters text in the customer id field
        self.browser.find_element(By.NAME, "cusid").send_keys("Your customerid")
        self.browser.find_element(By.NAME, "AccSubmit").click()
        # asserts that the message is the same as the other message
        message = self.browser.switch_to.alert.text
        assert message == "Customer does not existcould not be deleted!! First delete all accounts of this customer then delete the customer!!"
        self.browser.switch_to.alert.accept()

    # tests the reset button
    def test_dc08_reset_button(self):
        self.browser.switch_to.alert.accept()
        # enters text in the customer id field
        self.browser.find_element(By.NAME, "cusid").send_keys("qwer 1234")
        # asserts that the message is the same as the other message
        self.browser.find_element(By.NAME, "res").click()
        message = self.browser.find_element(By.NAME, "res").text
        assert message == ""

    # closes the browser
    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()


if __name__ == '__main__':
    unittest.main()
