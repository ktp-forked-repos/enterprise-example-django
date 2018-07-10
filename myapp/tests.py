from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


class GenomelinkBrowserTestCase(StaticLiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        # $ brew install chromedriver
        super(GenomelinkBrowserTestCase, cls).setUpClass()
        cls.browser = webdriver.Chrome()

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()
        super(GenomelinkBrowserTestCase, cls).tearDownClass()

    def setUp(self):
        pass

    def test_submit_without_file_should_alert(self):
        self.browser.get(self.live_server_url)
        self.browser.find_element_by_xpath('//button').click()

        self.browser.switch_to_frame(self.browser.find_element_by_id('genomelinkFrame'))
        self.browser.find_element_by_xpath('//button').click()

        alert = self.browser.switch_to_alert()
        self.assertEqual(alert.text, 'No file selected.')
        alert.accept()
