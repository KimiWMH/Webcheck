import os
import time
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from base.base_webpage import base_page
from configparser import ConfigParser

class baidu_page(base_page):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        config = ConfigParser()
        dir = os.path.abspath('.') 
        file_path = str(dir) + '\config\locator.ini'
        config.read(file_path)

        self.search_query = config.get("elementLocator", "baidu_search_query")
        self.submit_button  =  config.get("elementLocator", "baidu_submit_button")

    def input_product_name(self,input_text):   
        locator_input_searchbox = self.loc_split(self.search_query)
        assert self.click_element(locator_input_searchbox)
        assert self.set_text(locator_input_searchbox,input_text) 

    def click_search_button(self):
        locator_button_submit = self.loc_split(self.submit_button)
        assert self.click_element(locator_button_submit)
