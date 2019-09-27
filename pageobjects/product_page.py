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

        self.sresult_panel_name  = self.loc_split(config.get("elementLocator", "sresult_panel_name"))
        self.sresult_panel_downloadlink  = self.loc_split(config.get("elementLocator", "sresult_panel_downloadlink"))
    
    
    def click_open_close_all_button(self):
        locator_open_close_toggle_tag = self.loc_split(self.open_close_toggle_tag)
        assert self.click_element(locator_open_close_toggle_tag)
    
    def os_switch(self,platform,version):
        locator_os_switch_link = self.loc_split(self.os_switch_link)
        locator_os_platform_head= self.loc_split(self.os_platform_head)
        locator_os_platform_list = self.loc_split(self.os_platform_list)
        locator_os_platform_list_value = self.loc_split(self.os_platform_list_value)

        locator_os_version_head= self.loc_split(self.os_version_head)
        locator_os_version_list = self.loc_split(self.os_version_list)
        locator_os_version_list_value = self.loc_split(self.os_version_list_value)

        locator_os_submit_button = self.loc_split(self.os_submit_button)

        assert self.click_element(locator_os_switch_link)
        assert self.click_element(locator_os_platform_head)

        temp_platform_list = self.get_element(locator_os_platform_list)
        for i in self.get_element(locator_os_platform_list_value,element_driver=temp_platform_list,multi=True):
            if i.text == platform:
                i.click()

        assert self.click_element(locator_os_version_head)
        temp_version_list = self.get_element(locator_os_version_list)
        for i in self.get_element(locator_os_version_list_value,element_driver=temp_version_list,multi=True):
            if i.text == version:
                i.click()

        assert self.click_element(locator_os_submit_button)

    def get_os_list_context(self):

        locator_os_switch_link = self.loc_split(self.os_switch_link)
        locator_os_platform_head= self.loc_split(self.os_platform_head)
        locator_os_platform_list = self.loc_split(self.os_platform_list)
        locator_os_platform_list_value = self.loc_split(self.os_platform_list_value)
        locator_os_version_head= self.loc_split(self.os_version_head)
        locator_os_version_list = self.loc_split(self.os_version_list)
        locator_os_version_list_value = self.loc_split(self.os_version_list_value)
        locator_os_submit_button = self.loc_split(self.os_submit_button)

        platform = []
        version = []
        assert self.click_element(locator_os_switch_link)

        
        assert self.click_element(locator_os_platform_head) 
        temp_platform_list = self.get_element(locator_os_platform_list)
        elements_platform = self.get_element(locator_os_platform_list_value,element_driver=temp_platform_list,multi=True)
        for i in elements_platform:
            platform.append(i.text)
        assert self.click_element(locator_os_platform_head)

        for j in elements_platform:
            assert self.click_element(locator_os_platform_head)
            j.click() 
            assert self.click_element(locator_os_version_head)
            temp_version_list = self.get_element(locator_os_version_list)
            for i in self.get_element(locator_os_version_list_value,element_driver=temp_version_list,multi=True):
                if i.text != 'Select version':
                    version.append(i.text)

        return platform,version

    def get_panel_title(self):
        result_list = []
        link_list = []
        panel_name_list = self.get_element(self.sresult_panel_name,multi=True)
        panel_link_list = self.get_element(self.sresult_panel_downloadlink,multi=True)

        for link,name in zip(panel_link_list,panel_name_list):

            panel_context = name.text
            #panel_title = panel_context.split("(")[0].strip(' ')
            result_list.append(panel_context.replace('\n', '').strip(r".a{fill:#0096d6;}\n"))

            assert self.click_element(False,element = name)
            
            panel_link_context = link.get_attribute('href')
            result_list.append(panel_link_context)           

        return result_list