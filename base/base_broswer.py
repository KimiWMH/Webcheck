import os
from configparser import ConfigParser
from selenium import webdriver


class broswer_engine():

    def __init__(self):
        # read the browser type,url from config.ini file    
        config = ConfigParser()
        dir = os.path.abspath('.') 
        file_path = str(dir) + '\config\config.ini'
        chrome_driver_path = str(dir) + '\drivers\chromedriver.exe'
        config.read(file_path)
        
        self.browser = config.get("browserType", "browserName")
        self.url =  config.get("testServer", "URL")
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
        self.driver.quit()
