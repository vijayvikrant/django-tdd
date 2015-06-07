# Test for overall functionality of the application
# These are not unit tests


# write a user story - story for what a user can do with your website
# and write a functional test for each of it

import unittest
from selenium import webdriver

class HomePageTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_home_page(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('To-Do', self.browser.title)
        header = self.browser.find_element_by_tag_name('h1')
        self.assertIn('To-Do', header.text)

        input_box = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            input_box.get_attribute('placeholder'),
            'Enter a to-do item'
        )
        input_box.send_keys("Buy peacock feathers")
        input_box.send_keys("\n")

        # The below line will always make the test fail
        # force error for tests that are not completed
        #self.fail('finish the test!')

if __name__ == '__main__':
    unittest.main()
