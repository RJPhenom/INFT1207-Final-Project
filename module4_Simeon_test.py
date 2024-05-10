import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.select import Select


class NewAccount(unittest.TestCase):
    customerid = "alpha"

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
        cls.browser.find_element(By.XPATH, "/html/body/div[3]/div/ul/li[5]/a").click()

    # module 4 stuff

    def test_NA1_customer_id_cannot_be_empty(self):
        # Test case NA1
        self.browser.find_element(By.NAME, "cusid").send_keys(Keys.TAB)

        # Wait for error message to appear
        bozo = self.browser.find_element(By.XPATH, "//*[@id=\"message14\"]").text
        assert bozo == "Customer ID is required"

    def test_NA2_customer_id_must_be_numeric(self):
        # Test case NA2
        self.browser.find_element(By.NAME, "cusid").clear()
        self.browser.find_element(By.NAME, "cusid").send_keys("1234Acc")

        # Wait for error message to appear
        bozo = self.browser.find_element(By.XPATH, "//*[@id=\"message14\"]").text
        assert bozo == "Characters are not allowed"

    def test_NA3_customer_id_cannot_have_special_character(self):
        # Test case NA3
        self.browser.find_element(By.NAME, "cusid").clear()
        self.browser.find_element(By.NAME, "cusid").send_keys("123!@#")

        # Wait for error message to appear
        bozo = self.browser.find_element(By.XPATH, "//*[@id=\"message14\"]").text
        assert bozo == "Special characters are not allowed"

    def test_NA4_customer_id_cannot_have_blank_space(self):
        # Test case NA4
        self.browser.find_element(By.NAME, "cusid").clear()
        self.browser.find_element(By.NAME, "cusid").send_keys("123 12")

        # Wait for error message to appear
        bozo = self.browser.find_element(By.XPATH, "//*[@id=\"message14\"]").text
        assert bozo == "Characters are not allowed"

    def test_NA5_first_character_cannot_be_space(self):
        # Test case NA5
        self.browser.find_element(By.NAME, "cusid").clear()
        self.browser.find_element(By.NAME, "cusid").send_keys(Keys.SPACE)

        # Wait for error message to appear
        bozo = self.browser.find_element(By.XPATH, "//*[@id=\"message14\"]").text
        assert bozo == "First character cannot have space"

    # Verify initial deposit

    def test_NA6_verify_initial_deposit_cannot_be_empty(self):
        # Test case NA6
        self.browser.find_element(By.NAME, "inideposit").send_keys(Keys.TAB)

        # Wait for error message to appear
        bozo = self.browser.find_element(By.XPATH, "//*[@id=\"message19\"]").text
        assert bozo == "Initial Deposit must not be blank"

    def test_NA7_initial_deposit_must_be_numeric(self):
        # Test case NA7
        self.browser.find_element(By.NAME, "inideposit").clear()
        self.browser.find_element(By.NAME, "inideposit").send_keys("1234Acc")

        # Wait for error message to appear
        bozo = self.browser.find_element(By.XPATH, "//*[@id=\"message19\"]").text
        assert bozo == "Characters are not allowed"

    def test_NA8_initial_deposit_cannot_have_special_character(self):
        # Test case NA8
        self.browser.find_element(By.NAME, "inideposit").clear()
        self.browser.find_element(By.NAME, "inideposit").send_keys("123!@#")

        # Wait for error message to appear
        bozo = self.browser.find_element(By.XPATH, "//*[@id=\"message19\"]").text
        assert bozo == "Special characters are not allowed"

    def test_NA9_initial_deposit_cannot_have_blank_space(self):
        # Test case NA9
        self.browser.find_element(By.NAME, "inideposit").clear()
        self.browser.find_element(By.NAME, "inideposit").send_keys("123 12")

        # Wait for error message to appear
        bozo = self.browser.find_element(By.XPATH, "//*[@id=\"message19\"]").text
        assert bozo == "Special characters are not allowed"

    def test_NA10_first_character_cannot_be_space_NA10(self):
        # Test case NA10
        self.browser.find_element(By.NAME, "inideposit").send_keys(Keys.SPACE)

        # Wait for error message to appear
        bozo = self.browser.find_element(By.XPATH, "//*[@id=\"message19\"]").text
        assert bozo == "First character cannot have space"

    # verify account type dropdown

    def test_NA11_verify_account_type_dropdown_savings(self):
        # Test case NA11
        account_type_dropdown = Select(self.browser.find_element(By.NAME, "selaccount"))
        account_type_dropdown.select_by_visible_text("Savings")

        # Check if Savings is selected
        selected_option = account_type_dropdown.first_selected_option
        self.assertEqual(selected_option.text, "Savings")

    def test_NA12_verify_account_type_dropdown_current(self):
        # Test case NA12
        account_type_dropdown = Select(self.browser.find_element(By.NAME, "selaccount"))
        account_type_dropdown.select_by_visible_text("Current")

        # Check if Current is selected
        selected_option = account_type_dropdown.first_selected_option
        self.assertEqual(selected_option.text, "Current")

    # test reset button

    def test_NA13_reset_button(self):
        # Test case NA13

        # Input values into Customer ID and Initial Deposit fields
        self.browser.find_element(By.NAME, "cusid").clear()
        self.browser.find_element(By.NAME, "inideposit").clear()
        self.browser.find_element(By.NAME, "cusid").send_keys("qwer")
        self.browser.find_element(By.NAME, "inideposit").send_keys("123456")

        # Click on the reset button
        self.browser.find_element(By.NAME, "reset").click()

    # submit button

    def test_NA14_incorrect_customer_id_submit_button(self):
        # Test case NA14

        # Enter incorrect customer ID
        self.browser.find_element(By.NAME, "cusid").clear()
        self.browser.find_element(By.NAME, "cusid").send_keys("123456")

        # Click on the submit button
        self.browser.find_element(By.NAME, "button2").click()

        # Verify that the error message is displayed
        bozo = self.browser.find_element(By.XPATH, "//*[@id=\"message14\"]").text
        assert bozo == "Customer does not exist!!"

    def test_NA15_correct_customer_id_and_amount_submit_button(self):
        # Test case NA15

        # Enter correct customer ID and amount
        self.browser.find_element(By.NAME, "cusid").clear()
        self.browser.find_element(By.NAME, "inideposit").clear()
        self.browser.find_element(By.NAME, "cusid").send_keys("25274")

        self.browser.find_element(By.NAME, "inideposit").send_keys("10000")

        # Click on the submit button
        self.browser.find_element(By.NAME, "button2").click()

    # hyperlink

    def test_NA16_continue_hyperlink_after_successful_creation(self):
        # Test case NA16

        # Enter correct customer ID and amount
        self.browser.find_element(By.NAME, "cusid").clear()
        self.browser.find_element(By.NAME, "inideposit").clear()
        self.browser.find_element(By.NAME, "cusid").send_keys("25274")
        self.browser.find_element(By.NAME, "inideposit").send_keys("10000")

        # Click on the submit button
        self.browser.find_element(By.NAME, "button2").click()

        # Wait for the page to load after successful creation
        self.browser.implicitly_wait(5)

        # Click on the Continue hyperlink
        self.browser.find_element(By.LINK_TEXT, "Continue").click()

        # Verify that we are on the home page
        home_page_title = self.browser.title
        self.assertEqual(home_page_title, "Home Page")

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit().quit()


if __name__ == '__main__':
    unittest.main()
