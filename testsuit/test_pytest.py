import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import pytest 
from pageobjects.guide_page import guide_page
from pageobjects.product_page import product_page

class test_page(product_page,guide_page):
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)

class Test_Web_Data():

    @pytest.mark.skip(reason="Test Pytest Structure")
    @pytest.mark.parametrize("product_name",["M479"])
    def test_case(self,product_name):
        with test_page() as tp:
            tp.input_product_name(product_name)
            tp.click_search_button()
            tp.click_open_close_all_button()
           # tp.os_switch()
