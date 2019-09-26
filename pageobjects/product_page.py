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

        self.os_platform_head = config.get("elementLocator", "os_platform_head")
        self.os_platform_list = config.get("elementLocator", "os_platform_list")
        self.os_platform_list_value = config.get("elementLocator", "os_platform_list_value")

        self.os_version_head = config.get("elementLocator", "os_version_head")
        self.os_version_list = config.get("elementLocator", "os_version_list")
        self.os_version_list_value = config.get("elementLocator", "os_version_list_value")

        self.os_submit_button = config.get("elementLocator", "os_submit_button")

    def click_open_close_all_button(self):
        locator_open_close_toggle_tag = self.loc_split(self.open_close_toggle_tag)
        assert self.click_element(locator_open_close_toggle_tag)
    
    def os_switch(self,platform,version):
        assert self.click_element(self.os_switch_link)
        assert self.click_element(self.os_platform_head)

        temp_platform_list = self.get_element(self.os_platform_list)
        for i in self.get_element(self.os_platform_list_value,element_driver=temp_platform_list,Multi=True):
            if i.text == platform:
                assert self.click_element(i)


        temp_version_list = self.get_element(self.os_version_list)
        for i in self.get_element(self.os_version_list_value,element_driver=temp_version_list,Multi=True):
            if i.text == version:
                assert self.click_element(i)

        assert self.click_element(self.os_submit_button)