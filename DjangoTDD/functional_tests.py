import unittest


class HomePageTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_home_page(self):
        self.browser.set('http://localhost:8000')
        self.assertIn('To-Do', self.browser.title)

if __name__ == '__main__'
    unittest.main()