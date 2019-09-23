import os
import time
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from base.base_webpage import base_page
from configparser import ConfigParser

class product_page(base_page):
    """Wrap the guide page - https://support.hp.com/cn-zh/drivers/printers

    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        config = ConfigParser()
        dir = os.path.abspath('.') 
        file_path = str(dir) + '\config\locator.ini'
        config.read(file_path)

        self.open_close_toggle_tag = config.get("elementLocator", "open_close_toggle_tag")
        self.os_switch_link = config.get("elementLocator", "os_switch_link")    
        self.os_platform_list = config.get("elementLocator", "os_platform_list")
        self.os_to_select = config.get("elementLocator", "os_to_select")

    def click_open_close_all_button(self):
        locator_open_close_toggle_tag = self.loc_split(self.open_close_toggle_tag)
        assert self.click_element(locator_open_close_toggle_tag)
    
    def os_switch(self):
        locator_os_switch_link  = self.loc_split(self.os_switch_link )
        locator_os_platform_list = self.loc_split(self.os_platform_list)
        locator_os_to_select= self.loc_split(self.os_to_select)
        assert self.click_element(locator_os_switch_link)
        assert self.click_element(locator_os_platform_list)
        assert self.click_element(locator_os_to_select)