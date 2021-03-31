import unittest
from selenium import webdriver


class TestHomePage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox(executable_path='/usr/local/bin/geckodriver')
        self.driver.get('localhost:5000/')

    def tearDown(self):
        self.driver.quit()

    def test_app_has_homepage_template(self):
        self.assertIn('Named Entity Recognition', self.driver.title)

    def test_app_has_entity_table(self):
        entity_tbl = self.driver.find_element_by_css_selector('[data-test-id=entity_tbl]')
        self.assertIsNotNone(entity_tbl)

    def test_app_has_input_form(self):
        input_form = self.driver.find_element_by_css_selector('[data-test-id=input_form]')
        self.assertIsNotNone(input_form)

    def test_app_has_input_for_sent(self):
        input_sent = self.driver.find_element_by_css_selector('[data-test-id=input_sent]')
        self.assertIsNotNone(input_sent)

    def test_app_has_submit_button(self):
        submit_btn = self.driver.find_element_by_css_selector('[data-test-id=submit_btn]')
        self.assertIsNotNone(submit_btn)

    def test_app_submit_button_send_request_to_ner_endpoint(self):
        input_sent = self.driver.find_element_by_css_selector('[data-test-id=input_sent]')
        submit_btn = self.driver.find_element_by_css_selector('[data-test-id=submit_btn]')
        input_sent.send_keys("Kim lives in Madrid.")
        submit_btn.click()
        self.driver.implicitly_wait(3)
        page = self.driver.find_element_by_

