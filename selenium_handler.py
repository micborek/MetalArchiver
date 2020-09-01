from selenium import webdriver

# local webdriver directory
webdriver_path = "C:\chromedriver_win32\chromedriver.exe"


class SeleniumDriver:
    main_url = 'https://www.metal-archives.com'

    def __init__(self):
        try:
            self.driver = webdriver.Chrome(executable_path=webdriver_path)
            self.driver.get(self.main_url)
        except Exception as e:
            print(f'Error while launching Chrome Webdriver or accessing metal-archives.com: {e}')
