from selenium_handler import SeleniumDriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import export_file
import parse_html
import time
import sys
import json


class Scrape:
    parser = parse_html.HtmlParser()

    def main_handler(self):
        """This method is the main point of program's execution"""

        band_data = {}
        # choose the band to scrape
        band_site_html = self.get_user_input()

        # scrape main band info
        band_main_info = self.parser.parse_main_info(band_site_html)
        band_data['main'] = band_main_info

        # click 'read more' for comment if exists and scrape
        self.get_band_comment(band_data)

        # get releases data
        releases_data = self.get_releases_data(band_site_html)
        band_data['releases'] = releases_data

        # export json file with all band data
        exporter = export_file.ExportFile()
        exporter.export_all_to_json(band_data)

        print(f"Scraping data for {band_data.get('main').get('Name')} finished.")

    def get_band_comment(self, band_data):
        """The method for getting comment for a band if exists"""

        try:
            comment_read_more = sel_driver.driver.find_element_by_xpath('// *[ @ id = "band_info"] / div[3] / div / a')
            comment_read_more.click()
            time.sleep(2)  # TODO: apply wait for class
            html = sel_driver.driver.page_source
            comment = self.parser.parse_general_comment(html)
            band_data['main']['comment'] = comment
        except NoSuchElementException:
            pass

    def get_releases_data(self, band_site_html: str) -> list:
        """This is for adding releases data to band data"""

        releases_data = []
        releases = self.parser.get_releases_links(band_site_html)
        rel_count = 0
        for name, link in releases.items():
            rel_count += 1
            print(f"Scraping release '{name}' ({rel_count} of {len(releases)})")
            sel_driver.driver.get(link)
            html = sel_driver.driver.page_source
            rel = self.parser.parse_release_data(html)
            if rel:
                releases_data.append(rel)

        return releases_data

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
            results = self.parser.parse_search_results(html)

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
