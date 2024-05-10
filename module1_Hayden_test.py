import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


# asserts that the message is the same as the other message
class NewCustomer(unittest.TestCase):
    # opens the browser and logs in to the managers id
    # opens into the new customer tab on the side
    @classmethod
    def setUpClass(cls):
        cls.browser = webdriver.Chrome()
        cls.browser.maximize_window()
        cls.browser.get("https://demo.guru99.com/V4/")
        cls.browser.find_element(By.NAME, "uid").clear()
        cls.browser.find_element(By.NAME, "uid").send_keys("mngr564281")
        # sends the manager id
        cls.browser.find_element(By.NAME, "password").clear()
        cls.browser.find_element(By.NAME, "password").send_keys("bAgenAp")
        # sends the manager password
        cls.browser.find_element(By.NAME, "btnLogin").click()
        # submits
        cls.browser.find_element(By.XPATH, "//a[contains(text(),'New Customer')]").click()
        # enters the new customer tab

    # entering no values to the name field
    def test_nc01_verify_name_field(self):
        self.browser.refresh()
        self.browser.find_element(By.NAME, "name").click()
        # sends keys to the name field
        self.browser.find_element(By.NAME, "name").send_keys(Keys.TAB)
        self.browser.find_element(By.XPATH, "/html/body/table/tbody/tr/td/table/tbody/tr[1]/td/p").click()
        # asserts that the message is the same as the other message
        message = self.browser.find_element(By.ID, "message").text
        assert message == "Customer name must not be blank"

    # tests numbers in the name field
    def test_nc02_1_verify_name_field(self):
        self.browser.refresh()

        # sends keys to the name field
        self.browser.find_element(By.NAME, "name").send_keys("1234")
        # asserts that the message is the same as the other message
        message = self.browser.find_element(By.ID, "message").text
        assert message == "Numbers are not allowed"

    # tests numbers in the name field
    def test_nc02_2_verify_name_field(self):
        self.browser.refresh()

        # sends keys to the name field
        self.browser.find_element(By.NAME, "name").send_keys("name123")
        # asserts that the message is the same as the other message
        message = self.browser.find_element(By.ID, "message").text
        assert message == "Numbers are not allowed"

    # tests special characters in the name field
    def test_nc03_1_verify_name_field(self):
        self.browser.refresh()

        # sends keys to the name field
        self.browser.find_element(By.NAME, "name").send_keys("name!@#")
        # asserts that the message is the same as the other message
        message = self.browser.find_element(By.ID, "message").text
        assert message == "Special characters are not allowed"

    # tests special characters in the name field
    def test_nc03_2_verify_name_field(self):
        self.browser.refresh()
        # sends keys to the name field
        self.browser.find_element(By.NAME, "name").send_keys("!@#")
        # asserts that the message is the same as the other message
        message = self.browser.find_element(By.ID, "message").text
        assert message == "Special characters are not allowed"

    #  tests a blank space in the name field
    def test_nc04_verify_name_field(self):
        self.browser.refresh()
        # sends keys to the name field
        self.browser.find_element(By.NAME, "name").send_keys(" ")
        # asserts that the message is the same as the other message
        message = self.browser.find_element(By.ID, "message").text
        assert message == "First character can not have space"

    # tests an empty entry in the address field
    def test_nc05_verify_address_field(self):
        self.browser.refresh()
        # sends keys to the address field
        self.browser.find_element(By.NAME, "addr").click()
        self.browser.find_element(By.NAME, "addr").send_keys(Keys.TAB)
        # asserts that the message is the same as the other message
        message = self.browser.find_element(By.ID, "message3").text
        assert message == "ADDRESS Field must not be blank"

    # tests a blank space in the address field
    def test_nc06_verify_address_field(self):
        self.browser.refresh()
        # sends keys to the address field
        self.browser.find_element(By.NAME, "addr").send_keys(" ")
        # asserts that the message is the same as the other message
        message = self.browser.find_element(By.ID, "message3").text
        assert message == "First character can not have space"

    # tests an empty entry in the city field
    def test_nc07_verify_city_field(self):
        self.browser.refresh()
        self.browser.find_element(By.NAME, "city").click()
        # sends keys to the city field
        self.browser.find_element(By.NAME, "city").send_keys(Keys.TAB)
        # asserts that the message is the same as the other message
        message = self.browser.find_element(By.ID, "message4").text
        assert message == "City Field must be not blank"

    # tests number in the city field
    def test_nc08_1_verify_city_field(self):
        self.browser.refresh()
        # sends keys to the city field
        self.browser.find_element(By.NAME, "city").send_keys("1234")
        # asserts that the message is the same as the other message
        message = self.browser.find_element(By.ID, "message4").text
        assert message == "Numbers are not allowed"

    # tests number in the city field
    def test_nc08_2_verify_city_field(self):
        self.browser.refresh()
        # sends keys to the city field
        self.browser.find_element(By.NAME, "city").send_keys("city123")
        # asserts that the message is the same as the other message
        message = self.browser.find_element(By.ID, "message4").text
        assert message == "Numbers are not allowed"

    # tests special characters in the city field
    def test_nc09_1_verify_city_field(self):
        self.browser.refresh()
        # sends keys to the city field
        self.browser.find_element(By.NAME, "city").send_keys("city!@#")
        # asserts that the message is the same as the other message
        message = self.browser.find_element(By.ID, "message4").text
        assert message == "Special characters are not allowed"

    # tests special characters in the city field
    def test_nc09_2_verify_city_field(self):
        self.browser.refresh()
        # sends keys to the city field
        self.browser.find_element(By.NAME, "city").send_keys("!@#")
        # asserts that the message is the same as the other message
        message = self.browser.find_element(By.ID, "message4").text
        assert message == "Special characters are not allowed"

    # tests a blank space in the city field
    def test_nc10_verify_city_field(self):
        self.browser.refresh()
        # sends keys to the city field
        self.browser.find_element(By.NAME, "city").send_keys(" ")
        # asserts that the message is the same as the other message
        message = self.browser.find_element(By.ID, "message4").text
        assert message == "First character can not have space"

    # tests an empty state field
    def test_nc11_verify_state_field(self):
        self.browser.refresh()
        # sends keys to the state field
        self.browser.find_element(By.NAME, "state").click()
        self.browser.find_element(By.NAME, "state").send_keys(Keys.TAB)
        # asserts that the message is the same as the other message
        message = self.browser.find_element(By.ID, "message5").text
        assert message == "State must not be blank"

    # tests number in the state field
    def test_nc12_1_verify_state_field(self):
        self.browser.refresh()
        # sends keys to the state field
        self.browser.find_element(By.NAME, "state").send_keys("1234")
        # asserts that the message is the same as the other message
        message = self.browser.find_element(By.ID, "message5").text
        assert message == "Numbers are not allowed"

    # tests number in the state field
    def test_nc12_2_verify_state_field(self):
        self.browser.refresh()
        # sends keys to the state field
        self.browser.find_element(By.NAME, "state").send_keys("state123")
        # asserts that the message is the same as the other message
        message = self.browser.find_element(By.ID, "message5").text
        assert message == "Numbers are not allowed"

    # tests special characters in the state field
    def test_nc13_1_verify_state_field(self):
        self.browser.refresh()
        # sends keys to the state field
        self.browser.find_element(By.NAME, "state").send_keys("state!@#")
        # asserts that the message is the same as the other message
        message = self.browser.find_element(By.ID, "message5").text
        assert message == "Special characters are not allowed"

    # tests special characters in the state field
    def test_nc13_2_verify_state_field(self):
        self.browser.refresh()
        # sends keys to the state field
        self.browser.find_element(By.NAME, "state").send_keys("!@#")
        # asserts that the message is the same as the other message
        message = self.browser.find_element(By.ID, "message5").text
        assert message == "Special characters are not allowed"

    # tests a blank space in the state field
    def test_nc14_verify_state_field(self):
        self.browser.refresh()
        # sends keys to the state field
        self.browser.find_element(By.NAME, "state").send_keys(" ")
        # asserts that the message is the same as the other message
        message = self.browser.find_element(By.ID, "message5").text
        assert message == "First character cannot have space"

    # tests numbers in the pin field
    def test_nc15_1_verify_pin_field(self):
        self.browser.refresh()
        # sends keys to the pin field
        self.browser.find_element(By.NAME, "pinno").send_keys("1234")
        # asserts that the message is the same as the other message
        message = self.browser.find_element(By.ID, "message6").text
        assert message == "Characters are not allowed"

    # tests numbers in the pin field
    def test_nc15_2_verify_pin_field(self):
        self.browser.refresh()
        # sends keys to the pin field
        self.browser.find_element(By.NAME, "pinno").send_keys("pin1234")
        # asserts that the message is the same as the other message
        message = self.browser.find_element(By.ID, "message6").text
        assert message == "Characters are not allowed"

    # tests empty pin field
    def test_nc16_verify_pin_field(self):
        self.browser.refresh()
        self.browser.find_element(By.NAME, "pinno").clear()
        # sends keys to the pin field
        self.browser.find_element(By.NAME, "pinno").send_keys(Keys.TAB)
        # asserts that the message is the same as the other message
        message = self.browser.find_element(By.ID, "message6").text
        assert message == "PIN code must not be blank"

    # tests pin must have 6 digits
    def test_nc17_1_verify_pin_field(self):
        self.browser.refresh()
        self.browser.find_element(By.NAME, "pinno").click()
        # sends keys to the pin field
        self.browser.find_element(By.NAME, "pinno").send_keys("12")
        # asserts that the message is the same as the other message
        message = self.browser.find_element(By.ID, "message6").text
        assert message == "PIN Code must have 6 Digits"

    # tests pin must have 6 digits
    def test_nc17_2_verify_pin_field(self):
        self.browser.refresh()
        # sends keys to the pin field
        self.browser.find_element(By.NAME, "pinno").send_keys("123")
        # asserts that the message is the same as the other message
        message = self.browser.find_element(By.ID, "message6").text
        assert message == "PIN Code must have 6 Digits"

    # tests special characters in the pin field
    def test_nc18_1_verify_pin_field(self):
        self.browser.refresh()
        # sends keys to the pin field
        self.browser.find_element(By.NAME, "pinno").send_keys("!@#")
        # asserts that the message is the same as the other message
        message = self.browser.find_element(By.ID, "message6").text
        assert message == "Special characters are not allowed"

    # tests special characters in the pin field
    def test_nc18_2_verify_pin_field(self):
        self.browser.refresh()
        self.browser.find_element(By.NAME, "pinno").clear()
        # sends keys to the pin field
        self.browser.find_element(By.NAME, "pinno").send_keys("123!@#")
        # asserts that the message is the same as the other message
        message = self.browser.find_element(By.ID, "message6").text
        assert message == "Special characters are not allowed"

    # tests blank space in the pin field
    def test_nc19_verify_pin_field(self):
        self.browser.refresh()
        # sends keys to the pin field
        self.browser.find_element(By.NAME, "pinno").send_keys(" ")
        # asserts that the message is the same as the other message
        message = self.browser.find_element(By.ID, "message6").text
        assert message == "First character cannot have space"

    # tests blank space in the pin field
    def test_nc20_verify_pin_field(self):
        self.browser.refresh()
        # sends keys to the pin field
        self.browser.find_element(By.NAME, "pinno").send_keys(" ")
        # asserts that the message is the same as the other message
        message = self.browser.find_element(By.ID, "message6").text
        assert message == "Characters are not allowed"

    # tests empty telephone field
    def test_nc21_verify_mobile_number_field(self):
        self.browser.refresh()
        self.browser.find_element(By.NAME, "telephoneno").click()
        # sends keys to the mobile number field
        self.browser.find_element(By.NAME, "telephoneno").send_keys(Keys.TAB)
        # asserts that the message is the same as the other message
        message = self.browser.find_element(By.ID, "message7").text
        assert message == "Mobile no must not be blank"

    # tests blank space in telephone field
    def test_nc22_verify_mobile_number_field(self):
        self.browser.refresh()
        # sends keys to the mobile number field
        self.browser.find_element(By.NAME, "telephoneno").send_keys(" ")
        # asserts that the message is the same as the other message
        message = self.browser.find_element(By.ID, "message7").text
        assert message == "First character can not have space"

    # tests space telephone field
    def test_nc23_verify_mobile_number_field(self):
        self.browser.refresh()
        # sends keys to the mobile number field
        self.browser.find_element(By.NAME, "telephoneno").send_keys("123 123")
        # asserts that the message is the same as the other message
        message = self.browser.find_element(By.ID, "message7").text
        assert message == "Characters are not allowed"

    # tests special characters in telephone field
    def test_nc24_1_verify_mobile_number_field(self):
        self.browser.refresh()
        # sends keys to the mobile number field
        self.browser.find_element(By.NAME, "telephoneno").send_keys("886636!@12")
        # asserts that the message is the same as the other message
        message = self.browser.find_element(By.ID, "message7").text
        assert message == "Special characters are not allowed"

    # tests special characters in telephone field
    def test_nc24_2_verify_mobile_number_field(self):
        self.browser.refresh()
        # sends keys to the mobile number field
        self.browser.find_element(By.NAME, "telephoneno").send_keys(" !@88662682")
        # asserts that the message is the same as the other message
        message = self.browser.find_element(By.ID, "message7").text
        assert message == "Special characters are not allowed"

    # tests special characters in telephone field
    def test_nc24_3_verify_mobile_number_field(self):
        self.browser.refresh()
        # sends keys to the mobile number field
        self.browser.find_element(By.NAME, "telephoneno").send_keys("88663682!@")
        # asserts that the message is the same as the other message
        message = self.browser.find_element(By.ID, "message7").text
        assert message == "Special characters are not allowed"

    # tests empty email field
    def test_nc25_verify_email_field(self):
        self.browser.refresh()
        # sends keys to the email field
        self.browser.find_element(By.NAME, "emailid").send_keys(Keys.TAB)
        # asserts that the message is the same as the other message
        message = self.browser.find_element(By.ID, "message9").text
        assert message == "Email ID must not be blank"

    # tests inputs in email field
    def test_nc26_1_verify_email_field(self):
        self.browser.refresh()
        self.browser.find_element(By.NAME, "emailid").clear()
        # sends keys to the email field
        self.browser.find_element(By.NAME, "emailid").send_keys("guru99@gmail")
        # asserts that the message is the same as the other message
        message = self.browser.find_element(By.ID, "message9").text
        assert message == "Email-ID is not valid\""
        self.browser.find_element(By.NAME, "emailid").clear()

    # tests inputs in email field
    def test_nc26_2_verify_email_field(self):
        self.browser.refresh()
        # sends keys to the email field
        self.browser.find_element(By.NAME, "emailid").send_keys("guru99")
        # asserts that the message is the same as the other message
        message = self.browser.find_element(By.ID, "message9").text
        assert message == "Email-ID is not valid\""
        self.browser.find_element(By.NAME, "emailid").clear()

    # tests inputs in email field
    def test_nc26_3_verify_email_field(self):
        self.browser.refresh()
        # sends keys to the email field
        self.browser.find_element(By.NAME, "emailid").send_keys("Guru99@")
        # asserts that the message is the same as the other message
        message = self.browser.find_element(By.ID, "message9").text
        assert message == "Email-ID is not valid\""
        self.browser.find_element(By.NAME, "emailid").clear()

    # tests inputs in email field
    def test_nc26_4_verify_email_field(self):
        self.browser.refresh()
        # sends keys to the email field
        self.browser.find_element(By.NAME, "emailid").send_keys("guru99@gmail.")
        # asserts that the message is the same as the other message
        message = self.browser.find_element(By.ID, "message9").text
        assert message == "Email-ID is not valid\""
        self.browser.find_element(By.NAME, "emailid").clear()

    # tests inputs in email field
    def test_nc26_5_verify_email_field(self):
        self.browser.refresh()
        # sends keys to the email field
        self.browser.find_element(By.NAME, "emailid").send_keys("guru99gmail.com")
        # asserts that the message is the same as the other message
        message = self.browser.find_element(By.ID, "message9").text
        assert message == "Email-ID is not valid\""

    # tests blank space in email field
    def test_nc27_verify_email_field(self):
        self.browser.refresh()
        # sends keys to the email field
        self.browser.find_element(By.NAME, "emailid").send_keys(" ")
        # asserts that the message is the same as the other message
        message = self.browser.find_element(By.ID, "message9").text
        assert message == "Email-ID is not valid"

    # tests empty entry in password field
    def test_nc28_verify_password_field(self):
        self.browser.refresh()
        self.browser.find_element(By.NAME, "password").clear()
        # sends keys to the password field
        self.browser.find_element(By.NAME, "password").send_keys(Keys.TAB)
        # asserts that the message is the same as the other message
        message = self.browser.find_element(By.ID, "message18").text
        assert message == "Password must not be blank"

    # closes the browser
    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()


if __name__ == '__main__':
    unittest.main()
