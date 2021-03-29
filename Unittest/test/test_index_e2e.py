import unittest
from selenium import webdriver


class E2ETests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox(executable_path='/usr/local/bin/geckodriver')
        self.driver.get('http://localhost:5000')

    def tearDown(self):
        self.driver.quit()

    def test_browser_title_contains_app_name(self):
        self.assertIn('Named Entity', self.driver.title)

    def test_page_heading_is_named_entity_finder(self):
        heading = self._find("heading").text
        self.assertEqual("Named Entity Finder", heading)

    def test_page_has_input_for_text(self):
        input_element = self._find('input-text')
        self.assertIsNotNone(input_element)

    def test_page_has_button_for_submitting_text(self):
        submit_button = self._find('submit_btn')
        self.assertIsNotNone(submit_button)

    def test_page_has_ner_table(self):
        input_element = self._find('input-text')
        submit_button = self._find('submit-btn')
        input_element.send_keys("France and Germany share a border in Europe")
        submit_button.click()
        table = self._find("ner_table")
        self.assertIsNotNone(table)

    def test_ner_table_show_entity_results_when_nonempty_sent_is_submitted_by_submit_button(self):
        input_element = self._find('input-text')
        submit_button = self._find('submit-btn')
        input_element.send_keys("France and Germany share a border in Europe")
        submit_button.click()
        table = self._find("ner_table")
        expected_result = 'France'
        self.assertEqual(table.find_element_by_tag_name("td").text, expected_result)

    def _find(self, val):
        input_element = self.driver.find_element_by_css_selector(f'[data-test-id="{val}"')
        return input_element
