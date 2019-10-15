import os
from configparser import ConfigParser
from selenium import webdriver
from selenium.common.exceptions import TimeoutException

class broswer_engine():
    """Broswer Engine descriptor.

    :param url:  `str`
        Store url will use 
    :param browser:  `str`
        which kind of browser you would use
    :param driver:  `webdriver`
        This element is expected to be called with browser

    Broswer Engine is used to init the webdriver.
    use this factory to creater your own webdriver element

        >>>from base.base_broswer import broswer_engine
        >>>Class MyWebPage(broswer_engine):
            my_browser = self.open_browser()
            self.close_browser()

        Browser wrapper open/close function to handle these basic need
    """
    def __init__(self):
        # read the browser type,url from config.ini file    
        config = ConfigParser()
        dir = os.path.abspath('.') 
        file_path = str(dir) + r'\config\browser_config.ini'
        chrome_driver_path = str(dir) + '\drivers\chromedriver.exe'
        config.read(file_path)
        
        self.browser = config.get("browserType", "browserName")
        self.url =  config.get("testServer", "URL")
        # Extend more browser type
        if self.browser  == "Firefox":
            self.driver = webdriver.Firefox()
        elif self.browser  == "Chrome":
            self.driver = webdriver.Chrome(chrome_driver_path)

    def open_browser(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(4)
        return self.driver

    def close_browser(self):
        try:
            self.driver.quit()
        except TimeoutException as TE:
            print("TimeOut!!! Could not close the browser.")

