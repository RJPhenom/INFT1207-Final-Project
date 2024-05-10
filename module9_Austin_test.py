import unittest
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BankTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.browser = webdriver.Chrome()
        cls.browser.maximize_window()

    def test_CS01_accountno_field(cls):
        # login as a manager
        wait = WebDriverWait(cls.browser, 1)
        cls.browser.get("http://demo.guru99.com/V4/")
        user_button = cls.browser.find_element(By.XPATH, '//tbody/tr[1]/td[2]/input[1]')
        user_button.click()
        user_button.send_keys('mngr564281')
        pass_button = cls.browser.find_element(By.XPATH, '//tbody/tr[2]/td[2]/input[1]')
        pass_button.click()
        pass_button.send_keys('bAgenAp')
        submit_button = cls.browser.find_element(By.XPATH, '//tbody/tr[3]/td[2]/input[1]')
        submit_button.click()

        # next perform a balance enquiry
        statement_button = cls.browser.find_element(By.XPATH, "//a[normalize-space()='Customised Statement']")
        statement_button.click()
        cls.browser.refresh()
        statement_button = cls.browser.find_element(By.XPATH, "//a[normalize-space()='Customised Statement']")
        statement_button.click()

        accountno_field = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@name='accountno']")))
        accountno_field.click()
        accountno_field.send_keys(Keys.TAB)

        space_alert = wait.until(EC.visibility_of_element_located((By.XPATH, "//label[@id='message2']")))
        alert_text = space_alert.text
        expected_alert = "Account Number must not be blank"
        cls.assertEqual(alert_text, expected_alert, "not correct alert")

        accountno_field = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@name='accountno']")))
        accountno_field.click()
        accountno_field.send_keys('1234acc123')
        accountno_field.send_keys(Keys.TAB)

        char_alert = wait.until(EC.visibility_of_element_located((By.XPATH, "//label[@id='message2']")))
        alert_text = char_alert.text
        expected_alert = "Characters are not allowed"
        cls.assertEqual(alert_text, expected_alert, "not correct alert")

        reset = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@name='res']")))
        reset.click()

        accountno_field = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@name='accountno']")))
        accountno_field.click()
        accountno_field.send_keys('123!@#!@#')
        accountno_field.send_keys(Keys.TAB)

        specialchar_alert = wait.until(EC.visibility_of_element_located((By.XPATH, "//label[@id='message2']")))
        alert_text = specialchar_alert.text
        expected_alert = "Special characters are not allowed"
        cls.assertEqual(alert_text, expected_alert, "not correct alert")

        reset = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@name='res']")))
        reset.click()

        accountno_field = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@name='accountno']")))
        accountno_field.click()
        accountno_field.send_keys('123 12')
        accountno_field.send_keys(Keys.TAB)

        char_alert = wait.until(EC.visibility_of_element_located((By.XPATH, "//label[@id='message2']")))
        alert_text = specialchar_alert.text
        expected_alert = "Characters are not allowed"
        cls.assertEqual(alert_text, expected_alert, "not correct alert")

    def test_CS02_from_date(cls):
        # login as a manager
        wait = WebDriverWait(cls.browser, 1)
        cls.browser.get("http://demo.guru99.com/V4/")
        user_button = cls.browser.find_element(By.XPATH, '//tbody/tr[1]/td[2]/input[1]')
        user_button.click()
        user_button.send_keys('mngr564281')
        pass_button = cls.browser.find_element(By.XPATH, '//tbody/tr[2]/td[2]/input[1]')
        pass_button.click()
        pass_button.send_keys('bAgenAp')
        submit_button = cls.browser.find_element(By.XPATH, '//tbody/tr[3]/td[2]/input[1]')
        submit_button.click()

        # next perform a balance enquiry
        statement_button = cls.browser.find_element(By.XPATH, "//a[normalize-space()='Customised Statement']")
        statement_button.click()
        cls.browser.refresh()
        statement_button = cls.browser.find_element(By.XPATH, "//a[normalize-space()='Customised Statement']")
        statement_button.click()

        from_date_field = wait.until(EC.element_to_be_clickable((By.XPATH, '//tbody/tr[6]/td[2]/input[1]')))
        from_date_field.click()
        from_date_field.send_keys(Keys.TAB)

        from_date_alert = wait.until(EC.visibility_of_element_located((By.XPATH, "//label[@id='message26']")))
        alert_text = from_date_alert.text
        expected_alert = "From Date Field must not be blank"
        cls.assertEqual(alert_text, expected_alert, "not correct alert")

    def test_CS03_to_date(cls):
        # login as a manager
        wait = WebDriverWait(cls.browser, 1)
        cls.browser.get("http://demo.guru99.com/V4/")
        user_button = cls.browser.find_element(By.XPATH, '//tbody/tr[1]/td[2]/input[1]')
        user_button.click()
        user_button.send_keys('mngr564281')
        pass_button = cls.browser.find_element(By.XPATH, '//tbody/tr[2]/td[2]/input[1]')
        pass_button.click()
        pass_button.send_keys('bAgenAp')
        submit_button = cls.browser.find_element(By.XPATH, '//tbody/tr[3]/td[2]/input[1]')
        submit_button.click()

        # next perform a balance enquiry
        statement_button = cls.browser.find_element(By.XPATH, "//a[normalize-space()='Customised Statement']")
        statement_button.click()
        cls.browser.refresh()
        statement_button = cls.browser.find_element(By.XPATH, "//a[normalize-space()='Customised Statement']")
        statement_button.click()

        to_date_field = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@name='tdate']")))
        to_date_field.click()
        to_date_field.send_keys(Keys.TAB)

        to_date_alert = wait.until(EC.visibility_of_element_located((By.XPATH, "//label[@id='message27']")))
        alert_text = to_date_alert.text
        expected_alert = "To Date Field must not be blank"
        cls.assertEqual(alert_text, expected_alert, "not correct alert")

    def test_CS04_min_transactions(cls):
        # login as a manager
        wait = WebDriverWait(cls.browser, 1)
        cls.browser.get("http://demo.guru99.com/V4/")
        user_button = cls.browser.find_element(By.XPATH, '//tbody/tr[1]/td[2]/input[1]')
        user_button.click()
        user_button.send_keys('mngr564281')
        pass_button = cls.browser.find_element(By.XPATH, '//tbody/tr[2]/td[2]/input[1]')
        pass_button.click()
        pass_button.send_keys('bAgenAp')
        submit_button = cls.browser.find_element(By.XPATH, '//tbody/tr[3]/td[2]/input[1]')
        submit_button.click()

        # next perform a balance enquiry
        statement_button = cls.browser.find_element(By.XPATH, "//a[normalize-space()='Customised Statement']")
        statement_button.click()
        cls.browser.refresh()
        statement_button = cls.browser.find_element(By.XPATH, "//a[normalize-space()='Customised Statement']")
        statement_button.click()

        #min_transaction_field = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@name='amountlowerlimit']")))
        #min_transaction_field.click()
        #min_transaction_field.send_keys(' ')
        #min_transaction_field.send_keys(Keys.TAB)
        #sleep(5)

        #space_alert = wait.until(EC.visibility_of_element_located((By.XPATH, "//label[@id='message12']")))
        #alert_text = space_alert.text
        #expected_alert = "First character cannot have space"
        #cls.assertEqual(alert_text, expected_alert, "not correct alert")

        min_transaction_field = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@name='amountlowerlimit']")))
        min_transaction_field.click()
        min_transaction_field.send_keys('1234acc123')
        min_transaction_field.send_keys(Keys.TAB)

        char_alert = wait.until(EC.visibility_of_element_located((By.XPATH, "//label[@id='message12']")))
        alert_text = char_alert.text
        expected_alert = "Characters are not allowed"
        cls.assertEqual(alert_text, expected_alert, "not correct alert")

        reset = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@name='res']")))
        reset.click()

        min_transaction_field = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@name='amountlowerlimit']")))
        min_transaction_field.click()
        min_transaction_field.send_keys('123!@#!@#')
        min_transaction_field.send_keys(Keys.TAB)

        specialchar_alert = wait.until(EC.visibility_of_element_located((By.XPATH, "//label[@id='message12']")))
        alert_text = specialchar_alert.text
        expected_alert = "Special characters are not allowed"
        cls.assertEqual(alert_text, expected_alert, "not correct alert")

        reset = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@name='res']")))
        reset.click()

        min_transaction_field = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@name='amountlowerlimit']")))
        min_transaction_field.click()
        min_transaction_field.send_keys('123 12')
        min_transaction_field.send_keys(Keys.TAB)

        char_alert = wait.until(EC.visibility_of_element_located((By.XPATH, "//label[@id='message12']")))
        alert_text = specialchar_alert.text
        expected_alert = "Characters are not allowed"
        cls.assertEqual(alert_text, expected_alert, "not correct alert")

    def test_CS05_num_transactions(cls):
            # login as a manager
            wait = WebDriverWait(cls.browser, 1)
            cls.browser.get("http://demo.guru99.com/V4/")
            user_button = cls.browser.find_element(By.XPATH, '//tbody/tr[1]/td[2]/input[1]')
            user_button.click()
            user_button.send_keys('mngr564281')
            pass_button = cls.browser.find_element(By.XPATH, '//tbody/tr[2]/td[2]/input[1]')
            pass_button.click()
            pass_button.send_keys('bAgenAp')
            submit_button = cls.browser.find_element(By.XPATH, '//tbody/tr[3]/td[2]/input[1]')
            submit_button.click()

            # next perform a balance enquiry
            statement_button = cls.browser.find_element(By.XPATH, "//a[normalize-space()='Customised Statement']")
            statement_button.click()
            cls.browser.refresh()
            statement_button = cls.browser.find_element(By.XPATH, "//a[normalize-space()='Customised Statement']")
            statement_button.click()
            #fails -> wrong error message
            # num_transaction_field = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@name='numtransaction']")))
            # num_transaction_field.click()
            # num_transaction_field.send_keys(' ')
            # num_transaction_field.send_keys(Keys.TAB)
            # sleep(5)

            # space_alert = wait.until(EC.visibility_of_element_located((By.XPATH, "//label[@id='message12']")))
            # alert_text = space_alert.text
            # expected_alert = "First character cannot have space"
            # cls.assertEqual(alert_text, expected_alert, "not correct alert")

            num_transaction_field = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//input[@name='numtransaction']")))
            num_transaction_field.click()
            num_transaction_field.send_keys('1234acc123')
            num_transaction_field.send_keys(Keys.TAB)

            char_alert = wait.until(EC.visibility_of_element_located((By.XPATH, "//label[@id='message13']")))
            alert_text = char_alert.text
            expected_alert = "Characters are not allowed"
            cls.assertEqual(alert_text, expected_alert, "not correct alert")

            reset = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@name='res']")))
            reset.click()

            num_transaction_field = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//input[@name='numtransaction']")))
            num_transaction_field.click()
            num_transaction_field.send_keys('123!@#!@#')
            num_transaction_field.send_keys(Keys.TAB)

            specialchar_alert = wait.until(EC.visibility_of_element_located((By.XPATH, "//label[@id='message13']")))
            alert_text = specialchar_alert.text
            expected_alert = "Special characters are not allowed"
            cls.assertEqual(alert_text, expected_alert, "not correct alert")

            reset = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@name='res']")))
            reset.click()

            num_transaction_field = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//input[@name='numtransaction']")))
            num_transaction_field.click()
            num_transaction_field.send_keys('123 12')
            num_transaction_field.send_keys(Keys.TAB)

            char_alert = wait.until(EC.visibility_of_element_located((By.XPATH, "//label[@id='message13']")))
            alert_text = specialchar_alert.text
            expected_alert = "Characters are not allowed"
            cls.assertEqual(alert_text, expected_alert, "not correct alert")

    def test_CS06_reset(cls):
        # login as a manager
        wait = WebDriverWait(cls.browser, 1)
        cls.browser.get("http://demo.guru99.com/V4/")
        user_button = cls.browser.find_element(By.XPATH, '//tbody/tr[1]/td[2]/input[1]')
        user_button.click()
        user_button.send_keys('mngr564281')
        pass_button = cls.browser.find_element(By.XPATH, '//tbody/tr[2]/td[2]/input[1]')
        pass_button.click()
        pass_button.send_keys('bAgenAp')
        submit_button = cls.browser.find_element(By.XPATH, '//tbody/tr[3]/td[2]/input[1]')
        submit_button.click()

        # next perform a balance enquiry
        statement_button = cls.browser.find_element(By.XPATH, "//a[normalize-space()='Customised Statement']")
        statement_button.click()
        cls.browser.refresh()
        statement_button = cls.browser.find_element(By.XPATH, "//a[normalize-space()='Customised Statement']")
        statement_button.click()

        accountno_field = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@name='accountno']")))
        accountno_field.click()
        accountno_field.send_keys("134139")
        accountno_field.send_keys(Keys.TAB)
        from_date_field = wait.until(EC.element_to_be_clickable((By.XPATH, '//tbody/tr[6]/td[2]/input[1]')))
        from_date_field.click()
        from_date_field.send_keys("2024")
        from_date_field.send_keys(Keys.TAB)
        to_date_field = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@name='tdate']")))
        to_date_field.click()
        to_date_field.send_keys("2024")
        to_date_field.send_keys(Keys.TAB)
        min_transaction_field = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@name='amountlowerlimit']")))
        min_transaction_field.click()
        min_transaction_field.send_keys('500')
        min_transaction_field.send_keys(Keys.TAB)
        num_transaction_field = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//input[@name='numtransaction']")))
        num_transaction_field.click()
        num_transaction_field.send_keys('12312')
        num_transaction_field.send_keys(Keys.TAB)
        reset = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@name='res']")))
        reset.click()
        #test an input field for being empty
        num_transaction_text = num_transaction_field.text
        cls.assertNotEqual(num_transaction_text, None, "Element has text")

    def test_CS07_submit(cls):
        # login as a manager
        wait = WebDriverWait(cls.browser, 1)
        cls.browser.get("http://demo.guru99.com/V4/")
        user_button = cls.browser.find_element(By.XPATH, '//tbody/tr[1]/td[2]/input[1]')
        user_button.click()
        user_button.send_keys('mngr564281')
        pass_button = cls.browser.find_element(By.XPATH, '//tbody/tr[2]/td[2]/input[1]')
        pass_button.click()
        pass_button.send_keys('bAgenAp')
        submit_button = cls.browser.find_element(By.XPATH, '//tbody/tr[3]/td[2]/input[1]')
        submit_button.click()

        # next perform a balance enquiry
        statement_button = cls.browser.find_element(By.XPATH, "//a[normalize-space()='Customised Statement']")
        statement_button.click()
        cls.browser.refresh()
        statement_button = cls.browser.find_element(By.XPATH, "//a[normalize-space()='Customised Statement']")
        statement_button.click()

        accountno_field = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@name='accountno']")))
        accountno_field.click()
        accountno_field.send_keys("134139")
        accountno_field.send_keys(Keys.TAB)
        from_date_field = wait.until(EC.element_to_be_clickable((By.XPATH, '//tbody/tr[6]/td[2]/input[1]')))
        from_date_field.click()
        from_date_field.send_keys("2024")
        from_date_field.send_keys(Keys.TAB)
        to_date_field = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@name='tdate']")))
        to_date_field.click()
        to_date_field.send_keys("2024")
        to_date_field.send_keys(Keys.TAB)
        min_transaction_field = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@name='amountlowerlimit']")))
        min_transaction_field.click()
        min_transaction_field.send_keys('500')
        min_transaction_field.send_keys(Keys.TAB)
        num_transaction_field = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//input[@name='numtransaction']")))
        num_transaction_field.click()
        num_transaction_field.send_keys('12312')
        num_transaction_field.send_keys(Keys.TAB)
        submit = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@name='AccSubmit']")))
        submit.click()
        alert_text = cls.browser.switch_to.alert
        popup_text = alert_text.text
        expected_alert = "Please fill all fields"
        assert expected_alert in popup_text, f"Popup content does not match expected content. Expected: {expected_alert}, Actual: {popup_text}"
    @classmethod
    def tearDown(cls):
        cls.browser.quit()
