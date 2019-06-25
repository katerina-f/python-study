
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import unittest
import time

email = 'email'
passw = 'passw'

class TestAuthorization(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Safari()

    def tearDown(self):
        self.driver.close()

    def test_authorization(self):
        self.driver.get("https://passport.yandex.ru/auth/")
        self.assertIn("Авторизация", self.driver.title)
        elem = self.driver.find_element_by_name('login')
        elem.send_keys(email)
        elem.send_keys(Keys.ENTER)
        time.sleep(2)
        elem = self.driver.find_element_by_name('passwd')
        elem.send_keys(passw)
        elem.send_keys(Keys.ENTER)
        time.sleep(2)
        self.assertIn("Яндекс.Паспорт", self.driver.title)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestAuthorization)
    unittest.TextTestRunner(verbosity=2).run(suite)
