from selenium_handler import SeleniumDriver
from selenium.webdriver.common.keys import Keys
import parse_html
import time
import sys


class Scrape:

    def main_handler(self):
        """This method is the main point of program's execution"""

        # choose the band to scrape
        band_site_html = self.get_user_input()

        # scrape main band info
        band_main_info = parse_html.parse_main_info(band_site_html)

        # get releases data
        releases = parse_html.get_releases_links(band_site_html)
        for name, link in releases.items():
            # TODO: parse release, add function for parsing in parse_html
            print(name, link)

        # click 'read more' comment and scrape
        # comment_read_more = sel_driver.driver.find_element_by_xpath('// *[ @ id = "band_info"] / div[3] / div / a')
        # if comment_read_more:
        #     comment_read_more.click()
        #     html = sel_driver.driver.page_source
        #     #TODO: scrape 'read more' info

    def get_user_input(self) -> str:
        """This method is taking user input for searching bands"""

        band_to_search = input('Enter the band\'s name or enter Q to quit.')
        if band_to_search.upper() == 'Q':
            sys.exit(0)

        text_box = sel_driver.driver.find_element_by_xpath('//*[@id="searchQueryBox"]')
        text_box.send_keys(band_to_search)
        text_box.send_keys(Keys.ENTER)

        time.sleep(3)  # change it to wait for an element
        current_url = sel_driver.driver.current_url

        # if site shows search results page - multiple or zero results for query
        if 'https://www.metal-archives.com/search?searchString' in current_url:
            html = sel_driver.driver.page_source
            # TODO:add handling if more than one page of results
            results = parse_html.parse_search_results(html)

            # run the method again if no results
            if not results:
                print('No results found.')
                self.get_user_input()

            results_len = len(results)
            for res in results:
                print(f"{res['num']}. - {res['name']} - {res['country']} - {res['genre']}")

            # get user input - choose one of results
            input_check = True
            while input_check:
                try:
                    user_choice = input('Enter the number of result which you want to choose or Q to exit.')
                    if user_choice.upper() == 'Q':
                        sys.exit(0)
                    elif int(user_choice) not in range(1, results_len + 1):
                        raise ValueError
                    else:
                        input_check = False
                except ValueError:
                    print(f'You need to enter a number in range 1 - {results_len} or Q.')

            # get the chosen band's page if more than one result
            for res in results:
                if res.get('num') == int(user_choice):
                    sel_driver.driver.get(res['href'])
                    time.sleep(2)  # TODO: apply wait for class
                    html = sel_driver.driver.page_source
                    return html

        # if only one result was found
        else:
            print(f'One result found. Would you like to download info for {band_to_search.title()}?')
            confirm = input('Press ENTER or enter any value to quit.')
            if confirm == "":
                html = sel_driver.driver.page_source
                return html
            else:
                sys.exit(0)


print("Loading app...")
sel_driver = SeleniumDriver()

scrape = Scrape()
scrape.main_handler()
