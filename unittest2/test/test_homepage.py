import unittest
from selenium import webdriver


class TestHomePage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox(executable_path='/usr/local/bin/geckodriver')
        self.driver.get('localhost:5000/')

    def tearDown(self):
        self.driver.quit()

    def test_homepage_template_exist(self):
        self.assertIn('Named Entity Recognition', self.driver.title)

    def test_homepage_has_appropirate_tags(self):
        entity_tbl = self.driver.find_element_by_css_selector('[data-test-id=entity_tbl]')
        self.assertIsNotNone(entity_tbl)

        input_form = self.driver.find_element_by_css_selector('[data-test-id=input_form]')
        self.assertIsNotNone(input_form)

        input_sent = self.driver.find_element_by_css_selector('[data-test-id=input_sent]')
        self.assertIsNotNone(input_sent)

        submit_btn = self.driver.find_element_by_css_selector('[data-test-id=submit_btn]')
        self.assertIsNotNone(submit_btn)

    def test_hompage_submit_button_and_entity_table_works(self):
        input_sent = self.driver.find_element_by_css_selector('[data-test-id=input_sent]')
        submit_btn = self.driver.find_element_by_css_selector('[data-test-id=submit_btn]')
        input_sent.send_keys("Kim lives in Madrid.")
        submit_btn.click()
        self.driver.implicitly_wait(3)
        table_body = self.driver.find_element_by_css_selector('[data-test-id=entity_tbl] > tbody')
        table_rows = table_body.find_elements_by_tag_name('tr')

        self.assertEqual(table_rows[0].find_element_by_tag_name('td').text, 'Kim')

