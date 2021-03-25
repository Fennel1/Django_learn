from selenium import webdriver
import unittest

class NewTest(unittest.TestCase) :

    def setUp(self):        #  before test
        self.browser = webdriver.Firefox()

    def tearDown(self):     # after test
        self.browser.quit()

    def test(self):

        self.browser.get('http://localhost:8000')

        self.assertIn('To-Do', self.browser.title)
        self.fail('finish the test')

if __name__ == '__main__':
    unittest.main(warnings='ignore')