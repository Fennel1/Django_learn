from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest


class NewTest(unittest.TestCase):

    def setUp(self):  # before test
        self.browser = webdriver.Firefox()

    def tearDown(self):  # after test
        self.browser.quit()

    def check_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_main(self):
        self.browser.get('http://localhost:8000')

        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('coding')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(5)

        self.check_row_in_list_table('1: coding')

        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('code success')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(5)

        self.check_row_in_list_table('1: coding')
        self.check_row_in_list_table('2: code success')

        # inputbox = self.browser.find_element_by_id('id_new_item')
        # inputbox.send_keys('coding')
        # inputbox.send_keys(Keys.ENTER)
        # time.sleep(1)
        # inputbox = self.browser.find_element_by_id('id_new_item')
        # inputbox.send_keys('code success')
        # inputbox.send_keys(Keys.ENTER)
        # time.sleep(1)

        # self.assertEqual(
        #     inputbox.get_attribute('placeholder'),
        #     'Enter a to-do item'
        # )

        # f"New to-do item did not appear in table. contents were\n{table.text}"

        self.fail('finish')


if __name__ == '__main__':
    unittest.main(warnings='ignore')
