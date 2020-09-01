from selenium_handler import SeleniumDriver


class Scrape:

    def main_handler(self):
        """This method is the main point of program's execution"""

        self.get_user_input()

    def get_user_input(self):
        """This method is taking user input for searching bands"""

        user_input = input('Enter the band\'s name.')


# need to make it headless later
sel_driver = SeleniumDriver()

scrape = Scrape()
scrape.main_handler()
