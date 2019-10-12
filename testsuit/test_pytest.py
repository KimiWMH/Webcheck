import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import pytest 
from pageobjects.guide_page import guide_page
from pageobjects.product_page import product_page
from data.data import get_test_data
import pprint as p 
class test_page(product_page,guide_page):
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)



class Test_Web_Data():
    verify_data = get_test_data()
    #@pytest.mark.skip(reason="Test Pytest Structure")
    @pytest.mark.parametrize("data",[data for data in verify_data])
 
    def test_case(self,data):        
        with test_page() as tp:
            tp.input_product_name(data['product_name'])
            tp.click_search_button()
            tp.os_switch(data['os_platform'],data['os_version']) 
            tp.click_open_close_all_button()
            if not data['driver_name'] =="Skip":
                panel_data = tp.get_panel_title() 
                try:  
                    panel_data.index(data['driver_name'])
                    panel_data.index(data['driver_link_header'])
                except ValueError as e:
                    raise AssertionError(data)
            print("Pass")
        