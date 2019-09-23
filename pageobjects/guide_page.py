import os
import time
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from base.base_webpage import base_page
from configparser import ConfigParser

class guide_page(base_page):
    """Wrap the guide page - https://support.hp.com/cn-zh/drivers/printers

    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        config = ConfigParser()
        dir = os.path.abspath('.') 
        file_path = str(dir) + '\config\locator.ini'
        config.read(file_path)

        self.search_query = config.get("elementLocator", "search_query")
        self.submit_button  =  config.get("elementLocator", "submit_button")

    def __enter__(self):      
        self.open_browser()
        return self 

    def __exit__(self,*args):
        self.close_browser()

    def input_product_name(self,input_text):   
        locator_input_searchbox = self.loc_split(self.search_query)
        assert self.set_text(locator_input_searchbox,input_text) 

    def click_search_button(self):
        locator_button_submit = self.loc_split(self.submit_button)
        assert self.click_element(locator_button_submit)
