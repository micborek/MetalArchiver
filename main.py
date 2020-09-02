from selenium_handler import SeleniumDriver
from selenium.webdriver.common.keys import Keys
import parse_html
import time


class Scrape:

    def main_handler(self):
        """This method is the main point of program's execution"""

        self.get_user_input()

    def get_user_input(self):
        """This method is taking user input for searching bands"""

        band_to_search = input('Enter the band\'s name.')
        # band_to_search = 'hate'  # for testing

        text_box = sel_driver.driver.find_element_by_xpath('//*[@id="searchQueryBox"]')
        text_box.send_keys(band_to_search)
        text_box.send_keys(Keys.ENTER)

        time.sleep(3)  # change it to wait for an element
        current_url = sel_driver.driver.current_url

        # add 'no results' if statement
        # if site returns more than 1 search result
        if 'https://www.metal-archives.com/search?searchString' in current_url:
            html = sel_driver.driver.page_source
            # add handling if more than one page of results
            results = parse_html.parse_search_results(html)
            results_len = len(results)
            print(f'{results_len} results found:')
            for res in results:
                print(f"{res['num']}. - {res['name']} - {res['country']} - {res['genre']}")
            # enter number of band you would like to scrape

        # if only one result was found
        else:
            print('One result found')


# need to make it headless later
sel_driver = SeleniumDriver()

scrape = Scrape()
scrape.main_handler()
