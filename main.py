from selenium_handler import SeleniumDriver
from selenium.webdriver.common.keys import Keys
import time


class Scrape:

    def main_handler(self):
        """This method is the main point of program's execution"""

        self.get_user_input()

    def get_user_input(self):
        """This method is taking user input for searching bands"""

        band_to_search = input('Enter the band\'s name.')
        # band_to_search = 'metallica' # for testing

        text_box = sel_driver.driver.find_element_by_xpath('//*[@id="searchQueryBox"]')
        text_box.send_keys(band_to_search)
        text_box.send_keys(Keys.ENTER)

        time.sleep(3) # change it to wait for an element
        html = sel_driver.driver.page_source
        foo = 'bar'


# need to make it headless later
sel_driver = SeleniumDriver()

scrape = Scrape()
scrape.main_handler()
