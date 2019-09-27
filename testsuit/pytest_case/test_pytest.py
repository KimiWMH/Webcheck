import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import pytest 
from pageobjects.guide_page import guide_page
from pageobjects.product_page import product_page
import pprint as p 
class test_page(product_page,guide_page):
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)



class Test_Web_Data():
    #@pytest.mark.skip(reason="Test Pytest Structure")
    @pytest.mark.parametrize("product_name",["M479"])
    @pytest.mark.parametrize("os_platform",["SAP"])
    @pytest.mark.parametrize("os_version",["SAP"])    
    def test_case(self,product_name,os_platform,os_version):        
        dict = {
            'driver_link': '', 
            'driver_name': '', 
            'driver_type': '', 
            'os_platform': os_platform,
            'os_version': os_version, 
            'produc_name': product_name
            }
        with test_page() as tp:
            tp.input_product_name("M479")
            tp.click_search_button()
            tp.os_switch(os_platform,os_version)
            tp.click_open_close_all_button()
            k= tp.get_panel_title()
        for item in k:
            if item%2 !=0:
                dict['driver_link'] = item
            else:
                dict['driver_name'] = item
            p.pprint(dict)
        