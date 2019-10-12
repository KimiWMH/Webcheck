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
        self.locator_open_close_toggle_tag = self.loc_split(config.get("elementLocator", "open_close_toggle_tag"))
        self.locator_os_switch_link = self.loc_split(config.get("elementLocator", "os_switch_link"))
        self.locator_os_platform_head= self.loc_split(config.get("elementLocator", "os_platform_head"))
        self.locator_os_platform_list = self.loc_split(config.get("elementLocator", "os_platform_list"))
        self.locator_os_platform_list_value = self.loc_split(config.get("elementLocator", "os_platform_list_value"))
        self.locator_os_version_head= self.loc_split(config.get("elementLocator", "os_version_head"))
        self.locator_os_version_list = self.loc_split(config.get("elementLocator", "os_version_list"))
        self.locator_os_version_list_value = self.loc_split(config.get("elementLocator", "os_version_list_value"))
        self.locator_os_submit_button = self.loc_split(config.get("elementLocator", "os_submit_button"))
        self.sresult_panel_name  = self.loc_split(config.get("elementLocator", "sresult_panel_name"))
        self.sresult_panel_downloadlink  = self.loc_split(config.get("elementLocator", "sresult_panel_downloadlink"))
        self.hiden_downlink = self.loc_split(config.get("elementLocator", "hiden_download_link"))

    def click_open_close_all_button(self):
        assert self.click_element(self.locator_open_close_toggle_tag)
    
    def os_switch(self,platform,version):
        assert self.click_element(self.locator_os_switch_link)
        assert self.click_element(self.locator_os_platform_head)

        temp_platform_list = self.get_element(self.locator_os_platform_list)
        tag = False
        for i in self.get_element(self.locator_os_platform_list_value,element_driver=temp_platform_list,multi=True):
            if i.text == platform:
                i.click()
                tag = True
        if tag:
            assert self.click_element(self.locator_os_version_head)
        else:
            raise ValueError("could not find os platform") 

        tag = False
        temp_version_list = self.get_element(self.locator_os_version_list)
        for i in self.get_element(self.locator_os_version_list_value,element_driver=temp_version_list,multi=True):
            if i.text == version:
                i.click()
                tag = True
        if tag:
            assert self.click_element(self.locator_os_submit_button)
        else:
            raise ValueError("could not find os version") 

    def get_os_list_context(self):
        platform = []
        version = []
        assert self.click_element(self.locator_os_switch_link)
        assert self.click_element(self.locator_os_platform_head) 
        temp_platform_list = self.get_element(self.locator_os_platform_list)
        elements_platform = self.get_element(self.locator_os_platform_list_value,element_driver=temp_platform_list,multi=True)
        for i in elements_platform:
            if i.text != 'Select operating system':
                platform.append(i.text)

        assert self.click_element(self.locator_os_platform_head)
        for j in elements_platform:
            assert self.click_element(self.locator_os_platform_head)
            j.click() 
            assert self.click_element(self.locator_os_version_head)
            temp_version_list = self.get_element(self.locator_os_version_list)
            for i in self.get_element(self.locator_os_version_list_value,element_driver=temp_version_list,multi=True):
                if i.text != 'Select version':
                    version.append(i.text)
        return platform,version

    def get_panel_title(self):
        result_list = []
        n = 0
        panel_name_list = self.get_element(self.sresult_panel_name,multi=True)
        panel_link_list = self.get_element(self.sresult_panel_downloadlink,multi=True)

        for name in panel_link_list:
            panel_context = name.get_attribute('href')
            result_list.append(panel_context) 

        for name in panel_name_list:
            panel_context = name.text
            result_list.insert(n,panel_context.replace('\n', '').strip(r".a{fill:#0096d6;}\n"))
            assert self.click_element(False,element = name)   
            n+=4

        return result_list

        result_list = []
        link_list = []
        panel_name_list = self.get_element(self.sresult_panel_name,multi=True)
        
        for name in panel_name_list:
            panel_context = name.text
            #panel_title = panel_context.split("(")[0].strip(' ')
            result_list.append(panel_context.replace('\n', '').strip(r".a{fill:#0096d6;}\n"))
            assert self.click_element(False,element = name)

        hiden_link_list = self.get_element(self.hiden_downlink,multi=True)   
        for link in hiden_link_list:
            panel_link_context = link.get_attribute('href')
           # panel_link_context = link.text
            result_list.append(panel_link_context)      

        return result_list