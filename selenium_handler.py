from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class SeleniumDriver:
    """This is a class for creating webdriver object"""

    webdriver_path = "C:/chromedriver_win32/chromedriver.exe"
    main_url = 'https://www.metal-archives.com'

    def __init__(self):
        try:
            options = Options()
            options.add_argument('--headless')
            self.driver = webdriver.Chrome(executable_path=self.webdriver_path, chrome_options=options)
            self.driver.get(self.main_url)
        except Exception as e:
            print(f'Error while launching Chrome Webdriver or accessing metal-archives.com: {e}')
